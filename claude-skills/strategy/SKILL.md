---
name: strategy
description: Create PRDs for new features following the 6-phase workflow. Use when starting new work, creating requirements, or beginning the planning phase with Erik.
---

# Strategy

> **Adapter for:** `playbooks/strategy/`

---

## When to Activate

**User signals:**
- "let's build X"
- "I want to add a feature for..."
- "create a PRD"
- "start planning [feature]"
- "/strategy"

**Context:**
- Beginning new feature work
- Before opening Kiro
- Erik describing what he wants

---

## Pre-Flight

Before writing PRD:

1. **Check existing services:**
```bash
cat $PROJECTS_ROOT/project-scaffolding/EXTERNAL_RESOURCES.yaml | grep -A10 "services_by_function"
```

2. **Determine path:**
- Full Workflow (schema/auth/infra changes)
- Light Path (<3 files, <2 hours)
- Exploration (R&D, not shipping)

---

## PRD Must Include

| Section | What |
|---------|------|
| Overview | Problem + who it's for |
| Goals | Outcomes (not specs) |
| Non-Goals | What we're NOT building |
| Constraints | Security, tech stack, performance |
| Integration | Existing infra, services, notifications |
| Metrics | How we know it works |

---

## PRD Must NOT Include

- User stories ("As a...") - Kiro generates
- EARS requirements - Kiro generates
- Data schemas - Kiro generates
- Task breakdowns - Kiro generates

**Key insight:** PRD = intent. Kiro = specifications.

---

## Output Format

```markdown
# PRD: [Feature Name]

## Project Overview
[2-3 sentences: problem + audience]

## Goals
- [Outcome 1]
- [Outcome 2]

## Non-Goals
- [Explicitly not building]

## Constraints
- **Security:** [auth method, access rules]
- **Tech Stack:** [required languages/frameworks]
- **Performance:** [requirements]

## Integration Context
- **Existing Infra:** [from EXTERNAL_RESOURCES.yaml]
- **Publishing:** [where output goes]
- **Notifications:** [who gets told what]

## Success Metrics
- [How we measure success]

## Open Questions for Kiro
- [Decisions for Kiro to make]
```

---

## Red Flags

- No security section → ASK
- No non-goals → ASK
- No integration context → ASK
- User stories in PRD → REMOVE
- Schemas in PRD → REMOVE

---

## Constraints

- ALWAYS check EXTERNAL_RESOURCES.yaml first
- ALWAYS include non-goals
- ALWAYS include security constraints
- NEVER write specifications (that's Kiro's job)
- NEVER skip the completeness checklist

**Full playbook:** `agent-skills-library/playbooks/strategy/README.md`
