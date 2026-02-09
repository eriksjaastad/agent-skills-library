# Judge Playbook

> **Tool-agnostic instructions for Phase 5: Final Verdict**

## Purpose

Final PASS/FAIL verdict before merge. The Judge reviews code from Floor Manager, verifies against PRD intent, and ensures production-readiness.

**Key insight:** Judge reviews against the ORIGINAL PRD, not just the Proposal. Requirements lost in translation must be caught here.

---

## When to Use

- After implementation is complete
- After audit passes (P1 = 0)
- Before merge to main
- When Floor Manager marks work as done

---

## Required Inputs

The Judge MUST have access to:
- `PRD.md` - Original source of truth
- `PROPOSAL_FINAL.md` - Implementation plan
- Traceability table (from Phase 2.5)
- `_handoff/DEPENDENCIES.md` - Infrastructure check

**Do not proceed without all four inputs.**

---

## The Judge Checklist

### 1. Industrial Hardening (Governance)

| Check | What to Verify |
|-------|----------------|
| M1: Path Standards | No machine-specific absolute paths |
| M2: Error Handling | No silent `except: pass` patterns |
| M3: Security | No API keys or secrets in code |
| H1: Subprocess Integrity | All `subprocess.run` use `check=True` and `timeout` |
| H3: Atomic Writes | Critical file updates use temp-and-rename pattern |

### 2. Source Traceability ("Nothing Lost" Check)

| Check | What to Verify |
|-------|----------------|
| PRD Audit | Every PRD requirement accounted for in final code |
| Status | Each requirement is: IMPLEMENTED, DESCOPED, or DEFERRED |
| Traceability | Table from Phase 2.5 matches final implementation |
| No Silent Drops | No PRD requirement vanished without documentation |

### 3. Code Quality

- [ ] No hardcoded paths (machine-specific)
- [ ] No exposed secrets
- [ ] All imports resolve
- [ ] App starts without error
- [ ] No obvious syntax errors

### 4. Requirement Coverage

- [ ] All PROPOSAL_FINAL.md requirements implemented
- [ ] Traceability table verified (if exists)
- [ ] No requirements silently dropped
- [ ] DESCOPED items documented with reason

### 5. Integration Verification ("No Dangling Wires")

- [ ] Trace one item through full pipeline (create → process → output)
- [ ] All state transitions work (draft → pending → approved → published)
- [ ] Data appears where expected (correct tables, correct files)
- [ ] All APIs callable with expected responses
- [ ] UI connects to backend (if applicable)

### 6. Production Hardening

**Dependencies & Environment:**
- [ ] Dependencies pinned to specific versions
- [ ] Virtual environment properly configured
- [ ] Secrets in `.env` or Doppler, not code

**File Operations:**
- [ ] Critical writes use atomic pattern
- [ ] Write operations validated before success
- [ ] Destructive scripts have `--dry-run` flag

**Process & Shell:**
- [ ] `subprocess.run()` includes timeout
- [ ] Subprocess uses `check=True` or explicit error handling
- [ ] No silent `except: pass`

**Testing:**
- [ ] Every component has test coverage
- [ ] Tests verify specific values (no weak assertions)
- [ ] External dependencies mocked
- [ ] At least one integration test
- [ ] TEST_SUITE.md documents coverage

---

## Verdict Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | All checklist items verified, or minor issues that don't block |
| **FAIL** | Any requirement missing, integration broken, critical path untested, PRD requirement missing without DESCOPED, hardening violated |
| **HALT** | Security issue, scope creep, fundamental architecture problem |

---

## Red Flags (Stop and Fail)

| Red Flag | Question to Ask |
|----------|-----------------|
| Proposal has fewer requirements than PRD | "Where did REQ-XXX go? Why not DESCOPED?" |
| Empty traceability columns | "Why no implementation file or test for this?" |
| Missing infrastructure code | "PRD required pipeline/notifications - where?" |
| Broken data lifecycle | "Can I trace data from creation to destination?" |

---

## Output Format

```markdown
## Judge Verdict: [Feature]

**Date:** YYYY-MM-DD
**Verdict:** PASS / FAIL / HALT

### Summary
[1-2 sentence summary of review]

### Checklist Results

#### Industrial Hardening
- [x] M1: Path Standards
- [x] M2: Error Handling
- [ ] M3: Security - FAIL: API key in config.py:42

#### Source Traceability
- [x] PRD Audit complete
- [x] All requirements traced

#### Code Quality
- [x] No hardcoded paths
- [x] All imports resolve

#### Requirement Coverage
- [x] All PROPOSAL requirements implemented
- [x] DESCOPED items documented

#### Integration Verification
- [x] Full pipeline traced
- [x] State transitions verified

#### Production Hardening
- [x] Dependencies pinned
- [ ] Missing timeout on subprocess - line 87

### Issues Found
| Severity | Issue | Location |
|----------|-------|----------|
| FAIL | API key in code | config.py:42 |
| WARN | Missing timeout | worker.py:87 |

### Verdict Rationale
[Why PASS/FAIL/HALT]

### Required Actions (if FAIL)
1. [Action 1]
2. [Action 2]
```

---

## FAIL Protocol

On FAIL:
1. Document specific issues
2. Return to Floor Manager with feedback
3. Floor Manager fixes issues
4. Re-run audit (`/audit`)
5. Return to Judge for re-review

**Do NOT:**
- Skip issues to get to PASS
- Mark FAIL as PASS with "TODO" notes
- Proceed to merge with known issues

---

## HALT Protocol

On HALT:
1. Stop all work immediately
2. Create `HALT.md` with details
3. Notify Erik (Conductor)
4. Do not resume until HALT resolved

---

## Role Boundaries

**Judge (this skill):**
- Reviews completed work
- Verifies against PRD
- Issues PASS/FAIL/HALT
- Documents issues

**NOT Judge's job:**
- Fixing code (that's Floor Manager)
- Changing requirements (that's PRD)
- Descoping features (that's Super Manager)

---

## Related

- `/audit` skill for automated code review (runs before Judge)
- `/work` skill for implementation (Floor Manager)
- REVIEWS_AND_GOVERNANCE_PROTOCOL.md for full standards
- Project-workflow.md for complete workflow context
