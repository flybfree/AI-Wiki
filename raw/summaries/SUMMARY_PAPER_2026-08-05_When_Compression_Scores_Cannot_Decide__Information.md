---
title: When Compression Scores Cannot Decide: Information Boundaries for Group-Robust LLM Pruning
url: http://arxiv.org/abs/2608.02940v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_23-07-29Z_WhenCompressionScoresCannotDecide_InformationBound.md
generated_at: 2026-08-05 01:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why a compression score can misidentify optimal model pruning candidates and proposes an information-theoretic framework to define boundaries of what each statistic can reliably capture. It demonstrates that dense scores with high reliability still select endpoints worse than alternatives, revealing unresolved group-specific damage.

## Key Takeaways
- A dense pruning score with 0.906 split-half reliability predicted a 16.1% gain but its selected endpoint was 6.0% and 7.7% worse than two controls.
- For equal-weight groups, a conic law gives the exact pooling price for positive linear fixed-candidate damage, including diagonal and full PSD second moments.
- Relative to balanced uniform allocation, a coarse depth allocation cuts worst-group perplexity inflation by 12.6--20.9% across three dense LLMs.

## Context
This work addresses a persistent challenge in large language model compression where statistical metrics do not fully capture the nuanced trade-offs between model capacity and performance. By delineating information interfaces, the authors provide a principled view of when pruning decisions are justified.

## Implications
For practitioners, this framework offers a way to validate that compression scores truly improve worst-group perplexity rather than merely boosting average metrics. It encourages more careful evaluation protocols that respect group-specific damage, leading to more robust and equitable model optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02940v1)
