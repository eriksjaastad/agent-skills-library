---
name: compound
description: Capture learnings after completing work. Use after finishing tasks, fixing bugs, or discovering insights worth preserving. Prompts for reflection and appends to LEARNINGS.md.
---

# Compound

> **Adapter for:** `playbooks/compound/`

---

## When to Activate

**User signals:**
- "what did we learn?"
- "capture learnings"
- "let's compound"
- "/compound"

**Best timing:**
- After completing a task
- After fixing a tricky bug
- After making a non-obvious decision
- After hitting a wall and breaking through

---

## Process

1. **Reflect:** What was the goal? What happened?
2. **Extract:** Turn observations into specific learnings
3. **Categorize:** [Technical], [Process], [Domain], [Tooling], [Pattern]
4. **Record:** Append to LEARNINGS.md
5. **Link:** Connect to task IDs and files

---

## Prompt Flow

When user invokes /compound, ask:

```markdown
## Compound: Capture Learnings

Let's extract value from the work just completed.

**1. What did we learn?**
(Technical details, process insights, domain knowledge)

**2. What should we do differently?**
(Actionable changes for future work)

**3. What surprised us?**
(Unexpected findings worth noting)
```

Then format and append to LEARNINGS.md.

---

## Output Format

### Interaction

```markdown
## Compound: Capture Learnings

Based on [task/work just completed]:

### What did we learn?
- [Technical] [specific learning]
- [Process] [specific learning]

### What to do differently
- [Action item]

### Recorded
Appended to: Documents/reference/LEARNINGS.md
```

### LEARNINGS.md Entry

```markdown
## [Date] - [Context] (#[task-id])

### What we learned
- [Category] Learning text

### What to do differently
- Action item

### Related
- Task: #[id]
- Files: [paths]
```

---

## Constraints

- ALWAYS make learnings specific (not vague)
- ALWAYS make learnings actionable
- ALWAYS include date and context
- ALWAYS categorize with [Technical], [Process], etc.
- NEVER record obvious/trivial learnings
- Link to task ID when available

---

## File Location

Default: `Documents/reference/LEARNINGS.md`

If not found, check:
- `LEARNINGS.md` in project root
- Create if doesn't exist (with header template)

---

## Categories

| Tag | For |
|-----|-----|
| `[Technical]` | Code, APIs, libraries |
| `[Process]` | Workflow, collaboration |
| `[Domain]` | Business rules, requirements |
| `[Tooling]` | IDE, CLI, infrastructure |
| `[Pattern]` | Reusable approaches |

**Full playbook:** `agent-skills-library/playbooks/compound/README.md`
