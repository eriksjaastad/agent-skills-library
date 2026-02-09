# Strategy Playbook

> **Tool-agnostic instructions for Phase 1: PRD Creation**

## Purpose

Create a Product Requirements Document (PRD) that captures human intent and constraints. This is the first phase of the 6-phase workflow.

**Key insight:** The PRD captures WHAT and WHY. Kiro (Phase 2) generates HOW.

---

## When to Use

- Starting a new feature
- Beginning a new project
- Before entering Kiro for spec generation
- When Erik says "let's build X"

---

## Pre-PRD Checklist

Before writing the PRD, verify:

### 1. Check External Services
```bash
cat $PROJECTS_ROOT/project-scaffolding/EXTERNAL_RESOURCES.yaml | grep -A10 "services_by_function"
```

**Ask:**
- Does infrastructure for this already exist?
- Can we reuse existing services (Discord webhooks, email, APIs)?
- What new infrastructure will this feature need?

### 2. Determine Path
```
Is this shipping to production?
├── No  → Exploration Mode (document findings, never merge)
└── Yes → Does it touch schema, auth, or infrastructure?
    ├── Yes → Full Workflow (all 6 phases)
    └── No  → Is it isolated to <3 files and <2 hours?
        ├── Yes → Light Path (PROPOSAL_LIGHT.md → Judge only)
        └── No  → Full Workflow
```

**When unsure:** Default to Full Workflow.

---

## PRD Structure

### What TO Include (Intent Level)

```markdown
# PRD: [Feature Name]

## 1. Project Overview
What problem are we solving? Who's it for? (2-3 sentences)

## 2. Goals
What we want to achieve (outcomes, not specifications)

## 3. Non-Goals
What we're explicitly NOT building (critical for scope)

## 4. Constraints
- **Security:** Authentication method, authorization rules
- **Tech Stack:** Languages, frameworks, hosting mandates
- **Performance:** Response times, scale expectations
- **Compliance:** Regulatory requirements (if any)

## 5. Integration Context
- Existing infrastructure to use (from EXTERNAL_RESOURCES.yaml)
- External services needed
- Publishing destination (where does output go?)
- Notification channels

## 6. Success Metrics
How do we know it's working? What numbers to track?

## 7. Key Decisions Already Made
Architecture constraints, patterns to follow

## 8. Open Questions for Kiro
Technical decisions you want Kiro to resolve
```

### What NOT to Include (Kiro Generates These)

| Don't Write | Kiro Generates |
|-------------|----------------|
| User stories ("As a...") | requirements.md |
| EARS requirements | requirements.md |
| Data schemas | design.md |
| Workflow diagrams | design.md |
| API specifications | design.md |
| Task breakdowns | tasks.md |

**If you're writing "As a user, I want..." - STOP. That's front-running Kiro.**

---

## PRD Completeness Checklist

Before moving to Kiro, verify:

### Vision (Required)
- [ ] Project overview (2-3 sentences)
- [ ] Goals (outcomes, not specs)
- [ ] Non-goals (scope boundaries)
- [ ] Target users

### Constraints (Required - Kiro needs these)
- [ ] Security requirements
- [ ] Tech stack mandates
- [ ] Performance requirements
- [ ] Compliance/legal (if any)

### Integration Context (Required)
- [ ] Existing infrastructure to use
- [ ] External services needed
- [ ] Publishing destination
- [ ] Notification channels

### Success Metrics (Required)
- [ ] How do we know it's working?
- [ ] What numbers to track?

### Human Touchpoints
- [ ] Where does human approve/reject?
- [ ] Who gets notified?

---

## Red Flags (Stop and Fix)

| Red Flag | Question to Ask |
|----------|-----------------|
| No security section | "Who can access this? How do they authenticate?" |
| No non-goals | "What are we explicitly NOT building?" |
| No integration context | "What existing infrastructure should this use?" |
| No success metrics | "How will we know this is working?" |
| No publishing destination | "Where does the output actually go?" |
| "TBD" or "later" in constraints | "Is this actually ready for Kiro?" |
| User stories in PRD | "Remove - let Kiro generate from Goals" |
| Schemas in PRD | "Describe intent, not structure" |

---

## Output

**File:** `[project]/PRD.md`

**Next Phase:** Phase 2 (Kiro) - Open in Kiro IDE and run:
```
#PRD.md Generate a spec from this.
```

---

## Role Boundaries

**Super Manager (this skill):**
- Creates PRD with Erik
- Checks EXTERNAL_RESOURCES.yaml
- Captures intent and constraints
- Hands off to Kiro

**NOT Super Manager's job:**
- Writing code
- Generating specifications (that's Kiro)
- Executing tasks (that's Floor Manager)

---

## Related

- `/trace` skill for Phase 2.5 traceability
- `/propose` skill for Phase 3 proposals
- Project-workflow.md for full pipeline
- EXTERNAL_RESOURCES.yaml for services registry
