---
title: Start Classifying: Categorical Critics for LLM Reinforcement Learning
url: http://arxiv.org/abs/2608.02181v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_13-05-38Z_StartClassifying_CategoricalCriticsforLLMReinforce.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether a classification‑based training objective can replace the standard scalar mean‑squared error (MSE) head in Proximal Policy Optimization for large language models operating under verifiable rewards. By introducing HL‑Gauss PPO, which uses a categorical predictor over a discretized value support and trains it with cross‑entropy against smoothed targets, the authors show that the critic signal improves across multiple reasoning tasks on both Qwen2.5 and Qwen3 backbones.

## Key Takeaways
- HL‑Gauss PPO replaces scalar MSE regression with a categorical predictor trained via cross‑entropy against smoothed HL‑Gauss targets.
- The classifier’s output is decoded to a scalar expectation for GAE and PPO, leaving the actor update unchanged and non‑distributional.
- Experiments on reasoning prefixes reveal that neither larger head size nor binary classification alone yields gains; HL‑Gauss improves Brier score, calibration error, and produces more symmetric, lower‑variance advantages.

## Context
Large language model reinforcement learning often relies on sparse binary rewards, making scalar MSE critics sensitive to small value errors. Traditional PPO assumes a continuous value function, which can lead to poor calibration and unstable training. This work introduces categorical value learning as an alternative surrogate that better handles discrete reward spaces while preserving the simplicity of PPO’s actor update.

## Implications
For practitioners developing RL agents with verifiable rewards, adopting categorical critics like HL‑Gauss may enhance stability and performance without altering the core algorithmic structure. The findings encourage broader exploration of non‑scalar critic heads in reinforcement learning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02181v1)
