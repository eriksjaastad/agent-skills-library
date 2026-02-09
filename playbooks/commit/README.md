# Commit Playbook

> **Tool-agnostic instructions for creating git commits**

## Purpose

Create well-structured git commits that:
1. Follow conventional commits format
2. Link to task IDs for traceability
3. Respect git safety rules

---

## Conventional Commits Format

```
<type>(<scope>): <description> (#<task-id>)

[optional body]

[optional footer]
Co-Authored-By: <agent-name> <noreply@anthropic.com>
```

### Types

| Type | When to Use |
|------|-------------|
| `feat` | New feature (wholly new functionality) |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Code change that neither fixes nor adds |
| `perf` | Performance improvement |
| `test` | Adding or fixing tests |
| `chore` | Build process, dependencies, tooling |

### Scope (Optional)

The module, component, or area affected:
- `feat(auth): Add OAuth2 support`
- `fix(api): Handle null response`
- `docs(readme): Update installation steps`

### Task ID Linking

Always include task ID when one exists:
- `feat(kanban): Add drag-drop reordering (#4521)`
- `fix: Resolve login timeout (#4532)`

If no task exists, omit the task ID (don't make one up).

---

## Process

### Step 1: Check Status

```bash
git status
```

Review:
- What files are staged?
- What files are modified but not staged?
- Are there untracked files that should be included?

### Step 2: Check Diff

```bash
git diff          # Unstaged changes
git diff --staged # Staged changes
```

Understand what you're committing before writing the message.

### Step 3: Check Recent Commits

```bash
git log --oneline -10
```

Match the repository's commit message style.

### Step 4: Stage Files

Stage specific files (preferred over `git add .`):

```bash
git add path/to/file1 path/to/file2
```

**Never stage:**
- `.env` files
- Credentials or secrets
- Large binaries (unless intentional)

### Step 5: Write Commit Message

Focus on the "why" not the "what":

**Bad:** `Update user.py`
**Good:** `fix(auth): Prevent session timeout during file upload (#4532)`

**Bad:** `Add function`
**Good:** `feat(export): Add CSV export for reports (#4540)`

### Step 6: Commit

```bash
git commit -m "$(cat <<'EOF'
type(scope): description (#task-id)

Optional body explaining why this change was made.

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### Step 7: Verify

```bash
git status
git log -1
```

Confirm the commit was created successfully.

---

## Safety Rules

### NEVER Do

- `--no-verify` or `-n` - Don't bypass pre-commit hooks
- `--amend` after hook failure - Creates a new commit instead
- `git add .` or `git add -A` blindly - Review what you're adding
- Force push to main/master
- Commit secrets or credentials

### ALWAYS Do

- Read the diff before committing
- Use specific file paths when staging
- Include task ID when one exists
- Fix hook failures properly (don't bypass)
- Create NEW commits after hook failures (not amend)

---

## Examples

### Simple Bug Fix

```bash
git add src/auth/session.py
git commit -m "fix(auth): Extend session timeout to 30 minutes (#4532)"
```

### Feature with Body

```bash
git add src/export/ tests/test_export.py
git commit -m "$(cat <<'EOF'
feat(export): Add CSV export for task reports (#4540)

Adds ability to export filtered task lists as CSV files.
Includes date range filtering and column selection.

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### Documentation Update

```bash
git add README.md docs/installation.md
git commit -m "docs: Update installation instructions for Python 3.11"
```

### Refactor (No Task)

```bash
git add src/utils/helpers.py
git commit -m "refactor(utils): Extract date parsing to dedicated function"
```

---

## Hook Failure Recovery

If pre-commit hook fails:

1. **Fix the issue** (linting, tests, etc.)
2. **Re-stage files:** `git add <fixed-files>`
3. **Create NEW commit** (don't use --amend)
4. **Verify:** `git log -1`

The previous commit didn't happen, so --amend would modify an older commit.

---

## Related

- [Conventional Commits](https://www.conventionalcommits.org/)
- Project task tracker: `pt tasks`
