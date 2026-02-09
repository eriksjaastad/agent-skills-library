---
name: security-sentinel
description: Security-focused code review identifying injection vulnerabilities, auth issues, secrets exposure, and OWASP Top 10 risks. Use when reviewing security-sensitive code or conducting security audits.
---

# Security Sentinel

> **Adapter for:** `playbooks/security-sentinel/`

---

## When to Activate

**User signals:**
- "security review this code"
- "check for vulnerabilities"
- "audit this for security"
- "is this secure?"
- "/security-sentinel"

**Best for:**
- Auth/authorization code
- Payment processing
- User input handling
- API endpoints
- Database queries

---

## Review Focus

### Injection (A03)
- SQL injection (parameterized queries?)
- Command injection (shell=True?)
- XSS (innerHTML, dangerouslySetInnerHTML?)

### Auth (A01, A07)
- Permission checks present?
- Ownership validated?
- Rate limiting?

### Secrets (A02)
- Hardcoded credentials?
- Keys in code?
- Tokens logged?

### Validation
- Input validated?
- Types checked?
- Size limits?

---

## Output Format

```markdown
## Security Review: [target]

### Critical Issues
- **[Vuln Type]** at [location]
  - Impact: [what could happen]
  - Fix: [how to remediate]

### High Issues
[same format]

### Medium Issues
[same format]

### Low Issues
[same format]

### Summary
- **Risk Level:** [Critical/High/Medium/Low]
- **Key Concerns:** [1-2 sentences]
- **Recommended Actions:** [prioritized list]
```

---

## Severity Guide

| Level | Meaning |
|-------|---------|
| Critical | Exploitable, data breach risk |
| High | Exploitable with effort |
| Medium | Defense-in-depth gap |
| Low | Best practice issue |

---

## Quick Checks

```
□ SQL uses parameterized queries
□ No shell=True with user input
□ No innerHTML with user data
□ Auth checks on all endpoints
□ Ownership validated before actions
□ No hardcoded secrets
□ Input validated and sanitized
□ Errors don't leak sensitive info
```

---

## Constraints

- ALWAYS check for OWASP Top 10
- ALWAYS provide severity ratings
- ALWAYS suggest specific fixes
- NEVER just say "looks secure" without analysis

**Full playbook:** `agent-skills-library/playbooks/security-sentinel/README.md`
