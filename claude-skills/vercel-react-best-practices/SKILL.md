---
name: vercel-react-best-practices
description: React and Next.js performance optimization guidelines from Vercel Engineering. Use when writing, reviewing, or refactoring React/Next.js code.
---

# Vercel React Best Practices

> **Adapter for:** `playbooks/vercel-react-best-practices/`
> **Version:** 1.0.0
> **Source:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

---

## Skill Overview

**What this skill does:**
Provides 57 performance optimization rules across 8 categories for React and Next.js applications, prioritized by impact.

**Canonical instructions:** `../../playbooks/vercel-react-best-practices/SKILL.md`

**Full compiled guide:** `../../playbooks/vercel-react-best-practices/AGENTS.md` (82KB)

---

## When to Activate This Skill

**User signals:**
- "Review this React code for performance"
- "Optimize this Next.js component"
- "Check for performance issues"
- "Refactor for better performance"

**Context requirements:**
- React or Next.js project
- Writing, reviewing, or refactoring components

---

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Eliminating Waterfalls | CRITICAL | `async-` |
| 2 | Bundle Size Optimization | CRITICAL | `bundle-` |
| 3 | Server-Side Performance | HIGH | `server-` |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | `client-` |
| 5 | Re-render Optimization | MEDIUM | `rerender-` |
| 6 | Rendering Performance | MEDIUM | `rendering-` |
| 7 | JavaScript Performance | LOW-MEDIUM | `js-` |
| 8 | Advanced Patterns | LOW | `advanced-` |

---

## Process

1. Identify the category relevant to the current task
2. Reference specific rules in `playbooks/vercel-react-best-practices/rules/`
3. Apply rules by priority (CRITICAL first)
4. Each rule has: incorrect example, correct example, impact metrics

---

## Success Criteria

**This skill is successful when:**
- [ ] Code follows CRITICAL rules (async waterfalls, bundle size)
- [ ] Appropriate patterns used for the context (server vs client)
- [ ] No unnecessary re-renders or blocking operations

---

*Added: 2026-01-25*
*Source: skills.sh / vercel-labs/agent-skills*
