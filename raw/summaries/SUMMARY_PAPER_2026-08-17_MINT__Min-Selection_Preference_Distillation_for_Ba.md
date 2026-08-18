---
title: MINT: Min-Selection Preference Distillation for Balanced Multi-Objective Alignment
url: http://arxiv.org/abs/2608.14828v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_19-01-56Z_MINT_Min_SelectionPreferenceDistillationforBalance.md
generated_at: 2026-08-17 21:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Mint (MIN-selection preference distillation), a simple modification to preference‑based training that balances multi‑objective alignment by ranking candidates according to their weakest objective rather than a weighted sum. The method eliminates the collapse of additive rewards, producing agents that improve all objectives simultaneously and reduce imbalance dramatically. Experiments on emotional support and adversarial negotiation show the weaker axis rising from 0.37 to 0.64 with statistical significance.

## Key Takeaways
- Mint replaces the additive reward ranking with a min‑selection rule, which selects the candidate whose weakest objective is highest, thereby distilling a balanced policy.
- The approach achieves the p → negative infinity limit of a generalized‑mean family, effectively shifting from additive to worst‑case selection without altering the DPO objective.
- In multi‑turn interactions, imbalance correction persists as long as the reference policy remains imbalanced, indicating robust and lasting alignment.

## Context
Preference distillation is widely used to align language agents with human preferences, but additive reward functions often cause one objective to dominate while others deteriorate. This limitation hampers applications requiring balanced behavior across multiple goals such as emotional support or negotiation.

## Implications
The min‑selection technique offers a practical fix for imbalanced preference training, enabling more reliable agent performance in complex multi‑objective settings. Practitioners can adopt this one‑line change to improve balance and reduce model collapse without redesigning the entire training pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14828v1)
