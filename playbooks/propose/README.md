# Propose Playbook

> **Tool-agnostic instructions for Phase 3: Proposal Creation**

## Purpose

Convert Kiro specs into a PROPOSAL_FINAL.md for Agent Hub execution. This is the final Super Manager deliverable before handoff.

**Key insight:** The proposal must re-expand "compressed" infrastructure details. Generic "implement feature" tasks lead to island features.

---

## When to Use

- After traceability check passes (Phase 2.5)
- Before handoff to Floor Manager
- When converting Kiro tasks.md to Agent Hub format

---

## Inputs Required

1. **PRD.md** - Original source of truth (intent + constraints)
2. **.kiro/specs/[feature]/requirements.md** - EARS requirements
3. **.kiro/specs/[feature]/design.md** - Technical architecture
4. **.kiro/specs/[feature]/tasks.md** - Implementation tasks
5. **Traceability table** - From Phase 2.5

---

## Infrastructure Mandate

**CRITICAL:** The proposal MUST explicitly include these sections. They often get compressed in Kiro and need re-expansion.

### 1. Storage Strategy
- Specific paths for file storage (`data/pending/`, `data/exports/`)
- Database tables and their schemas
- How data moves between storage locations

### 2. State Machine
- All lifecycle states (`draft` → `pending` → `approved` → `published`)
- Exact transitions and triggers
- What happens in each state

### 3. Publishing Pipeline
- How approved content goes live
- Physical mechanism ("Script X moves file Y to folder Z")
- API calls, webhooks, or file operations

### 4. Notification Events
- What events trigger alerts
- Who gets notified
- Which channels (Discord, email, etc.)

---

## Proposal Structure

```markdown
# PROPOSAL_FINAL.md

## Feature: [Name]
**Date:** YYYY-MM-DD
**PRD:** [link to PRD.md]
**Kiro Specs:** .kiro/specs/[feature]/

---

## Objective
[Clear statement from PRD - what we're building and why]

---

## Acceptance Criteria
[From requirements.md - what must be true when done]
- [ ] Criterion 1
- [ ] Criterion 2

---

## Technical Design Summary
[Key decisions from design.md]

### Storage Strategy
- Files: [paths]
- Database: [tables/collections]

### State Machine
```
[state] → [transition] → [state]
```

### Publishing Pipeline
[How approved content goes live]

### Notification Events
| Event | Recipient | Channel |
|-------|-----------|---------|
| [event] | [who] | [how] |

---

## Implementation Tasks
[From tasks.md - in execution order]

### Task 1: [Name]
- **Goal:** [what this accomplishes]
- **Files:** [files to create/modify]
- **Done when:** [specific criteria]

### Task 2: [Name]
...

---

## Traceability
[Table from Phase 2.5]

| PRD Intent | Requirement | Task | File | Test |
|------------|-------------|------|------|------|
| ... | ... | ... | ... | ... |

---

## Dependencies
[What must exist before execution - feeds DEPENDENCIES.md]

---

## Out of Scope
[Explicitly what this proposal does NOT include]
```

---

## Proposal Completeness Checklist

Before finalizing:

### Infrastructure
- [ ] Storage locations explicitly documented
- [ ] State machine with all transitions
- [ ] Publishing mechanism specified
- [ ] Notification triggers defined
- [ ] External service dependencies listed

### Traceability
- [ ] Every PRD goal accounted for
- [ ] Descoped items documented with reason
- [ ] Tasks trace to requirements

### Execution Readiness
- [ ] Tasks ordered correctly (dependencies respected)
- [ ] Each task has clear "done when" criteria
- [ ] Files to modify are identified

---

## Red Flags (Stop and Fix)

| Red Flag | Question to Ask |
|----------|-----------------|
| "the database" without schema | What are the actual tables? |
| No state transitions | How does data move through the system? |
| Publishing mentioned without mechanism | What is the physical act of publishing? |
| "Notifications" without events | What triggers what alert to whom? |
| Tasks focus only on logic | Where's the plumbing code? |

---

## Output

**File:** `[project]/_handoff/PROPOSAL_FINAL.md`

**Next Phase:** Phase 4 (Handoff) - Verify infrastructure exists

---

## Template Location

Use: `_tools/agent-hub/templates/PROPOSAL_FINAL.template.md`

---

## Role Boundaries

**Super Manager (this skill):**
- Creates PROPOSAL_FINAL.md
- Re-expands compressed infrastructure
- Ensures traceability
- Prepares for handoff

**NOT Super Manager's job:**
- Writing code (that's Workers)
- Executing tasks (that's Floor Manager)
- Verifying infrastructure exists (that's /handoff)

---

## Related

- `/trace` skill for Phase 2.5 traceability
- `/handoff` skill for Phase 4 infrastructure verification
- Project-workflow.md Phase 3 section
- PROPOSAL_FINAL.template.md for full template
