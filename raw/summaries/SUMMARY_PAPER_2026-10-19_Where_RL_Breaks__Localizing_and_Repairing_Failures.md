---
title: Where RL Breaks: Localizing and Repairing Failures via Targeted Continued Pretraining
url: http://arxiv.org/abs/2610.25836v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_05-48-15Z_WhereRLBreaks_LocalizingandRepairingFailuresviaTar.md
generated_at: 2026-10-19 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why reinforcement learning with verifiable rewards (RLVR) fails to improve language model reasoning beyond what the base model already knows. The authors discover that RL failures are localized to specific characteristic n-grams in the model's own rollouts, and they propose using these failure signals to retrieve targeted text from the pretraining corpus for continued pretraining before RL training. Despite using only 35 million tokens—orders of magnitude smaller than typical mid-training data—this approach consistently outperforms random continued pretraining across multiple model families and reasoning benchmarks.

## Key Takeaways
- RL failures in reasoning tasks are not diffuse but are strongly predicted by a small set of characteristic n-grams, including reflection phrases like "let's recheck" and specific operations such as "the inverse of A." These failure signatures persist throughout the entire RL training process, indicating that RL cannot overcome gaps in the base model's pretrained knowledge. However, the model often produces correct answers to the same question in other rollouts, meaning the failures are within the model's latent capability but blocked by specific missing knowledge.
- The authors introduce a targeted continued pretraining pipeline: they extract failure n-grams from RL rollouts, use them to retrieve relevant text from the pretraining corpus, and continue pretraining the base model on this small corpus (only 35M tokens) before applying RL. This method outperforms continued pretraining on an equivalent amount of randomly sampled pretraining text in 10 out of 11 experimental settings, including a 2.0-point improvement on GSM8K when inserted before mid-training.
- The retrieved data transfers across model families: text retrieved based on OLMo2-1B's failure patterns improves Qwen3-4B performance by 1.9 points on a mixed reasoning benchmark, suggesting that failure n-grams capture generalizable knowledge gaps rather than model-specific quirks.

## Context
This work addresses a growing concern in the AI research community: RLVR methods like GRPO and PPO-based fine-tuning are widely deployed to boost reasoning capabilities, yet mounting evidence shows they primarily sharpen existing base-model abilities rather than teaching genuinely new knowledge. By identifying the precise linguistic and operational signatures where models fail, this paper bridges the gap between post-training optimization and pretraining data curation, offering a principled diagnostic tool for understanding the limits of RL-based training in large language models.

## Implications
For practitioners building reasoning models, this work provides a practical and inexpensive signal—failure n-grams from RL rollouts—that can guide data selection for continued pretraining without requiring massive new corpora or expensive annotation pipelines. The cross-model transferability of retrieved text suggests that knowledge gaps identified in one model family can inform training data for entirely different architectures, potentially reducing the cost and complexity of model development. For the broader field, it reframes RL failure analysis from a purely post-training concern into a pretraining data curation problem, encouraging tighter integration between pretraining and post-training stages in the model development lifecycle.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25836v1)
