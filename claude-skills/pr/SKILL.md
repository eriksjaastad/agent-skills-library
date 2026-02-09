---
name: pr
description: Create pull requests with structured descriptions, summaries, and test plans. Use when creating PRs, pushing branches for review, or preparing code for merge.
---

# PR (Pull Request Creation)

> **Adapter for:** `playbooks/pr/`

---

## When to Activate

**User signals:**
- "create a PR"
- "open a pull request"
- "push this for review"
- "/pr"

**Context requirements:**
- Must be in a git repository
- Should have commits to include in PR
- Branch should differ from main/master

---

## Process

1. **Check branch state:** `git status`, `git log origin/main..HEAD`
2. **Check remote tracking:** `git branch -vv`
3. **Push if needed:** `git push -u origin <branch>`
4. **Analyze ALL commits:** `git log main..HEAD` (not just latest)
5. **Create PR:** `gh pr create` with structured body
6. **Verify:** `gh pr view`

---

## PR Format

### Title
- Under 70 characters
- Imperative mood: "Add feature" not "Added feature"
- No details - put those in description

### Body
```markdown
## Summary
- [1-3 bullets on what changed and why]

## Test plan
- [ ] [Verification steps]

## Related
- Closes #[task-id]
```

---

## Output Format

When executing /pr:

```markdown
## Branch Status
- Branch: [name]
- Commits: [count] ahead of main
- Files changed: [count]

## PR Details
**Title:** [title]

**Description:**
[full PR body]

## Result
PR URL: [url]
```

---

## Constraints

- NEVER create PR without reviewing all commits
- NEVER use vague descriptions ("various fixes")
- ALWAYS include Summary section
- ALWAYS include Test plan with checkboxes
- ALWAYS link task IDs when they exist
- ALWAYS use HEREDOC for PR body

---

## Command Template

```bash
gh pr create --title "Title here" --body "$(cat <<'EOF'
## Summary
- Change 1
- Change 2

## Test plan
- [ ] Step 1
- [ ] Step 2

## Related
- Closes #1234
EOF
)"
```

**Full playbook:** `agent-skills-library/playbooks/pr/README.md`
