---
name: tool-runner-patterns
description: Best practices for implementing Claude's Tool Runner pattern, including tool definitions, error handling, security, and integration with the AI Router for agentic workflows.
---

# Tool Runner Patterns

> **Adapter for:** `playbooks/tool-runner-patterns/`
> **Version:** 1.0.0
> **Implementation:** `$PROJECTS_ROOT/_tools/ai_router/tools.py`

---

## Skill Overview

**What this skill does:**
Guides the implementation of Claude's Tool Runner pattern for building agentic workflows. Covers tool definitions, best practices, security considerations, and integration with the existing AI Router infrastructure.

**Canonical instructions:** `../../playbooks/tool-runner-patterns/README.md`

---

## When to Activate This Skill

**User signals:**
- "I want Claude to be able to take actions"
- "How do I add tools to my AI agent?"
- "Build an agent that can read/write files"
- "Implement tool use with Claude"
- "Make Claude agentic"

**Context requirements:**
- Building an AI application with the Anthropic API
- Need for Claude to execute functions/tools
- Creating a personal assistant or automation

---

## Claude-Specific Output Format

When helping implement tools, provide:

```markdown
## Tool Definition

\`\`\`python
@tool("tool_name")
def tool_name(param1: str, param2: int = 10) -> dict:
    """
    Clear description of what this tool does.
    
    Explain when Claude should use it.
    Explain what it returns and any limitations.
    """
    return {"result": ...}
\`\`\`

## Integration

\`\`\`python
from _tools.ai_router import ToolRouter

router = ToolRouter(tools=[tool_name])
result = router.run("User request here")
\`\`\`

## Security Notes
- [Any security considerations]
- [Input validation needed]

## Testing
\`\`\`python
# How to test this tool
\`\`\`
```

---

## Quick Reference

### Create a Tool

```python
from _tools.ai_router import tool

@tool("my_tool")
def my_tool(query: str) -> dict:
    """Description of what this tool does."""
    return {"result": query.upper()}
```

### Run with ToolRouter

```python
from _tools.ai_router import ToolRouter

router = ToolRouter(
    tools=[my_tool],
    max_turns=5,
    verbose=True,
)

result = router.run("Use my_tool on 'hello'")
print(result.text)
```

---

## Constraints

- Always set `max_turns` to prevent infinite loops
- Validate file paths to prevent directory traversal
- Use `is_error: true` for tool failures, not exceptions
- Include detailed descriptions in tool definitions
- Test tools in isolation before integration

---

## Common Patterns

| Pattern | Description |
|---------|-------------|
| File Operations | read, write, list, search files |
| API Integration | web search, weather, external services |
| System Commands | run shell commands (with restrictions) |
| Data Processing | calculate, transform, validate |

---

## See Also

- Playbook: `playbooks/tool-runner-patterns/README.md`
- Implementation: `_tools/ai_router/tools.py`
- Test: `_tools/ai_router/scripts/test_tool_runner.py`
