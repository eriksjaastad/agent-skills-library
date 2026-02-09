---
name: propose
description: Create PROPOSAL_FINAL.md from Kiro specs for Agent Hub execution. Use after traceability check to prepare handoff to Floor Manager.
---

# Propose

> **Adapter for:** `playbooks/propose/`

---

## When to Activate

**User signals:**
- "create the proposal"
- "prepare for handoff"
- "convert Kiro specs"
- "write PROPOSAL_FINAL"
- "/propose"

**Context:**
- After traceability passes
- Before handoff to Floor Manager
- When Kiro specs are ready

---

## Inputs Required

- PRD.md (original intent)
- .kiro/specs/[feature]/requirements.md
- .kiro/specs/[feature]/design.md
- .kiro/specs/[feature]/tasks.md
- Traceability table

---

## Infrastructure Mandate

The proposal MUST explicitly include:

| Section | What to Document |
|---------|------------------|
| Storage Strategy | Paths, tables, schema |
| State Machine | States and transitions |
| Publishing Pipeline | How content goes live |
| Notification Events | Triggers and channels |

**These get compressed in Kiro - re-expand them.**

---

## Output Format

```markdown
# PROPOSAL_FINAL.md

## Feature: [Name]
**Date:** YYYY-MM-DD
**PRD:** PRD.md
**Kiro Specs:** .kiro/specs/[feature]/

## Objective
[What and why from PRD]

## Acceptance Criteria
- [ ] [From requirements.md]

## Technical Design Summary

### Storage Strategy
- Files: [paths]
- Database: [tables]

### State Machine
[state] → [state] → [state]

### Publishing Pipeline
[How approved content becomes visible]

### Notification Events
| Event | Recipient | Channel |
|-------|-----------|---------|

## Implementation Tasks
[Ordered from tasks.md with done criteria]

## Traceability
[Table from Phase 2.5]

## Dependencies
[What must exist before execution]

## Out of Scope
[What this doesn't include]
```

---

## Red Flags

| Flag | Action |
|------|--------|
| No state machine | Add transitions |
| No storage paths | Specify locations |
| No publishing mechanism | Define how content goes live |
| Generic "implement X" tasks | Expand with specifics |

---

## Constraints

- ALWAYS include infrastructure mandate sections
- ALWAYS include traceability table
- ALWAYS specify "done when" for each task
- NEVER leave storage/state machine implicit
- NEVER proceed without PRD + Kiro specs

**Output:** `[project]/_handoff/PROPOSAL_FINAL.md`

**Full playbook:** `agent-skills-library/playbooks/propose/README.md`
