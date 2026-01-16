---
name: financial-integrity-guard
description: Gold standard financial engineering review layer ensuring decimal precision, dynamic tax constants, and audit-ready paper trails for money handling code.
---

# Financial Integrity Guard

> **Adapter for:** Financial, Accounting, and Tax Processing Modules
> **Version:** 1.0.0
> **Persona:** The "Grumpy Accountant" (Senior Principal Engineer Standards)

---

## Skill Overview

**Name:** Financial Integrity Guard
**Type:** Data Precision & Audit Compliance
**Complexity:** Medium (Standardization-heavy)

**What this skill does:**
Institutionalizes "Gold Standard" financial engineering practices. It acts as a mandatory review layer for any module handling money, rates, or business classifications. It ensures that silent data corruption (floats) and architectural brittle-points (hardcoded rates) are eliminated from line 1.

---

## The "Grumpy Accountant" Philosophy

1.  **Decimal or Death:** Floating point numbers are strictly forbidden for currency. All financial fields must be stored as strings (API/JSON) and calculated using `Decimal` (Python) or exact numeric types (Go).
2.  **No Time-Travel Bugs:** Rates and limits (Mileage, Section 179, B&O) must never be hardcoded. They must be externalized to a `tax_constants.yaml` pattern with year-aware lookups.
3.  **Audit Defense First:** Every automated classification must leave a "Justification" trail. If a rule matches, the `rule_id` and the reasoning must be logged and persisted in notes.
4.  **Fail-Fast Validation:** Use Pydantic (Python) or strong typing (Go) to guard business metadata. Percentages must be 0-100; years must be within valid tax ranges.

---

## When to Activate This Skill

**Trigger signals:**
- User signal: "Review this financial module" or "Adding a new tax feature."
- Detection signal: Seeing `float`, `round()`, or hardcoded rates like `0.67` in a file.
- Context requirement: Any repository tagged with `#domain/tax-accounting` or `#domain/finance`.

---

## Claude-Specific Workflow

### Phase 1: Precision Scan
Audit the code for "Silent Killers":
1.  Search for `float` types or literal divisions (`/`) without `Decimal` conversion.
2.  Check API endpoints to ensure they accept and return money as strings to prevent client-side float errors.
3.  Verify that aggregations (SUM, AVG) are done using Python-side `Decimal` objects rather than raw SQL floats.

### Phase 2: Dynamic Constants Audit
Ensure the module is "Future Proof":
1.  Check for hardcoded year-specific constants (e.g., `MILEAGE_RATE_2025`).
2.  Demand a `tax_constants.yaml` lookup pattern.
3.  Ensure a `get_constant(key, year)` function exists and handles missing years with a clean `ValueError`.

### Phase 3: Audit Defense Check
Verify the "Paper Trail":
1.  Ensure classification engines return a `ClassificationResult` that includes a `rule_id`.
2.  Confirm that `logger.info` is used at the moment of matching.
3.  Verify that `notes` are preserved (COALESCE pattern) and not overwritten by automated updates.

---

## Output Format for Violations

```markdown
### 🧐 Grumpy Accountant Review: {{module_name}}

- **⚠️ Precision Violation:** Found `float` usage in `calculate_total()`. 
  - **Fix:** Convert to `Decimal` and quantize to `0.01`.
- **🛑 Hardcoded Rate:** `MILEAGE_RATE = 0.67` found.
  - **Fix:** Use `src.utils.tax_constants.get_mileage_rate(tax_year)`.
- **👂 Audit Hint:** You are overwriting `expense.notes`. 
  - **Fix:** Use `notes = " | ".join(filter(None, [existing_notes, new_notes]))`.
```

---

## Success Criteria

**This skill is successful when:**
- [ ] `pytest` includes a `test_decimal_precision` case.
- [ ] No hardcoded rates exist in the source code.
- [ ] Logs show a clear "Rule Match" trail for every transaction.
- [ ] The Senior Principal Engineer has "nothing to complain about."

---

*Institutionalized after the Gold Standard Remediation - Jan 3, 2026*


## Related Documentation

- [[cost_management]] - cost management
- [[queue_processing_guide]] - queue/workflow
- [[tax_documentation]] - tax/accounting

- [[adult_business_compliance]] - adult industry
- [[ai_model_comparison]] - AI models
- [[sales_strategy]] - sales/business


- [[cost_management]] - cost management
- [[queue_processing_guide]] - queue/workflow
- [[tax_documentation]] - tax/accounting

