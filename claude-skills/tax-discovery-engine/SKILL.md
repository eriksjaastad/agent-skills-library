---
name: tax-discovery-engine
description: Intelligence layer for tax processing that transforms transactions into IRS-defensible business expenses, identifying AI R&D deductions and generating audit-ready justifications.
---

# Tax Discovery Engine

> **Adapter for:** Tax Processing Intelligence & AI Router
> **Version:** 1.0.0
> **Persona:** The "Tax Explorer" (Optimizing for AI R&D Write-offs)

---

## Skill Overview

**Name:** Tax Discovery Engine
**Type:** Write-off Hunting & Audit Justification
**Complexity:** High (Intelligence-heavy)

**What this skill does:**
Acts as the "Intelligence Layer" for the Tax Processing system. It transforms raw transactions into IRS-defensible business expenses by applying an "Explorer" lens. It identifies high-value AI R&D deductions (GPUs, LLM tokens, research courses) and generates audit-ready justification sentences.

---

## 🤖 AI Router Integration

This skill is designed to operate across a two-tier inference model to balance cost and capability:

| Tier | Model | Purpose |
| :--- | :--- | :--- |
| **L1: Tagging** | **Local (Ollama/Llama 3)** | Noise reduction, bulk keyword tagging, and initial triage of raw CSV data. |
| **L2: Defense** | **Sonnet 3.5** | High-fidelity reasoning for IRS Publication mapping and generating complex "Audit Defense" sentences. |

---

## 📊 The "Explorer" Deduction Matrix

Mapping common AI/Explorer vendors to Schedule C lines:

| Vendor | IRS Category | Schedule C Line | Pub Ref | Explorer Justification |
| :--- | :--- | :--- | :--- | :--- |
| **OpenAI / Anthropic** | Software / Subscriptions | Line 18 (Office) | Pub 535 | LLM API tokens for AI-driven model research and agent development. |
| **AWS / GCP / Vercel** | Cloud Infrastructure | Line 18 (Office) | Pub 535 | Distributed compute and hosting for R&D application experiments. |
| **Apple / Nvidia** | Equipment / Hardware | Line 13 (Depr) | Pub 946 | High-end development rigs and GPUs for local model training (Section 179). |
| **Growth School / Coursera** | Education & Training | Line 27a (Other) | Pub 334 | Skill maintenance for existing software engineering/AI trade. |

---

## When to Activate This Skill

**Trigger signals:**
- User signal: "Find more write-offs" or "Justify these expenses."
- Data signal: Detection of keywords from the Deduction Matrix in unclassified items.
- Session signal: After a bulk import of 2025/2026 transaction data.

---

## Claude-Specific Workflow

### Phase 1: Local Triage (L1)
1. Scan raw transactions using the local model.
2. Group items by Merchant similarity (e.g., all `APPLE.COM/BILL`).
3. Tag potential "Explorer" items based on the Deduction Matrix keywords.

### Phase 2: Interactive Triage
Generate a **Clarification List** for Erik to confirm business intent:
- *Example:* "I found a $2,499 charge at Apple. Is this the new AI dev rig? Confirm business use % for Section 179."
- *Example:* "Is this Growth School course for AI Agent skill maintenance?"

### Phase 3: Defense Generation (L2)
For every confirmed item, use Sonnet 3.5 to output a **Defense Sentence**:
- **Template:** "This [Merchant] expense is a critical [Usage] tool for [Specific R&D Task], deductible under [Pub Ref]."
- **Persistence:** Append this sentence to the `NormalizedExpense.notes` field.

---

## Success Criteria

**This skill is successful when:**
- [ ] Every high-value asset (>$500) has an attached justification sentence.
- [ ] False positive rate in write-off detection is <5%.
- [ ] Erik spends <5 minutes per batch confirming "Explorer" intent via Interactive Triage.
- [ ] Final report includes mapping to at least 3 distinct IRS Publications.

---

*Institutionalized for the AI Intelligence Phase - Jan 3, 2026*


## Related Documentation

- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[ai_training_methodology]] - AI training
- [[cost_management]] - cost management
- [[queue_processing_guide]] - queue/workflow
- [[tax_documentation]] - tax/accounting


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[ai_model_comparison]] - AI models
- [[case_studies]] - examples
- [[research_methodology]] - research


- [[LOCAL_MODEL_LEARNINGS]] - local AI

- [[ai_training_methodology]] - AI training
- [[cost_management]] - cost management
- [[queue_processing_guide]] - queue/workflow
- [[tax_documentation]] - tax/accounting


- [[LOCAL_MODEL_LEARNINGS]] - local AI

