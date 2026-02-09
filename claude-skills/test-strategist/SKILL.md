---
name: test-strategist
description: Test coverage review identifying missing tests, quality issues, and flaky test risks. Use when reviewing test suites, planning test strategy, or investigating test failures.
---

# Test Strategist

> **Adapter for:** `playbooks/test-strategist/`

---

## When to Activate

**User signals:**
- "what tests are missing?"
- "review these tests"
- "is this well tested?"
- "why didn't tests catch this?"
- "/test-strategist"

**Best for:**
- PR reviews (test coverage)
- Post-bug analysis
- Test suite health checks
- New feature planning
- Flaky test investigation

---

## Review Focus

### Coverage
- Happy path tested?
- Error paths tested?
- Edge cases (empty, null, boundary)?

### Quality
- Assertions specific?
- Tests independent?
- Mocks minimal?

### Reliability
- Time-dependent logic?
- Shared state?
- Non-deterministic?

---

## Output Format

```markdown
## Test Review: [target]

### Missing Coverage
- **[Feature/Path]**: [what's untested]
  - Risk: [what could break]
  - Suggested: [test to add]

### Quality Issues
- **[Test Name]**: [problem]
  - Fix: [improvement]

### Flaky Risks
- **[Test Name]**: [cause]
  - Fix: [how to stabilize]

### Summary
- **Coverage:** [Good/Moderate/Poor]
- **Quality:** [Strong/Adequate/Weak]
- **Priority Gaps:** [top missing tests]
```

---

## Severity Guide

| Level | Meaning |
|-------|---------|
| Critical | Core functionality untested |
| High | Important path missing |
| Medium | Edge cases not covered |
| Low | Quality improvement |

---

## Quick Checks

```
[ ] Happy path tested
[ ] Error paths tested
[ ] Edge cases covered
[ ] Specific assertions
[ ] Independent tests
[ ] No time dependencies
[ ] Minimal mocking
```

---

## Constraints

- ALWAYS check happy, error, and edge paths
- ALWAYS note missing critical coverage
- ALWAYS suggest specific tests to add
- NEVER just say "tests look fine" without analysis

**Full playbook:** `agent-skills-library/playbooks/test-strategist/README.md`
