# Platform Rules Expert Playbook

> **Tool-agnostic knowledge base for agent configuration across platforms**

## Purpose

Consolidate knowledge about configuring AI agents across:
- Claude Code (CLI)
- Cursor (IDE)
- Antigravity/Gemini (IDE)

Understand where config lives, what enforces vs guides, and how to audit.

---

## Critical Distinction: Policy vs Enforcement

| Type | What It Does | Can Be Bypassed? |
|------|--------------|------------------|
| **Policy** | Guides agent behavior via prompts | Yes - agent can ignore |
| **Enforcement** | Blocks actions at system level | No - hard technical block |

**Policy examples:** Markdown rules files, CLAUDE.md, .cursorrules
**Enforcement examples:** Hooks, UI settings, shell blocks

**Key insight:** Policy is "please don't". Enforcement is "you can't".

---

## Platform 1: Claude Code (CLI)

### Configuration Locations

| File | Type | Scope | Purpose |
|------|------|-------|---------|
| `~/.claude/settings.json` | Enforcement | Global | Permissions, hooks |
| `~/.claude/hooks/*.py` | Enforcement | Global | PreToolUse/PostToolUse intercepts |
| `~/.claude/skills/` | Policy | Global | Personal skills |
| `.claude/skills/` | Policy | Project | Project-specific skills |
| `CLAUDE.md` | Policy | Project | Project instructions |

### settings.json Structure

```json
{
  "permissions": {
    "allow": ["Bash", "Edit", "Write", "Read"],
    "deny": []
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "$HOME/.claude/hooks/your-hook.py",
        "timeout": 5
      }]
    }]
  }
}
```

### Hook Types

| Hook | When | Use Case |
|------|------|----------|
| `PreToolUse` | Before tool executes | Block dangerous commands |
| `PostToolUse` | After tool executes | Validate output, log actions |

### Hook Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Allow (proceed) |
| 2 | Block (show stderr to Claude) |

### Auditing Claude Code

```bash
# Check permissions
cat ~/.claude/settings.json | jq '.permissions'

# List active hooks
cat ~/.claude/settings.json | jq '.hooks'

# Check hook files exist
ls -la ~/.claude/hooks/

# Verify hook is executable
file ~/.claude/hooks/*.py
```

### Common Gotchas

1. **Hook path must be absolute or use $HOME** - relative paths fail
2. **Hooks need shebang** - `#!/usr/bin/env python3`
3. **Exit code matters** - return 2 to block, not 1
4. **stderr shown to Claude** - use it to explain why blocked

---

## Platform 2: Cursor (IDE)

### Configuration Locations

| File | Type | Scope | Purpose |
|------|------|-------|---------|
| `.cursor/rules/*.md` | Policy | Project | Workspace rules |
| `.cursorrules` | Policy | Project | Legacy single-file rules |
| Cursor Settings UI | Enforcement | Global | Protection toggles |

### UI Settings (Enforcement)

Access via: Cursor > Settings > AI

| Setting | What It Does |
|---------|--------------|
| Auto-Run Mode | "Ask Every Time" prevents auto-execution |
| File-Deletion Protection | Blocks file deletion |
| Browser Protection | Blocks browser automation |
| MCP Tools Protection | Requires approval for MCP |
| Dotfile Protection | Protects .env, .gitignore, etc. |
| External-File Protection | Blocks files outside project |

### Rules File Structure

```markdown
# .cursor/rules/00_security.md

## Security Rules

### NEVER Do
- NEVER use `rm` for deletion
- NEVER bypass pre-commit hooks

### ALWAYS Do
- ALWAYS use `trash` for file removal
- ALWAYS run tests before committing
```

### Auditing Cursor

```bash
# Check rules files
ls -la .cursor/rules/

# Check legacy rules
cat .cursorrules 2>/dev/null || echo "No .cursorrules"

# UI settings must be checked manually in Cursor
```

### Common Gotchas

1. **Rules files are policy, not enforcement** - agent can ignore
2. **UI settings are the real enforcement** - set "Ask Every Time"
3. **Multiple rules files load in order** - use 00_, 01_ prefixes
4. **.cursorrules vs .cursor/rules/** - new projects use directory

---

## Platform 3: Antigravity/Gemini (IDE)

### Configuration Locations

| File | Type | Scope | Purpose |
|------|------|-------|---------|
| `~/.gemini/GEMINI.md` | Policy | Global | Global rules |
| `.agent/rules/*.md` | Policy | Project | Workspace rules |
| Terminal Execution Policy | Enforcement | Global | UI setting |

### Global Rules (~/.gemini/GEMINI.md)

```markdown
# GEMINI.md - Global Agent Rules

## Security: Default-Deny Command Policy

### Default stance
- Default: DO NOT auto-run terminal commands
- Prefer "ask me first" over "guess if safe"

### Forbidden operations
- NEVER use `rm` or permanent deletion
- NEVER modify .env files
- NEVER bypass git hooks
```

### Workspace Rules (.agent/rules/)

```markdown
# .agent/rules/00_security_default_deny.md

## Command Policy
- Default DENY all terminal commands
- Ask before executing anything destructive
```

### UI Settings (Enforcement)

Access via: Agent settings > Terminal Execution Policy

| Setting | Recommendation |
|---------|----------------|
| Terminal Execution Policy | "Ask for confirmation" |

### Auditing Antigravity

```bash
# Check global rules
cat ~/.gemini/GEMINI.md

# Check workspace rules
ls -la .agent/rules/

# UI settings must be checked manually
```

### Common Gotchas

1. **GEMINI.md is policy, not enforcement** - agent guidance only
2. **Real enforcement is UI setting** - Terminal Execution Policy
3. **.agent/rules/ must exist** - create directory if missing

---

## Defense Layers (All Platforms)

| Layer | Type | Location | Enforcement Level |
|-------|------|----------|-------------------|
| 1. Shell block | Hard | `~/.zshrc` | Kernel-level |
| 2. Claude hooks | Hard | `~/.claude/hooks/` | PreToolUse intercept |
| 3. Cursor UI | Hard | Cursor settings | "Ask Every Time" |
| 4. Antigravity UI | Hard | Agent settings | Terminal Policy |
| 5. Rules files | Soft | `.cursor/rules/`, `.agent/rules/` | Prompt injection |

### Shell-Level Block (Last Resort)

```bash
# In ~/.zshrc
rm() {
  echo "BLOCKED: rm is disabled. Use 'trash' instead."
  return 1
}
```

This blocks ALL rm usage, including from agents.

---

## Applying Security Policies

### Step 1: Enforcement First

Set up hard blocks that can't be bypassed:
1. Shell-level blocks in ~/.zshrc
2. Claude Code hooks in ~/.claude/hooks/
3. Cursor UI: "Ask Every Time"
4. Antigravity UI: Terminal Execution Policy

### Step 2: Policy Second

Add guidance that shapes behavior:
1. CLAUDE.md with project rules
2. .cursor/rules/ with workspace rules
3. .agent/rules/ with Antigravity rules

### Step 3: Audit Regularly

```bash
# Quick audit script
echo "=== Claude Code ==="
cat ~/.claude/settings.json | jq '.hooks' 2>/dev/null

echo "=== Cursor Rules ==="
ls .cursor/rules/ 2>/dev/null || echo "None"

echo "=== Antigravity Rules ==="
ls .agent/rules/ 2>/dev/null || echo "None"

echo "=== Shell Blocks ==="
grep -A3 "^rm()" ~/.zshrc 2>/dev/null || echo "None"
```

---

## Cross-Platform Skill Deployment

### Same Skill, Different Platforms

| Platform | Skill Location | Format |
|----------|----------------|--------|
| Claude Code | `claude-skills/name/SKILL.md` | YAML frontmatter |
| Cursor | `cursor-rules/name/` | Markdown rules |
| Antigravity | `.agent/rules/` | Markdown rules |

### Pattern

1. Write canonical playbook in `playbooks/name/`
2. Create platform adapters that reference playbook
3. Each adapter uses platform-native format

---

## Troubleshooting

### Hook Not Blocking

1. Check exit code (must be 2, not 1)
2. Check hook path in settings.json
3. Verify hook is executable
4. Check stderr output (shown to Claude)

### Rules Being Ignored

1. Rules are policy, not enforcement
2. Check UI settings for real enforcement
3. Agent may not have loaded rules file

### Cross-Platform Inconsistency

1. Each platform has different enforcement mechanisms
2. Shell-level blocks work across all platforms
3. Use defense-in-depth (multiple layers)

---

## Related

- SECURITY_EVOLUTION.md (project-tracker)
- ~/.claude/hooks/README.md
- project-scaffolding templates
