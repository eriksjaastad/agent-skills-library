# Cursor Rules

> **Lightweight adapters that connect Cursor to playbooks**

This directory contains Cursor-specific wrappers for playbooks.

---

## What Are Cursor Rules?

**Cursor Rules** are instructions that tell Cursor AI how to behave in your projects.

They live in `.cursorrules` files (in project root) and tell Cursor:
- Coding standards to follow
- Processes to use
- What to check for
- Project-specific context

**Official Docs:** https://docs.cursor.com/context/rules-for-ai

---

## How This Directory Works

### The Pattern:

```
agent-skills-library/
├── playbooks/pr-review/          ← The actual instructions (canonical)
│   ├── README.md
│   └── checklist.md
│
└── cursor-rules/pr-review/       ← Thin wrapper for Cursor
    └── RULE.md                    → "Follow playbooks/pr-review/"
```

### Why Separate?

1. **Playbooks are tool-agnostic** - Work with any AI
2. **Cursor rules are Cursor-specific** - Add Cursor features
3. **Single source of truth** - Update playbook once, all tools benefit
4. **Easy adaptation** - Cursor-specific formatting stays here

---

## Structure

Each skill gets its own directory:

```
cursor-rules/
├── README.md                      ← You are here
│
├── pr-review/                     ← Example skill
│   └── RULE.md                    ← Cursor adapter
│
└── debugging-routine/             ← Another skill
    └── RULE.md
```

---

## What Goes in RULE.md

A Cursor rule adapter should:

1. **Reference the playbook** (canonical source)
2. **Add Cursor-specific formatting** (if needed)
3. **Add Cursor-specific constraints** (if needed)
4. **Be SHORT** (the playbook has the details)

### Template:

```markdown
# [Skill Name] (Cursor Rule)

**Follow:** `agent-skills-library/playbooks/[skill-name]/`

## When to Apply
[Describe when Cursor should use this skill]

## Cursor-Specific Notes
- Output format: [specify if different from playbook]
- File handling: [any Cursor-specific file operations]
- Context: [what files Cursor should reference]

## Process
See the playbook for full process:
agent-skills-library/playbooks/[skill-name]/README.md

## Quick Checklist
[Optional: short version for quick reference]
```

---

## Using in Projects

### Method 1: Copy into .cursorrules

```bash
# In your project
cat agent-skills-library/cursor-rules/pr-review/RULE.md >> .cursorrules
```

### Method 2: Reference directly

In your project's `.cursorrules`:

```
# PR Review Skill
Follow: agent-skills-library/playbooks/pr-review/
See also: agent-skills-library/cursor-rules/pr-review/RULE.md
```

### Method 3: Include directive (if Cursor supports it)

```
@include agent-skills-library/cursor-rules/pr-review/RULE.md
```

---

## Example: PR Review

### playbooks/pr-review/README.md (Canonical)
```markdown
# PR Review Process

## Steps
1. Check code quality
2. Check tests
3. Check documentation
4. Verify no secrets
5. Give constructive feedback

[Full detailed instructions...]
```

### cursor-rules/pr-review/RULE.md (Adapter)
```markdown
# PR Review (Cursor Rule)

**Follow:** agent-skills-library/playbooks/pr-review/

## When to Apply
When reviewing pull requests or code changes in Cursor.

## Cursor-Specific Notes
- Use Cursor's diff view to see changes
- Check @workspace for related files
- Output format: Markdown with emoji indicators

## Quick Checklist
- ✅ Code quality (see playbook)
- ✅ Tests (see playbook)
- ✅ Docs (see playbook)
- ✅ Security (see playbook)
```

---

## Cursor-Specific Features

### What You Can Add Here:

1. **File context:**
   ```
   When reviewing, check:
   - @workspace for related files
   - package.json for dependencies
   - README.md for project standards
   ```

2. **Output formatting:**
   ```
   Format feedback as:
   ## Changes Reviewed
   [file list]
   
   ## Issues Found
   - ❌ [issue]
   
   ## Suggestions
   - 💡 [suggestion]
   ```

3. **Cursor commands:**
   ```
   After review, suggest:
   - "Fix linting issues" → Run formatter
   - "Add tests" → Generate test file
   ```

4. **Project-specific overrides:**
   ```
   For THIS project:
   - Use TypeScript strict mode
   - Follow Next.js 14 conventions
   - No client-side API keys
   ```

---

## Migration from Existing .cursorrules

### Step 1: Identify Reusable Rules

Look at your current `.cursorrules` files:

```bash
# Find all cursor rules
find ~/projects -name ".cursorrules"

# See what's in them
cat ~/projects/my-project/.cursorrules
```

### Step 2: Categorize

Ask for each rule:
- **Reusable across projects?** → Extract to playbook
- **Project-specific?** → Keep in project `.cursorrules`
- **Cursor-specific formatting?** → Create adapter in cursor-rules/

### Step 3: Extract to Playbook

For reusable rules:

1. Create playbook: `playbooks/[skill-name]/`
2. Write tool-agnostic version
3. Create Cursor adapter: `cursor-rules/[skill-name]/RULE.md`

### Step 4: Update Project

In project `.cursorrules`, replace:

**Before:**
```
[Long detailed instructions about PR reviews...]
[Long detailed instructions about code quality...]
[Long detailed instructions about testing...]
```

**After:**
```
# Shared Skills
Follow: agent-skills-library/playbooks/pr-review/
Follow: agent-skills-library/playbooks/code-quality/
Follow: agent-skills-library/playbooks/testing-standards/

# Project-Specific
- This project uses Next.js 14
- API routes in app/api/
- Use server components by default
```

---

## Best Practices

### DO:
- ✅ Keep adapters SHORT (reference playbook)
- ✅ Add Cursor-specific formatting here
- ✅ Test with real projects
- ✅ Update when playbook changes

### DON'T:
- ❌ Duplicate playbook content
- ❌ Put tool-agnostic instructions here (use playbook)
- ❌ Create adapter without playbook
- ❌ Make project-specific (use project `.cursorrules`)

---

## Testing

### Test a Cursor Rule:

1. **Copy to project:**
   ```bash
   cat cursor-rules/pr-review/RULE.md >> my-project/.cursorrules
   ```

2. **Try it:**
   - Make a code change
   - Ask Cursor to review it
   - See if it follows the process

3. **Refine:**
   - Did Cursor understand?
   - Did it follow the steps?
   - Update adapter or playbook as needed

---

## Current Adapters

### Planned/Placeholder:
- `pr-review/` - PR review process
- `debugging-routine/` - Debugging workflow

### To Add:
- (Create adapters as you create playbooks)

---

## Resources

### Learning Cursor Rules
- **Official Docs:** https://docs.cursor.com/context/rules-for-ai
- **Video Tutorial:** Search YouTube for "Cursor rules tutorial"
- **Community Examples:** https://github.com/cursor-ai/cursor-rules

### Writing Good Rules
- Be specific (not vague)
- Use examples
- Test with real code
- Iterate based on results

---

*Cursor rules are thin wrappers. The playbook has the real content.*

