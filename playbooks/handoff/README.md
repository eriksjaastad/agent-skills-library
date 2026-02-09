# Handoff Playbook

> **Tool-agnostic instructions for Phase 4: Pre-Execution Verification**

## Purpose

Verify that all infrastructure exists before handing off to the Floor Manager. This is the final gate - the "ground" must be ready for the "building."

**Key insight:** Worker agents are optimistic. If the proposal says "save to database," they assume the table exists. Verify before handoff.

---

## When to Use

- After PROPOSAL_FINAL.md is complete
- Before Floor Manager begins execution
- When all planning is done and ready for implementation

---

## The Handoff Boundary

**After this phase, Super Manager steps back.**

The handoff is complete when:
1. Infrastructure is verified
2. DEPENDENCIES.md is created
3. Files are placed in `_handoff/`
4. Floor Manager takes over

---

## Pre-Handoff Verification Checklist

### Database Readiness
- [ ] All tables/collections referenced in proposal exist
- [ ] OR: Their creation is explicitly Task 1 in the proposal
- [ ] Schema matches what design.md specifies

**Check:**
```bash
# For SQLite
sqlite3 [database.db] ".tables"
sqlite3 [database.db] ".schema [table_name]"

# For PostgreSQL
psql -c "\dt" [database]
psql -c "\d [table_name]" [database]
```

### External Services
- [ ] All required API keys configured
- [ ] Environment variables set (check `.env` or Doppler)
- [ ] Service accounts have correct permissions

**Check:**
```bash
# Verify env vars exist
grep "API_KEY" .env
doppler secrets get [KEY_NAME] --plain
```

### Directory Structure
- [ ] All output directories exist
- [ ] Write permissions confirmed
- [ ] OR: Directory creation is Task 1

**Check:**
```bash
ls -la data/exports/
ls -la data/pending/
```

### Prerequisite Features
- [ ] Features this depends on are merged
- [ ] Those features passed Judge review
- [ ] Integration points are verified

**Check:**
```bash
# Check git log for merged PRs
git log --oneline --grep="[feature name]"
```

---

## DEPENDENCIES.md Template

Create this file to document verification:

```markdown
# Dependencies Check: [Feature Name]

**Date:** YYYY-MM-DD
**Proposal:** PROPOSAL_FINAL.md
**Status:** READY / BLOCKED

## Database Dependencies

| Table/Collection | Status | Notes |
|------------------|--------|-------|
| `users` | ✓ Exists | — |
| `recipe_reviews` | Create in Task 1 | Migration included |

## External Service Dependencies

| Service | Status | Configuration |
|---------|--------|---------------|
| SendGrid API | ✓ Configured | Doppler: SENDGRID_API_KEY |
| Stripe | BLOCKED | Need API key from Erik |

## File System Dependencies

| Directory | Status | Notes |
|-----------|--------|-------|
| `data/exports/` | ✓ Exists | — |
| `data/pending/` | Create in Task 1 | — |

## Prerequisite Features

| Feature | Status | Reference |
|---------|--------|-----------|
| User auth | ✓ Merged | PR #42 |
| Admin dashboard | ✓ Merged | PR #38 |

## Blockers

| Blocker | Owner | ETA |
|---------|-------|-----|
| Stripe API key | Erik | [date] |

---

**If any blocker exists, handoff DOES NOT PROCEED.**
```

---

## Handoff Checklist

| Dependency Type | What to Check | Status |
|-----------------|---------------|--------|
| Database | Tables exist or Task 1 creates them | ✓ / Create / BLOCKED |
| External API | Service configured | ✓ / BLOCKED |
| Prerequisite | Feature merged | ✓ / BLOCKED |
| File System | Directory exists or Task 1 creates it | ✓ / Create |

---

## BLOCKED Protocol

**If ANY dependency is BLOCKED:**

1. Document the blocker in DEPENDENCIES.md
2. **DO NOT PROCEED** with handoff
3. Return to Phase 3 (Propose) to address blocker
4. Notify Erik with specific blocker details
5. Re-attempt handoff when resolved

**The handoff is complete only when the ground is verified.**

---

## File Placement

When ready, place files in `_handoff/`:

```
[project]/
├── _handoff/
│   ├── PROPOSAL_FINAL.md
│   ├── DEPENDENCIES.md
│   └── drafts/           # Worker output location
```

---

## Output

**Files:**
- `[project]/_handoff/PROPOSAL_FINAL.md`
- `[project]/_handoff/DEPENDENCIES.md`

**Status:** READY or BLOCKED

**Next Phase:** Phase 5 (Execution) - Floor Manager takes over

---

## Role Boundaries

**Super Manager (this skill):**
- Verifies infrastructure exists
- Creates DEPENDENCIES.md
- Places files in _handoff/
- **Steps back after handoff**

**Floor Manager (takes over):**
- Reads PROPOSAL_FINAL.md
- Orchestrates workers
- Executes against the proposal

---

## Related

- `/propose` skill for Phase 3 proposal creation
- `/work` skill for Phase 5 execution (Floor Manager)
- Project-workflow.md Phase 4 section
- DEPENDENCIES.md template
