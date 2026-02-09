---
name: audit
description: Run automated code review before Judge verdict. Use after implementation to catch security issues, hardcoded paths, and code quality problems.
---

# Audit

> **Adapter for:** `playbooks/audit/`

---

## When to Activate

**User signals:**
- "run code review"
- "audit this code"
- "check before merge"
- "ready for review"
- "/audit"

**Context:**
- After implementation complete
- After `pt tasks done`
- Before Judge review

---

## Run the Audit

```bash
python $PROJECTS_ROOT/project-tracker/scripts/warden_audit.py --project-path .
```

---

## Severity Levels

| Level | Action |
|-------|--------|
| P1 | **FAIL** - Must fix |
| P2 | Warn - Note for Judge |
| P3 | Info - Optional fix |

---

## Common P1 Issues

| Issue | Bad | Good |
|-------|-----|------|
| Hardcoded path | `/Users/erik/...` | `os.getenv("PROJECT_ROOT")` |
| Secret in code | `api_key = "sk-..."` | `os.getenv("API_KEY")` |
| Dangerous delete | `os.remove(f)` | `send2trash(f)` |
| Bare except | `except: pass` | `except Error as e: log` |

---

## Output Format

```markdown
## Audit Results: [Feature]

**Status:** PASS / FAIL

### P1 Errors (Must Fix)
- [ ] [file:line] [issue]

### P2 Warnings (For Judge)
- [file:line] [issue]

### Summary
- P1: [count] (must be 0)
- P2: [count]
- P3: [count]
```

---

## Workflow

1. Run audit
2. Fix all P1 issues
3. Re-run until P1 = 0
4. Proceed to /judge

---

## Constraints

- ALWAYS run audit before Judge
- ALWAYS fix P1 issues
- ALWAYS document P2 for Judge
- NEVER skip or suppress P1 errors
- NEVER proceed with P1 count > 0

**Next:** `/judge` for final verdict

**Full playbook:** `agent-skills-library/playbooks/audit/README.md`
