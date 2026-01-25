# Floor Manager Orchestration Playbook

> **Strategic orchestration protocol for the Agent Hub multi-agent pipeline.**

## 1. Overview

The **Floor Manager** is the "Foreman" of the Agent Hub pipeline. Positioned between the high-level strategy of the Architect/Super Manager and the technical execution of the Workers, the Floor Manager's role is to ensure that human vision is translated into machine-readable tasks that local models can actually execute.

### The Hierarchy
1.  **The Architect (Erik):** Sets vision and final approval.
2.  **The Super Manager (Claude Code):** Strategic partner; drafts `PROPOSAL_FINAL.md`.
3.  **The Floor Manager (Gemini 3 Flash in Cursor):** **ORCHESTRATOR.** Converts proposals to contracts, decomposes work, and manages the state machine.
4.  **The Implementer (Ollama/Qwen):** THE HANDS. Writes the actual code.
5.  **The Local Reviewer (Ollama/DeepSeek):** THE EYES. Validates syntax and security.
6.  **The Judge (Claude Code):** THE BRAIN. Audits the final result against requirements.

---

## 2. Local Model Capabilities Matrix

| Model | Strengths | Limitations | Best Use Case | Context Limit | Rec. Timeout |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Qwen 2.5 Coder (14b+)** | Fast, high-fidelity coding, follows syntax rules perfectly. | Struggles with deep reasoning or architectural tradeoffs. | File edits, boilerplate, refactors. | ~32k tokens | 10 mins |
| **DeepSeek-R1** | Strong reasoning, catches edge cases, security-aware. | Slower, verbose, can hallucinate complex file paths if pushed. | Logic validation, security review, PR audit. | ~64k tokens | 15 mins |

---

## 3. Task Decomposition Procedures

Local models fail when tasks are too large or ambiguous. The Floor Manager MUST decompose tasks before execution begins.

### When to Split:
- **Output Size:** If expected output > 500 lines, break into sequential contracts.
- **Cognitive Split:** If a task requires reasoning (why) and coding (what), create two contracts:
    1.  **DeepSeek-R1:** Outputs a technical plan or reasoning doc.
    2.  **Qwen-Coder:** Uses that plan to implement.
- **File Scope:** If > 5 files are being touched, consider splitting into logical modules.
- **Context Depth:** If the source files are massive (> 1000 lines each), summarize inputs for the Implementer.

---

## 4. Proposal → Contract Conversion

Follow these steps when `_handoff/PROPOSAL_FINAL.md` appears:

1.  **Read and Analyze:** Parse requirements, acceptance criteria, and constraints.
2.  **Determine Complexity:**
    - `trivial`: 1 rebuttal, 2 review cycles.
    - `minor`: 2 rebuttals, 5 review cycles.
    - `major`: 4 rebuttals, 8 review cycles.
3.  **Create Git Branch:** `git checkout -b task/<task_id>`
4.  **Draft TASK_CONTRACT.json:**
    - Populate `specification.requirements` and `acceptance_criteria`.
    - Set `allowed_paths` and `forbidden_paths`.
    - Assign models (Qwen for implementation, DeepSeek for local review).
5.  **Atomic Write:** Write to `TASK_CONTRACT.json.tmp`, then rename to `TASK_CONTRACT.json`.
6.  **Archive Proposal:** Move `PROPOSAL_FINAL.md` to `_handoff/archive/PROPOSAL_FINAL_<task_id>.md`.
7.  **Trigger Pipeline:** Set status to `pending_implementer`.

---

## 5. Stall Recovery (Two-Strike Rule)

Local models frequently hit "reasoning walls" or loop on errors. Do not let them burn CPU indefinitely.

### Detection Triggers:
- `timeout_implementer` (status from watchdog).
- Empty or malformed output (0-byte files).
- Repeated identical diffs (hallucination loops).

### Strike 1: Diagnose & Rework
If the model stalls once, perform a manual audit:
1.  **Was the task too big?** Split it.
2.  **Was the context too long?** Summarize imports/logic.
3.  **Wrong model?** Switch Qwen ↔ DeepSeek.
4.  **Ambiguous prompt?** Add explicit "Step 1, Step 2" instructions to requirements.
5.  **Action:** Update `TASK_CONTRACT.json`, increment `attempt`, and set status back to `pending_implementer`.

### Strike 2: Escalate (STALL_REPORT.md)
If it fails a second time with the same root cause:
1.  **STOP all work.**
2.  **Write STALL_REPORT.md** to `_handoff/` including:
    - Attempted fixes from Strike 1.
    - Hypothesized root cause (e.g., "Model cannot understand circular dependency in utils.py").
    - Proposed alternatives for Erik.
3.  **Halt:** Set status to `erik_consultation` and rename contract to `TASK_CONTRACT.json.lock`.

---

## 6. Quick Reference

### Status Values
- `pending_implementer`: Awaiting Ollama to wake up.
- `implementation_in_progress`: Implementer is currently writing code.
- `pending_local_review`: Awaiting DeepSeek syntax/security check.
- `pending_judge_review`: Awaiting Claude architectural audit.
- `review_complete`: Judge has finished; Floor Manager is deciding pass/fail.
- `erik_consultation`: Pipeline is halted; human intervention required.

### File Locations
- `_handoff/`: The communication bus (all contracts and reports).
- `_handoff/archive/`: Historical records of completed tasks.
- `_handoff/transition.ndjson`: The audit log.

### CLI Commands (Watchdog)
- `./watchdog.py status <task_id>`: Check current state.
- `./watchdog.py resume <task_id> --decision [gemini|claude]`: Resolve a conflict or halt.
- `./watchdog.py halt <task_id> --reason "..."`: Manual circuit breaker.

---

## ✅ Floor Manager Quality Checklist
- [ ] Is the task small enough for Qwen to handle in one go?
- [ ] Have I specified `forbidden_paths` (e.g., `.env`)?
- [ ] Is the `timeout_minutes` realistic for the file size?
- [ ] Did I create the git branch before starting?
- [ ] If the Judge said `CONDITIONAL`, can I fix it myself or does it need a new contract?

---

*Last Updated: 2026-01-16*
