# Skill Usage Tracker

> **Purpose:** Track which projects use which skills and their maturity levels  
> **Last Updated:** January 16, 2026  
> **Maintained by:** Monthly skill review process

---

## Quick Reference

| Skill | Status | Projects | Last Verified |
|-------|--------|----------|---------------|
| ai-router-delegation | 🟡 Emerging | 1 | Jan 2026 |
| audit-whisperer | 🟡 Emerging | 1 | Jan 2026 |
| debugging-routine | 🟡 Emerging | 1 | Jan 2026 |
| financial-integrity-guard | 🟡 Emerging | 1 | Jan 2026 |
| pr-review | 🟡 Emerging | 1 | Jan 2026 |
| skill-lifecycle-manager | 🔵 Candidate | 1 | Jan 2026 |
| spec-driven-developer | 🟡 Emerging | 1 | Jan 2026 |
| tax-discovery-engine | 🟡 Emerging | 1 | Jan 2026 |
| youtube-channel-analysis | 🟡 Emerging | 2 | Jan 2026 |

---

## Maturity Levels

```
🔵 CANDIDATE    - 1 project, watching for evidence
🟡 EMERGING     - 2 projects, needs 3rd to promote
🟢 PROVEN       - 3+ projects, ready for wide adoption
🏆 MATURE       - Battle-tested, reference quality
```

---

## Detailed Usage Evidence

### ai-router-delegation

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| tax-organizer | Jan 2026 | AI Router integration for local model delegation |

**Promotion path:** Needs 2 more projects to use this pattern

---

### audit-whisperer

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| project-tracker | Jan 2026 | Triage and filter audit tool output |

**Promotion path:** Needs 2 more projects to use this pattern

---

### debugging-routine

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| agent-skills-library | Jan 2026 | Standard debugging workflow |

**Promotion path:** Apply to 2 more projects

---

### financial-integrity-guard

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| tax-organizer | Jan 2026 | Decimal precision and audit trails |

**Promotion path:** Needs 2 more projects with financial/accounting needs

---

### pr-review

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| project-scaffolding | Jan 2026 | Code review process |

**Promotion path:** Apply to 2 more projects with PR workflows

---

### skill-lifecycle-manager

**Status:** 🔵 Candidate  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| agent-skills-library | Jan 2026 | Meta-skill for managing skills |

**Promotion path:** This skill is inherently tied to agent-skills-library; may stay 🔵

---

### spec-driven-developer

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| agent-skills-library | Jan 2026 | Spec-first development |

**Promotion path:** Apply to 2 more projects

---

### tax-discovery-engine

**Status:** 🟡 Emerging  
**Projects:** 1

| Project | Date Added | Notes |
|---------|------------|-------|
| tax-organizer | Jan 2026 | Write-off detection and IRS justification |

**Promotion path:** Domain-specific; may stay 🟡 (only relevant to tax projects)

---

### youtube-channel-analysis

**Status:** 🟡 Emerging  
**Projects:** 2

| Project | Date Added | Notes |
|---------|------------|-------|
| analyze-youtube-videos | Dec 2025 | Primary implementation |
| agent-skills-library | Jan 2026 | Skill definition and testing |

**Promotion path:** 1 more project to promote to 🟢

---

## Pending Promotions

Skills at 🟡 with 2 projects (ready for promotion with 1 more):

| Skill | Current Projects | Needed |
|-------|------------------|--------|
| youtube-channel-analysis | 2 | 1 more project |

---

## Recently Promoted

| Skill | Promoted | Evidence |
|-------|----------|----------|
| *(none yet)* | | |

---

## Monthly Review Log

### January 2026

**Date:** January 16, 2026  
**Reviewer:** Claude + Erik

**Actions taken:**
- Initial SKILL_USAGE.md created
- All 8 existing skills inventoried
- skill-lifecycle-manager skill created
- Detection script added

**Next review:** February 2026

---

## How to Update This File

1. **When a project adopts a skill:**
   - Add row to that skill's usage table
   - Update project count in Quick Reference
   - Update "Last Verified" date

2. **When promoting a skill:**
   - Change status (🟡 → 🟢)
   - Move to "Recently Promoted" section
   - Note evidence

3. **Monthly review:**
   - Run `python scripts/detect_skill_candidates.py`
   - Verify counts match detection output
   - Update "Last Verified" dates

---

*This file is the source of truth for skill adoption. Keep it updated during monthly reviews.*
