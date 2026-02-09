---
name: performance-oracle
description: Performance-focused code review identifying algorithmic complexity, N+1 queries, memory issues, and optimization opportunities. Use when reviewing performance-sensitive code or investigating slowdowns.
---

# Performance Oracle

> **Adapter for:** `playbooks/performance-oracle/`

---

## When to Activate

**User signals:**
- "review this for performance"
- "is this efficient?"
- "optimize this code"
- "why is this slow?"
- "/performance-oracle"

**Best for:**
- Data processing code
- Database queries
- API endpoints
- Loops and algorithms
- Memory-intensive operations

---

## Review Focus

### Complexity
- Nested loops? O(n^2)?
- List lookups? Use sets?
- Sorting in loops?

### Database
- N+1 queries?
- Missing eager loading?
- Unbounded queries?

### I/O
- Sequential requests?
- Blocking calls?
- Missing pooling?

### Memory
- Loading all data?
- Unbounded growth?
- String concat in loops?

---

## Output Format

```markdown
## Performance Review: [target]

### Critical Issues
- **[Issue Type]** at [location]
  - Impact: [what happens at scale]
  - Fix: [specific optimization]

### High Issues
[same format]

### Medium Issues
[same format]

### Optimization Opportunities
- [Non-critical improvements]

### Summary
- **Risk Level:** [Critical/High/Medium/Low]
- **Key Concerns:** [1-2 sentences]
- **Quick Wins:** [easy high-impact fixes]
```

---

## Severity Guide

| Level | Meaning |
|-------|---------|
| Critical | Will cause outages at scale |
| High | Noticeable slowdown |
| Medium | Suboptimal but works |
| Low | Micro-optimization |

---

## Quick Checks

```
[ ] No nested loops over same data
[ ] No queries inside loops
[ ] Pagination on list endpoints
[ ] Caching for expensive operations
[ ] Concurrent I/O where beneficial
[ ] No unbounded memory growth
```

---

## Constraints

- ALWAYS check for N+1 queries
- ALWAYS note Big O complexity
- ALWAYS suggest specific fixes
- NEVER just say "looks fine" without analysis

**Full playbook:** `agent-skills-library/playbooks/performance-oracle/README.md`
