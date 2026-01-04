# Claude Skills

> **Claude-specific adapters that connect Claude to playbooks**

This directory contains Claude-specific wrappers for playbooks.

---

## What Are Claude Skills?

**Claude Skills** are instructions for Claude AI that define:
- How to handle specific tasks
- What process to follow
- Output format preferences
- Project-specific knowledge

In Claude (via Anthropic Console or API), you can:
- Create **Projects** with custom instructions
- Add **Knowledge** (documents Claude can reference)
- Set **System Prompts** for behavior

**Official Docs:** https://support.anthropic.com/en/articles/9517075-what-are-projects

---

## How This Directory Works

### The Pattern:

```
agent-skills-library/
├── playbooks/pr-review/          ← The actual instructions (canonical)
│   ├── README.md
│   └── checklist.md
│
└── claude-skills/pr-review/      ← Thin wrapper for Claude
    ├── SKILL.md                   → "Follow playbooks/pr-review/"
    └── resources/                 → Optional Claude-specific files
        └── pr_template.md
```

### Why Separate?

1. **Playbooks are tool-agnostic** - Work with any AI
2. **Claude skills are Claude-specific** - Add Claude features
3. **Single source of truth** - Update playbook once, all tools benefit
4. **Easy adaptation** - Claude-specific formatting stays here

---

## Structure

Each skill gets its own directory:

```
claude-skills/
├── README.md                      ← You are here
│
├── pr-review/                     ← Example skill
│   ├── SKILL.md                   ← Claude adapter
│   └── resources/                 ← Optional Claude resources
│       └── pr_template.md
│
└── debugging-routine/             ← Another skill
    └── SKILL.md
```

---

## What Goes in SKILL.md

A Claude skill adapter should:

1. **Reference the playbook** (canonical source)
2. **Add Claude-specific output formatting**
3. **Add Claude-specific constraints**
4. **Be SHORT** (the playbook has the details)

### Template:

```markdown
# [Skill Name] (Claude Skill)

**Follow:** `agent-skills-library/playbooks/[skill-name]/`

## When to Apply
[Describe when Claude should use this skill]

## Claude-Specific Notes

### Output Format
[How Claude should structure its response]

Example:
```
## Analysis
[Claude's analysis]

## Recommendations
1. [recommendation]
2. [recommendation]

## Next Steps
[what to do next]
```

### Constraints
- [Any Claude-specific limitations or preferences]

### Resources
[If resources/ directory exists, reference files here]

## Process
See the playbook for full process:
agent-skills-library/playbooks/[skill-name]/README.md

## Quick Reference
[Optional: short checklist for Claude]
```

---

## Using with Claude

### Method 1: In Claude Projects (Web)

1. **Create a Project** in Claude web interface
2. **Add Knowledge:** Upload playbook files
3. **Custom Instructions:** Copy SKILL.md content
4. **Resources:** Upload any files from resources/

### Method 2: In API Calls

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-key")

# Load playbook and skill
with open("playbooks/pr-review/README.md") as f:
    playbook = f.read()

with open("claude-skills/pr-review/SKILL.md") as f:
    skill = f.read()

# Use in system prompt
response = client.messages.create(
    model="claude-opus-4",
    system=[
        {"type": "text", "text": playbook},
        {"type": "text", "text": skill}
    ],
    messages=[
        {"role": "user", "content": "Review this PR..."}
    ]
)
```

### Method 3: In Custom Instructions

If using Claude Chat with custom instructions:
- Paste playbook reference
- Paste skill adapter
- Claude will follow for all conversations

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

### claude-skills/pr-review/SKILL.md (Adapter)
```markdown
# PR Review (Claude Skill)

**Follow:** agent-skills-library/playbooks/pr-review/

## When to Apply
When asked to review pull requests or code changes.

## Claude-Specific Output Format

```
## Code Review Summary
[Brief overview of changes]

## Quality Assessment
- Code Quality: [rating/notes]
- Test Coverage: [rating/notes]
- Documentation: [rating/notes]
- Security: [rating/notes]

## Issues Found
[List of issues with severity and suggestions]

## Recommendations
[Prioritized list of improvements]

## Approval Status
[Approve / Request Changes / Comment]
```

## Constraints
- Be constructive and specific
- Provide code examples when suggesting changes
- Explain WHY not just WHAT
```

---

## Claude-Specific Features

### What You Can Add Here:

1. **Output structure:**
   ```markdown
   Always structure responses as:
   1. Summary (1-2 sentences)
   2. Detailed analysis
   3. Recommendations
   4. Next steps
   ```

2. **Tone/style:**
   ```markdown
   Communication style:
   - Professional but friendly
   - Explain reasoning
   - Provide examples
   - Ask clarifying questions if needed
   ```

3. **Context handling:**
   ```markdown
   When reviewing:
   - Ask for additional context if needed
   - Reference project standards from knowledge base
   - Consider previous feedback in conversation
   ```

4. **Resource templates:**
   ```markdown
   Use template from resources/pr_template.md
   to structure feedback.
   ```

---

## resources/ Directory

Optional directory for Claude-specific files:

```
claude-skills/pr-review/
├── SKILL.md
└── resources/
    ├── pr_template.md        ← Template for PR feedback
    ├── examples.md           ← Claude-specific examples
    └── glossary.md           ← Project-specific terms
```

**Use for:**
- Output templates
- Example interactions
- Project-specific glossary
- Reference data

**Don't duplicate:**
- Keep main content in playbook
- Resources are for Claude-specific adaptations only

---

## Migration from Existing Claude Instructions

### Step 1: Find Current Instructions

Check where you currently have Claude instructions:
- Claude Projects (web interface)
- API system prompts
- Custom instructions
- Scattered in conversations

### Step 2: Categorize

For each instruction:
- **Reusable across tasks?** → Extract to playbook
- **Task-specific?** → Keep as project knowledge
- **Claude-specific formatting?** → Create skill adapter

### Step 3: Extract to Playbook

For reusable instructions:
1. Create playbook: `playbooks/[skill-name]/`
2. Write tool-agnostic version
3. Create Claude adapter: `claude-skills/[skill-name]/SKILL.md`

### Step 4: Update Claude Projects

**Before:**
```
[Long detailed instructions about everything...]
```

**After:**

**Project Knowledge:**
- Add: `playbooks/pr-review/README.md`
- Add: `playbooks/code-quality/README.md`

**Custom Instructions:**
```
Follow the playbooks provided in project knowledge.

Output format preferences:
- Use markdown
- Start with summary
- Provide specific examples
- Explain reasoning

[Project-specific context...]
```

---

## Best Practices

### DO:
- ✅ Keep adapters SHORT (reference playbook)
- ✅ Add Claude-specific output formatting
- ✅ Use resources/ for templates
- ✅ Test with real tasks

### DON'T:
- ❌ Duplicate playbook content
- ❌ Put tool-agnostic instructions here (use playbook)
- ❌ Create skill without playbook
- ❌ Make project-specific (use Claude Projects)

---

## Testing

### Test a Claude Skill:

1. **Create Claude Project:**
   - Upload playbook as knowledge
   - Add skill adapter to custom instructions

2. **Try it:**
   - Give Claude a task that uses the skill
   - See if it follows the process
   - Check output format

3. **Refine:**
   - Did Claude understand?
   - Was output format correct?
   - Update adapter or playbook as needed

---

## Current Skills

### Current Skills:
- `financial-integrity-guard/` - Institutionalizes "Gold Standard" financial engineering practices.
- `tax-discovery-engine/` - AI-optimized write-off hunting and audit justification.
- `audit-whisperer/` - Triage and filtering for project audit output.
- `debugging-routine/` - Standardized debugging workflow.
- `pr-review/` - Pull request review process.
- `youtube-channel-analysis/` - Analytical tool for YouTube data.

---

## Resources

### Learning Claude Projects
- **Anthropic Docs:** https://support.anthropic.com/en/articles/9517075-what-are-projects
- **API Documentation:** https://docs.anthropic.com/claude/reference/messages
- **Prompt Library:** https://docs.anthropic.com/claude/prompt-library

### Writing Good Skills
- Be specific about output format
- Use Claude's strengths (reasoning, examples)
- Test with various inputs
- Iterate based on responses

---

## Claude Code-Specific Details

> **For Claude Code (desktop app with built-in skills system)**

### Skill File Format

Claude Code uses YAML frontmatter in `SKILL.md` files:

```markdown
---
name: your-skill-name
description: Clear description with natural trigger keywords
allowed-tools: Read, Grep, Glob  # Optional: restrict tools
model: sonnet  # Optional: sonnet, opus, haiku
---

# Your Skill Name

## Instructions
[Your instructions here]
```

### Metadata Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase, hyphens/numbers only (max 64 chars) |
| `description` | Yes | Natural trigger keywords (max 1024 chars) |
| `allowed-tools` | No | Restrict which tools Claude can use |
| `model` | No | Specify model (sonnet, opus, haiku) |

### Tool Restrictions

Limit what Claude can do for safety:

```yaml
---
name: read-only-analyzer
description: Analyzes code patterns without making changes
allowed-tools: Read, Grep, Glob
---
```

**Common patterns:**
- **Read-only:** `Read, Grep, Glob`
- **Code generation:** `Read, Write, Edit, Grep, Glob`
- **Full automation:** (no restriction)

### Skill Scopes

- **Personal skills:** `~/.claude/skills/` (available everywhere)
- **Project skills:** `.claude/skills/` (only in this project)
- **Plugin skills:** Bundled with plugins

### Writing Great Descriptions

Use natural trigger keywords:

✅ **Good:** "Analyzes YouTube channel data to generate video content ideas based on successful patterns"

❌ **Bad:** "YouTube helper"

The description determines when Claude offers to use your skill.

### Progressive Disclosure

Keep SKILL.md focused, use supporting files:

```markdown
For detailed API documentation, see [reference.md](reference.md)

For advanced examples, see [examples.md](examples.md)
```

Structure:
```
claude-skills/my-skill/
├── SKILL.md           ← Main skill (keep under 500 lines)
├── reference.md       ← API docs, detailed specs
├── examples.md        ← Usage examples
└── scripts/           ← Helper utilities
```

### Troubleshooting

**Skill Not Triggering?**
- Make description more specific
- Add natural trigger keywords
- Ensure YAML syntax is correct

**Multiple Skills Conflicting?**
- Make descriptions more distinct
- Use specific domain keywords
- Ensure each skill has unique purpose

**Skill Not Loading?**
- File must be named exactly `SKILL.md` (case-sensitive)
- Check YAML syntax (no tabs, start with `---`)
- Path structure: `.claude/skills/skill-name/SKILL.md`
- Try restarting Claude Code

---

*Claude skills are thin wrappers. The playbook has the real content.*

