---
name: trace
description: Verify PRD to Kiro traceability after spec generation. Use after Kiro creates specs to ensure no requirements were lost or silently descoped.
---

# Trace

> **Adapter for:** `playbooks/trace/`

---

## When to Activate

**User signals:**
- "check traceability"
- "verify Kiro output"
- "did we lose anything?"
- "trace the requirements"
- "/trace"

**Context:**
- After Kiro generates specs
- Before creating PROPOSAL_FINAL.md
- When reviewing spec completeness

---

## The Check

Verify the chain:
```
PRD Intent → Kiro Requirement → Kiro Task
```

---

## Quick Checklist

### Coverage
- [ ] Every PRD goal → EARS requirements
- [ ] Every PRD constraint → design.md
- [ ] Human touchpoints → tasks.md

### Orphans
- [ ] No tasks without PRD source
- [ ] No design contradicting constraints

### Descopes
- [ ] Dropped items documented as DESCOPED
- [ ] No "TBD", "later", "future" without reason

---

## Output Format

```markdown
## Traceability Check: [Feature]

### Status: [TRACED / GAPS / BLOCKED]

### Coverage Table
| PRD Intent | Kiro Requirement | Kiro Task | Status |
|------------|------------------|-----------|--------|
| [Goal 1] | REQ-1.1 | Task 1 | ✓ |
| [Goal 2] | REQ-2.1-2.3 | Task 2, 3 | ✓ |
| [Constraint: Security] | Design section 3 | Task 4 | ✓ |
| [Goal 3: Notifications] | — | — | DESCOPED |

### Gaps Found
- [Gap description and recommended action]

### Descoped Items
- [Item]: [Reason for descope]
```

---

## Red Flags

| Flag | Meaning |
|------|---------|
| PRD goal with no requirements | Kiro missed it |
| Task with no PRD source | Scope creep |
| "TBD" in tasks.md | Unresolved work |
| Constraint not in design | Will cause issues |

---

## Constraints

- ALWAYS compare PRD goals to Kiro requirements
- ALWAYS document descoped items
- ALWAYS flag "TBD/later/future" in tasks
- NEVER proceed to /propose with gaps unflagged

**Full playbook:** `agent-skills-library/playbooks/trace/README.md`
