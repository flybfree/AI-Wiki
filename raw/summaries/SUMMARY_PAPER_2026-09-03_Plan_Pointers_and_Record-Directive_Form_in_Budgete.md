---
title: Plan Pointers and Record-Directive Form in Budgeted Verification of Inherited Agent Memory
url: http://arxiv.org/abs/2609.03450v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-05-38Z_PlanPointersandRecord_DirectiveForminBudgetedVerif.md
generated_at: 2026-09-03 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how an agent that holds six one‑line memories selects a stored record when prompted, focusing on two directive forms — a pointer to the exact record or a criterion that identifies it — and reports measured differences across twelve studies with 14,760 attempts. It finds that length‑matched criteria generally outperform bare IDs by about +35 points in Study D, but this advantage disappears for some models under certain conditions.

## Key Takeaways
- Length‑matched criterion exceeds a bare ID by roughly +35 points in Study D, indicating stronger retrieval guidance when the criterion matches record length.
- Appending the ID nullifies the criterion effect on Claude Opus 5 (40/40 to 0/40), showing that the ID overrides the directive in those models.
- A one‑character plan pointer yields +78 points improvement after correction, demonstrating a powerful shortcut for decision making.

## Context
This work sheds light on how memory retrieval is steered by prompt engineering in large language agents. The results reveal that even small edits to stored directives can dramatically alter model behavior, highlighting the need for precise specification of retrieval logic within AI systems.

## Implications
For developers and researchers building agents with inherited memories, these findings suggest that directive design must consider model‑specific quirks and that a single character change can be decisive. Practitioners should therefore test both pointer and criterion forms to avoid unexpected failures in production deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03450v1)
