#!/usr/bin/env python3
"""
Validate Agent Skills against the official specification.

Specification: https://agentskills.io/specification

Usage:
    python scripts/validate_skills.py
    python scripts/validate_skills.py --fix  # Auto-fix issues (future)
"""

import re
import sys
from pathlib import Path

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def validate_name(name: str, directory_name: str) -> list[str]:
    """Validate the 'name' field according to spec."""
    errors = []
    
    if not name:
        errors.append("Missing required field: 'name'")
        return errors
    
    # Max 64 characters
    if len(name) > 64:
        errors.append(f"'name' exceeds 64 characters ({len(name)} chars)")
    
    # Lowercase letters, numbers, and hyphens only
    if not re.match(r'^[a-z0-9-]+$', name):
        errors.append("'name' must contain only lowercase letters, numbers, and hyphens")
    
    # Must not start or end with hyphen
    if name.startswith('-') or name.endswith('-'):
        errors.append("'name' must not start or end with a hyphen")
    
    # Must not contain consecutive hyphens
    if '--' in name:
        errors.append("'name' must not contain consecutive hyphens")
    
    # Must match parent directory name
    if name != directory_name:
        errors.append(f"'name' ({name}) must match directory name ({directory_name})")
    
    return errors


def validate_description(description: str) -> list[str]:
    """Validate the 'description' field according to spec."""
    errors = []
    
    if not description:
        errors.append("Missing required field: 'description'")
        return errors
    
    # Max 1024 characters
    if len(description) > 1024:
        errors.append(f"'description' exceeds 1024 characters ({len(description)} chars)")
    
    # Non-empty (already checked above, but be explicit)
    if not description.strip():
        errors.append("'description' must be non-empty")
    
    return errors


def parse_frontmatter(content: str) -> tuple[dict[str, str] | None, list[str]]:
    """Parse YAML frontmatter from SKILL.md content."""
    errors = []
    
    # Check for frontmatter delimiters
    if not content.startswith('---'):
        errors.append("Missing YAML frontmatter (must start with '---')")
        return None, errors
    
    # Find the closing delimiter
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append("Invalid YAML frontmatter (missing closing '---')")
        return None, errors
    
    frontmatter_text = parts[1].strip()
    if not frontmatter_text:
        errors.append("Empty YAML frontmatter")
        return None, errors
    
    # Parse simple YAML (key: value pairs)
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()
    
    return frontmatter, errors


def validate_skill_file(skill_path: Path) -> tuple[bool, list[str]]:
    """Validate a single SKILL.md file."""
    errors = []
    
    if not skill_path.exists():
        return False, [f"File not found: {skill_path}"]
    
    content = skill_path.read_text()
    directory_name = skill_path.parent.name
    
    # Skip template directory
    if directory_name.startswith('_'):
        return True, []
    
    # Parse frontmatter
    frontmatter, parse_errors = parse_frontmatter(content)
    errors.extend(parse_errors)
    
    if frontmatter is None:
        return False, errors
    
    # Validate required fields
    name = frontmatter.get('name', '')
    description = frontmatter.get('description', '')
    
    errors.extend(validate_name(name, directory_name))
    errors.extend(validate_description(description))
    
    return len(errors) == 0, errors


def validate_all_skills(skills_dir: Path) -> tuple[int, int, dict[str, list[str]]]:
    """Validate all skills in the directory."""
    passed = 0
    failed = 0
    all_errors: dict[str, list[str]] = {}
    
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        
        # Skip hidden and template directories
        if skill_dir.name.startswith('.') or skill_dir.name.startswith('_'):
            continue
        
        skill_file = skill_dir / "SKILL.md"
        
        if not skill_file.exists():
            failed += 1
            all_errors[skill_dir.name] = [f"Missing SKILL.md file"]
            continue
        
        is_valid, errors = validate_skill_file(skill_file)
        
        if is_valid:
            passed += 1
        else:
            failed += 1
            all_errors[skill_dir.name] = errors
    
    return passed, failed, all_errors


def print_report(passed: int, failed: int, all_errors: dict[str, list[str]]) -> None:
    """Print validation report."""
    total = passed + failed
    
    print(f"\n{BOLD}Agent Skills Validation Report{RESET}")
    print(f"{'=' * 50}")
    print(f"Specification: https://agentskills.io/specification")
    print(f"{'=' * 50}\n")
    
    if failed == 0:
        print(f"{GREEN}✅ All {total} skills pass validation!{RESET}\n")
    else:
        print(f"{RED}❌ {failed}/{total} skills have issues{RESET}\n")
        
        for skill_name, errors in all_errors.items():
            print(f"{RED}• {skill_name}/{RESET}")
            for error in errors:
                print(f"  {YELLOW}⚠ {error}{RESET}")
            print()
    
    print(f"{BOLD}Summary:{RESET}")
    print(f"  {GREEN}Passed: {passed}{RESET}")
    print(f"  {RED}Failed: {failed}{RESET}")
    print()


def main() -> int:
    """Main entry point."""
    # Find the claude-skills directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    skills_dir = project_root / "claude-skills"
    
    if not skills_dir.exists():
        print(f"{RED}Error: claude-skills directory not found at {skills_dir}{RESET}")
        return 1
    
    print(f"Validating skills in: {skills_dir}")
    
    passed, failed, all_errors = validate_all_skills(skills_dir)
    print_report(passed, failed, all_errors)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
