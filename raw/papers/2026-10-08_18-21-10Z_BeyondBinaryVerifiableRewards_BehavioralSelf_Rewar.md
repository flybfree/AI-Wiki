---
title: Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents
published: 2026-10-08T18:21:10Z
authors: Yiran Wu, Andrew Zhao, Yurui Chang, Qingyun Wu, Xuan Feng
url: http://arxiv.org/abs/2610.12598v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents

## Abstract
Reinforcement learning with verifiable rewards (RLVR) provides reliable supervision for software engineering agents through executable tests, but binary rewards fail to distinguish trajectories with substantially different debugging quality. We investigate whether the current policy can judge its own trajectories and use these judgments to improve task performance without a separately trained reward model. To this end, we introduce Behavioral Self-Rewarding (BSR), a reward-refinement method that reuses the policy to compare observable debugging behavior among trajectories from the same task with the same verifier outcome. BSR aggregates pairwise preferences into task-local scores and converts them into bounded auxiliary rewards, introducing reward contrast while preserving the verifier-defined pass/fail ordering. This provides additional supervision from already-collected trajectories without requiring new environment interactions. Experiments on SWE-bench Verified and SWE-bench-Live show consistent improvements across the evaluated Qwen3-14B and Qwen3-32B configurations, supporting using the policy's own comparative judgments as a complementary learning signal for training software engineering agents.

## Metadata
- **Published**: 2026-10-08T18:21:10Z
- **Authors**: Yiran Wu, Andrew Zhao, Yurui Chang, Qingyun Wu, Xuan Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12598v1)