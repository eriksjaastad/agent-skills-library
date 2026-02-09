---
name: platform-rules-expert
description: Expert knowledge on configuring AI agents across Claude Code, Cursor, and Antigravity. Use when setting up security policies, auditing agent configuration, or understanding where config lives per platform.
---

# Platform Rules Expert

> **Adapter for:** `playbooks/platform-rules-expert/`

---

## When to Activate

**User signals:**
- "how do I configure agent rules?"
- "where does cursor config live?"
- "audit my agent security"
- "set up hooks for claude"
- "/platform-rules"

**Context:**
- Setting up new project security
- Auditing existing configuration
- Troubleshooting why rules aren't working
- Understanding policy vs enforcement

---

## Core Knowledge

### Policy vs Enforcement

| Type | Mechanism | Bypassable? |
|------|-----------|-------------|
| **Policy** | Markdown rules, CLAUDE.md | Yes |
| **Enforcement** | Hooks, UI settings, shell blocks | No |

**Policy = guidance. Enforcement = hard block.**

---

## Platform Quick Reference

### Claude Code
| What | Where |
|------|-------|
| Permissions | `~/.claude/settings.json` |
| Hooks | `~/.claude/hooks/*.py` |
| Skills | `~/.claude/skills/` or `.claude/skills/` |
| Project rules | `CLAUDE.md` |

### Cursor
| What | Where |
|------|-------|
| Rules | `.cursor/rules/*.md` |
| Legacy rules | `.cursorrules` |
| **Enforcement** | Cursor Settings UI |

### Antigravity
| What | Where |
|------|-------|
| Global rules | `~/.gemini/GEMINI.md` |
| Project rules | `.agent/rules/*.md` |
| **Enforcement** | Terminal Execution Policy UI |

---

## Output Format

### For Audit Requests

```markdown
## Platform Configuration Audit

### Claude Code
- **Permissions:** [list]
- **Hooks:** [active hooks]
- **Issues:** [any problems found]

### Cursor
- **Rules files:** [count and names]
- **UI Settings:** [check manually]
- **Issues:** [any problems found]

### Antigravity
- **Global rules:** [exists/missing]
- **Project rules:** [count and names]
- **Issues:** [any problems found]

### Recommendations
- [Priority 1 fix]
- [Priority 2 fix]
```

### For Setup Requests

```markdown
## Platform Setup Guide

### Step 1: Enforcement (Hard Blocks)
[Shell blocks, hooks, UI settings]

### Step 2: Policy (Guidance)
[Rules files, CLAUDE.md]

### Step 3: Verification
[Commands to verify setup]
```

---

## Quick Audit Commands

```bash
# Claude Code
cat ~/.claude/settings.json | jq '.hooks'
ls ~/.claude/hooks/

# Cursor
ls .cursor/rules/

# Antigravity
cat ~/.gemini/GEMINI.md
ls .agent/rules/

# Shell blocks
grep -A3 "^rm()" ~/.zshrc
```

---

## Constraints

- ALWAYS distinguish policy from enforcement
- ALWAYS recommend enforcement first, policy second
- ALWAYS mention shell-level blocks as last resort
- NEVER suggest policy alone is sufficient for security

---

## Common Issues

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Rules ignored | Policy not enforcement | Use hooks/UI settings |
| Hook not blocking | Wrong exit code | Return 2, not 1 |
| Inconsistent behavior | Platform differences | Add shell-level block |

**Full playbook:** `agent-skills-library/playbooks/platform-rules-expert/README.md`
