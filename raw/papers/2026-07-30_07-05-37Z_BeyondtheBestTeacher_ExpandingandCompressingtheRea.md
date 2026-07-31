---
title: Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold
published: 2026-07-30T07:05:37Z
authors: Songshuo Lu, Zhi Chen, Yaohua Tang
url: http://arxiv.org/abs/2607.27770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold

## Abstract
A single reinforcement-learning run can produce a strong reasoner yet an incomplete teacher: it often amplifies only a subset of the valid solution modes. We argue that reinforcement learning (RL)-trained policies should therefore be viewed as local probes of a multi-basin reasoning solution manifold, rather than as globally reliable supervisors. Based on this view, we propose an expand-then-compress framework that couples teacher construction with multi-teacher policy distillation. In the expansion stage, Residual Group Relative Policy Optimization (RGRPO) trains a sequence of teachers from a common initialization and redirects each later round toward examples not yet covered by the accumulated teacher union. In the compression stage, reliability-gated Teacher-Union On-policy Distillation (TU-OPD) lets the student learn from its own response prefixes. For each example, only reliable teachers contribute, and their sampled-token OPD losses are weighted by their per-example quality. We further introduce Consensus-Residual Decomposition, which preserves a winner teacher's excess token preferences over its reliable peers, preventing specialist behavior from being suppressed during teacher aggregation. Experiments on mathematical reasoning, code generation, and instruction following show that the resulting Qwen3-1.7B student consistently outperforms the strongest individual teacher across all three domains, yielding relative improvements of 2.0%, 8.3%, and 6.9%, respectively, while retaining single-model inference. These results establish a simple but powerful principle: stronger students can be obtained not by selecting a single better teacher, but by deliberately constructing and compressing a complementary teacher union.

## Metadata
- **Published**: 2026-07-30T07:05:37Z
- **Authors**: Songshuo Lu, Zhi Chen, Yaohua Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27770v1)