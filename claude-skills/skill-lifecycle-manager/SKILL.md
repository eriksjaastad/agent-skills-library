---
name: skill-lifecycle-manager
description: Manage the full lifecycle of AI skills including detection of patterns worth becoming skills, promotion based on usage evidence, and enhancement from real-world feedback.
---

# Skill Lifecycle Manager

> **Adapter for:** `playbooks/skill-lifecycle-manager/`
> **Version:** 1.0.0
> **Meta-skill:** This skill manages other skills

---

## Skill Overview

**What this skill does:**
Provides a systematic process for detecting, creating, promoting, and enhancing AI skills based on usage patterns across projects. It prevents "skill sprawl" and ensures skills are created based on evidence, not gut feeling.

**Canonical instructions:** `../../playbooks/skill-lifecycle-manager/README.md`

---

## When to Activate This Skill

**User signals:**
- "What patterns are repeating across my projects?"
- "Should this become a skill?"
- "Is this skill ready to promote?"
- "Run the monthly skill review"
- "Which skills should I use for this project?"
- "Help me create a new skill"

**Scheduled triggers:**
- Monthly skill review (first week of each month)
- After completing a major project milestone
- When starting a new project (skill selection)

---

## Claude-Specific Workflow

### Phase 1: Detection

When asked to find skill candidates:

```markdown
I'll analyze your projects for repeated patterns that could become skills.

**Running detection:**
1. Scanning for skill references in .cursorrules, CLAUDE.md, AGENTS.md
2. Finding repeated instruction patterns
3. Checking skill usage across projects

**Detection Results:**

## 📊 Current Skill Usage
| Skill | Status | Projects |
|-------|--------|----------|
| [skill-name] | [🔵/🟡/🟢] | [count] |

## 🚀 Promotion Candidates
[Skills at 🟡 with 2 projects - ready for 3rd]

## 💡 New Skill Candidates
[Patterns found in 2+ projects not yet skills]
```

### Phase 2: Decision Support

When asked whether something should become a skill:

```markdown
## Skill Candidate Assessment: [Pattern Name]

**Evidence:**
- Found in: [list projects]
- Usage pattern: [how it's being used]

**Checklist:**
- [ ] AI-instructable? (Clear steps an AI can follow)
- [ ] Time-saving? (Significant benefit)
- [ ] Stable? (Not changing frequently)
- [ ] Reusable? (Other projects would benefit)

**Recommendation:** [Create skill / Wait for more evidence / Keep project-specific]

**If creating:**
1. Playbook location: `playbooks/[name]/README.md`
2. Skill location: `claude-skills/[name]/SKILL.md`
3. Required frontmatter: name + description
```

### Phase 3: Creation

When asked to create a new skill:

```markdown
## Creating Skill: [skill-name]

**Step 1: Create Playbook**
Location: `playbooks/[skill-name]/README.md`
[Generate playbook content based on pattern]

**Step 2: Create SKILL.md**
Location: `claude-skills/[skill-name]/SKILL.md`

Required frontmatter:
---
name: [skill-name]
description: [Clear description with trigger keywords]
---

**Step 3: Validate**
Run: `python scripts/validate_skills.py`

**Step 4: Track**
Add to SKILL_USAGE.md with initial project(s)
```

### Phase 4: Monthly Review

When asked to run the monthly review:

```markdown
## Monthly Skill Review - [Month Year]

### 1. Detection Results
[Run scripts/detect_skill_candidates.py and summarize]

### 2. Promotion Decisions
| Skill | Current | Projects | Action |
|-------|---------|----------|--------|
| [name] | 🟡 | 3 | → Promote to 🟢 |

### 3. Enhancement Needs
[Any skills with gaps or feedback to incorporate]

### 4. New Skills to Create
[Candidates with enough evidence]

### 5. Validation
- [ ] All skills pass validation
- [ ] SKILL_USAGE.md updated
- [ ] Changes committed

### Summary
- Skills tracked: X
- In use: Y
- Promoted: Z
- Created: N
```

---

## Output Format

### Skill Status Report

```markdown
## Skill Status Report

**Generated:** [Date]
**Skills Tracked:** [Count]

### By Maturity Level

**🟢 Proven (3+ projects)**
- skill-a (5 projects)
- skill-b (3 projects)

**🟡 Emerging (2 projects)**
- skill-c (2 projects) ← Ready for promotion with 1 more

**🔵 Candidate (1 project)**
- skill-d (watching)

### Promotion Opportunities
[Skills at 2 projects that could be promoted]

### Enhancement Backlog
[Skills with known gaps or feedback]
```

---

## Constraints

- Always validate skills after changes: `python scripts/validate_skills.py`
- Never create skills for patterns in only 1 project (wait for evidence)
- Always include proper YAML frontmatter (Agent Skills spec compliance)
- Track promotion decisions with evidence, not gut feeling
- Keep playbooks tool-agnostic; put Claude-specific bits in SKILL.md

---

## Integration Points

### Scripts Available

| Script | Purpose |
|--------|---------|
| `scripts/validate_skills.py` | Check spec compliance |
| `scripts/detect_skill_candidates.py` | Find patterns and usage |

### Files to Maintain

| File | Purpose |
|------|---------|
| `SKILL_USAGE.md` | Track which projects use which skills |
| `playbooks/*/README.md` | Canonical skill instructions |
| `claude-skills/*/SKILL.md` | Claude adapters with frontmatter |

---

## Success Criteria

**This skill is working when:**
- [ ] Monthly reviews happen consistently
- [ ] Promotions are based on usage evidence (3+ projects)
- [ ] No "orphan" skills created and never used
- [ ] Skill enhancements flow from real project feedback
- [ ] Validation passes for all skills

---

*A meta-skill that manages skills. Self-referential and proud of it.*
