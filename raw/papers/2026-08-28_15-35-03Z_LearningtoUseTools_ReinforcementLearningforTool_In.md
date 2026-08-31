---
title: Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning
published: 2026-08-28T15:35:03Z
authors: Minghui Xu, Zi Wang
url: http://arxiv.org/abs/2608.28447v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning

## Abstract
Current large language models (LLMs) increasingly benefit from external tool integration, especially for tasks requiring reliable computation and verification. Motivated by this, we study calculator tool calling for improving mathematical reasoning on the Countdown task. We first analyze reasoning failures and find that calculation errors account for a substantial portion of incorrect responses. We then construct supervised fine-tuning datasets to teach the model useful tool-use patterns and how to interpret returned outputs. Building on this tool-formatted policy, we apply several on-policy reinforcement learning methods, including RLOO, RLOO++, GRPO, and DAPO, using automatically verifiable final-answer rewards. To enable a more reliable evaluation, we construct a fresh 1,024-problem held-out Countdown benchmark with no exact overlap with the training data. Our results show that calculator tool integration consistently improves both SFT and RL baselines, yielding roughly 10 percentage-point gains across pass@k. Among the RL methods, Tool-DAPO achieves the strongest performance, improving pass@1 from 35.8% for Tool-SFT to 66.0%. Further analysis shows that RL encourages more effective tool use even when only final-answer rewards are provided. These findings suggest that tool integration reduces arithmetic and verification errors, while RL increases the probability of correct reasoning traces.

## Metadata
- **Published**: 2026-08-28T15:35:03Z
- **Authors**: Minghui Xu, Zi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28447v1)