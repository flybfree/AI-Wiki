---
title: Instruction-Conditioned Exploration with Asymmetric Reinforcement Learning and Self-Distillation
published: 2026-08-03T11:47:52Z
authors: Jim Dilkes, Vahid Yazdanpanah, Sebastian Stein
url: http://arxiv.org/abs/2608.02087v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instruction-Conditioned Exploration with Asymmetric Reinforcement Learning and Self-Distillation

## Abstract
Post-training Large Language Models (LLMs) with Reinforcement Learning (RL) has become an important tool for improving model capabilities, but the LLM action-space structure introduces challenges distinct from classical RL, with implications for inducing exploration. New methods are required that leverage the broad knowledge and flexibility of pre-trained LLMs to deliberately generate diverse experience at training time. We propose Instruction-Conditioned Exploration (ICE), which supplements task prompts during training with one of several distinct instructions, increasing the coverage of behaviours attempted. To facilitate ICE, we propose Asymmetric-RL/SD, a combined Reinforcement Learning and Self-Distillation training objective, to transfer explored behaviours to the unconditioned test-time policy. ICE with the Asymmetric-RL/SD objective improves Qwen3-1.7B held-out pass@1 performance at $4$K response length on mathematical reasoning tasks by $5.0\%$ relative to training with DAPO, with improvement persisting at a longer 8K context.

## Metadata
- **Published**: 2026-08-03T11:47:52Z
- **Authors**: Jim Dilkes, Vahid Yazdanpanah, Sebastian Stein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02087v1)