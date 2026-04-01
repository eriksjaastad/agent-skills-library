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

**How does Antigravity use it?**  
`/antigravity-rules/` - Thin wrappers that reference playbooks.

**How to add a new skill:**
1. Create `playbooks/my-skill/README.md` (the canonical instructions)
2. Create `cursor-rules/my-skill/RULE.md` (Cursor wrapper)
3. Create `claude-skills/my-skill/SKILL.md` (Claude wrapper)
4. Create `antigravity-rules/my-skill/RULE.md` (Antigravity wrapper)

**Naming convention:**  
`lowercase-with-dashes` (e.g., `pr-review`, `debugging-routine`)

**Versioning:**  
Use git for tracking. See "Versioning & Upgrades" section below for detailed versioning strategy.

---

## Overview

Reusable AI agent skills and playbooks library documenting patterns for Claude, Cursor, and general AI workflows. This foundation-complete knowledge base contains 15 markdown files organizing proven skills, cursor rules, playbooks, and integration guides that can be reused across multiple AI-assisted development projects. The library focuses on capturing successful patterns for AI collaboration and making them available for future projects.

## Key Components

### Skills
- `claude-skills/` - Claude-specific patterns (27 skills)
  - Code review techniques
  - Documentation generation
  - Architecture analysis
  - Refactoring workflows
  - **Audit Whisperer** - Contextual hygiene & noise reduction
  - **AI Router Delegation** - Strategic task routing & floor management

### Rules
- `cursor-rules/` - Cursor IDE rules (25 rules)
  - Project-specific configurations
  - Code style enforcement
  - AI behavior guidelines
  - Context management
  - **AI Router Delegation** - Rules for Floor Manager/Worker workflow

- `antigravity-rules/` - Antigravity agent rules (10+ adapters)
  - Integration guides and workflows
  - Agent-specific patterns
  - Links to canonical playbooks

### Playbooks
- `playbooks/` - Reusable workflows (26 playbooks)
  - Sprint planning
  - Bug investigation
  - Feature development
  - Testing strategies
  - **AI Router Delegation** - Chain of Command & Atomic Delegation protocol

### Documentation
- Root documentation (3 MD files)
  - `README.md` - Library overview
  - `FIRST_SKILL_COMPLETE.md` - Milestone
  - `INTEGRATION_GUIDE.md` - Usage guide

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
- [... [truncated]

---

## Status

**Tags:** #map/project #p/agent-skills-library  
**Status:** #status/active  
**Last Major Update:** December 2025 (foundation complete)  
**Purpose:** Pattern library for AI-assisted development

## Recent Activity

- 2026-01-11: docs: add Context Bridge size warning (learning loop capture)
- 2026-01-11: feat: add staged-prompt-engineering playbook
- 2026-01-03: Initial commit: Codify agent skills for Muffin Pan Recipes ecosystem


scaffolding_version: 1.0.0
scaffolding_date: 2026-01-14

## Related Documentation

- [Code Review Anti-Patterns](../.agent/rules/CODE_REVIEW_ANTI_PATTERNS.md) - code review
- [Tiered AI Sprint Planning](patterns/tiered-ai-sprint-planning.md) - prompt engineering
- [AI Model Cost Comparison](../.agent/rules/MODEL_COST_COMPARISON.md) - AI models
- [Agent Skills Library](../agent-skills-library/README.md) - Agent Skills
- [muffinpanrecipes/README](../ai-model-scratch-build/README.md) - Muffin Pan Recipes
- [AGENTS.md](AGENTS.md)
- [CLAUDE.md](CLAUDE.md)
- [FIRST_SKILL_COMPLETE.md](FIRST_SKILL_COMPLETE.md)
- [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)
- [README.md](README.md)
- [TODO.md](TODO.md)
- [skill-agent-recommendation-loop.md](skill-agent-recommendation-loop.md)
- [skill-niche-scarcity-engineering.md](skill-niche-scarcity-engineering.md)
- [skill-resource-aliasing-protocol.md](skill-resource-aliasing-protocol.md)
- [skill-social-dispatcher-logic.md](skill-social-dispatcher-logic.md)
## CI / Automated Code Review

Pull requests are automatically reviewed by Claude Sonnet via a [centralized reusable workflow](https://github.com/eriksjaastad/tools/blob/main/.github/workflows/claude-review-reusable.yml) hosted in the `tools` repo.

**On every PR:**
- Tests run (if any exist)
- AI reviews the diff against project standards and governance protocol
- Posts a sticky review comment and a `claude-review` commit status
- Auto-merges on APPROVE, blocks on REQUEST_CHANGES

See [tools repo](https://github.com/eriksjaastad/tools) for configuration details.
