# Security Sentinel Playbook

> **Tool-agnostic instructions for security-focused code review**

## Purpose

Identify security vulnerabilities in code:
1. Injection attacks (SQL, command, XSS)
2. Authentication and authorization flaws
3. Secrets and credential exposure
4. Data validation issues
5. OWASP Top 10 vulnerabilities

---

## When to Use

- During code review (PR review phase)
- Before merging sensitive changes
- After adding auth/payment/data handling code
- As part of security audit

---

## Review Checklist

### 1. Injection Vulnerabilities

#### SQL Injection
```python
# BAD - string concatenation
query = f"SELECT * FROM users WHERE id = {user_id}"

# GOOD - parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

**Check for:**
- String interpolation in SQL queries
- Dynamic query building without parameterization
- ORM raw query methods

#### Command Injection
```python
# BAD - shell=True with user input
subprocess.run(f"echo {user_input}", shell=True)

# GOOD - argument list, no shell
subprocess.run(["echo", user_input])
```

**Check for:**
- `shell=True` with any external input
- `os.system()` calls
- Backtick execution in scripts

#### XSS (Cross-Site Scripting)
```javascript
// BAD - innerHTML with user data
element.innerHTML = userInput;

// GOOD - textContent (auto-escaped)
element.textContent = userInput;
```

**Check for:**
- `innerHTML`, `outerHTML` with user data
- `dangerouslySetInnerHTML` in React
- Template rendering without escaping

### 2. Authentication Issues

**Check for:**
- Hardcoded credentials
- Weak password requirements
- Missing rate limiting on auth endpoints
- Session tokens in URLs
- Insecure "remember me" implementations

### 3. Authorization Issues

**Check for:**
- Missing permission checks
- IDOR (Insecure Direct Object Reference)
- Privilege escalation paths
- Missing ownership validation

```python
# BAD - no ownership check
def delete_document(doc_id):
    Document.delete(doc_id)

# GOOD - verify ownership
def delete_document(doc_id, user_id):
    doc = Document.get(doc_id)
    if doc.owner_id != user_id:
        raise PermissionError()
    doc.delete()
```

### 4. Secrets Exposure

**Check for:**
- API keys in code
- Passwords in config files
- Tokens in logs
- Secrets in error messages
- `.env` files committed

```python
# BAD
api_key = "sk-live-abc123..."

# GOOD
api_key = os.getenv("API_KEY")
```

### 5. Data Validation

**Check for:**
- Missing input validation
- Type coercion issues
- Buffer/size limits
- File upload validation (type, size, content)

### 6. Cryptography Issues

**Check for:**
- Weak algorithms (MD5, SHA1 for passwords)
- Hardcoded IVs/salts
- ECB mode usage
- Missing HTTPS enforcement

---

## OWASP Top 10 Quick Reference

| # | Risk | What to Check |
|---|------|---------------|
| A01 | Broken Access Control | Permission checks, IDOR |
| A02 | Cryptographic Failures | Weak crypto, exposed secrets |
| A03 | Injection | SQL, command, XSS |
| A04 | Insecure Design | Threat modeling gaps |
| A05 | Security Misconfiguration | Debug modes, default creds |
| A06 | Vulnerable Components | Outdated dependencies |
| A07 | Auth Failures | Weak auth, session issues |
| A08 | Data Integrity Failures | Unsigned updates, CI/CD |
| A09 | Logging Failures | Missing logs, sensitive data in logs |
| A10 | SSRF | Unvalidated URLs, internal access |

---

## Output Format

```markdown
## Security Review: [file/PR]

### Critical Issues
- [Issue]: [Location] - [Impact] - [Fix]

### High Issues
- [Issue]: [Location] - [Impact] - [Fix]

### Medium Issues
- [Issue]: [Location] - [Impact] - [Fix]

### Low Issues
- [Issue]: [Location] - [Impact] - [Fix]

### Recommendations
- [Prioritized list]

### Summary
[Overall security posture assessment]
```

---

## Severity Levels

| Level | Criteria |
|-------|----------|
| Critical | Exploitable now, data breach risk |
| High | Exploitable with effort, significant impact |
| Medium | Defense-in-depth issue, limited impact |
| Low | Best practice violation, minimal risk |

---

## Related

- OWASP Top 10: https://owasp.org/Top10/
- pr-review skill for general review
- Platform security: platform-rules-expert skill
