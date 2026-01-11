# AI Router Delegation Playbook

> **Strategic delegation protocol for AI Agents (Floor Managers) using the AI Router.**

## 🎯 Purpose
To empower AI Agents (Floor Managers) to use the **AI Router** as a highly efficient "Worker" while maintaining cost control, quality, and project integrity. This playbook defines how to break down complex instructions into atomic tasks that can be routed effectively.

## 🏗️ The Chain of Command
1. **The Architect (Human/High-Level AI):** Strategy, cross-project context, and brainstorming.
2. **The Floor Manager (Project AI):** Interprets instructions, manages files, and **delegates** work.
3. **The AI Router (The Worker):** Executes specific, atomic tasks using local or cloud models.

---

## 📋 The Delegation Protocol

### 1. Atomic Breakdown
Never send a high-level goal (e.g., "Refactor the authentication system") directly to the Router. 
- **Decompose** the goal into discrete steps (e.g., "Add type hints to `auth.py`", "Update `validate_token` logic", "Write unit test for `auth.py`").
- **Delegate** each step as a separate `chat()` call.

### 2. Context Injection
The Router is "blind" to the codebase. You (the Floor Manager) must provide the context.
- **Inject signatures:** Provide function signatures for dependencies.
- **Inject snippets:** Provide the specific code block being modified.
- **Be minimal:** Only send what is needed for that specific task to save tokens and avoid confusion.

### 3. Tier Selection Strategy
Choose the appropriate tier based on the **Task Budget** and **Nature of Task**:

| Task Type | Recommended Tier | Example |
|-----------|------------------|---------|
| **Extractive** | `local` | Classification, summaries, extraction, simple logic checks. |
| **Simple Generative** | `cheap` | Refactoring, code cleanup, adding documentation. |
| **Complex Generative** | `expensive` | Creating new complex algorithms, security-critical code. |

### 4. Strict Verification
When a task's success is mandatory for your next step:
- Use `strict=True` in the `chat()` call.
- This ensures the Router raises a loud exception on failure, preventing you from proceeding with bad data or incomplete work.

---

## ✅ Quality Checklist for Floor Managers

- [ ] Have I broken this task into its smallest logical piece?
- [ ] Have I included all necessary code context (but no more)?
- [ ] Did I choose the most cost-effective tier for this specific task?
- [ ] If the task is critical, am I using `strict=True`?
- [ ] Have I reviewed the `telemetry.jsonl` to verify the Worker's performance?

---

## 🚀 Example Delegation
```python
from router import AIRouter

# Floor Manager injecting context for an atomic task
function_to_fix = """
def get_user(id):
    return db.query("SELECT * FROM users WHERE id=" + id)
"""

result = AIRouter().chat(
    tier="cheap",
    strict=True,
    messages=[{
        "role": "user", 
        "content": f"Fix the SQL injection in this function: {function_to_fix}"
    }]
)
```

