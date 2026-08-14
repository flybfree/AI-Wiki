---
title: Where You Measure Decides What You Measure: Position Selection in Ablation-Based SAE Evaluation
url: http://arxiv.org/abs/2608.13337v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_15-06-56Z_WhereYouMeasureDecidesWhatYouMeasure_PositionSelec.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the choice of token where a sparse autoencoder latent is measured influences evaluation results, showing that this choice is often dictated by the dictionary rather than experimenter intent. It demonstrates that two models with similar latent semantics can be compared at different tokens, causing variance in reported numbers to stem from position differences. The authors propose a single line of code to fix the protocol and audit five papers.

## Key Takeaways
- The token selected for measuring latent impact is usually chosen by the dictionary, not by the researcher, leading to inconsistent comparisons.
- Two autoencoders with matching decoder similarity can still be evaluated at different tokens, causing most variance to reflect position rather than true differences.
- A simple evaluation fix—measuring all latents at the same token—eliminates this artifact across corpus sizes.

## Context
In AI research, ablation studies rely on sparse autoencoders to isolate the effect of latent dimensions. However, standard practice often fails to disclose where each measurement is taken, obscuring true performance differences and making results incomparable across studies.

## Implications
For practitioners, adopting a consistent position protocol ensures that reported numbers reflect genuine model behavior rather than arbitrary token selection. This standardization will improve reproducibility and trust in AI evaluation metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13337v1)
