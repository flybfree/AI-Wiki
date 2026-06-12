---
title: Automated reproducibility assessments in the social and behavioral sciences using large language models
url: http://arxiv.org/abs/2606.13670v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-11_17-58-36Z_Automatedreproducibilityassessmentsinthesocialandb.md
generated_at: 2026-06-11 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language models can automatically evaluate the reproducibility of social and behavioral science studies by comparing their predictions to original results and human reanalysis. Using a dataset of 76 published claims, the LLM pipeline recovered effect sizes in 41% of cases within a small tolerance and matched qualitative conclusions in 96% of instances, outperforming human reanalysts who succeeded only 34% and 74% respectively.

## Key Takeaways
- The LLM achieved reproducibility recovery for 41% of studies with effect size estimates within ±0.05 of Cohen's d, a narrow tolerance that indicates high fidelity.
- Qualitative alignment was strong: the model matched original conclusions in 96% of cases, far exceeding human reanalysis at 74%, showing superior consistency judgment.
- In seven studies the LLM could not generate viable effect sizes, highlighting remaining limitations and data complexity challenges.

## Context
Automating reproducibility assessment is crucial as it reduces reliance on labor‑intensive manual checks. This study demonstrates that LLMs can serve as scalable auditors, offering a low‑cost alternative to human reanalysis in fields where resources are scarce.

## Implications
For researchers, the tool enables systematic auditing of empirical claims without extensive computational effort. For publishers and funding agencies, it provides an objective metric to evaluate claim robustness, potentially improving transparency and trust in social science literature.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.13670v1)
