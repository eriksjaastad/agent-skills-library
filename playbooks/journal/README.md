# Journal Preparation Playbook

> **Tool-agnostic instructions for preparing an agent to write a journal entry**

## Purpose

Prepare the writing agent with full context before journaling by:
1. Loading the project's writing instructions
2. Enforcing a privacy guardrail on past entries
3. Sweeping the Kanban board for anomalies
4. Checking for unmerged PRs
5. Identifying stale branches

This playbook does NOT write the journal. It gathers context so the writing agent can produce a grounded, honest entry.

---

## Pre-Flight Checks

### 1. Load Writing Instructions

Read `~/projects/ai-journal/BEFORE_YOU_WRITE.md` and internalize its guidance. This document defines the tone, structure, and philosophy for journal entries.

### 2. Privacy Guardrail

**Do not read existing journal entries.** The `entries/` directory is off-limits. Each entry should be written fresh without influence from past entries. This prevents echo-chamber journaling where the agent just rephrases what it said before.

### 3. Kanban Board Sweep

Query the project tracker for all open tasks:

```
pt tasks
```

Flag anomalies:
- **Stale In Progress:** Cards marked "In Progress" with no recent commits or activity
- **Zombie Review:** Cards in "Review" where the associated PR is already merged
- **Aging To Do:** Cards sitting in "To Do" for more than a week without being picked up
- **Orphaned cards:** Tasks that reference deleted branches or closed PRs

These anomalies are journaling fuel -- they reveal what's actually happening vs. what was planned.

### 4. Open PR Check

List unmerged pull requests:

```
gh pr list --state open
```

For multi-repo workflows, iterate across project directories. Note:
- PRs older than 3 days (may be stuck in review)
- PRs with failing CI (need attention)
- PRs that are approved but not merged (forgotten?)

### 5. Stale Branch Audit

List remote branches that aren't main:

```
git branch -r | grep -v HEAD | grep -v main
```

Stale branches indicate abandoned work, completed features that weren't cleaned up, or experiments that were forgotten. All useful journal material.

---

## Output

Present findings as a structured summary that the writing agent can use as raw material. Do not editorialize -- let the journal writer decide what matters.

```
## Journal Prep Summary

### Writing Instructions
- Key points from BEFORE_YOU_WRITE.md

### Board Anomalies
- [list findings]

### Open PRs
- [list with age and status]

### Stale Branches
- [list with last activity if known]
```

---

## Constraints

- Never read past journal entries
- Never use raw SQL on the task database
- Never write the journal -- only prepare context
- Use `pt` CLI for all task queries
