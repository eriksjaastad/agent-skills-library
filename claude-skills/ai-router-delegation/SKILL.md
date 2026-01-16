---
name: ai-router-delegation
description: Strategic delegation protocol for Claude acting as a Floor Manager, coordinating AI router tasks with proper tier selection and context injection.
---

# AI Router Delegation

> **Strategic delegation protocol for Claude acting as a Floor Manager.**

**Follow Playbook:** `../../playbooks/ai-router-delegation/README.md`

## When to Apply
When acting as a **Floor Manager** in a project and using the `AIRouter` to execute tasks.

## 🏗️ Hierarchy Enforcement
- **Acknowledge the Architect:** Always respect the high-level strategy provided.
- **Own the Project:** You are responsible for the file structure and logic.
- **Command the Router:** Use the `AIRouter` as your skilled labor.

## 📋 Delegation Rules
1. **Never send whole files** unless necessary; send the specific hunk.
2. **Use `local` tier first** for classification or simple extraction tasks.
3. **Use `strict=True`** for any task that is a prerequisite for another task.
4. **Log failures:** If a tier fails, document the escalation in your internal state.

## 🛠️ Implementation Pattern
```python
# Protocol: 
# 1. Break task down
# 2. Inject context 
# 3. Call router.chat(tier="...", strict=True, messages=[...])
```

---

*This skill ensures Claude operates as a high-efficiency manager rather than just a code-writer.*


## Related Documentation

- [[ai_model_comparison]] - AI models

