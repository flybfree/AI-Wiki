---
title: Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results
url: http://arxiv.org/abs/2607.20090v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_12-45-04Z_ReinforcementLearningforLargeLanguageModelSelectiv.md
generated_at: 2026-07-23 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces SelectBench, a benchmark for selective evidence adoption in retrieval‑augmented large language models, and demonstrates that post‑training with DAPO improves the model’s ability to accept useful information while rejecting harmful content. On a corrected test set the success rate rises modestly from 22.46% to around 25.5%, and forbidden‑content adoption is reduced.

## Key Takeaways  
- The selective evidence adoption system reduces false or unsafe answers by lowering the acceptance of misleading statements, raising the correct usage rate from 22.46% to about 25.54% with rule‑based DAPO.  
- Forbidden‑content prompts are adopted far less often after training, indicating improved safety without harming overall performance on standard benchmarks like MMLU and HotpotQA.  
- The improvement is modest and does not survive Holm correction, suggesting that stronger reward shaping or more iterations are needed for robust gains.

## Context  
Retrieval‑augmented language models often incorporate irrelevant or deceptive information from external sources, which can degrade answer quality and safety. This work addresses the need to balance evidence use with content filtering in a controlled setting, providing a practical benchmark for future research on safe AI deployment.

## Implications  
Practitioners can leverage this post‑training technique to fine‑tune large models without extensive retraining, offering a lightweight way to improve factuality and safety. However, the limited gains highlight that more sophisticated reward design is required for production‑grade robustness against prompt injection attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20090v1)
