# Tool Runner Patterns Playbook

> **Version:** 1.0.0  
> **Last Updated:** January 16, 2026  
> **Purpose:** Best practices for implementing Claude's Tool Runner pattern in agentic workflows

---

## Overview

This playbook documents patterns for implementing tool use with Claude, based on the [official Tool Runner beta](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use).

**Key concepts:**
- **Tools**: Functions that Claude can call during a conversation
- **Tool Runner**: Automated loop that executes tools when requested
- **Agentic workflows**: Multi-turn conversations where Claude takes actions

---

## When to Use This Playbook

**Triggers:**
- Building an AI agent that needs to take actions
- Implementing file operations, API calls, or system commands via Claude
- Creating a personal assistant with capabilities beyond text generation
- Migrating from manual tool handling to Tool Runner

**User signals:**
- "I want Claude to be able to do X"
- "How do I add tools to my AI?"
- "Claude should be able to search/read/write files"

---

## Tool Definition Best Practices

### 1. Write Detailed Descriptions

The description is the most important field. Claude uses it to decide when to call the tool.

**Good:**
```python
@tool("search_codebase")
def search_codebase(query: str, file_type: str = "*") -> list[str]:
    """
    Search for code matching a pattern in the current project.
    
    Use this when the user asks to find specific code, functions, or patterns.
    Returns a list of file paths and matching line numbers.
    Does NOT read file contents - use read_file for that.
    
    Args:
        query: Regular expression pattern to search for
        file_type: File extension filter (e.g., "py", "ts", "*" for all)
    """
```

**Bad:**
```python
@tool("search")
def search(q: str) -> list[str]:
    """Search."""  # Too vague!
```

### 2. Use Clear Parameter Names

```python
# Good: Clear intent
def get_weather(city: str, country_code: str = "US") -> dict: ...

# Bad: Ambiguous
def get_weather(loc: str, cc: str = "US") -> dict: ...
```

### 3. Handle Errors Gracefully

Return error information rather than raising exceptions:

```python
@tool("read_file")
def read_file(path: str) -> dict:
    """Read contents of a file."""
    try:
        content = Path(path).read_text()
        return {"content": content, "lines": content.count("\n") + 1}
    except FileNotFoundError:
        return {"error": f"File not found: {path}"}
    except PermissionError:
        return {"error": f"Permission denied: {path}"}
```

---

## Common Tool Patterns

### Pattern 1: File Operations

```python
@tool("list_directory")
def list_directory(path: str = ".", pattern: str = "*") -> list[str]:
    """List files and directories in a path."""
    ...

@tool("read_file")
def read_file(path: str, lines: int | None = None) -> dict:
    """Read file contents, optionally limiting to first N lines."""
    ...

@tool("write_file")
def write_file(path: str, content: str) -> dict:
    """Write content to a file. Creates parent directories if needed."""
    ...
```

### Pattern 2: Search & Discovery

```python
@tool("grep_search")
def grep_search(pattern: str, path: str = ".", file_type: str = "*") -> list[dict]:
    """Search for a pattern in files, returns matches with context."""
    ...

@tool("find_files")
def find_files(name_pattern: str, path: str = ".") -> list[str]:
    """Find files by name pattern (supports wildcards)."""
    ...
```

### Pattern 3: External APIs

```python
@tool("web_search")
def web_search(query: str, num_results: int = 5) -> list[dict]:
    """Search the web and return relevant results."""
    ...

@tool("get_weather")
def get_weather(location: str) -> dict:
    """Get current weather for a location."""
    ...
```

### Pattern 4: System Information

```python
@tool("get_system_info")
def get_system_info() -> dict:
    """Get system information (OS, memory, disk space)."""
    ...

@tool("run_command")
def run_command(command: str, timeout: int = 30) -> dict:
    """Run a shell command with timeout. Returns stdout/stderr."""
    ...
```

---

## Tool Runner Architecture

### Basic Flow

```
User Message
     ↓
┌────────────────────────────────────────┐
│  ToolRouter.run()                       │
│  ┌──────────────────────────────────┐  │
│  │ 1. Send to Claude with tools     │  │
│  │ 2. If tool_use → execute         │  │
│  │ 3. Send result back              │  │
│  │ 4. Repeat until end_turn         │  │
│  └──────────────────────────────────┘  │
└────────────────────────────────────────┘
     ↓
Final Response
```

### Integration with AI Router

The `ToolRouter` integrates with the existing `AIRouter` infrastructure:

```python
from _tools.ai_router import AIRouter, ToolRouter, tool

# Basic chat (no tools)
router = AIRouter()
result = router.chat([{"role": "user", "content": "Hello"}])

# Agentic with tools
@tool("my_tool")
def my_tool(x: str) -> str:
    return x.upper()

tool_router = ToolRouter(tools=[my_tool])
result = tool_router.run("Process this with my_tool: hello")
```

---

## Error Handling

### Tool Execution Errors

When a tool raises an exception, include error details:

```python
{
    "type": "tool_result",
    "tool_use_id": "toolu_123",
    "content": "Error: File not found",
    "is_error": true
}
```

Claude will adapt and may try alternative approaches.

### Max Turns Protection

Always set a maximum number of turns to prevent infinite loops:

```python
router = ToolRouter(
    tools=my_tools,
    max_turns=10,  # Stop after 10 tool calls
)
```

---

## Security Considerations

### 1. Validate Inputs

Never trust tool inputs blindly:

```python
@tool("read_file")
def read_file(path: str) -> dict:
    # Validate path is within allowed directory
    allowed_root = Path("./workspace").resolve()
    requested = Path(path).resolve()
    
    if not str(requested).startswith(str(allowed_root)):
        return {"error": "Access denied: path outside workspace"}
    
    return {"content": requested.read_text()}
```

### 2. Limit Dangerous Operations

```python
# Dangerous - don't do this
@tool("run_command")
def run_command(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True)  # 😱

# Safer - whitelist commands
ALLOWED_COMMANDS = {"ls", "cat", "grep", "find"}

@tool("run_command")  
def run_command(cmd: str) -> dict:
    base_cmd = cmd.split()[0]
    if base_cmd not in ALLOWED_COMMANDS:
        return {"error": f"Command not allowed: {base_cmd}"}
    # Execute with restrictions...
```

### 3. Rate Limiting

Consider adding rate limits for expensive operations:

```python
from functools import wraps
from time import time

def rate_limit(calls_per_minute: int):
    def decorator(func):
        calls = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time()
            calls[:] = [t for t in calls if now - t < 60]
            if len(calls) >= calls_per_minute:
                return {"error": "Rate limit exceeded"}
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@tool("expensive_api_call")
@rate_limit(10)  # Max 10 calls per minute
def expensive_api_call(query: str) -> dict:
    ...
```

---

## Testing Tools

### Unit Testing Individual Tools

```python
def test_read_file():
    # Create temp file
    tmp = Path("/tmp/test.txt")
    tmp.write_text("hello\nworld")
    
    result = read_file.execute(path=str(tmp))
    
    assert result["content"] == "hello\nworld"
    assert result["lines"] == 2
```

### Integration Testing with Mock

```python
def test_tool_router_with_mock():
    @tool("mock_tool")
    def mock_tool(x: str) -> str:
        return f"processed: {x}"
    
    router = ToolRouter(tools=[mock_tool], verbose=True)
    result = router.run("Use mock_tool on 'test'")
    
    assert len(result.tool_calls) >= 1
    assert any(tc.tool_name == "mock_tool" for tc in result.tool_calls)
```

---

## References

- [Claude Tool Use Documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)
- [Tool Runner Beta](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#tool-runner-beta)
- AI Router implementation: `$PROJECTS_ROOT/_tools/ai_router/tools.py`
