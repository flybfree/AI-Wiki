---
title: Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning
url: http://arxiv.org/abs/2610.11152v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_03-15-00Z_DoLLMsLearnfromRewardsinContext__Rethinkingtherole.md
generated_at: 2026-10-08 21:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether in-context learning (ICL) in large language models can genuinely function as reinforcement learning (RL) when the model is conditioned on raw trajectory-reward pairs during inference. Through controlled experiments across four benchmarks and six models, the authors find that the reward signal has negligible impact on performance improvement, while trajectories drive gains regardless of their semantic content. The authors conclude that direct in-context reinforcement learning is better understood as a special case of ICL rather than as true inference-time RL.

## Key Takeaways
- The reward signal is effectively ignored by LLMs in direct ICRL settings: flipping reward values, randomizing them, or removing them entirely leaves the model's improvement curve virtually unchanged. This holds even when meta-prompts explicitly instruct the model to explore, exploit, or reason over rewards, suggesting the model does not genuinely use reward as a learning signal.
- Trajectories drive performance improvement, but not through their semantic content. Shuffled or corrupted trajectories produce results comparable to real, coherent trajectories, indicating that the model extracts statistical or structural patterns rather than learning from meaningful action-outcome sequences.
- The observed patterns closely mirror known behaviors in standard ICL, leading the authors to reframe direct ICRL as a special case of ICL. This means that factors like input distribution, demonstration quality, and prompt structure matter far more than RL-specific mechanisms such as reward shaping or exploration strategies.

## Context
As LLM agents increasingly rely on accumulating experience in context at inference time rather than updating model parameters, the community has adopted the term "in-context reinforcement learning" to describe this process. However, the foundational assumption that rewards serve as genuine learning signals in this setting has never been rigorously tested. This paper fills that gap by isolating the simplest possible ICRL setup and applying ablation-style experiments to determine whether reward actually plays the causal role attributed to it, challenging a widely accepted framing in the LLM agent research community.

## Implications
For practitioners designing LLM-based agents, this finding suggests that engineering effort should focus on ICL factors such as demonstration selection, input distribution, and prompt structure rather than on RL-specific techniques like reward shaping or exploration scheduling. Agent memory systems may benefit more from carefully curated context examples than from reward-weighted trajectory storage. For the broader field, this reframing calls for more precise terminology and evaluation protocols when claiming that an LLM agent performs reinforcement learning at inference time, potentially reshaping how benchmarks and agent architectures are designed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11152v1)
