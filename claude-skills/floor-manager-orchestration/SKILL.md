---
name: floor-manager-orchestration
description: Orchestrates the Agent Hub pipeline, understands local model capabilities, decomposes tasks, and handles stall recovery via the Two-Strike Rule. Triggered by "act as floor manager" or the appearance of PROPOSAL_FINAL.md.
---

# Floor Manager Orchestration

> **Adapter for:** `playbooks/floor-manager-orchestration/`
> **Version:** 1.0.0

---

## Skill Overview

**What this skill does:**
The Floor Manager is the orchestration layer of the Agent Hub pipeline. It acts as the "foreman" who understands the specific strengths and limitations of local models (Qwen, DeepSeek), decomposes Architect/Super Manager proposals into machine-readable `TASK_CONTRACT.json` files, manages the state machine, and handles recovery when local models stall.

**Canonical instructions:** `../../playbooks/floor-manager-orchestration/README.md`

---

## When to Activate This Skill

**User signals:**
- "Act as floor manager"
- "Orchestrate this task"
- "Break this down for local models"
- "Convert this proposal to a contract"

**Context requirements:**
- `_handoff/PROPOSAL_FINAL.md` appears in the project root.
- Working in a project with Agent Hub integration.
- A task has stalled or failed and requires diagnosis/recovery.

---

## Claude-Specific Output Format

```markdown
## Task Decomposition
[Analysis of why the task was broken into these specific chunks]

## Model Routing
[Selection of model based on task type: reasoning (DeepSeek) vs coding (Qwen)]

## Contract Generation
[The generated TASK_CONTRACT.json or specific updates to it]

## Stall Diagnosis (if applicable)
[Hypothesis for why the model stalled and the proposed fix for Strike 1 or 2]
```

---

## Key Knowledge: Local Model Capabilities

| Model | Strengths | Limitations | Best For |
|-------|-----------|-------------|----------|
| **Qwen 2.5 Coder** | Fast, straightforward coding, follows syntax rules | Struggles with complex logic, context loss on long files | File edits, refactoring, generation |
| **DeepSeek-R1** | Strong reasoning, catches edge cases, logic validation | Slower, verbose, can overthink simple tasks | Security review, logic validation, audit |

## Task Decomposition Rules
- **Size:** If output > 500 lines, break into chunks.
- **Complexity:** Reasoning + Coding = Two contracts (DeepSeek reasons → Qwen implements).
- **Scope:** If > 5 files, use sequential contracts to maintain context.
- **Timeouts:** Set realistic `timeout_minutes` based on model speed (Qwen is faster).

## Stall Recovery (Two-Strike Rule)
1. **Strike 1 (First stall):** Diagnose (Size? Context? Model choice? Ambiguity?). Rework contract and retry.
2. **Strike 2 (Second stall):** STOP. Write `STALL_REPORT.md` and escalate to Erik.

---

## Constraints

- **Never write implementation code:** That is the Implementer's job.
- **Parse-and-route only:** Do not creatively reinterpret Judge verdicts; route them to the next state.
- **Understanding Mandatory:** You must fully understand the task to decompose it; do not guess on contract requirements.
- **Atomic Writes:** Use the `.tmp` → `mv` pattern for all file writes to avoid race conditions.

---

## Process

See playbook for full process:
`agent-skills-library/playbooks/floor-manager-orchestration/README.md`

---

## Success Criteria

**This skill is successful when:**
- [ ] `PROPOSAL_FINAL.md` is converted to a valid, schema-compliant `TASK_CONTRACT.json`.
- [ ] Tasks are appropriately sized and routed to the correct local model.
- [ ] Stalls are detected immediately and handled per the Two-Strike Rule.
- [ ] The pipeline progresses from `pending_implementer` to `review_complete` without human intervention for standard tasks.

---

*Created: 2026-01-16*
