# Integration Guide - Using Agent Skills Library

> **How to reference the skills library from different tools**

This guide shows how to make your projects aware of the agent-skills-library so they can use skills.

---

## The Problem

The skills library lives at:
```
.
```

But when you're working in a project:
```
../my-project
```

The AI tools don't automatically know about the skills library. You need to tell them.

---

## Quick Reference

| Tool | How to Reference Skills |
|------|------------------------|
| **Cursor** | Add to `.cursorrules` |
| **Claude Code** | Add to `.claude/skills/` |
| **VS Code** | Add to workspace settings |
| **Anti-Gravity** | Add to project config |
---

## Cursor Integration

### Method 1: Project .cursorrules (Recommended)

In your project's `.cursorrules` file:

```
# Agent Skills Library
Reference skills from: .

Available skills:
- PR Review: See agent-skills-library/playbooks/pr-review/
- Debugging: See agent-skills-library/playbooks/debugging-routine/

When appropriate, follow the processes defined in these playbooks.
```

### Method 2: Global Cursor Settings

In Cursor settings (Cmd+,):
- Search for "Rules for AI"
- Add global rules that reference the library

**Pros:** Available in all projects  
**Cons:** Can't customize per project

### Method 3: Include from Template

When using project-scaffolding template:
```bash
# In new project
cp ../project-scaffolding/templates/.cursorrules-with-skills.template .cursorrules

# Template already references agent-skills-library
```

---

## Claude Code Integration

### Method 1: Symlink Skills (Recommended)

Create symlinks from your project to the skills library:

```bash
cd ../my-project
mkdir -p .claude/skills

# Link specific skills
ln -s claude-skills/pr-review .claude/skills/pr-review
```

**Pros:** Skills stay in sync with library  
**Cons:** Need to symlink each skill you want

### Method 2: Reference in Project Skill

Create a "meta-skill" that references the library:

```bash
mkdir -p .claude/skills/library-reference
```

Create `.claude/skills/library-reference/SKILL.md`:

```markdown
---
name: library-reference
description: Access skills from the central agent-skills-library
---

# Skills Library Reference

This project uses skills from the central library at:
.

## Available Skills

### PR Review
Location: agent-skills-library/playbooks/pr-review/
[Include key instructions or reference the playbook]

### Debugging Routine
Location: agent-skills-library/playbooks/debugging-routine/
[Include key instructions or reference the playbook]
```

---

## VS Code Integration

Add to `.vscode/settings.json`:

```json
{
  "aiAssistant.contextFiles": [
    "playbooks/pr-review/README.md",
    "playbooks/debugging-routine/README.md"
  ],
  "aiAssistant.instructions": "Reference skills from agent-skills-library when applicable"
}
```

---

## Anti-Gravity Integration

Add to your Anti-Gravity project config:

```yaml
# .antigravity/config.yaml
skills:
  library_path: .
  enabled_skills:
    - pr-review
    - debugging-routine
    - code-quality
```

---

## Project Scaffolding Integration

When creating new projects, the template should include skills library references.

### In project-scaffolding templates:

**`.cursorrules.template`:**
```
# Agent Skills Library
Reference: .

[Include key skills relevant to most projects]
```

**`Documents/README.md`:**
```markdown
## AI Assistance

This project uses skills from the central agent-skills-library.

See: .
```

---

## Best Practices

### DO:
- ✅ Reference specific playbooks by path
- ✅ Keep references up to date as skills evolve
- ✅ Document which skills are relevant to each project
- ✅ Use templates to automate references

### DON'T:
- ❌ Copy playbook content into project (defeats single source of truth)
- ❌ Hard-code outdated skill content
- ❌ Reference skills that aren't relevant to the project
- ❌ Forget to update references when skills change

---

## Verification Checklist

After adding skills library to a project:

- [ ] Can Cursor see the skills? (test with a task)
- [ ] Are paths correct? (absolute paths recommended)
- [ ] Are only relevant skills referenced?
- [ ] Is `.cursorrules` committed to git?
- [ ] Do other team members have access to skills library?

---

## Troubleshooting

### "Cursor doesn't see the skills"
- Check paths are absolute
- Verify `.cursorrules` is in project root
- Try explicit "Follow playbook at [path]" instruction

### "Skills are outdated in my project"
- You're copying content instead of referencing
- Switch to path references
- Update to use library paths

### "Too many skills loaded"
- Reference only skills relevant to this project
- Use conditional references (only when needed)

---

*Created: December 29, 2024*  
*Update this guide as you add new tools/editors*

## Related Documentation

- [PROJECT_KICKOFF_GUIDE](../project-scaffolding/Documents/PROJECT_KICKOFF_GUIDE.md) - project setup
- [AI Model Cost Comparison](Documents/reference/MODEL_COST_COMPARISON.md) - AI models
- [Agent Skills Library](../agent-skills-library/README.md) - Agent Skills
- [Project Scaffolding](../project-scaffolding/README.md) - Project Scaffolding
