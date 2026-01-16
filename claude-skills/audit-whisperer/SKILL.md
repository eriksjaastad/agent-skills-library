---
name: audit-whisperer
description: Contextual hygiene and noise reduction layer that filters audit tool output and surfaces relevant tips without blocking development workflow.
---

# Audit Whisperer

> **Adapter for:** `project-tracker` and `audit-agent` integration
> **Version:** 0.1.0 (Draft)
> **Tool:** Claude + Go Audit Agent + AI Router (Local-first)

---

## Skill Overview

**Name:** Audit Whisperer
**Type:** Contextual Hygiene & Noise Reduction
**Complexity:** Low (Integration-heavy)

**What this skill does:**
Acts as a "Pragmatic Triage" layer between the fast, high-volume output of the Go `audit` tool and the user. It uses the `ai_router` (local model preferred) to filter out minor formatting noise and only surface "Whispers" (helpful, non-blocking tips) that are relevant to the user's current session or active projects.

---

## When to Activate This Skill

**Trigger signals:**
- User signal: "What should I clean up?" or "Any tips for this project?"
- Automated signal: After a `./pt scan` or significant project activity (e.g., git commit, many file edits).
- Context requirement: The project being audited must be "Active" or recently modified.

---

## The "Whisper" Philosophy

1. **Never Block Development:** No hard errors, no "fail on save," no mandatory fixes.
2. **Context is King:** If Erik is working on `holoscape`, whisper about `holoscape`. Don't whisper about a forgotten tag in a 2-year-old research folder.
3. **Helpfulness over Compliance:** Phrase findings as tips (👂), not violations (⚠️).
4. **Local-First Inference:** Always try to use the local Ollama model (`llama3.2`) for triage to save costs and maintain privacy.

---

## Claude-Specific Workflow

### Phase 1: Noise Filtering
When presented with raw NDJSON data from the Go `audit` tool:
1. Identify the project(s) the user is currently focused on.
2. Filter for issues in those specific projects.
3. Use the local model to categorize issues into:
   - **Mute:** Minor formatting (e.g., trailing whitespace, missing empty line).
   - **Whisper:** Missing mandatory metadata (e.g., `created` date, project `type`).
   - **Alert:** Critical safety violations (e.g., `rm` usage in a script).

### Phase 2: Dashboard Presentation
Generate a "Whisper Summary" for the Project Dashboard:
- Icon: 👂 (Whisper)
- Text: "Hey, since you're in [Project], the audit tool noticed [Issue]. Want to fix it?"
- Action: Provide a one-click "Apply Fix" button (calling `audit fix`).

---

## Output Format for Whispers

```markdown
### 👂 Active Whispers for {{project_name}}

- **Context:** Recently edited `00_Index_*.md`
- **Tip:** You missed the `#status/active` tag. Adding this will help the dashboard track your progress.
- **Action:** [✨ Apply Fix via Go Audit] | [Ignore]
```

---

## Success Criteria

**This skill is successful when:**
- [ ] Erik receives fewer than 3 alerts per session.
- [ ] Every "Whisper" surfaced is directly related to what he is working on.
- [ ] No development work is slowed down by "Rule Enforcement."
- [ ] Triage is handled locally (FREE).

---

*Drafted during the Gold Standard marathon session - Jan 2, 2026*


## Related Documentation

- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[cost_management]] - cost management
- [[dashboard_architecture]] - dashboard/UI
- [[queue_processing_guide]] - queue/workflow


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[adult_business_compliance]] - adult industry
- [[ai_model_comparison]] - AI models
- [[holoscape_architecture]] - Holoscape
- [[research_methodology]] - research


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[cost_management]] - cost management
- [[dashboard_architecture]] - dashboard/UI
- [[queue_processing_guide]] - queue/workflow


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[audit-agent/README]] - Audit Agent
- [[holoscape/README]] - Holoscape
- [[project-tracker/README]] - Project Tracker


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[cost_management]] - cost management
- [[dashboard_architecture]] - dashboard/UI
- [[queue_processing_guide]] - queue/workflow


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[adult_business_compliance]] - adult industry
- [[ai_model_comparison]] - AI models
- [[holoscape_architecture]] - Holoscape
- [[research_methodology]] - research


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[cost_management]] - cost management
- [[dashboard_architecture]] - dashboard/UI
- [[queue_processing_guide]] - queue/workflow


- [[LOCAL_MODEL_LEARNINGS]] - local AI

