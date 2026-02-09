# Compound Playbook

> **Tool-agnostic instructions for capturing learnings after work**

## Purpose

Compound knowledge after each work cycle by:
1. Reflecting on what happened
2. Extracting reusable learnings
3. Recording them for future reference
4. Closing the learning loop

---

## Why Compound?

Knowledge compounds over time - but only if captured.

Without active capture:
- Same mistakes repeat
- Patterns aren't recognized
- Onboarding stays hard
- Institutional knowledge lives in heads

With active capture:
- Learnings accumulate
- Patterns become explicit
- Future work improves
- Knowledge survives context loss

---

## When to Compound

Run `/compound` after:
- Completing a task
- Fixing a bug (especially a tricky one)
- Discovering unexpected behavior
- Making a decision that wasn't obvious
- Hitting a wall and finding a way through

**Don't wait for "big" learnings.** Small observations compound too.

---

## The Compound Questions

### 1. What did we learn?

Facts discovered during the work:
- Technical details (API behavior, library quirks)
- Process insights (what slowed us down, what helped)
- Domain knowledge (business rules, edge cases)

### 2. What should we do differently?

Actionable changes for future work:
- Process improvements
- Code patterns to adopt or avoid
- Tools or techniques to use

### 3. What surprised us?

Unexpected findings worth noting:
- Assumptions that were wrong
- Behavior that wasn't documented
- Connections that weren't obvious

---

## Process

### Step 1: Reflect

Think about the work just completed:
- What was the goal?
- What actually happened?
- What was harder than expected?
- What was easier than expected?

### Step 2: Extract Learnings

For each insight:
- Make it specific (not vague)
- Make it actionable (what to do with this)
- Make it findable (good keywords)

**Bad:** "API is weird"
**Good:** "The Stripe API returns 200 OK for some errors - always check the `error` field in the response body, not just HTTP status"

### Step 3: Categorize

Common categories:
- `[Technical]` - Code, APIs, libraries
- `[Process]` - Workflow, collaboration
- `[Domain]` - Business rules, requirements
- `[Tooling]` - IDE, CLI, infrastructure
- `[Pattern]` - Reusable approach

### Step 4: Record

Append to `Documents/reference/LEARNINGS.md` (or project equivalent):

```markdown
## [Date] - [Brief Context]

### What we learned
- [Learning 1]
- [Learning 2]

### What to do differently
- [Action 1]
- [Action 2]

### Related
- Task: #[id]
- Files: [relevant paths]
```

### Step 5: Link

If learning relates to:
- A task: include task ID
- Specific code: include file paths
- A pattern: link to pattern doc

---

## LEARNINGS.md Format

```markdown
# Learnings

> Captured knowledge from project work. Newest entries at top.

---

## 2026-01-28 - Session timeout fix (#4532)

### What we learned
- [Technical] Session heartbeat doesn't extend during active uploads
- [Domain] Users regularly upload files >100MB that take 20+ minutes

### What to do differently
- Add activity-based heartbeat extension for long-running operations
- Test with realistic file sizes, not just small test files

### Related
- Task: #4532
- Files: src/auth/session.py, src/upload/handler.py

---

## 2026-01-27 - Database safety incident

### What we learned
- [Process] AI agents will run DROP TABLE if not explicitly blocked
- [Tooling] Shell-level rm block works but agents find other deletion methods

### What to do differently
- Use allowlist approach instead of denylist for dangerous operations
- Add database-specific protections, not just filesystem

### Related
- Task: #4600
- Files: ~/.zshrc, ~/.claude/hooks/

---
```

---

## Anti-Patterns

### Too Vague
- "Learned about the API" (which API? what specifically?)
- "Should be more careful" (careful about what?)

### Too Obvious
- "Tests should pass before committing"
- "Read the docs"

### Not Actionable
- "This was frustrating" (what to do about it?)
- "The code is complex" (what specifically? how to handle it?)

---

## Examples

### Good Technical Learning

```markdown
## 2026-01-28 - Stripe webhook handling (#4550)

### What we learned
- [Technical] Stripe sends webhooks with 5-second timeout - handler must respond fast
- [Technical] Webhook signatures use raw body bytes, not parsed JSON - parse AFTER verification

### What to do differently
- Move heavy processing to background job, acknowledge webhook immediately
- Never call `request.json()` before signature verification
```

### Good Process Learning

```markdown
## 2026-01-28 - Multi-file refactor (#4545)

### What we learned
- [Process] Refactoring 10+ files in one PR made review impossible
- [Process] Reviewers missed bugs because diff was overwhelming

### What to do differently
- Split large refactors into atomic PRs (max 5 files, single concern)
- Create tracking issue for multi-PR refactors
```

---

## Related

- Project workflow: `Project-workflow.md`
- Retrospective phase in workflow
- LEARNINGS.md template in project-scaffolding
