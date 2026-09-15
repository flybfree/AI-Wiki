---
title: MOSCOPT: Mixture-of-Skills Collective Optimization for LLM Agents
published: 2026-09-13T09:57:59Z
authors: Zhenyu Zhang1, Jiudong Yang
url: http://arxiv.org/abs/2609.14399v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOSCOPT: Mixture-of-Skills Collective Optimization for LLM Agents

## Abstract
Natural language prompts and skills serve as the strategic backbone of LLM-based agents. Recent advances in prompt and skill optimization have achieved notable gains, yet all existing methods optimize a \emph{single} text template---missing the synergy among multiple complementary strategies. We propose MOSCOPT, a text-native, parameter-free algorithm that jointly optimizes a pool of $N$ skills and a gating skill $G$ that dynamically selects $K$ skills per step. To effectively optimize the skills, we build the EditAdam with internally maintained dual states. Through the three-phase interleaved updates with EditAdam, the system monotonically improves without gradient or parameter tuning. Extensive experiments and detailed ablations across 5 benchmarks and 3 target LLMs demonstrate that MOSCOPT consistently outperforms all baselines, and confirm that both the mixture-of-skills architecture with selective activation and the collective evolution with three-phase interleaving are essential to its superior performance. Code is released https://github.com/zhangzhenyu13/SummerClaw/tree/master/summerclaw/agent_trainer/algorithms/moscopt.

## Metadata
- **Published**: 2026-09-13T09:57:59Z
- **Authors**: Zhenyu Zhang1, Jiudong Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14399v1)