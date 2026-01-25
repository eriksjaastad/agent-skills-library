# PR Review (Cursor Rule)

> **Placeholder - Cursor adapter for PR review playbook**

**Follow:** `agent-skills-library/playbooks/pr-review/`

## When to Apply
When reviewing pull requests or code changes in Cursor.

## Cursor-Specific Notes

### Output Format
Structure your review as:

```markdown
## Changes Reviewed
- [list files changed]

## Issues Found
- ❌ [issue with severity]
- ❌ [issue with severity]

## Suggestions
- 💡 [suggestion]
- 💡 [suggestion]

## Approval
[Approve / Request Changes / Comment]
```

### File Context
When reviewing:
- Use @workspace to check related files
- Check project `.cursorrules` for standards
- Look at test files for coverage

## Process
See playbook for full review process:
`agent-skills-library/playbooks/pr-review/README.md`

---

*This is a placeholder. Fill in when playbook is complete.*

## Related Documentation

- [Code Review Anti-Patterns](Documents/reference/CODE_REVIEW_ANTI_PATTERNS.md) - code review
- [Agent Skills Library](../agent-skills-library/README.md) - Agent Skills
