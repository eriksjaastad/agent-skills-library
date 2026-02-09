# Pull Request Playbook

> **Tool-agnostic instructions for creating pull requests**

## Purpose

Create well-structured pull requests that:
1. Have clear, concise titles
2. Include structured descriptions
3. Link to related tasks
4. Facilitate efficient review

---

## PR Structure

### Title

Keep under 70 characters. Use imperative mood:
- "Add user authentication"
- "Fix session timeout bug"
- "Update API documentation"

**Don't put details in title** - that's what the description is for.

### Description Template

```markdown
## Summary
- [1-3 bullet points describing what changed]

## Test plan
- [ ] [How to verify this works]
- [ ] [Edge cases tested]

## Related
- Closes #[task-id]
- Related to #[other-task-id]
```

---

## Process

### Step 1: Verify Branch State

```bash
git status
git log origin/main..HEAD --oneline
git diff main...HEAD --stat
```

Understand:
- Are all changes committed?
- What commits will be in this PR?
- Is the branch up to date with main?

### Step 2: Check Remote

```bash
git remote -v
git branch -vv
```

Confirm:
- Remote is configured
- Branch tracks remote (or needs push with -u)

### Step 3: Push Branch

If not pushed yet:
```bash
git push -u origin <branch-name>
```

If already pushed:
```bash
git push
```

### Step 4: Analyze Changes

Review ALL commits in the PR, not just the latest:
```bash
git log main..HEAD
git diff main...HEAD
```

Draft description based on the full scope of changes.

### Step 5: Create PR

Using GitHub CLI:
```bash
gh pr create --title "Short title" --body "$(cat <<'EOF'
## Summary
- First change
- Second change

## Test plan
- [ ] Verify X works
- [ ] Check Y edge case
EOF
)"
```

### Step 6: Verify

```bash
gh pr view
```

Confirm PR was created and description is correct.

---

## Description Guidelines

### Summary Section

Focus on the "why" and high-level "what":
- What problem does this solve?
- What behavior changes?
- What's the user impact?

**Bad:**
- "Changed user.py"
- "Added function"

**Good:**
- "Extends session timeout to prevent logout during file uploads"
- "Adds CSV export for task reports with date filtering"

### Test Plan Section

Be specific and actionable:
- How can a reviewer verify this works?
- What scenarios should they test?
- Are there edge cases to check?

**Bad:**
- "Test it"
- "Works on my machine"

**Good:**
- "1. Log in as admin user"
- "2. Navigate to Settings > Export"
- "3. Select date range and click Export"
- "4. Verify CSV downloads with correct columns"

### Related Section

Link to tracking systems:
- `Closes #123` - Auto-closes task when PR merges
- `Related to #456` - Links without auto-close
- `Depends on #789` - Shows dependency

---

## Safety Rules

### NEVER Do

- Force push to main/master
- Create PR without reviewing all commits
- Use vague descriptions ("various fixes")
- Skip the test plan

### ALWAYS Do

- Review the full diff before creating PR
- Include meaningful summary
- Provide testable verification steps
- Link to related tasks

---

## Examples

### Feature PR

```bash
gh pr create --title "Add CSV export for reports" --body "$(cat <<'EOF'
## Summary
- Adds Export button to Reports page
- Supports CSV format with configurable columns
- Includes date range filtering

## Test plan
- [ ] Navigate to Reports > Export
- [ ] Select columns and date range
- [ ] Click Export and verify CSV content
- [ ] Test with empty result set

## Related
- Closes #4540
EOF
)"
```

### Bug Fix PR

```bash
gh pr create --title "Fix session timeout during uploads" --body "$(cat <<'EOF'
## Summary
- Extends session heartbeat during active file uploads
- Prevents unexpected logout mid-upload

## Test plan
- [ ] Start uploading a large file (>100MB)
- [ ] Wait 15+ minutes
- [ ] Verify upload completes without session timeout

## Related
- Closes #4532
EOF
)"
```

---

## Related

- [GitHub CLI Documentation](https://cli.github.com/manual/gh_pr_create)
- PR Review skill: `pr-review`
- Commit skill: `commit`
