---
name: judge
description: Issue final PASS/FAIL verdict before merge. Use after audit passes to verify against PRD, check integration, and ensure production-readiness.
---

# Judge

> **Adapter for:** `playbooks/judge/`

---

## When to Activate

**User signals:**
- "review this code"
- "ready for verdict"
- "can this merge?"
- "final review"
- "/judge"

**Context:**
- After `/audit` passes (P1 = 0)
- After Floor Manager marks done
- Before merge to main

---

## Required Inputs

- [ ] PRD.md (original intent)
- [ ] PROPOSAL_FINAL.md (implementation plan)
- [ ] Traceability table (from trace)
- [ ] DEPENDENCIES.md (infrastructure check)

**Do not proceed without all inputs.**

---

## The Checklist (Summary)

### Industrial Hardening
- [ ] No hardcoded paths
- [ ] No bare except:pass
- [ ] No secrets in code
- [ ] Subprocess has timeout + check=True
- [ ] Atomic writes for critical files

### Source Traceability
- [ ] Every PRD requirement accounted for
- [ ] Status: IMPLEMENTED / DESCOPED / DEFERRED
- [ ] No silent drops

### Code Quality
- [ ] Imports resolve
- [ ] App starts
- [ ] No syntax errors

### Integration ("No Dangling Wires")
- [ ] Trace one item through full pipeline
- [ ] State transitions work
- [ ] Data appears where expected

### Production Hardening
- [ ] Dependencies pinned
- [ ] Tests exist with real assertions
- [ ] External deps mocked

---

## Verdicts

| Verdict | When |
|---------|------|
| **PASS** | All checks pass |
| **FAIL** | Any requirement missing or hardening violated |
| **HALT** | Security issue or architecture problem |

---

## Output Format

```markdown
## Judge Verdict: [Feature]

**Verdict:** PASS / FAIL / HALT

### Summary
[1-2 sentences]

### Issues Found
| Severity | Issue | Location |
|----------|-------|----------|
| [level] | [issue] | [file:line] |

### Required Actions (if FAIL)
1. [Action]
```

---

## FAIL Protocol

1. Document issues
2. Return to Floor Manager
3. Floor Manager fixes
4. Re-run `/audit`
5. Return to `/judge`

---

## Constraints

- ALWAYS verify against original PRD
- ALWAYS check traceability
- ALWAYS document issues precisely
- NEVER skip to PASS with "TODO" notes
- NEVER proceed to merge with known FAIL

**Full playbook:** `agent-skills-library/playbooks/judge/README.md`
