---
name: tasks
description: Manage tasks via project-tracker Kanban system. Use for listing tasks, creating new tasks, starting work, marking done, or checking task status across projects.
---

# Tasks

> **Adapter for:** `playbooks/tasks/`

---

## When to Activate

**User signals:**
- "what tasks do I have?"
- "create a task for..."
- "start task #123"
- "mark task done"
- "show my in progress tasks"
- "/tasks"

**Context:**
- Beginning a work session (check tasks)
- Starting new work (create/start task)
- Finishing work (mark done)
- Quick capture of ideas

---

## CLI Reference

**Location:** `$PROJECTS_ROOT/project-tracker/pt`

| Action | Command |
|--------|---------|
| List all | `pt tasks` |
| Filter project | `pt tasks -p <project>` |
| Filter status | `pt tasks -s "In Progress"` |
| Show details | `pt tasks show <id>` |
| Create | `pt tasks create "desc" -p <project>` |
| Start work | `pt tasks start <id>` |
| Mark done | `pt tasks done <id>` |
| Update | `pt tasks update <id> -s "To Do"` |

---

## Task States

```
Backlog → To Do → In Progress → Done
```

---

## Output Format

### For List Requests

```markdown
## Tasks - [project or "all"]

| ID | Status | Priority | Description |
|----|--------|----------|-------------|
| #123 | In Progress | High | Task description |
| #124 | To Do | Medium | Another task |

**Total:** [count] tasks
```

### For Show Requests

```markdown
## Task #[id]

**Project:** [name]
**Status:** [status]
**Priority:** [priority]
**Created:** [date]

### Description
[full description]
```

### For Create/Start/Done

```markdown
## Task [Action]

[Confirmation message]

**Task:** #[id] - [description]
**Status:** [new status]
```

---

## Workflow Integration

### Before Work
```bash
pt tasks -p <project>      # Check available
pt tasks show <id>         # Read details
pt tasks start <id>        # Claim task
```

### After Work
```bash
pt tasks done <id>         # Mark complete
# Then run /compound
```

---

## Constraints

- ALWAYS use pt CLI, never raw SQL
- ALWAYS start task before working on it
- ALWAYS mark done when complete
- Include task ID in commits: `feat: Add feature (#123)`

---

## Quick Reference

```bash
# What's open?
pt tasks -p myproject

# Start working
pt tasks start 123

# Done working
pt tasks done 123

# Quick capture
pt tasks create "Add caching" -p myproject
```

**Full playbook:** `agent-skills-library/playbooks/tasks/README.md`
