# Performance Oracle Playbook

> **Tool-agnostic instructions for performance-focused code review**

## Purpose

Identify performance issues and optimization opportunities:
1. Algorithmic complexity (Big O)
2. Memory usage and leaks
3. I/O bottlenecks
4. Caching opportunities
5. Database query efficiency

---

## When to Use

- Reviewing code that processes large datasets
- Before deploying high-traffic endpoints
- When users report slow performance
- During optimization sprints
- Reviewing loops, recursion, or data structures

---

## Review Checklist

### 1. Algorithmic Complexity

#### Time Complexity
```python
# BAD - O(n^2) nested loop
for item in items:
    if item in other_list:  # O(n) lookup each time
        process(item)

# GOOD - O(n) with set lookup
other_set = set(other_list)  # O(n) once
for item in items:
    if item in other_set:  # O(1) lookup
        process(item)
```

**Check for:**
- Nested loops over same data
- Repeated list/array searches (use sets/dicts)
- Sorting inside loops
- Recursive calls without memoization

#### Space Complexity
```python
# BAD - loads all into memory
data = file.read()  # Entire file in memory

# GOOD - streaming/chunked
for line in file:  # One line at a time
    process(line)
```

**Check for:**
- Loading entire files/datasets into memory
- Unbounded list growth
- Deep recursion (stack overflow risk)
- Large intermediate data structures

### 2. Database Queries

#### N+1 Queries
```python
# BAD - N+1 problem
users = User.all()
for user in users:
    print(user.orders.count())  # Query per user

# GOOD - eager loading
users = User.all().prefetch_related('orders')
for user in users:
    print(len(user.orders))  # No extra queries
```

**Check for:**
- Queries inside loops
- Missing `select_related` / `prefetch_related`
- `SELECT *` when only few columns needed
- Missing indexes on filtered/joined columns
- Unbounded queries (missing LIMIT)

#### Query Efficiency
```python
# BAD - fetch all, filter in Python
all_users = User.objects.all()
active = [u for u in all_users if u.is_active]

# GOOD - filter in database
active = User.objects.filter(is_active=True)
```

### 3. I/O Operations

#### Blocking I/O
```python
# BAD - sequential API calls
results = []
for url in urls:
    results.append(fetch(url))  # Blocks each time

# GOOD - concurrent
import asyncio
results = await asyncio.gather(*[fetch(url) for url in urls])
```

**Check for:**
- Sequential HTTP requests (batch or parallelize)
- Synchronous file I/O in async context
- Missing connection pooling
- Unbuffered I/O operations

### 4. Caching Opportunities

**Check for:**
- Repeated expensive computations
- Frequently accessed, rarely changed data
- API responses that could be cached
- Missing memoization on pure functions

```python
# GOOD - memoization
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation(n):
    # ...
```

### 5. Memory Management

**Check for:**
- Circular references preventing GC
- Global caches without size limits
- Large objects held longer than needed
- String concatenation in loops (use join)

```python
# BAD - O(n^2) string concatenation
result = ""
for item in items:
    result += str(item)

# GOOD - O(n) with join
result = "".join(str(item) for item in items)
```

### 6. Frontend Performance

**Check for:**
- Large bundle sizes (code splitting needed?)
- Render-blocking resources
- Unnecessary re-renders (React memo, useMemo)
- Missing lazy loading for images/components
- Layout thrashing (forced reflows)

---

## Common Anti-Patterns

| Anti-Pattern | Impact | Fix |
|--------------|--------|-----|
| N+1 queries | DB overload | Eager loading |
| Nested loops | O(n^2) or worse | Use hashmaps/sets |
| Load all data | Memory exhaustion | Pagination/streaming |
| String concat in loop | O(n^2) | Use join() |
| Sync I/O in async | Thread blocking | Use async equivalents |
| No pagination | Slow queries | Add LIMIT/OFFSET |
| SELECT * | Wasted bandwidth | Select needed columns |

---

## Output Format

```markdown
## Performance Review: [file/PR]

### Critical Issues
- **[Issue Type]** at [location]
  - Impact: [specific performance impact]
  - Current: O(n^2) / 100ms per request / etc.
  - Suggested: O(n) / batch queries / etc.
  - Fix: [specific code change]

### High Issues
[same format]

### Medium Issues
[same format]

### Optimization Opportunities
- [Potential improvement that isn't critical]

### Metrics to Watch
- [Specific metrics to monitor after changes]

### Summary
- **Risk Level:** [Critical/High/Medium/Low]
- **Key Concerns:** [1-2 sentences]
- **Quick Wins:** [easy fixes with high impact]
```

---

## Severity Levels

| Level | Criteria |
|-------|----------|
| Critical | Will cause outages/timeouts at scale |
| High | Noticeable slowdown, scalability blocker |
| Medium | Suboptimal but functional |
| Low | Micro-optimization opportunity |

---

## Quick Checks

```
[ ] No nested loops over same data
[ ] Database queries not in loops
[ ] Pagination on list endpoints
[ ] Caching for repeated computations
[ ] Async/concurrent I/O where beneficial
[ ] No unbounded memory growth
[ ] Indexes on filtered/sorted columns
[ ] Connection pooling configured
```

---

## Related

- security-sentinel skill for security review
- test-strategist skill for test coverage
- Database-specific optimization guides
