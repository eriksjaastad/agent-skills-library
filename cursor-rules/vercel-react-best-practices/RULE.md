# Vercel React Best Practices

> **Adapter for:** `playbooks/vercel-react-best-practices/`
> **Source:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

---

## Quick Reference

When writing or reviewing React/Next.js code, apply these rules by priority:

### CRITICAL
- **async-parallel** - Use `Promise.all()` for independent operations
- **async-defer-await** - Move await into branches where actually used
- **bundle-barrel-imports** - Import directly, avoid barrel files
- **bundle-dynamic-imports** - Use `next/dynamic` for heavy components

### HIGH
- **server-cache-react** - Use `React.cache()` for per-request dedup
- **server-parallel-fetching** - Restructure to parallelize fetches

### MEDIUM
- **rerender-memo** - Extract expensive work into memoized components
- **rerender-derived-state** - Subscribe to derived booleans, not raw values

---

## Full Guide

See `playbooks/vercel-react-best-practices/AGENTS.md` for all 57 rules with examples.

Individual rules: `playbooks/vercel-react-best-practices/rules/*.md`

---

*Added: 2026-01-25*
