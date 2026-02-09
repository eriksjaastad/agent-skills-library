# Trace Playbook

> **Tool-agnostic instructions for Phase 2.5: Traceability Check**

## Purpose

Ensure no PRD intent gets lost between PRD → Kiro → Implementation. This is the verification step after Kiro generates specs but before creating the Proposal.

**Key insight:** Information compression is the enemy. Requirements disappear as they pass through the pipeline.

---

## When to Use

- After Kiro generates requirements.md, design.md, tasks.md
- Before creating PROPOSAL_FINAL.md
- When reviewing Kiro output for completeness
- After any spec regeneration

---

## The Traceability Chain

```
PRD Intent → Kiro Requirement → Kiro Task → Implementation File → Test
```

Every item in the PRD must trace forward. Every item in tasks.md must trace backward.

---

## Traceability Checklist

### Coverage Check
- [ ] Every PRD goal has corresponding EARS requirements in requirements.md
- [ ] Every PRD constraint (security, performance, tech stack) is reflected in design.md
- [ ] Human touchpoints from PRD have corresponding tasks in tasks.md
- [ ] Integration context from PRD appears in design.md

### Orphan Check
- [ ] No "orphan" tasks that don't trace back to a PRD goal or constraint
- [ ] No design decisions that contradict PRD constraints

### Descope Check
- [ ] If intent was descoped, it's documented as "DESCOPED: [reason]"
- [ ] No requirements silently dropped
- [ ] Search tasks.md for "TBD", "later", "future" - flag these

### Test Coverage Check
- [ ] Critical user stories have identified test coverage in tasks.md

---

## Traceability Table (Recommended for Complex Features)

Create this table to track coverage:

```markdown
| PRD Intent | Kiro Requirement | Kiro Task | Implementation | Test |
|------------|------------------|-----------|----------------|------|
| Goal: User login | REQ-1.1, REQ-1.2 | Task 1.2 | src/auth.py | test_auth.py |
| Goal: Admin dashboard | REQ-2.1-2.4 | Task 2.1, 2.3 | src/admin.py | test_admin.py |
| Constraint: JWT auth | Design decision | Task 1.1 | src/auth.py | — |
| Goal: Email alerts | DESCOPED | — | — | — |
```

**This table becomes the Judge's checklist in Phase 5.**

---

## Kiro Output Validation

Before leaving Kiro, verify:

| Check | How | Red Flag |
|-------|-----|----------|
| Goals covered | Each PRD goal has EARS requirements | Missing goal coverage |
| Constraints honored | Security, tech stack reflected in design.md | Constraints ignored |
| Integration addressed | External services appear in design.md | Integration missing |
| Human touchpoints | Review/approval flows have tasks | No human review tasks |
| No deferrals | Search for "TBD", "later", "future" | Work being descoped |
| Non-goals respected | Nothing builds what PRD said NOT to build | Scope creep |

**If any check fails:** Go back to Kiro chat and address the gap.

---

## Common Losses to Watch For

### The Silent Descope
PRD says "email notifications" → Kiro has no email tasks → No one notices until production

**Fix:** Explicit DESCOPED documentation required

### The Compressed Requirement
PRD says "recipes go through approval before publishing" → Kiro tasks just say "implement approval" → No state machine, no transitions

**Fix:** Verify state machine and transitions in design.md

### The Missing Plumbing
PRD mentions "save to database" → Kiro assumes table exists → Implementation fails at runtime

**Fix:** Check design.md includes all schema changes

### The Orphan Task
Kiro generates "refactor auth module" → Not in PRD → Scope creep

**Fix:** Every task traces to PRD goal or constraint

---

## Output

**Deliverable:** Traceability table (in PROPOSAL_FINAL.md)

**Status:**
- TRACED: All PRD intent accounted for
- GAPS: Document gaps before proceeding
- BLOCKED: Kiro rework needed

**Next Phase:** Phase 3 (Propose) - Create PROPOSAL_FINAL.md

---

## Role Boundaries

**Super Manager (this skill):**
- Reviews Kiro output against PRD
- Creates traceability table
- Documents descopes
- Flags gaps

**NOT Super Manager's job:**
- Fixing Kiro specs (ask Kiro to regenerate)
- Writing code
- Making architectural decisions (that's Kiro)

---

## Related

- `/strategy` skill for Phase 1 PRD creation
- `/propose` skill for Phase 3 proposals
- Project-workflow.md Phase 2.5 section
