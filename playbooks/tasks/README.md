# Tasks Playbook

> **Tool-agnostic instructions for task management via project-tracker**

## Purpose

Manage work through a centralized Kanban system:
1. Track tasks across all projects
2. Maintain work state (Backlog → To Do → In Progress → Done)
3. Provide traceability for commits and PRs
4. Enable "No Ticket, No Work" discipline

---

## The pt CLI

Location: `$PROJECTS_ROOT/project-tracker/pt`

All task operations go through this CLI. Never use raw SQL on the database.

---

## Core Commands

### List Tasks

```bash
# All open tasks
pt tasks

# Filter by project
pt tasks -p <project-name>

# Filter by status
pt tasks -s "In Progress"
pt tasks -s "To Do"
pt tasks -s "Backlog"

# Include completed
pt tasks --all

# Combine filters
pt tasks -p project-tracker -s "To Do"
```

### Show Task Details

```bash
pt tasks show <task-id>
```

Returns full task info including:
- Description/prompt
- Status and priority
- Created/updated timestamps
- Project association

### Create Task

```bash
# Basic creation
pt tasks create "Task description" -p <project-name>

# With status and priority
pt tasks create "Fix login bug" -p myproject -s "To Do" --priority High
```

**Priority levels:** Critical, High, Medium, Low

### Start Task

```bash
pt tasks start <task-id>
```

Moves task to "In Progress". Use when beginning work.

### Complete Task

```bash
pt tasks done <task-id>
```

Moves task to "Done". Use when work is finished.

### Update Task

```bash
# Change status
pt tasks update <task-id> -s "To Do"

# Change priority
pt tasks update <task-id> --priority High

# Change description
pt tasks update <task-id> -t "New description"
```

---

## Task Workflow

### Before Starting Work

```bash
# Check what's assigned/available
pt tasks -p <project>

# Read the full task
pt tasks show <task-id>

# Claim the task
pt tasks start <task-id>
```

### During Work

- Reference task ID in commits: `fix(auth): Resolve timeout (#4532)`
- Task stays "In Progress" until complete

### After Work

```bash
# Mark complete
pt tasks done <task-id>

# Run /compound to capture learnings
```

---

## Task States (Kanban)

```
┌──────────┐    ┌─────────┐    ┌─────────────┐    ┌──────┐
│ Backlog  │ → │  To Do  │ → │ In Progress │ → │ Done │
└──────────┘    └─────────┘    └─────────────┘    └──────┘
```

| State | Meaning |
|-------|---------|
| Backlog | Captured but not prioritized |
| To Do | Prioritized, ready to start |
| In Progress | Actively being worked on |
| Done | Completed |

---

## Best Practices

### Task Hygiene

1. **One task = one piece of work** - Don't combine unrelated changes
2. **Clear descriptions** - Future you needs to understand
3. **Link everything** - Commits, PRs, learnings reference task IDs
4. **Close promptly** - Don't leave tasks "In Progress" when done

### "No Ticket, No Work"

Before writing code:
1. Check if task exists
2. If not, create one
3. Start the task
4. Then work

This ensures:
- All work is tracked
- Nothing falls through cracks
- Easy to see what's in progress

### Quick Capture

Got an idea mid-work? Quick capture it:

```bash
pt tasks create "Idea: Add caching to API" -p myproject
```

Don't context-switch. Capture and continue.

---

## Output Formats

### Default (Human-Readable)

```
Tasks - project-tracker

#4532 | In Progress | High | Fix session timeout during file upload
#4540 | To Do | Medium | Add CSV export for reports

Total: 2 tasks
```

### JSON (Machine-Readable)

```bash
pt tasks --json
```

Useful for scripting and automation.

---

## Integration Points

### With /commit

Include task ID in commit message:
```
feat(export): Add CSV export (#4540)
```

### With /pr

Link in PR description:
```markdown
## Related
- Closes #4540
```

### With /compound

Reference task when capturing learnings:
```markdown
## 2026-01-28 - Session timeout fix (#4532)
```

---

## Web Dashboard

```bash
pt launch
```

Opens Kanban board at `localhost:8000/kanban`

Visual interface for:
- Drag-drop task movement
- Filtering and search
- Bulk operations

---

## Related

- project-tracker CLAUDE.md for full CLI reference
- /commit skill for task-linked commits
- /pr skill for task-linked PRs
- /compound skill for task-linked learnings
