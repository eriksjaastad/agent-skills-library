# Skill Lifecycle Manager Playbook

> **Version:** 1.0.0  
> **Last Updated:** January 16, 2026  
> **Purpose:** Manage the full lifecycle of AI skills - from detection to retirement

---

## Overview

This playbook defines the process for:
1. **Detecting** patterns that should become skills
2. **Creating** new skills from proven patterns
3. **Promoting** skills based on usage evidence
4. **Enhancing** skills based on real-world feedback
5. **Retiring** skills that are no longer useful

---

## When to Use This Playbook

**Triggers:**
- Monthly skill review (scheduled)
- New pattern discovered in 2+ projects
- Skill enhancement request from a project
- New project asking "what skills should I use?"

**User signals:**
- "What patterns are repeating?"
- "Should this become a skill?"
- "Is this skill ready to promote?"
- "Which skills should I use for this project?"

---

## Skill Maturity Levels

```
🔵 CANDIDATE (1 project)
  │  Pattern observed, not yet proven
  │
  ↓  Applied in 2nd project + works
  
🟡 EMERGING (2 projects)
  │  Pattern works but needs more evidence
  │
  ↓  Applied in 3rd project + battle-tested
  
🟢 PROVEN (3+ projects)
  │  Reliable, ready for wide adoption
  │
  ↓  No changes needed for 6+ months
  
🏆 MATURE (reference quality)
     Gold standard, stable
```

---

## The Detection Process

### Step 1: Run Detection Script

```bash
cd agent-skills-library
python scripts/detect_skill_candidates.py
```

**What it finds:**
- Which skills are used in which projects
- Skills ready for promotion (🟡 → 🟢)
- Repeated patterns that might become skills

### Step 2: Review Candidates

For each detected candidate:

| Question | Yes → | No → |
|----------|-------|------|
| Is this pattern AI-instructable? | Consider as skill | Document as pattern only |
| Does it save significant time? | Worth creating | May not be worth the overhead |
| Is it stable or still evolving? | Create skill | Wait until stable |
| Would other projects benefit? | Create shared skill | Keep project-specific |

### Step 3: Decision Matrix

| Evidence | Action |
|----------|--------|
| 1 project uses pattern | 🔵 Watch - document but don't create skill yet |
| 2 projects use pattern | 🟡 Create skill - mark as Emerging |
| 3+ projects use pattern | 🟢 Create/promote skill - mark as Proven |
| Pattern causes problems | ❌ Don't create or retire existing |

---

## Creating a New Skill

### Checklist

- [ ] Pattern observed in 2+ projects
- [ ] Pattern is stable (not changing frequently)
- [ ] Pattern is AI-instructable (clear steps)
- [ ] Playbook created (`playbooks/skill-name/README.md`)
- [ ] Claude adapter created (`claude-skills/skill-name/SKILL.md`)
- [ ] SKILL.md has valid frontmatter (name + description)
- [ ] Validation passes (`python scripts/validate_skills.py`)

### File Structure

```
agent-skills-library/
├── playbooks/
│   └── new-skill/
│       ├── README.md          ← Canonical instructions
│       └── CHANGELOG.md       ← Version history (optional)
│
├── claude-skills/
│   └── new-skill/
│       └── SKILL.md           ← Claude adapter with frontmatter
│
└── cursor-rules/
    └── new-skill/
        └── RULE.md            ← Cursor adapter (optional)
```

### SKILL.md Template

```yaml
---
name: skill-name
description: Clear description with natural trigger keywords for when to use this skill.
---

# Skill Name

> **Adapter for:** `playbooks/skill-name/`
> **Version:** 1.0.0

## When to Activate

[Trigger conditions]

## Output Format

[Claude-specific formatting]

## Process

See playbook: `playbooks/skill-name/README.md`
```

---

## Promoting a Skill (🟡 → 🟢)

### Requirements

- [ ] Skill used successfully in 3+ projects
- [ ] No significant issues reported
- [ ] Instructions are stable (no major changes needed)
- [ ] Evidence documented in SKILL_USAGE.md

### Process

1. **Verify usage:** Run `python scripts/detect_skill_candidates.py`
2. **Check quality:** Review any feedback or issues
3. **Update metadata:** Change status from 🟡 to 🟢 in tracking
4. **Announce:** Note in CHANGELOG or commit message

---

## Enhancing a Skill

### When to Enhance

- Skill used differently than documented
- Edge cases discovered in real usage
- Better approach found through experience
- Feedback from users/projects

### Enhancement Workflow

1. **Document the gap:** What's missing or wrong?
2. **Propose change:** Update playbook with improvement
3. **Test:** Apply to at least one project
4. **Validate:** Run validation script
5. **Version:** Bump version number (see Versioning section)
6. **Commit:** Clear commit message with change summary

### Versioning

| Change Type | Version Bump | Example |
|-------------|--------------|---------|
| Typo fix, clarification | PATCH (x.x.1) | 1.0.0 → 1.0.1 |
| New section, enhanced steps | MINOR (x.1.x) | 1.0.0 → 1.1.0 |
| Complete rewrite, breaking | MAJOR (1.x.x) | 1.0.0 → 2.0.0 |

---

## Retiring a Skill

### When to Retire

- Skill not used in any active projects
- Better alternative exists
- Pattern no longer relevant
- Causes more problems than it solves

### Retirement Process

1. **Verify non-usage:** Run detection script
2. **Check for dependents:** Any projects still reference it?
3. **Archive:** Move to `_archived/` or delete
4. **Document:** Note retirement in CHANGELOG

---

## Monthly Review Process

**Time required:** 15-30 minutes

### Checklist

```markdown
## Monthly Skill Review - [Month Year]

**Detection:**
- [ ] Run: `python scripts/detect_skill_candidates.py`
- [ ] Review skill usage report
- [ ] Note any new candidates

**Promotions:**
- [ ] Any 🟡 skills hit 3 projects? → Promote to 🟢
- [ ] Document evidence for each promotion

**Enhancements:**
- [ ] Any skills need updates based on usage?
- [ ] Any feedback to incorporate?

**New Skills:**
- [ ] Any 🔵 candidates ready to create?
- [ ] Create with proper structure and frontmatter

**Validation:**
- [ ] Run: `python scripts/validate_skills.py`
- [ ] All skills pass?

**Summary:**
- Skills tracked: X
- Skills in use: Y
- Promotions this month: Z
- New skills created: N
```

---

## Tracking Skill Usage

### SKILL_USAGE.md

Maintain a tracking file:

```markdown
# Skill Usage Tracker

## Usage Summary

| Skill | Status | Projects | Last Verified |
|-------|--------|----------|---------------|
| pr-review | 🟢 Proven | 5 | Jan 2026 |
| debugging-routine | 🟡 Emerging | 2 | Jan 2026 |

## Detailed Evidence

### pr-review
- **project-a** (Dec 2025): Used in .cursorrules, works well
- **project-b** (Jan 2026): Integrated with CI review process
- **project-c** (Jan 2026): Custom checklist added
```

---

## Integration with project-scaffolding

This skill works with the governance process in `project-scaffolding`:

| Concern | Owner |
|---------|-------|
| Detection script | agent-skills-library |
| Skill validation | agent-skills-library |
| Usage tracking | agent-skills-library |
| Promotion decisions | Human (monthly review) |
| Workflow documentation | project-scaffolding |

The detection script outputs data; humans make promotion decisions.

---

## Success Criteria

**This playbook is working if:**
- [ ] No skills are "orphaned" (created but never used)
- [ ] Promotions happen based on evidence, not gut feeling
- [ ] Skill enhancements flow back from real usage
- [ ] Monthly review takes < 30 minutes
- [ ] New team members can understand skill maturity at a glance

---

## Related Resources

- **Validation script:** `scripts/validate_skills.py`
- **Detection script:** `scripts/detect_skill_candidates.py`
- **Usage tracking:** `SKILL_USAGE.md`
- **Agent Skills Spec:** https://agentskills.io/specification

---

*This playbook manages the skills that manage your AI workflows. Meta? Yes. Useful? Also yes.*
