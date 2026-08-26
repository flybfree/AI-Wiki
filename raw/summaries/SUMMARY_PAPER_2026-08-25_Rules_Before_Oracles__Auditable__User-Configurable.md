---
title: Rules Before Oracles: Auditable, User-Configurable Argument Selection for Deliberative Polling
url: http://arxiv.org/abs/2608.23979v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_02-14-13Z_RulesBeforeOracles_Auditable_User_ConfigurableArgu.md
generated_at: 2026-08-25 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a set of auditable, voter‑controlled rules that replace opaque rankers with recomputable argument selection in deliberative polls. The authors demonstrate that a simple one‑hop reversed endorsement flow, parameterised by a weight function, satisfies seven checkable criteria and improves coverage, order, and mass metrics over random or learned selections.

## Key Takeaways
- The rule is indistinguishable from a random slate on coverage alone because it ignores the order of reasons, but it leads at every prefix on order and mass when authoring is non‑degenerate.  
- A flat weight policy collapses completeness dramatically (0.81 to 0.34) while normalising by author count recovers it to 0.44, showing the weight function as a crucial security control.  
- The choice between ranking arms lies on a coverage‑versus‑mass trade‑off that only a legible rule can expose to voters.

## Context
Deliberative polling relies on mechanisms that decide which arguments each participant sees, yet current implementations use black‑box rankers that hide the selection process. This paper addresses the need for transparent, voter‑configurable rules that preserve both accuracy and legibility in AI‑driven recommendation systems.

## Implications
For practitioners, these rules can be integrated into open‑source platforms to ensure that AI recommendations are interpretable and contestable. By making selection criteria explicit, the approach strengthens trust and aligns AI outcomes with democratic values of accountability and fairness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23979v1)
