---
title: TaPR: Test-Aware Policy Refinement for Feedback-Conditioned Code Generation
published: 2026-08-01T07:35:06Z
authors: Aofan Liu, Jingxiang Meng, Fangxin Liu, Yongbiao Chen
url: http://arxiv.org/abs/2608.00494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TaPR: Test-Aware Policy Refinement for Feedback-Conditioned Code Generation

## Abstract
Multi-turn code agents rely on execution feedback to repair incorrect programs, yet standard reinforcement learning paradigms optimize and evaluate policy performance primarily using single-shot outcome rewards. This misalignment conflates initial code generation with feedback-driven refinement, discards granular execution signals across intermediate turns, and fails to evaluate whether the policy actually acquires self-repair capabilities. We propose Test-aware Policy Refinement (TaPR), a framework that transforms execution feedback into a dense per-turn test-pass-ratio reward under a consistent multi-turn interaction protocol. Across six models on 219 code-generation problems from LiveCodeBench, TaPR improves the pooled three-turn success rate (Pass@3) by 2.44 percentage points. In the predefined 7B/8B high-headroom slice, pooled accuracy increases from 30.25% to 33.56% (+3.31 pp), with 42 improvements and 13 regressions in paired trials. On a matched Qwen3-8B ablation, the dense reward supplies nonzero feedback in all of the first ten steps and reaches a higher Hard-subset peak than outcome-only GRPO within the tested budget, although GRPO nearly matches pooled Pass@3 by step 300. Our primary contribution is a reward-decomposition framework and a turn-aware evaluation protocol that decouple first-shot generation quality from multi-turn repair competence.

## Metadata
- **Published**: 2026-08-01T07:35:06Z
- **Authors**: Aofan Liu, Jingxiang Meng, Fangxin Liu, Yongbiao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00494v1)