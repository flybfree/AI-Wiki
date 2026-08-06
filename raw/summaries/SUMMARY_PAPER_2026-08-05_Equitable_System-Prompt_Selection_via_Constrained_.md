---
title: Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO
url: http://arxiv.org/abs/2608.04339v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_01-35-08Z_EquitableSystem_PromptSelectionviaConstrainedMixed.md
generated_at: 2026-08-05 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a constrained mixed‑strategy GroupDRO framework for selecting system prompts that balances quality across diverse question phrasings. By assigning weights to prompts in an existing pool rather than optimizing the prompt text itself, the method minimizes worst‑case information loss while keeping overall performance close to average‑selection baselines. Experiments on five large language models and two bilingual benchmarks show up to 13.7 % improvement in worst‑case metrics without sacrificing average quality.

## Key Takeaways
- The framework decouples pool generation from selection, allowing any existing prompt pool to be used with complementary prompts instead of a single optimized one.
- It enforces a constraint on the mean loss to remain near that of average‑based selection, ensuring overall system performance stays stable while improving worst‑case outcomes.
- Multi‑prompt weights reveal genuine complementarity across different evaluation metrics and question groups, indicating that diverse prompts can collectively address varied answer quality issues.

## Context
Large language models often produce inconsistent answers when questions are paraphrased, highlighting a need for robust prompt selection strategies. Traditional approaches optimize single prompts, which may fail to cover all phrasing variations, leading to suboptimal user experiences across domains such as medical and finance advice.

## Implications
Practitioners can adopt this ensemble‑based method to enhance system reliability without retraining models or redesigning data pipelines. By leveraging weighted prompt pools, developers can deliver more equitable responses, reducing disparities that could affect decision‑making in high‑stakes applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04339v1)
