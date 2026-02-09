---
name: commit
description: Create git commits following conventional commits format with task ID linking. Use when committing code changes, staging files, or preparing commits.
---

# Commit

> **Adapter for:** `playbooks/commit/`

---

## When to Activate

**User signals:**
- "commit this"
- "create a commit"
- "stage and commit"
- "/commit"

**Context requirements:**
- Must be in a git repository
- Should have changes to commit (staged or unstaged)

---

## Process

1. **Check status:** `git status` (no -uall flag)
2. **Check diff:** `git diff` and `git diff --staged`
3. **Check style:** `git log --oneline -5` to match repo conventions
4. **Stage files:** Add specific files (not `git add .`)
5. **Commit:** With conventional format and task ID
6. **Verify:** `git status` and `git log -1`

---

## Commit Message Format

```
type(scope): description (#task-id)

[optional body]

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Types
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `refactor` - Code restructuring
- `test` - Tests
- `chore` - Tooling/dependencies

---

## Output Format

When executing /commit:

```markdown
## Changes to Commit
- [file1]: [what changed]
- [file2]: [what changed]

## Commit Message
```
type(scope): description (#task-id)
```

## Result
[Commit hash and confirmation]
```

---

## Constraints

- NEVER use `--no-verify` or `-n`
- NEVER use `--amend` after hook failure (create new commit)
- NEVER stage `.env`, credentials, or secrets
- ALWAYS use HEREDOC for multi-line messages
- ALWAYS include Co-Authored-By footer
- ALWAYS link task ID when one exists

---

## Safety

After hook failure:
1. Fix the issue
2. Re-stage files
3. Create NEW commit (not amend)

**Full playbook:** `agent-skills-library/playbooks/commit/README.md`
