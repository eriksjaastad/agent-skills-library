# Audit Playbook

> **Tool-agnostic instructions for Phase 5: Code Review Gate**

## Purpose

Run automated code review before Judge review. This is the quality gate between implementation and final approval.

**Key insight:** Run code review immediately after implementation, not at midnight when exhausted. Catch 90% of issues before Judge sees the code.

---

## When to Use

- After implementation is complete
- Before Judge review
- After `pt tasks done [id]`
- When code is ready for review

---

## The Audit Tool

**Primary tool:** `warden_audit.py`

```bash
# From project root
python $PROJECTS_ROOT/project-tracker/scripts/warden_audit.py --project-path $PROJECT_ROOT

# Or if project has its own
python scripts/warden_audit.py
```

---

## What It Checks

### P1 - Blocking (Must Fix)
- Hardcoded absolute paths (`/Users/erik/...`)
- Secrets in code (API keys, tokens)
- Dangerous functions without safety (`rm`, `unlink`, `shutil.rmtree`)
- Security issues (SQL injection patterns, command injection)
- Bare `except: pass` error swallowing

### P2 - Warning (Should Fix)
- Missing error handling
- Subprocess without timeout
- Non-atomic file writes
- Missing type hints on public functions

### P3 - Info (Nice to Fix)
- Documentation gaps
- Code style issues
- Minor optimizations

---

## Severity Actions

| Severity | Action |
|----------|--------|
| P1 (Blocking) | **FAIL** - Must fix before Judge review |
| P2 (Warning) | Log for Judge, but proceed |
| P3 (Info) | Note in review, no action required |

---

## Audit Workflow

### 1. Run the Audit
```bash
python scripts/warden_audit.py --project-path .
```

### 2. Review Output
```
=== WARDEN AUDIT RESULTS ===

P1 ERRORS (Blocking):
- [file:line] Hardcoded path: /Users/erik/projects/...
- [file:line] Bare except:pass found

P2 WARNINGS:
- [file:line] subprocess.run without timeout

P3 INFO:
- [file:line] Missing docstring
```

### 3. Fix P1 Issues
All P1 issues must be resolved before proceeding.

### 4. Document P2 for Judge
Note warnings for Judge review but don't block.

### 5. Proceed to Judge
When P1 count = 0, ready for `/judge`.

---

## Common P1 Issues

### Hardcoded Paths
```python
# BAD
path = "/Users/erik/projects/myapp/data/"

# GOOD
path = os.path.join(os.getenv("PROJECT_ROOT", "."), "data")
```

### Secrets in Code
```python
# BAD
api_key = "sk-live-abc123..."

# GOOD
api_key = os.getenv("API_KEY")
```

### Dangerous Functions
```python
# BAD
os.remove(file)
shutil.rmtree(dir)

# GOOD
send2trash.send2trash(file)
# Or use trash CLI
```

### Bare Except
```python
# BAD
try:
    risky_operation()
except:
    pass

# GOOD
try:
    risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

---

## Output Format

```markdown
## Audit Results: [Feature/PR]

**Date:** YYYY-MM-DD
**Status:** PASS / FAIL

### P1 Errors (Blocking)
- [ ] Fixed: [file:line] [issue description]

### P2 Warnings (For Judge)
- [file:line] [issue description]

### P3 Info
- [file:line] [issue description]

### Summary
- P1: [count] (must be 0 to proceed)
- P2: [count]
- P3: [count]
```

---

## When Audit Fails

1. **Fix all P1 issues**
2. Re-run audit
3. Repeat until P1 count = 0
4. Then proceed to Judge

**Do NOT:**
- Skip the audit
- Suppress P1 errors
- Mark P1 as P2 to proceed

---

## Integration with Agent Hub

If using Antigravity/Agent Hub:
- Audit runs automatically after implementation
- P1 failures return to Floor Manager
- Judge only sees code that passes P1

---

## Role Boundaries

**Floor Manager (this skill):**
- Runs audit tool
- Fixes P1 issues
- Documents P2 for Judge
- Confirms ready for review

**NOT Floor Manager's job:**
- Final approval (that's Judge)
- Changing audit rules
- Suppressing errors

---

## Related

- `/work` skill for implementation
- `/judge` skill for final verdict (next step)
- warden_audit.py documentation
- REVIEWS_AND_GOVERNANCE_PROTOCOL.md
