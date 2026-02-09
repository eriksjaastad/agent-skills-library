# Test Strategist Playbook

> **Tool-agnostic instructions for test coverage review and strategy**

## Purpose

Evaluate and improve test coverage:
1. Identify missing test cases
2. Assess test quality and reliability
3. Recommend testing strategies
4. Review test architecture
5. Spot flaky or brittle tests

---

## When to Use

- Reviewing PRs with new features (what tests are missing?)
- After discovering bugs (why wasn't this caught?)
- During test suite health checks
- Planning test strategy for new projects
- Evaluating test reliability

---

## Review Checklist

### 1. Coverage Analysis

#### Happy Path
- Is the main success case tested?
- Are all return values verified?
- Are side effects checked?

#### Edge Cases
```python
# Test edge cases for a function that processes lists
def test_process_items():
    assert process([]) == []           # Empty input
    assert process([1]) == [1]         # Single item
    assert process([1,2,3]) == [3,2,1] # Normal case
    assert process(None) raises ValueError  # Null input
```

**Check for:**
- Empty inputs ([], "", {}, None)
- Boundary values (0, -1, MAX_INT)
- Single element cases
- Large inputs (stress testing)

#### Error Paths
- Are exceptions tested?
- Are error messages verified?
- Are cleanup/rollback paths tested?

```python
# BAD - only tests happy path
def test_create_user():
    user = create_user("valid@email.com")
    assert user.email == "valid@email.com"

# GOOD - also tests error paths
def test_create_user_invalid_email():
    with pytest.raises(ValidationError) as exc:
        create_user("not-an-email")
    assert "Invalid email" in str(exc.value)
```

### 2. Test Quality

#### Assertions
```python
# BAD - weak assertion
def test_get_users():
    users = get_users()
    assert users  # Only checks truthy

# GOOD - specific assertions
def test_get_users():
    users = get_users()
    assert len(users) == 3
    assert users[0].name == "Alice"
    assert all(u.is_active for u in users)
```

**Check for:**
- Meaningful assertions (not just "assert result")
- Checking specific values, not just types
- Verifying side effects (DB changes, API calls)
- Testing behavior, not implementation

#### Independence
```python
# BAD - tests depend on order
class TestUser:
    def test_create(self):
        self.user = create_user()  # Shared state

    def test_delete(self):
        delete_user(self.user)  # Depends on test_create

# GOOD - independent tests
class TestUser:
    def test_create(self):
        user = create_user()
        assert user.id is not None

    def test_delete(self):
        user = create_user()  # Own setup
        delete_user(user)
        assert User.get(user.id) is None
```

**Check for:**
- Shared mutable state between tests
- Tests that must run in order
- Global state modifications
- Missing cleanup/teardown

### 3. Test Architecture

#### Unit vs Integration
```
Unit Tests:
- Fast, isolated
- Mock external dependencies
- Test single function/class

Integration Tests:
- Test components together
- Use real (test) database
- Test API endpoints end-to-end
```

**Check for:**
- Appropriate test type for what's being tested
- Unit tests that are actually integration tests
- Missing integration tests for critical paths
- Over-mocking hiding real bugs

#### Mocking
```python
# BAD - over-mocking (testing the mock, not the code)
@patch('module.function_a')
@patch('module.function_b')
@patch('module.function_c')
def test_process(mock_a, mock_b, mock_c):
    # What are we even testing?

# GOOD - mock only external boundaries
@patch('module.external_api_client')
def test_process(mock_client):
    mock_client.fetch.return_value = {"data": "test"}
    result = process()
    assert result.status == "success"
```

**Check for:**
- Mocking internal implementation details
- Missing assertions on mock calls
- Mocks returning unrealistic data
- Not resetting mocks between tests

### 4. Test Reliability

#### Flaky Tests
**Common causes:**
- Time-dependent logic
- Race conditions
- External service dependencies
- Random data without seeds
- Order-dependent tests

```python
# BAD - time-dependent, flaky
def test_token_expiry():
    token = create_token()
    time.sleep(2)
    assert token.is_expired()  # Flaky on slow CI

# GOOD - control time
def test_token_expiry(freezer):
    token = create_token()
    freezer.move_to(token.expires_at + timedelta(seconds=1))
    assert token.is_expired()
```

#### Determinism
```python
# BAD - random without seed
def test_shuffle():
    result = shuffle([1,2,3])
    assert result == [2,3,1]  # Fails randomly

# GOOD - seeded random
def test_shuffle():
    random.seed(42)
    result = shuffle([1,2,3])
    assert result == [2,3,1]  # Deterministic
```

### 5. Test Naming & Organization

```python
# BAD - unclear names
def test_user():
    pass
def test_user2():
    pass

# GOOD - descriptive names
def test_create_user_with_valid_email_succeeds():
    pass
def test_create_user_with_invalid_email_raises_validation_error():
    pass
```

**Naming pattern:** `test_<action>_<condition>_<expected_result>`

---

## Testing Strategy by Component

| Component | Focus | Tools |
|-----------|-------|-------|
| Pure functions | Unit tests, property tests | pytest, hypothesis |
| API endpoints | Integration tests | pytest + test client |
| Database code | Integration with test DB | pytest + fixtures |
| UI components | Component + E2E tests | jest, playwright |
| Background jobs | Integration tests | test harness |

---

## Output Format

```markdown
## Test Review: [file/PR]

### Missing Coverage
- **[Feature/Path]**: [what's not tested]
  - Risk: [what could break unnoticed]
  - Suggested test: [specific test to add]

### Test Quality Issues
- **[Test Name]**: [issue]
  - Problem: [why it's problematic]
  - Fix: [how to improve]

### Flaky Test Risks
- **[Test Name]**: [why it might be flaky]
  - Fix: [how to make deterministic]

### Recommendations
- [Prioritized list of improvements]

### Summary
- **Coverage Level:** [Good/Moderate/Poor]
- **Test Quality:** [Strong/Adequate/Weak]
- **Priority Gaps:** [most important missing tests]
```

---

## Severity Levels

| Level | Criteria |
|-------|----------|
| Critical | Core functionality untested |
| High | Important path missing coverage |
| Medium | Edge cases not covered |
| Low | Test quality improvement |

---

## Quick Checks

```
[ ] Happy path tested
[ ] Error paths tested
[ ] Edge cases covered (empty, null, boundary)
[ ] Assertions are specific and meaningful
[ ] Tests are independent (no shared state)
[ ] No time-dependent logic without mocking
[ ] Mocks are minimal and at boundaries
[ ] Test names describe behavior
```

---

## Related

- security-sentinel skill for security testing
- performance-oracle skill for performance testing
- Project test documentation
