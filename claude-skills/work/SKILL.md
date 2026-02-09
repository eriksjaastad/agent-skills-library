---
name: work
description: Execute implementation tasks against tracked Kanban items. Use when implementing code during Phase 5 execution.
---

# Work

> **Adapter for:** `playbooks/work/`

---

## When to Activate

**User signals:**
- "implement this"
- "start working on [task]"
- "write the code"
- "execute the proposal"
- "/work"

**Context:**
- After handoff is complete
- Task is ready in Kanban
- During active implementation

---

## Pre-Work

1. Verify handoff complete (DEPENDENCIES.md = READY)
2. Claim task: `pt tasks start [id]`
3. Read PROPOSAL_FINAL.md

---

## Workflow

```bash
# Start
pt tasks start [id]

# Work
# - Follow proposal tasks
# - Write to _handoff/drafts/
# - Commit with task ID

# Complete
pt tasks done [id]
```

---

## Code Standards

- [ ] No hardcoded paths
- [ ] No exposed secrets
- [ ] Imports resolve
- [ ] Tests pass
- [ ] Error handling present
- [ ] Subprocess has timeout

---

## Commit Format

```
type(scope): description (#task-id)

feat(auth): Add JWT validation (#4532)
fix(api): Handle null response (#4533)
```

---

## Output Location

```
_handoff/
└── drafts/      # Code goes here first
    ├── src/
    └── tests/
```

---

## When Stuck

| Problem | Action |
|---------|--------|
| Missing context | Check PROPOSAL_FINAL.md |
| Missing infrastructure | Return to /handoff |
| Test failures | Fix code, not tests |

---

## Constraints

- ALWAYS claim task before working
- ALWAYS reference task ID in commits
- ALWAYS write to drafts/ sandbox first
- NEVER work without a tracked task
- NEVER skip the audit step after

**Next:** `/audit` for code review gate

**Full playbook:** `agent-skills-library/playbooks/work/README.md`
