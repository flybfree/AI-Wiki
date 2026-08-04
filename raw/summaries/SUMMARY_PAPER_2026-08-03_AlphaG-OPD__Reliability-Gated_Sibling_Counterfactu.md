---
title: AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery
url: http://arxiv.org/abs/2608.01303v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_15-12-58Z_AlphaG_OPD_Reliability_GatedSiblingCounterfactuals.md
generated_at: 2026-08-03 23:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes AlphaG-OPD, a structural on‑policy distillation method for symbolic alpha factor discovery that converts terminal factor evaluations into local action guidance. The framework improves performance across multiple financial markets and random seeds compared with prior approaches.

## Key Takeaways
- Component I determines where to teach by exposing grammar‑valid sibling nodes at partial AST states visited by the current forward policy, guiding the learning process to relevant structural decisions.
- Component II decides reliability: it evaluates three supported siblings under four shared suffixes and only admits a KL‑bounded target when winner agreement is high and a positive empirical lower confidence bound (LCB) exists, ensuring trustworthy teaching signals.
- Component III controls how strongly and for how long to teach by consolidating accepted targets through bounded replay, score‑indexed expiry, and forward‑gradient balancing, without requiring additional factor evaluations.

## Context
On‑policy distillation aims to preserve the diversity of a reward‑proportional distribution while learning from completed expressions. Symbolic alpha factors provide high scores but lack direct feedback on structural choices, creating a gap that AlphaG-OPD addresses by focusing on intermediate sibling comparisons and gating reliable teaching signals.

## Implications
The method offers practitioners a way to enhance factor discovery without extra evaluations, boosting cross‑market robustness in finance. By integrating reliability gating and bounded consolidation, it can be applied beyond financial data to any domain where symbolic reasoning meets reinforcement learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01303v1)
