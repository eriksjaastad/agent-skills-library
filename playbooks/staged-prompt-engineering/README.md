# Staged Prompt Engineering

> Break complex work into atomic, verifiable chunks that AI agents can execute reliably.

---

## The Problem

When delegating work to AI agents:
- Long prompts cause timeouts or context loss
- Vague instructions lead to scope creep
- No verification = no confidence in results
- Failures are hard to diagnose

## The Solution

**Staged Prompt Engineering** - a pattern for structuring multi-step work into:
1. An **Index** that tracks overall progress
2. **Individual Prompts** (5-10 min each) with built-in verification
3. A **Verification Prompt** that confirms everything works together

---

## The Three Components

### 1. The Index

A master document that:
- Explains the feature/task context
- Lists **Done Criteria** (checkboxes for the whole feature)
- Provides **Execution Order** (which prompts, in what sequence)
- Defines **Key Constraints** (rules that apply to ALL prompts)
- Includes **Escalation Protocol** (what to do when things fail)
- Tracks **Progress** (status per prompt)

### 2. Individual Prompts

Each prompt is atomic (5-10 minutes) and includes:
- **CONSTRAINTS** section at the top (what NOT to do)
- **Task Description** (what TO do)
- **[ACCEPTANCE CRITERIA]** (mandatory checklist)
- **Context Bridge** (actual code/pattern to follow)
- **Verification Command** (how to test it worked)
- **Result** (PASS/FAIL hand-back)

### 3. Verification Prompt

The final prompt that:
- Tests all components together
- Has step-by-step verification commands
- Produces a summary table of PASS/FAIL
- Includes failure handling instructions

---

## Index Template

```markdown
# [Feature Name] - Prompts Index

**Feature:** [One-line description]
**Created:** [Date]
**Executor:** [Who runs this - Floor Manager, etc.]
**Worker Models:** [Recommended models]

---

## Context

[What exists already, what we're building, why]

---

## Done Criteria (Overall Feature)

All must pass for feature complete:

- [ ] **P1:** [First deliverable]
- [ ] **P2:** [Second deliverable]
- [ ] **P3:** [Third deliverable]
- [ ] **V1:** [Verification passes]

---

## Prompt Execution Order

Execute prompts in sequence. Each builds on the previous.

| # | Prompt File | Description | Est. Time |
|---|-------------|-------------|-----------|
| 1 | `PROMPT_01_*.md` | [What it does] | 5-10 min |
| 2 | `PROMPT_02_*.md` | [What it does] | 5-10 min |
| 3 | `PROMPT_V1_VERIFICATION.md` | Verify all components | 5 min |

---

## Key Constraints (Apply to ALL Prompts)

These constraints must be included in every prompt:

- DO NOT [thing that causes problems]
- DO NOT [another anti-pattern]
- COPY patterns from [existing file]
- TIMEOUT: Keep tasks atomic (5-10 min max)

---

## Reference Files

Floor Manager should provide these as context:

1. **[Pattern to follow]:** `path/to/file.py` (lines X-Y)
2. **[Config file]:** `config.py`

---

## Escalation Protocol

If a Worker times out or fails:

1. **Strike 1:** Retry with same model
2. **Strike 2:** Switch model (model-a → model-b)
3. **Strike 3:** HALT and report to Conductor

DO NOT manually implement failed Worker tasks.

---

## Progress Tracking

| Prompt | Status | Worker Model | Notes |
|--------|--------|--------------|-------|
| P1 | [ ] Pending | - | - |
| P2 | [ ] Pending | - | - |
| V1 | [ ] Pending | - | - |

**Overall Status:** [ ] Not Started / [ ] In Progress / [ ] Complete

---

**Hand to Floor Manager to begin execution.**
```

---

## Individual Prompt Template

```markdown
# Prompt [ID]: [Name]

**Task:** [One-line description]
**Estimated Time:** 5-10 minutes
**Worker Model:** [Recommended model]

---

## CONSTRAINTS (READ FIRST)

- DO NOT [anti-pattern 1]
- DO NOT [anti-pattern 2]
- COPY the structure pattern from [existing file]
- OUTPUT a single complete file

---

## Task Description

[What to create/modify, where it goes, what it should do]

---

## [ACCEPTANCE CRITERIA] (MANDATORY CHECKLIST)

- [ ] **File Created:** `path/to/file.py` exists
- [ ] **Function Works:** [Specific function] returns expected result
- [ ] **No Errors:** Import works without exceptions
- [ ] **Pattern Followed:** Matches structure in [reference file]

---

## Context Bridge

[Provide actual code or pattern to follow - not just description]
[⚠️ Keep under ~30 lines for smaller models - reference file paths for larger examples]

```python
# Example pattern the Worker should follow (keep brief!)
def example_function():
    """The Worker should create something like this."""
    pass
```

Or for larger patterns, reference instead of inline:

```markdown
See `scripts/existing_file.py` (lines 41-75) for the pattern to follow.
Key elements: [list what to copy]
```

---

## Verification Command

After creating the file, run:

```bash
cd /path/to/project
python -c "
from module import function
result = function()
assert result is not None, 'ERROR: Expected result'
print('OK - Verification passed')
"
```

**Expected:** [What success looks like]

---

## Result

- [ ] PASS: File created and verification command succeeds
- [ ] FAIL: Describe error

**Hand back to Floor Manager when complete.**
```

---

## Verification Prompt Template

```markdown
# Prompt V1: Verification

**Verifies:** [Feature name] - all components working together
**Estimated Time:** 5 minutes
**Model:** Any

---

## Done Criteria

All must pass:

- [ ] **Component 1:** [What to verify]
- [ ] **Component 2:** [What to verify]
- [ ] **Integration:** [Components work together]

---

## Verification Steps

### Step 1: [First Check]

```bash
[Command to run]
```

**Expected:** [What success looks like]

- [ ] PASS / [ ] FAIL

---

### Step 2: [Second Check]

```bash
[Command to run]
```

**Expected:** [What success looks like]

- [ ] PASS / [ ] FAIL

---

## Result Summary

| Criterion | Status |
|-----------|--------|
| Component 1 | [ ] PASS / [ ] FAIL |
| Component 2 | [ ] PASS / [ ] FAIL |
| Integration | [ ] PASS / [ ] FAIL |

**Overall V1:** [ ] PASS / [ ] FAIL

---

## If Any Step Fails

1. Note which step failed and the error message
2. Report back to Floor Manager
3. Floor Manager determines if retry or escalation needed

---

**Hand back to Floor Manager when complete.**
```

---

## Key Principles

### 1. Atomic Chunks (5-10 minutes)

Each prompt should be completable in 5-10 minutes. This:
- Prevents timeouts
- Makes failures easy to diagnose
- Allows progress tracking
- Enables model switching on retry

### 2. Constraints First

Always start prompts with what NOT to do:
- Prevents scope creep
- Stops common mistakes before they happen
- Makes intent crystal clear

### 3. Context Bridge

Don't just describe what you want - **show it**:
- Provide actual code patterns to follow
- Reference existing files as templates
- Give the Worker something to copy from

⚠️ **Warning for smaller models (qwen3:4b, etc.):**
Keep Context Bridge examples **under ~30 lines**. Large code blocks (~80+ lines) can trigger "Thinking..." analysis loops where the model parses the code instead of executing the task. For bigger examples, reference a file path instead of inlining the code:

```markdown
## Context Bridge

See `scripts/discovery/providers.py` (lines 41-75) for the pattern to follow.

Key elements to copy:
- Dataclass structure
- The `_init_*()` pattern
- Return type annotations
```

*Learning source: project-tracker Phase 4, Jan 2026 - qwen3:4b timeout on 80-line Context Bridge*

### 4. Built-in Verification

Every prompt includes its own test:
- Bash command to verify success
- Expected output clearly stated
- PASS/FAIL result tracking

### 5. Clear Hand-offs

End every prompt with explicit instructions:
- "Hand back to Floor Manager when complete"
- Prevents Workers from going rogue
- Maintains chain of command

### 6. Escalation Protocol

Define what happens on failure BEFORE it happens:
- Strike 1: Retry same model
- Strike 2: Switch models
- Strike 3: Halt and escalate

---

## Real-World Example

See `project-tracker/Documents/planning/phase4_agent_dispatcher/` for a complete implementation:

- `AGENT_DISPATCHER_INDEX.md` - Master index with progress tracking
- `PROMPT_A1_AGENT_REGISTRY.md` - Individual prompt with context bridge
- `PROMPT_A6_VERIFICATION.md` - Verification prompt with step-by-step tests

---

## When to Use This Pattern

**Good fit:**
- Multi-step features (3+ components)
- Work delegated to AI agents
- Tasks that need verification
- Complex integrations

**Not needed:**
- Single-file changes
- Quick fixes
- One-shot prompts

---

## Learning Loop

When prompts fail or timeout:
1. Document what went wrong
2. Identify if it was preventable (constraint missing? context insufficient?)
3. Update the Index constraints or prompt templates
4. Apply learning to future prompt sets

See: `project-scaffolding/patterns/learning-loop-pattern.md`

---

## Related

- **AI Router Delegation** - Choosing which model to use
- **Learning Loop Pattern** - Capturing what works
- **AGENTS.md Prompt Template** - Simpler single-prompt format
