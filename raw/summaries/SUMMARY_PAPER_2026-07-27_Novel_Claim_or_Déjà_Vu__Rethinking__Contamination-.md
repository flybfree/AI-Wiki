---
title: Novel Claim or Déjà Vu? Rethinking "Contamination-Free'' Dynamic Evaluation for Multimodal Automated Fact-Checking
url: http://arxiv.org/abs/2607.23514v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_07-29-47Z_NovelClaimorDéjàVu_Rethinking_Contamination_Free__.md
generated_at: 2026-07-27 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the assumption that dynamic fact‑checking benchmarks are contamination‑free holds true. It compares a static benchmark (AVeriTeC) with a newly built dynamic ClaimReview2025Q4 dataset, revealing that 17–29 % of post‑cutoff claims still contain outdated information and that this can inflate performance metrics by up to 11.34 Macro‑F1 points.

## Key Takeaways
- Dynamic evaluation reduces but does not eliminate contamination risks, as a significant portion (17.09 %–29.30 %) of post‑cutoff claims remain potentially contaminated.
- Many newly published claims can be verified using existing public knowledge available before the model’s cut‑off date or by synthesizing multiple pieces of that knowledge.
- Contamination leads to statistically significant inflation in MAFC performance, raising Macro‑F1 scores and distorting system rankings.

## Context
The rapid deployment of large language models for automated fact‑checking depends on reliable benchmark evaluation. Existing static benchmarks often reuse outdated data, masking true capabilities on fresh claims. This study highlights that such contamination can mislead research and industry assessments.

## Implications
Researchers must adopt strictly contamination‑controlled settings to obtain trustworthy performance estimates. Practitioners should be cautious of inflated metrics when evaluating MAFC systems, ensuring fair comparisons across models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23514v1)
