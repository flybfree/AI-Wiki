---
title: Selection Shapes the Boundary: A Preregistered Replication of Monotonicity and Label Agreement in Unselected NLI Populations
url: http://arxiv.org/abs/2607.19231v1
type: paper-summary
date: 2026-07-21
source_paper: 2026-07-21_16-03-05Z_SelectionShapestheBoundary_APreregisteredReplicati.md
generated_at: 2026-07-21 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reexamines a previously reported negative boundary in natural language inference label agreement by conducting a preregistered replication on unselected SNLI and MultiNLI datasets using the same monotonicity operator tagger. The results show that all predicted contrasts are positive, with no significant effect meeting the smallest interest threshold, indicating the earlier finding may reflect selection bias rather than a population‑level property.

## Key Takeaways
- The replication fails to reproduce the original negative Cliff's delta of -0.284 on unselected NLI populations.  
- All seven predicted contrasts yield positive values, with only one significant contrast having the opposite sign but still below the 0.10 effect size.  
- Simulated tagger misclassification reduces any potential effects, and manual re‑tagging yields four‑class agreement of 0.875 on a fresh sample.

## Context
Natural language inference studies often assume label agreement is a stable property across datasets, yet this work suggests that observed boundaries can be artifacts of selective annotation rather than intrinsic linguistic behavior. Understanding the role of selection in HLV metrics is crucial for reliable cross‑study comparisons and model evaluation.

## Implications
Researchers should explicitly state any sampling or re‑annotation procedures when reporting label agreement results to avoid misleading conclusions. Practitioners relying on these metrics must consider whether their data reflect true population properties or merely artifacts of the selection process used in prior work.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19231v1)
