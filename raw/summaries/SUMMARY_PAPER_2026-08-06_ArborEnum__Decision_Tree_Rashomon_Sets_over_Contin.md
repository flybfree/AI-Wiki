---
title: ArborEnum: Decision Tree Rashomon Sets over Continuous Features
url: http://arxiv.org/abs/2608.04310v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_00-40-28Z_ArborEnum_DecisionTreeRashomonSetsoverContinuousFe.md
generated_at: 2026-08-06 00:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ArborEnum, an algorithm that exactly enumerates decision‑tree Rashomon sets for continuous features by leveraging the ordered structure of those features. It also provides a relaxation for approximate enumeration and an anytime refinement process that converges to the full set. Experiments demonstrate orders‑of‑magnitude speedups over existing methods while preserving near‑perfect recall.

## Key Takeaways
- The Rashomon effect can be fully captured by enumerating all decision trees whose regularized loss is near‑optimal, but traditional approaches rely on binarizing continuous features which limits the set of possible splits.  
- ArborEnum exploits the natural ordering of continuous values to generate candidate thresholds without explicit binarization, thus preserving many valid trees and important features.  
- The anytime algorithm progressively refines threshold candidates, delivering increasingly detailed approximations that converge to the exact Rashomon set.

## Context
The Rashomon effect highlights how different models can perform similarly on a task yet differ in interpretability and robustness. Enumerating model sets is valuable for understanding this phenomenon but has been hampered by combinatorial complexity when features are continuous rather than discretized.

## Implications
For practitioners, ArborEnum enables more accurate feature importance analysis without sacrificing speed, supporting better decision‑tree selection and customization. In industry, this can lead to more reliable models that respect user preferences while maintaining computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04310v1)
