---
name: handoff
description: Verify infrastructure and prepare handoff to Floor Manager. Use after proposal is complete to ensure database, services, and directories exist before execution.
---

# Handoff

> **Adapter for:** `playbooks/handoff/`

---

## When to Activate

**User signals:**
- "verify dependencies"
- "check infrastructure"
- "ready for handoff"
- "prepare for execution"
- "/handoff"

**Context:**
- After PROPOSAL_FINAL.md is complete
- Before Floor Manager starts
- Final Super Manager step

---

## Verification Checklist

### Database
- [ ] Tables exist OR Task 1 creates them
- [ ] Schema matches design.md

### External Services
- [ ] API keys configured
- [ ] Env vars set (.env or Doppler)

### Directories
- [ ] Output paths exist OR Task 1 creates them
- [ ] Write permissions confirmed

### Prerequisites
- [ ] Dependent features merged
- [ ] Judge PASS confirmed

---

## Output Format

```markdown
# Dependencies Check: [Feature]

**Date:** YYYY-MM-DD
**Status:** READY / BLOCKED

## Database
| Table | Status |
|-------|--------|
| [name] | ✓ Exists / Create in Task 1 |

## External Services
| Service | Status | Config |
|---------|--------|--------|
| [name] | ✓ / BLOCKED | [location] |

## File System
| Directory | Status |
|-----------|--------|
| [path] | ✓ Exists / Create in Task 1 |

## Prerequisites
| Feature | Status |
|---------|--------|
| [name] | ✓ Merged |

## Blockers
| Blocker | Owner |
|---------|-------|
| [item] | [who] |
```

---

## BLOCKED Protocol

If ANY blocker exists:
1. Document in DEPENDENCIES.md
2. **DO NOT PROCEED**
3. Return to /propose
4. Notify Erik
5. Re-attempt when resolved

---

## File Placement

When READY:
```
_handoff/
├── PROPOSAL_FINAL.md
├── DEPENDENCIES.md
└── drafts/
```

---

## Constraints

- ALWAYS verify database tables
- ALWAYS check external service config
- ALWAYS create DEPENDENCIES.md
- NEVER proceed if BLOCKED
- After handoff, Super Manager steps back

**Full playbook:** `agent-skills-library/playbooks/handoff/README.md`
