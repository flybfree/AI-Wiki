---

title: "Summary: Learning to Adapt SFT Data for Better Reasoning Generalization"
url: http://arxiv.org/abs/2605.26924v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-26_12-20-53Z_LearningtoAdaptSFTDataforBetterReasoningGeneraliza.md
generated_at: "2026-06-11 10:47"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces Data Adaptation for Reasoning Tuning (DART), a method that uses reinforcement learning to transform existing supervised fine‑tuning data into a distributionally aligned version, improving the target model’s reasoning generalization. The method demonstrates that synthetic supervision can significantly boost reasoning performance.

## Key Takeaways
- The mapper model learns transformations that align SFT data with the target model's distribution, enhancing supervision quality.
- Direct fine‑tuning on misaligned expert data can degrade generalization due to distributional mismatch.
- DART achieves higher training efficiency than standalone RL and surpasses standard SFT results. This alignment reduces overfitting to the source data.

## Context
Current LLM research focuses on improving reasoning via post‑training tasks, yet many rely on raw expert data that may not suit the model’s internal representation. This paper addresses a key limitation: the need for synthetic supervision that matches both data distribution and learning dynamics.

## Implications
For practitioners, DART offers a practical way to boost SFT performance without large extra compute. Industry adoption could lead to more robust AI assistants that generalize better across tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.26924v1)
