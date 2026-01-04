# Playbooks

> **The canonical source of truth for AI agent instructions**

Playbooks are tool-agnostic process documentation that any AI can follow.

---

## What Is a Playbook?

A **playbook** is a documented process or skill that you want AI agents to follow consistently.

Think of it like:
- **SOP (Standard Operating Procedure)** in a business
- **Recipe** in cooking
- **Runbook** in DevOps
- **Pattern** in software design

### Key Characteristics:

1. **Tool-agnostic** - Works with any AI (Cursor, Claude, ChatGPT, etc.)
2. **Process-focused** - Describes HOW to do something, not what to build
3. **Reusable** - Apply across multiple projects
4. **Maintainable** - Single source to update
5. **Testable** - You can verify if AI followed it correctly

---

## What Goes in a Playbook?

### ✅ Good Playbook Topics:

- **Code review processes** (checklist, what to look for)
- **Debugging workflows** (systematic approach to finding bugs)
- **Documentation standards** (how to write good docs)
- **Testing strategies** (what tests to write, when)
- **Refactoring patterns** (when and how to refactor)
- **Architecture decisions** (principles to follow)
- **Domain knowledge** (business rules, constraints)
- **Quality standards** (code style, best practices)

### ❌ Not Good Playbook Topics:

- One-off tasks (just give direct instructions)
- Project-specific configs (keep in project `.cursorrules`)
- Constantly changing processes (wait until stable)
- Tool-specific features (that goes in adapters)

---

## Playbook Structure

Each playbook lives in its own directory with this recommended structure:

```
playbooks/
└── [skill-name]/
    ├── README.md           ← Overview and instructions
    ├── checklist.md        ← Quick reference checklist (optional)
    ├── decision-tree.md    ← Decision logic (optional)
    ├── examples/           ← Real examples (optional)
    │   ├── good_example.md
    │   └── bad_example.md
    └── resources/          ← Additional files (optional)
        └── template.md
```

### Minimum Required:
- `README.md` - Main instructions

### Recommended:
- `examples/` - Show don't tell
- `checklist.md` - Quick reference for AI

### Optional:
- `decision-tree.md` - Complex logic
- `resources/` - Templates, reference data

---

## How to Write a Good Playbook

### Template for README.md:

```markdown
# [Skill Name]

## Purpose
What does this playbook help accomplish?

## When to Use
In what situations should this playbook be applied?

## Prerequisites
What should be in place before using this?

## Process

### Step 1: [Action]
Detailed description of first step.

**What to look for:**
- Point 1
- Point 2

**What to avoid:**
- Anti-pattern 1
- Anti-pattern 2

### Step 2: [Action]
Continue with next steps...

## Examples
See examples/ directory for:
- Good: What success looks like
- Bad: Common mistakes to avoid

## Success Criteria
How do you know this was done correctly?

## Common Pitfalls
What mistakes do people (and AIs) commonly make?

## Related Playbooks
- Link to other relevant playbooks
```

---

## Example Playbooks

### Example 1: PR Review

```
playbooks/pr-review/
├── README.md              # Main process
├── checklist.md           # Quick checklist
└── examples/
    ├── good_pr.md         # Example of good PR
    └── bad_pr.md          # Example of bad PR
```

**What it contains:**
- How to review pull requests systematically
- What to check (code quality, tests, docs, security)
- How to give constructive feedback
- Examples of good and bad PRs

### Example 2: Debugging Routine

```
playbooks/debugging-routine/
├── README.md              # Main process
└── decision-tree.md       # Systematic approach
```

**What it contains:**
- Systematic approach to debugging
- Decision tree (what to check first, second, etc.)
- Common bug categories
- When to ask for help vs. keep investigating

### Example 3: Documentation Standards

```
playbooks/documentation-standards/
├── README.md              # Standards
├── templates/
│   ├── README_template.md
│   ├── API_doc_template.md
│   └── ARCHITECTURE_template.md
└── examples/
    ├── good_readme.md
    └── bad_readme.md
```

**What it contains:**
- What makes good documentation
- Required sections for different doc types
- Writing style guidelines
- Templates to use

---

## Writing Tips

### 1. Be Specific

**Bad:**
```
Review the code for quality issues.
```

**Good:**
```
Review for:
- Variable names (descriptive, not single letters)
- Function length (max 50 lines)
- Error handling (all errors caught and logged)
- Tests (100% coverage for business logic)
```

### 2. Provide Context

**Bad:**
```
Check for security issues.
```

**Good:**
```
Security checks:
- SQL injection: Are queries parameterized?
- XSS: Is user input sanitized?
- Auth: Are endpoints protected?
- Secrets: No API keys in code?
```

### 3. Show Examples

**Bad:**
```
Write good commit messages.
```

**Good:**
```
Commit message format:

Good:
- "fix: Handle null values in user profile API"
- "feat: Add email notification for password reset"

Bad:
- "fix stuff"
- "WIP"
- "asdfasdf"
```

### 4. Explain Why

**Bad:**
```
Functions should be small.
```

**Good:**
```
Functions should be small (max 50 lines) because:
- Easier to test
- Easier to understand
- Easier to reuse
- Catches bugs faster
```

---

## Testing Playbooks

### Test with Real Tasks

1. **Try it yourself:** Follow the playbook manually
2. **Give to AI:** Have Cursor/Claude follow it
3. **Observe results:** Did AI do what you wanted?
4. **Refine:** Update based on what worked/didn't

### Quality Checklist

- [ ] Clear purpose stated
- [ ] When to use is obvious
- [ ] Steps are specific and actionable
- [ ] Examples provided (good and bad)
- [ ] Success criteria defined
- [ ] Common pitfalls documented
- [ ] Tool-agnostic (no Cursor/Claude-specific stuff)

---

## Maintenance

### When to Update

- **Process changes:** Update immediately
- **New edge cases discovered:** Add to common pitfalls
- **Better examples found:** Add to examples/
- **AI misunderstands:** Clarify instructions

### Version Control

- Commit playbooks to git
- Use meaningful commit messages
- Review changes like you would code
- Test updates before committing

---

## Current Playbooks

### Planned/Placeholder:
- `pr-review/` - How to review pull requests
- `debugging-routine/` - Systematic debugging approach

### To Add:
- (Add your own as you identify repeating patterns)

---

## Creating Your First Playbook

### Step 1: Identify a Pattern

Think of a task you:
- Do repeatedly across projects
- Explain the same way each time
- Want AIs to handle consistently

### Step 2: Create Directory

```bash
mkdir playbooks/my-skill-name
cd playbooks/my-skill-name
```

### Step 3: Write README.md

Use the template above. Start simple:
- Purpose (one sentence)
- Process (bullet points)
- Example (one good, one bad)

### Step 4: Test It

- Give to Cursor in a real project
- See if it follows correctly
- Refine based on results

### Step 5: Expand Over Time

- Add more examples as you find them
- Add decision trees for complex logic
- Add checklists for quick reference

---

## Questions to Ask Yourself

When creating a playbook:

1. **Could I explain this to a junior developer in 5 minutes?**
   - If yes: Write it down
   - If no: Break it into smaller playbooks

2. **Do I do this the same way every time?**
   - If yes: Good playbook candidate
   - If no: Wait until process stabilizes

3. **Would this help across multiple projects?**
   - If yes: Belongs here
   - If no: Keep it project-specific

4. **Could an AI follow this without asking questions?**
   - If yes: Well-written playbook
   - If no: Add more detail/examples

---

*Start with one simple playbook. Build from there.*

