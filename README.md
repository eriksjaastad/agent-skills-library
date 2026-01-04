# Agent Skills Library

> **One source of truth, many tools**

A centralized library of AI agent instructions that works across Cursor, Claude, ChatGPT, and any future AI tool.

---

## TL;DR - Quick Index

**What is this?**  
A library of reusable AI instructions (playbooks) with tool-specific adapters.

**Where is the truth?**  
`/playbooks/` - Write instructions here once, use everywhere.

**How does Cursor use it?**  
`/cursor-rules/` - Thin wrappers that reference playbooks.

**How does Claude use it?**  
`/claude-skills/` - Thin wrappers that reference playbooks.

**How to add a new skill:**
1. Create `playbooks/my-skill/README.md` (the canonical instructions)
2. Create `cursor-rules/my-skill/RULE.md` (Cursor wrapper)
3. Create `claude-skills/my-skill/SKILL.md` (Claude wrapper)

**Naming convention:**  
`lowercase-with-dashes` (e.g., `pr-review`, `debugging-routine`)

**Versioning:**  
Use git for tracking. See "Versioning & Upgrades" section below for detailed versioning strategy.

---

## Versioning & Upgrades

> **Treat skills like software - version, test, and upgrade systematically**

### Why Version Skills?

Skills evolve over time:
- **Improvements discovered** through testing
- **Edge cases found** in real usage
- **Better patterns learned** from experience
- **Breaking changes** that need tracking
- **Need to rollback** if new version breaks things

Just like software, you need to know:
- What changed and why
- Which version works best
- When to upgrade
- How to rollback if needed

---

### Versioning Strategy

**Use Git as Primary Version Control:**

```bash
# Every skill change gets committed
git add playbooks/pr-review/
git commit -m "pr-review: Add security checklist (v1.1.0)"

# Tag major releases
git tag -a pr-review-v1.0.0 -m "PR review skill v1.0.0 - initial stable"
git tag -a pr-review-v1.1.0 -m "PR review skill v1.1.0 - added security"
```

**Semantic Versioning (SemVer) for Skills:**

`MAJOR.MINOR.PATCH` (e.g., `1.2.3`)

- **MAJOR (1.x.x)** - Breaking changes
  - Complete rewrite of process
  - Incompatible with previous version
  - Requires projects to update how they use it
  
- **MINOR (x.1.x)** - New features, backwards compatible
  - Added new checklist items
  - Added new examples
  - Enhanced existing steps
  
- **PATCH (x.x.1)** - Bug fixes, clarifications
  - Fixed typos
  - Clarified confusing instructions
  - Added missing details

**Example Version History:**

```
pr-review-v1.0.0 (2024-12-28) - Initial release
pr-review-v1.0.1 (2024-12-29) - Clarified security section
pr-review-v1.1.0 (2024-12-30) - Added performance checklist
pr-review-v2.0.0 (2025-01-15) - Complete rewrite with new structure
```

---

### Version Tracking in Skills

**Add version info to playbook README:**

```markdown
# PR Review Playbook

**Version:** 1.1.0  
**Last Updated:** 2024-12-30  
**Changelog:** See CHANGELOG.md

[Rest of playbook...]
```

**Create CHANGELOG.md for each skill:**

```markdown
# PR Review - Changelog

## [1.1.0] - 2024-12-30
### Added
- Performance checklist section
- Examples of performance issues

### Changed
- Reorganized security section for clarity

## [1.0.1] - 2024-12-29
### Fixed
- Typo in security section
- Clarified when to request changes vs. comment

## [1.0.0] - 2024-12-28
### Added
- Initial release
- Basic PR review process
- Code quality checklist
- Security checklist
```

---

### Directory Structure with Versioning

```
agent-skills-library/
├── playbooks/
│   └── pr-review/
│       ├── README.md              ← Current version
│       ├── CHANGELOG.md           ← Version history
│       └── checklist.md
│
└── .git/
    └── tags/                      ← Git tags for versions
        ├── pr-review-v1.0.0
        ├── pr-review-v1.1.0
        └── pr-review-v2.0.0
```

---

### Upgrade Process

**When to Upgrade a Skill:**

1. **Discovered through testing** - Skill doesn't work as expected
2. **Found edge case** - Real usage revealed gap
3. **Better approach found** - Learned improved method
4. **Breaking change needed** - Current approach fundamentally flawed

**Upgrade Workflow:**

```bash
# 1. Create branch for upgrade
git checkout -b upgrade/pr-review-v1.1.0

# 2. Update the playbook
# - Edit playbooks/pr-review/README.md
# - Update version number in README
# - Add entry to CHANGELOG.md

# 3. Test the changes
# - Use skill in real project
# - Document test results
# - Verify improvement over previous version

# 4. Commit with version info
git add playbooks/pr-review/
git commit -m "pr-review: v1.1.0 - Add performance checklist

Added:
- Performance review section
- Examples of common perf issues
- Checklist for optimization

Tested with: Project X, Y, Z
Results: Caught 3 perf issues that v1.0 missed"

# 5. Merge and tag
git checkout main
git merge upgrade/pr-review-v1.1.0
git tag -a pr-review-v1.1.0 -m "v1.1.0 - Performance checklist"
git push origin main --tags
```

---

### Testing Before Upgrade

**Validation Checklist:**

Before releasing new version:
- [ ] Test with at least 3 real examples
- [ ] Compare results to previous version
- [ ] Verify improvement or new capability
- [ ] Check backward compatibility (for MINOR/PATCH)
- [ ] Update CHANGELOG.md
- [ ] Update version number in README
- [ ] Document breaking changes (for MAJOR)

**Comparison Testing:**

```markdown
## Version Comparison: v1.0.0 vs v1.1.0

**Test Case:** PR with performance issues

**v1.0.0 Results:**
- Caught: Security issues, code quality
- Missed: 3 performance problems

**v1.1.0 Results:**
- Caught: Security issues, code quality, 3 perf problems
- Added value: Performance checklist and examples

**Verdict:** Upgrade improves detection, backward compatible ✅
```

---

### Rollback Strategy

**If new version has problems:**

```bash
# Rollback to previous version
git checkout pr-review-v1.0.0 playbooks/pr-review/

# Or revert the commit
git revert <commit-hash>

# Document why
git commit -m "Rollback pr-review to v1.0.0 - v1.1.0 causing issues

Issue: New performance checklist too strict, false positives
Action: Reverted to v1.0.0
Plan: Refine v1.1.0 and re-release as v1.1.1"
```

---

### Cross-Project Upgrade Management

**Track which projects use which versions:**

```markdown
# SKILL_USAGE.md

## PR Review Skill

| Project | Version | Last Tested | Notes |
|---------|---------|-------------|-------|
| Trading Projects | v1.1.0 | 2024-12-30 | Working well |
| Image Workflow | v1.0.1 | 2024-12-29 | Not upgraded yet |
| Cortana AI | v1.1.0 | 2024-12-30 | Upgrade successful |
```

**Upgrade Communication:**

When releasing new version, document:
- What changed
- Why it changed
- Impact on existing projects
- Upgrade instructions (if breaking)

---

### Version Compatibility

**Adapter Versioning:**

When playbook changes significantly, adapters may need updates:

```markdown
# cursor-rules/pr-review/RULE.md

**Playbook Version:** v1.1.0  
**Adapter Version:** v1.1.0  
**Compatible With:** Playbook v1.x.x

[Rest of adapter...]
```

**Breaking Changes:**

If MAJOR version changes playbook structure:
- Update all adapters (Cursor, Claude, etc.)
- Tag adapter versions to match
- Document migration path

---

### Maintenance Schedule

**Regular Review:**

- **Monthly:** Review usage, gather feedback
- **Quarterly:** Evaluate for improvements
- **Yearly:** Major version consideration (if needed)

**Between Reviews:**

- Patch versions as bugs found
- Minor versions as improvements discovered
- Document all changes in CHANGELOG

---

### Best Practices

**DO:**
- ✅ Commit every change with clear message
- ✅ Tag stable releases
- ✅ Maintain CHANGELOG.md
- ✅ Test before upgrading version
- ✅ Document breaking changes clearly
- ✅ Track which projects use which versions

**DON'T:**
- ❌ Skip version numbers (confusing)
- ❌ Make breaking changes in MINOR/PATCH
- ❌ Forget to update CHANGELOG
- ❌ Release untested versions
- ❌ Delete old versions (git history is valuable)

---

## The Problem This Solves

**Before:** You write the same instructions in multiple places:
- `.cursorrules` file for Cursor
- Custom instructions for Claude
- System prompts for ChatGPT
- Scattered documentation everywhere

**Result:** 
- Instructions get out of sync
- You forget which version is correct
- Adding a new AI tool means rewriting everything
- No single source of truth

**This Library:** Write instructions once, adapt them for each tool

---

## How It Works

### The Pattern: Canonical + Adapters

```
playbooks/           ← The TRUTH (tool-agnostic instructions)
    └── pr-review/
        ├── README.md
        └── checklist.md

cursor-rules/        ← Cursor adapter (thin wrapper)
    └── pr-review/
        └── RULE.md   → "Follow playbooks/pr-review"

claude-skills/       ← Claude adapter (thin wrapper)
    └── pr-review/
        └── SKILL.md  → "Follow playbooks/pr-review"
```

### Three Layers:

1. **Playbooks** (`playbooks/`) - The canonical content
   - Tool-agnostic instructions
   - Process documentation
   - Decision trees
   - Examples
   - This is where you edit and maintain content

2. **Cursor Rules** (`cursor-rules/`) - Cursor-specific wrappers
   - Small files that reference playbooks
   - Add Cursor-specific formatting/constraints
   - Goes into project `.cursorrules` files

3. **Claude Skills** (`claude-skills/`) - Claude-specific wrappers
   - Small files that reference playbooks
   - Add Claude-specific output formats
   - Add Claude-specific resources

---

## When to Use This

### ✅ Use for:
- **Repeatable processes** (PR reviews, debugging routines, code reviews)
- **Complex workflows** (multi-step procedures you want all AIs to follow)
- **Standards** (code style, documentation patterns, architecture decisions)
- **Domain knowledge** (project-specific context, business rules)

### ❌ Don't use for:
- One-off tasks
- Project-specific configs (those stay in project `.cursorrules`)
- Constantly changing processes (wait until they stabilize)

---

## Directory Structure

```
agent-skills-library/
├── README.md                    ← You are here
│
├── playbooks/                   ← CANONICAL CONTENT
│   ├── README.md                ← What playbooks are
│   ├── pr-review/               ← Example: PR review process
│   │   ├── README.md
│   │   ├── checklist.md
│   │   └── examples/
│   │       ├── good_pr.md
│   │       └── bad_pr.md
│   └── debugging-routine/       ← Example: Debugging workflow
│       ├── README.md
│       └── decision-tree.md
│
├── cursor-rules/                ← CURSOR ADAPTERS
│   ├── README.md                ← How to use with Cursor
│   ├── pr-review/
│   │   └── RULE.md              ← "Follow playbooks/pr-review"
│   └── debugging-routine/
│       └── RULE.md
│
└── claude-skills/               ← CLAUDE ADAPTERS
    ├── README.md                ← How to use with Claude
    ├── pr-review/
    │   ├── SKILL.md             ← "Use playbooks/pr-review"
    │   └── resources/
    │       └── pr_template.md
    └── debugging-routine/
        └── SKILL.md
```

---

## Quick Start

### 1. Create a New Playbook

```bash
cd /Users/eriksjaastad/projects/agent-skills-library/playbooks
mkdir my-new-skill
cd my-new-skill
```

Create `README.md`:
```markdown
# My New Skill

## Purpose
What this playbook helps you do.

## When to Use
Situations where this applies.

## Process
Step-by-step instructions.

## Examples
Show good and bad examples.
```

### 2. Add Cursor Adapter

```bash
cd ../../cursor-rules
mkdir my-new-skill
cd my-new-skill
```

Create `RULE.md`:
```markdown
# My New Skill (Cursor Rule)

**Follow:** `agent-skills-library/playbooks/my-new-skill/`

When working on [specific context], apply the process from the playbook above.

## Cursor-Specific Notes
- Output format: [specify]
- File handling: [specify]
```

### 3. Add to Project

In your project's `.cursorrules`:
```
# Include skill from library
@include agent-skills-library/cursor-rules/my-new-skill/RULE.md
```

---

## Usage Examples

### For Cursor

**Option 1: Direct reference in `.cursorrules`**
```
# PR Review Skill
When reviewing pull requests, follow the process in:
agent-skills-library/playbooks/pr-review/

Use the checklist from playbooks/pr-review/checklist.md
```

**Option 2: Use the pre-made adapter**
```
@include agent-skills-library/cursor-rules/pr-review/RULE.md
```

### For Claude

**In Projects feature:**
```
Knowledge: agent-skills-library/playbooks/pr-review/
Custom Instructions: See claude-skills/pr-review/SKILL.md
```

### For ChatGPT

**In Custom Instructions:**
```
Follow the debugging routine in:
agent-skills-library/playbooks/debugging-routine/
```

---

## Maintenance

### When to Update

1. **Process changes** → Update the playbook (single source)
2. **Tool-specific needs** → Update the adapter (Cursor/Claude rules)
3. **New examples** → Add to playbook examples/

### Version Control

- ✅ Commit playbooks (they're the source of truth)
- ✅ Commit adapters (they're lightweight)
- ✅ Use git to track changes
- ✅ Review changes like code (test with AIs)

---

## Migration Guide

### Step 1: Audit Existing Rules

Find all your current AI instructions:
```bash
# Find Cursor rules
find ~/projects -name ".cursorrules" -o -name "CLAUDE.md"

# List what's in them
grep -h "^#" ~/projects/*/.cursorrules
```

### Step 2: Identify Patterns

Look for:
- Instructions repeated across projects
- Process documentation
- Quality standards
- Domain knowledge

### Step 3: Extract to Playbooks

For each repeating pattern:
1. Create playbook in `playbooks/[skill-name]/`
2. Write tool-agnostic version
3. Add examples
4. Create adapters for tools you use

### Step 4: Update Projects

Replace duplicated rules with references:
```
# Before
[Long detailed instructions about PR reviews...]

# After  
Follow: agent-skills-library/playbooks/pr-review/
```

### Step 5: Test

- Try the playbook with Cursor
- Try with Claude
- Refine based on results

**Note:** Don't migrate everything at once! Start with 1-2 skills and expand.

---

## Learning Resources

### Understanding Cursor Rules
- **Cursor Docs:** https://docs.cursor.com/context/rules-for-ai
- **Video Tutorial:** [Search YouTube: "Cursor rules tutorial"]
- **Pattern:** `.cursorrules` files in project root tell Cursor how to behave

### Understanding Claude Projects
- **Anthropic Docs:** https://support.anthropic.com/en/articles/9517075-what-are-projects
- **Pattern:** Add knowledge files + custom instructions per project

### Prompt Engineering
- **Anthropic Prompt Library:** https://docs.anthropic.com/claude/prompt-library
- **OpenAI Best Practices:** https://platform.openai.com/docs/guides/prompt-engineering
- **Learn:** How to write clear, effective instructions for AI

### This Pattern
- **Inspired by:** Single source of truth principle (common in docs/config management)
- **Similar to:** 
  - Shared libraries in code (reusable modules)
  - Template inheritance (base + overrides)
  - Configuration management (canonical + overrides)

---

## Philosophy

### Write Once, Use Everywhere

Instead of:
```
Project A/.cursorrules     [PR review rules]
Project B/.cursorrules     [PR review rules - slightly different]
Claude Project C           [PR review rules - different again]
```

Do this:
```
agent-skills-library/playbooks/pr-review/  [Canonical rules]
  ↓
Project A → references playbook
Project B → references playbook  
Claude C → references playbook
```

### Benefits

1. **Consistency:** All AIs follow the same process
2. **Maintainability:** Update once, applies everywhere
3. **Scalability:** Easy to add new tools
4. **Learning:** Playbooks become your team's knowledge base
5. **Collaboration:** Share skills across projects/people

---

## Testing & Evaluation

> **Develop testing methodology alongside the skills**

### Why Test Skills?

You need to know if your playbooks actually work:
- Does the AI follow the instructions correctly?
- Does it produce the desired output?
- Is it consistent across different tools (Cursor, Claude, ChatGPT)?
- How do you measure improvement?

### What to Test

**Functional Testing:**
- [ ] AI understands the playbook
- [ ] AI follows the steps in order
- [ ] AI produces expected output format
- [ ] AI handles edge cases
- [ ] AI asks clarifying questions when needed

**Quality Testing:**
- [ ] Output meets quality standards
- [ ] Feedback is constructive and specific
- [ ] Explanations are clear
- [ ] Examples are relevant

**Consistency Testing:**
- [ ] Same playbook works in Cursor
- [ ] Same playbook works in Claude
- [ ] Same playbook works in ChatGPT
- [ ] Results are similar across tools

### How to Test

**Manual Testing (Start Here):**
1. Give AI a real task that uses the skill
2. Observe if it follows the playbook
3. Check output quality
4. Note what worked and what didn't
5. Refine and test again

**Example Test Cases:**
```markdown
## Test: PR Review Skill

**Input:** [Link to PR or code changes]
**Expected Output:** 
- Structured review following playbook format
- Identified issues with severity
- Constructive suggestions
- Approval decision

**Actual Output:** [What AI produced]
**Pass/Fail:** [Did it meet expectations?]
**Notes:** [What to improve]
```

**Automated Testing (Future):**
- Create test cases with expected outputs
- Run playbook against test cases
- Compare results
- Track success rate over time

### Metrics to Track

**Effectiveness:**
- % of times AI follows process correctly
- % of outputs that meet quality standards
- Time saved vs. manual process
- Number of revisions needed

**Consistency:**
- Variance in outputs across tools
- Variance in outputs over time
- Common failure patterns

**Usability:**
- How often you actually use the skill
- How often you reference vs. remember it
- How often you need to clarify instructions

### Testing Framework (To Develop)

**Phase 1 (Now):** Manual testing with notes
- Create `tests/` directory
- Document test cases
- Track results in markdown

**Phase 2 (Later):** Structured evaluation
- Define success criteria per skill
- Create evaluation rubrics
- Regular testing schedule

**Phase 3 (Future):** Automated testing
- Test suite with inputs/expected outputs
- Automated comparison
- Regression testing when updating playbooks

### Directory Structure for Tests

```
agent-skills-library/
├── playbooks/
├── cursor-rules/
├── claude-skills/
└── tests/                          ← To be developed
    ├── README.md                    ← Testing methodology
    ├── pr-review/
    │   ├── test-cases.md
    │   └── results/
    │       ├── 2024-12-28-cursor.md
    │       └── 2024-12-28-claude.md
    └── debugging-routine/
        └── test-cases.md
```

### Iteration Process

1. **Create skill** (playbook + adapters)
2. **Test with real tasks** (at least 3 examples)
3. **Document results** (what worked, what didn't)
4. **Refine playbook** (based on learnings)
5. **Test again** (verify improvements)
6. **Repeat** until consistent results

### Questions to Ask

After each test:
- Did the AI understand the instructions?
- Did it follow the process?
- Was the output useful?
- What would make it better?
- Were there edge cases not covered?
- Is this actually saving time?

### Anti-Patterns to Watch For

- **Over-specification:** Too detailed, AI gets lost
- **Under-specification:** Too vague, AI guesses
- **Tool-specific instructions in playbooks:** Should be in adapters
- **Untested assumptions:** "I think this will work" without trying it
- **One-shot testing:** Test once and assume it always works

---

## Next Steps

1. **Read:** `playbooks/README.md` - Understand what playbooks are
2. **Read:** `cursor-rules/README.md` - Learn Cursor integration
3. **Read:** `claude-skills/README.md` - Learn Claude integration
4. **Try:** Create one simple playbook for a task you repeat often
5. **Test:** Use it in one project, refine based on results
6. **Evaluate:** Document what worked and what needs improvement
7. **Expand:** Add more skills as you identify patterns

---

## Status

**Created:** December 28, 2024  
**Status:** Initial structure - ready to populate with real skills  
**Next:** Start with 1-2 playbooks for commonly repeated tasks  
**Testing:** To be developed alongside skills (see Testing & Evaluation section)

---

*This library grows with your needs. Start small, expand as patterns emerge.*

