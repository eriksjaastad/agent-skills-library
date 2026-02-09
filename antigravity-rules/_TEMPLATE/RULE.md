---
name: template-skill
description: Template for Antigravity skill adapters
---

# Template Antigravity Adapter

This template shows the structure for Antigravity skill adapters.

## Structure

Antigravity adapters are thin wrappers around canonical playbooks:

- **Frontmatter:** YAML with `name` and `description` fields
- **Content:** Brief description and link to canonical playbook
- **Trigger:** These adapters use `trigger: always_on` in the YAML header

## When to Create an Adapter

Create an adapter when:
1. There's a corresponding playbook in `agent-skills-library/playbooks/`
2. The skill is widely useful across projects
3. You want Antigravity users to have access to it

## Examples

See other adapters in `antigravity-rules/` for working examples.
