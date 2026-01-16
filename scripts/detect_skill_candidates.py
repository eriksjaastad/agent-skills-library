#!/usr/bin/env python3
"""
Detect Skill Candidates - Find patterns that should become skills.

This script scans projects to identify:
1. Repeated instruction patterns (potential new skills)
2. Skills ready for promotion (🟡 → 🟢)
3. Skills that need enhancement (diverged from usage)

Usage:
    python scripts/detect_skill_candidates.py
    python scripts/detect_skill_candidates.py --projects-root ~/projects
    python scripts/detect_skill_candidates.py --output-json

Specification: https://agentskills.io/specification
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


@dataclass
class SkillUsage:
    """Track where a skill is used."""
    skill_name: str
    projects: list[str] = field(default_factory=list)
    references: list[dict] = field(default_factory=list)  # {project, file, line}


@dataclass
class SkillFeedback:
    """Feedback on a skill from a project's 00_Index file."""
    skill_name: str
    project: str
    feedback: str
    feedback_type: str  # "improvement" or "new_pattern"


@dataclass
class SkillCandidate:
    """A pattern that might become a skill."""
    pattern: str
    description: str
    projects: list[str] = field(default_factory=list)
    evidence: list[dict] = field(default_factory=list)  # {project, file, context}
    confidence: str = "🔵 Candidate"  # 🔵 Candidate, 🟡 Emerging, 🟢 Proven


# Patterns that suggest repeated AI instructions
INSTRUCTION_PATTERNS = [
    # Direct skill references
    (r'playbooks/[\w-]+/', "Playbook reference"),
    (r'agent-skills-library', "Skills library reference"),
    (r'SKILL\.md', "Skill file reference"),
    
    # Common instruction patterns
    (r'when (reviewing|debugging|analyzing)', "Conditional workflow trigger"),
    (r'follow (the|this) (process|playbook|routine)', "Process reference"),
    (r'use (the|this) (checklist|template|format)', "Template usage"),
    (r'always (check|verify|ensure|validate)', "Validation requirement"),
    (r'never (commit|push|deploy) without', "Safety gate"),
    
    # AI-specific patterns
    (r'Claude should', "Claude-specific instruction"),
    (r'AI assistant', "AI instruction"),
    (r'when asked to', "AI trigger phrase"),
]

# Files to scan for instruction patterns
INSTRUCTION_FILES = [
    '.cursorrules',
    'CLAUDE.md',
    'AGENTS.md',
    '.cursor/rules/*.md',
    '.claude/skills/*/SKILL.md',
]

# Known skills to track usage
KNOWN_SKILLS = [
    'pr-review',
    'debugging-routine',
    'youtube-channel-analysis',
    'ai-router-delegation',
    'spec-driven-developer',
    'audit-whisperer',
    'financial-integrity-guard',
    'tax-discovery-engine',
    'staged-prompt-engineering',
]


def find_projects(projects_root: Path) -> list[Path]:
    """Find all project directories."""
    projects = []
    
    for item in projects_root.iterdir():
        if not item.is_dir():
            continue
        # Skip hidden directories and common non-project dirs
        if item.name.startswith('.') or item.name in ('node_modules', 'venv', '.venv', '__pycache__'):
            continue
        # Must have git or be a recognizable project
        if (item / '.git').exists() or (item / 'README.md').exists():
            projects.append(item)
    
    return sorted(projects)


def scan_file_for_patterns(file_path: Path) -> list[dict]:
    """Scan a file for instruction patterns."""
    matches = []
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return matches
    
    for line_num, line in enumerate(content.split('\n'), 1):
        for pattern, description in INSTRUCTION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                matches.append({
                    'file': str(file_path),
                    'line': line_num,
                    'pattern': pattern,
                    'description': description,
                    'context': line.strip()[:100],
                })
    
    return matches


def scan_project_for_skill_usage(project: Path, skill_name: str) -> list[dict]:
    """Find references to a specific skill in a project."""
    references = []
    
    # Files to check
    files_to_check = [
        project / '.cursorrules',
        project / 'CLAUDE.md',
        project / 'AGENTS.md',
    ]
    
    # Also check .cursor/rules/
    cursor_rules = project / '.cursor' / 'rules'
    if cursor_rules.exists():
        files_to_check.extend(cursor_rules.glob('*.md'))
    
    # Check .claude/skills/
    claude_skills = project / '.claude' / 'skills'
    if claude_skills.exists():
        for skill_dir in claude_skills.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / 'SKILL.md'
                if skill_file.exists():
                    files_to_check.append(skill_file)
    
    for file_path in files_to_check:
        if not file_path.exists():
            continue
        
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        
        # Look for skill name references
        patterns = [
            rf'playbooks/{skill_name}',
            rf'claude-skills/{skill_name}',
            rf'cursor-rules/{skill_name}',
            rf'{skill_name}/README',
            rf'{skill_name}/SKILL',
            rf'{skill_name}/RULE',
        ]
        
        for line_num, line in enumerate(content.split('\n'), 1):
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    references.append({
                        'project': project.name,
                        'file': str(file_path.relative_to(project)),
                        'line': line_num,
                        'context': line.strip()[:80],
                    })
                    break  # Only count once per line
    
    return references


def detect_skill_usage(projects_root: Path) -> dict[str, SkillUsage]:
    """Detect which projects use which skills."""
    usage = {}
    
    for skill_name in KNOWN_SKILLS:
        skill_usage = SkillUsage(skill_name=skill_name)
        
        for project in find_projects(projects_root):
            refs = scan_project_for_skill_usage(project, skill_name)
            if refs:
                skill_usage.projects.append(project.name)
                skill_usage.references.extend(refs)
        
        usage[skill_name] = skill_usage
    
    return usage


def collect_skill_feedback(projects_root: Path) -> list[SkillFeedback]:
    """Collect skill feedback from 00_Index files in projects."""
    feedback_list = []
    
    for project in find_projects(projects_root):
        # Find 00_Index files
        for index_file in project.glob("00_Index_*.md"):
            try:
                content = index_file.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue
            
            # Parse feedback sections
            in_skill_feedback = False
            in_new_patterns = False
            current_skill = None
            
            for line in content.split('\n'):
                line = line.strip()
                
                # Detect section starts
                if "Improvements suggested" in line or "Skill Feedback" in line:
                    in_skill_feedback = True
                    in_new_patterns = False
                    continue
                elif "New patterns emerging" in line or "patterns emerging" in line:
                    in_new_patterns = True
                    in_skill_feedback = False
                    continue
                elif line.startswith("## ") or line.startswith("---"):
                    # New section, reset
                    in_skill_feedback = False
                    in_new_patterns = False
                    continue
                
                # Parse bullet points
                if line.startswith("- ") and in_skill_feedback:
                    # Format: "- skill-name: feedback text"
                    if ":" in line:
                        parts = line[2:].split(":", 1)
                        skill_name = parts[0].strip()
                        feedback_text = parts[1].strip() if len(parts) > 1 else ""
                        if feedback_text and feedback_text not in ["[What could be better? Edge cases found?]", ""]:
                            feedback_list.append(SkillFeedback(
                                skill_name=skill_name,
                                project=project.name,
                                feedback=feedback_text,
                                feedback_type="improvement"
                            ))
                
                elif line.startswith("- ") and in_new_patterns:
                    # Format: "- Pattern description: Could this become a skill?"
                    if ":" in line:
                        parts = line[2:].split(":", 1)
                        pattern = parts[0].strip()
                        notes = parts[1].strip() if len(parts) > 1 else ""
                        if pattern and pattern not in ["[Pattern description]", ""]:
                            if notes not in ["[Could this become a skill? Used in other projects?]", ""]:
                                feedback_list.append(SkillFeedback(
                                    skill_name=pattern,
                                    project=project.name,
                                    feedback=notes,
                                    feedback_type="new_pattern"
                                ))
    
    return feedback_list


def detect_instruction_patterns(projects_root: Path) -> dict[str, list[dict]]:
    """Find repeated instruction patterns across projects."""
    patterns_by_project: dict[str, list[dict]] = defaultdict(list)
    
    for project in find_projects(projects_root):
        for file_pattern in INSTRUCTION_FILES:
            if '*' in file_pattern:
                # Glob pattern
                base, glob = file_pattern.rsplit('/', 1)
                search_dir = project / base
                if search_dir.exists():
                    for file_path in search_dir.glob(glob):
                        matches = scan_file_for_patterns(file_path)
                        if matches:
                            patterns_by_project[project.name].extend(matches)
            else:
                file_path = project / file_pattern
                if file_path.exists():
                    matches = scan_file_for_patterns(file_path)
                    if matches:
                        patterns_by_project[project.name].extend(matches)
    
    return dict(patterns_by_project)


def find_repeated_patterns(patterns_by_project: dict[str, list[dict]]) -> list[SkillCandidate]:
    """Find patterns that appear in multiple projects (skill candidates)."""
    # Group by pattern description
    pattern_occurrences: dict[str, list[dict]] = defaultdict(list)
    
    for project, matches in patterns_by_project.items():
        for match in matches:
            key = match['description']
            pattern_occurrences[key].append({
                'project': project,
                'file': match['file'],
                'context': match['context'],
            })
    
    # Find patterns in 2+ projects
    candidates = []
    for description, occurrences in pattern_occurrences.items():
        projects = list(set(o['project'] for o in occurrences))
        if len(projects) >= 2:
            confidence = "🟢 Proven" if len(projects) >= 3 else "🟡 Emerging"
            candidates.append(SkillCandidate(
                pattern=description,
                description=f"Pattern found in {len(projects)} projects",
                projects=projects,
                evidence=occurrences[:5],  # Limit evidence
                confidence=confidence,
            ))
    
    # Sort by number of projects (most common first)
    candidates.sort(key=lambda c: len(c.projects), reverse=True)
    
    return candidates


def generate_report(
    skill_usage: dict[str, SkillUsage],
    candidates: list[SkillCandidate],
    feedback: list[SkillFeedback],
    output_json: bool = False
) -> None:
    """Generate the detection report."""
    
    if output_json:
        report = {
            'skill_usage': {
                name: {
                    'projects': usage.projects,
                    'project_count': len(usage.projects),
                    'references': usage.references,
                }
                for name, usage in skill_usage.items()
            },
            'candidates': [
                {
                    'pattern': c.pattern,
                    'description': c.description,
                    'projects': c.projects,
                    'confidence': c.confidence,
                    'evidence': c.evidence,
                }
                for c in candidates
            ],
            'feedback': {
                'improvements': [
                    {
                        'skill': f.skill_name,
                        'project': f.project,
                        'feedback': f.feedback,
                    }
                    for f in feedback if f.feedback_type == "improvement"
                ],
                'new_patterns': [
                    {
                        'pattern': f.skill_name,
                        'project': f.project,
                        'notes': f.feedback,
                    }
                    for f in feedback if f.feedback_type == "new_pattern"
                ],
            },
        }
        print(json.dumps(report, indent=2))
        return
    
    # Text report
    print(f"\n{BOLD}Skill Detection Report{RESET}")
    print("=" * 60)
    print(f"Specification: https://agentskills.io/specification")
    print("=" * 60)
    
    # Skill usage section
    print(f"\n{BOLD}{CYAN}📊 Skill Usage Across Projects{RESET}\n")
    
    # Sort by usage count
    sorted_usage = sorted(skill_usage.items(), key=lambda x: len(x[1].projects), reverse=True)
    
    for skill_name, usage in sorted_usage:
        count = len(usage.projects)
        if count == 0:
            status = f"{RED}Not used{RESET}"
        elif count == 1:
            status = f"{YELLOW}🔵 1 project{RESET}"
        elif count == 2:
            status = f"{YELLOW}🟡 2 projects{RESET}"
        else:
            status = f"{GREEN}🟢 {count} projects{RESET}"
        
        print(f"  {skill_name:30} {status}")
        if usage.projects:
            print(f"    └─ {', '.join(usage.projects[:5])}")
    
    # Promotion candidates
    print(f"\n{BOLD}{CYAN}🚀 Promotion Candidates (🟡 → 🟢){RESET}\n")
    
    promotable = [s for s, u in skill_usage.items() if len(u.projects) == 2]
    if promotable:
        for skill_name in promotable:
            usage = skill_usage[skill_name]
            print(f"  {YELLOW}• {skill_name}{RESET}")
            print(f"    Used in: {', '.join(usage.projects)}")
            print(f"    Action: Apply to 1 more project to promote to 🟢")
    else:
        print(f"  {GREEN}No skills ready for promotion (all are 0, 1, or 3+ projects){RESET}")
    
    # New skill candidates
    print(f"\n{BOLD}{CYAN}💡 New Skill Candidates (Repeated Patterns){RESET}\n")
    
    if candidates:
        for candidate in candidates[:10]:  # Top 10
            color = GREEN if "Proven" in candidate.confidence else YELLOW
            print(f"  {color}{candidate.confidence}: {candidate.pattern}{RESET}")
            print(f"    Found in: {', '.join(candidate.projects[:5])}")
            if candidate.evidence:
                print(f"    Example: \"{candidate.evidence[0]['context'][:60]}...\"")
            print()
    else:
        print(f"  {GREEN}No new patterns detected{RESET}")
    
    # Skill feedback from projects
    print(f"\n{BOLD}{CYAN}📝 Skill Feedback from Projects{RESET}\n")
    
    improvements = [f for f in feedback if f.feedback_type == "improvement"]
    new_patterns = [f for f in feedback if f.feedback_type == "new_pattern"]
    
    if improvements:
        print(f"  {BOLD}Improvement Suggestions:{RESET}")
        for fb in improvements:
            print(f"    {YELLOW}• {fb.skill_name}{RESET} (from {fb.project})")
            print(f"      \"{fb.feedback}\"")
    else:
        print(f"  {GREEN}No improvement suggestions found in 00_Index files{RESET}")
        print(f"  (Add feedback to 00_Index_*.md → 'Skill Feedback' section)")
    
    if new_patterns:
        print(f"\n  {BOLD}New Patterns Proposed:{RESET}")
        for fb in new_patterns:
            print(f"    {YELLOW}• {fb.skill_name}{RESET} (from {fb.project})")
            print(f"      \"{fb.feedback}\"")
    else:
        print(f"\n  {GREEN}No new pattern proposals found{RESET}")
        print(f"  (Add ideas to 00_Index_*.md → 'New patterns emerging' section)")
    
    # Summary
    print(f"\n{BOLD}Summary{RESET}")
    print(f"  Skills tracked: {len(skill_usage)}")
    print(f"  Skills in use: {sum(1 for u in skill_usage.values() if u.projects)}")
    print(f"  Promotion candidates: {len(promotable)}")
    print(f"  New pattern candidates: {len(candidates)}")
    print(f"  Improvement suggestions: {len(improvements)}")
    print(f"  New pattern proposals: {len(new_patterns)}")
    print()


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Detect skill candidates and track skill usage across projects"
    )
    parser.add_argument(
        '--projects-root',
        type=Path,
        default=Path.home() / 'projects',
        help="Root directory containing projects (default: ~/projects)"
    )
    parser.add_argument(
        '--output-json',
        action='store_true',
        help="Output as JSON instead of text report"
    )
    
    args = parser.parse_args()
    
    if not args.projects_root.exists():
        print(f"{RED}Error: Projects root not found: {args.projects_root}{RESET}")
        return 1
    
    if not args.output_json:
        print(f"Scanning projects in: {args.projects_root}")
    
    # Detect skill usage
    skill_usage = detect_skill_usage(args.projects_root)
    
    # Detect instruction patterns
    patterns = detect_instruction_patterns(args.projects_root)
    
    # Find repeated patterns (skill candidates)
    candidates = find_repeated_patterns(patterns)
    
    # Collect skill feedback from 00_Index files
    feedback = collect_skill_feedback(args.projects_root)
    
    # Generate report
    generate_report(skill_usage, candidates, feedback, args.output_json)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
