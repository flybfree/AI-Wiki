---
title: Show Your Work in Swahili: Reinforcement Learning for Native-Language Mathematical Reasoning
url: http://arxiv.org/abs/2611.16104v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-11_23-25-01Z_ShowYourWorkinSwahili_ReinforcementLearningforNati.md
generated_at: 2026-11-15 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Fikiria, a two-stage training pipeline combining supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO) designed to improve mathematical reasoning in Swahili. The core innovation is a reward function that evaluates not only the correctness of the final numerical answer but also the surface fidelity of the Swahili reasoning chain by measuring its similarity to a reference chain-of-thought using ChrF++. The resulting model, Fikiria-AfriqueQwen-14B, achieves 79.2% accuracy on the AfriMGSM Swahili benchmark, outperforming GPT-4o under identical prompting and scoring conditions.

## Key Takeaways
- The reward design in Fikiria multiplies a strict format gate by a weighted combination of answer accuracy and ChrF++ similarity to an in-language reference reasoning trace. This means the model is explicitly trained to produce reasoning that looks like a native Swahili chain of thought, not merely to arrive at the correct number. The authors acknowledge that ChrF++ captures surface-level textual similarity rather than the logical validity of individual reasoning steps, which is an important limitation.
- The training dataset consists of 2,300 Swahili math problems created by translating GSM8K using GPT-4.1 and filtering outputs through SSA-COMET, a quality metric for machine translation. This pipeline demonstrates a practical recipe for building low-resource language training data at scale, though the reliance on a proprietary model for translation introduces potential quality and bias concerns.
- Under a fixed prompt and strict answer-format scoring, GPT-4o scores only 68.0% on AfriMGSM Swahili, partly because it frequently fails to comply with the required answer format. However, IrokoBench reports 78.8% for GPT-4o using a best-per-model prompt, a figure numerically close to Fikiria's 79.2% but not directly comparable due to differing evaluation protocols. A small human evaluation with co-author annotators actually preferred GPT-4o's outputs overall, suggesting that automated benchmark scores may not fully capture reasoning quality.

## Context
This work sits at the intersection of multilingual NLP, reinforcement learning for reasoning, and language equity in AI. Most mathematical reasoning benchmarks and training pipelines are built around English, and extending them to African languages like Swahili requires both data creation and evaluation infrastructure. The paper contributes to a growing body of work on African-language LLMs, including models like AfriqueQwen and benchmarks such as AfriMGSM and IrokoBench, while introducing a novel reward-shaping strategy that targets reasoning-trace fidelity rather than answer-only correctness.

## Implications
For practitioners building language models for African languages, Fikiria demonstrates that fine-tuning with a reasoning-trace-aware reward can yield competitive performance on math benchmarks without requiring massive proprietary datasets. However, the gap between automated benchmark scores and human evaluation preferences for GPT-4o highlights that surface-fidelity metrics like ChrF++ are insufficient proxies for true reasoning quality. Industry teams deploying multilingual reasoning systems should treat benchmark accuracy as one signal among many and invest in human-in-the-loop evaluation, especially for low-resource languages where reference data is scarce and translation pipelines may introduce systematic errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.16104v1)
