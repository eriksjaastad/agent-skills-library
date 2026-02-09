# Work Playbook

> **Tool-agnostic instructions for Phase 5: Task Execution**

## Purpose

Execute implementation tasks against a tracked Kanban task. This is the Floor Manager's primary operating mode during Phase 5.

**Key insight:** No Ticket, No Work. Every code change traces to a task.

---

## When to Use

- When ready to implement code
- After handoff is complete
- When a task is assigned from Kanban
- During active development phase

---

## Pre-Work Checklist

### 1. Verify Handoff Complete
- [ ] PROPOSAL_FINAL.md exists in `_handoff/`
- [ ] DEPENDENCIES.md shows READY (not BLOCKED)
- [ ] No unresolved blockers

### 2. Claim the Task
```bash
# Check available tasks
$PROJECTS_ROOT/project-tracker/pt tasks -p [project]

# Read task details
$PROJECTS_ROOT/project-tracker/pt tasks show [task-id]

# Start the task
$PROJECTS_ROOT/project-tracker/pt tasks start [task-id]
```

### 3. Understand the Work
- Read PROPOSAL_FINAL.md objective
- Review the specific task's "done when" criteria
- Check which files to modify

---

## Work Workflow

### Start
```bash
pt tasks start [id]    # Move to "In Progress"
```

### During Work
1. Follow the proposal's implementation tasks
2. Write code to `_handoff/drafts/` (sandbox)
3. Reference task ID in commits: `feat: Add feature (#123)`
4. Test changes locally

### Complete
```bash
pt tasks done [id]     # Move to "Done"
```

### Then
- Run `/audit` for code review gate
- Prepare for Judge review

---

## Code Quality Standards

### Must Do
- [ ] No hardcoded absolute paths (`/Users/...`)
- [ ] No exposed secrets (API keys in code)
- [ ] All imports resolve
- [ ] App starts without error
- [ ] Tests pass

### Must Have
- [ ] Timeout on subprocess calls
- [ ] Error handling (no bare `except: pass`)
- [ ] Atomic writes for critical files
- [ ] Logging for long operations

---

## Commit Standards

**Format:** `type(scope): description (#task-id)`

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `refactor` - Code restructure
- `test` - Tests
- `docs` - Documentation
- `chore` - Maintenance

**Example:**
```
feat(auth): Add JWT token validation (#4532)
```

---

## Output Location

Code goes to sandbox first:
```
[project]/
├── _handoff/
│   ├── drafts/         # Worker output here
│   │   ├── src/
│   │   └── tests/
│   ├── PROPOSAL_FINAL.md
│   └── DEPENDENCIES.md
```

After review, moves to main codebase.

---

## Task States

```
Backlog → To Do → In Progress → Done
                      ↑
                 YOU ARE HERE
```

- **Start:** `pt tasks start [id]` - Claims task, moves to In Progress
- **Done:** `pt tasks done [id]` - Marks complete, moves to Done
- **Block:** Create new task if blocked, link as dependency

---

## When Stuck

### Missing Context
1. Check PROPOSAL_FINAL.md
2. Check design.md in `.kiro/specs/`
3. Ask for clarification (create blocking task)

### Missing Infrastructure
1. Check DEPENDENCIES.md
2. If infrastructure missing, **STOP**
3. Return to /handoff for verification

### Test Failures
1. Fix the code, not the test
2. If test is wrong, document why
3. Never skip tests without documentation

---

## Role Boundaries

**Floor Manager (this skill):**
- Claims and executes tasks
- Writes code to sandbox
- Commits with task IDs
- Runs local tests

**NOT Floor Manager's job:**
- Creating PRDs (that's Super Manager)
- Making architectural decisions (that's design.md)
- Final approval (that's Judge)

---

## Related

- `/tasks` skill for Kanban operations
- `/commit` skill for commit standards
- `/audit` skill for code review (next step)
- `/judge` skill for final verdict
