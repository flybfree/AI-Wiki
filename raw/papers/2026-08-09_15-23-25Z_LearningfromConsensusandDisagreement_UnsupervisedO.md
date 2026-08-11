---
title: Learning from Consensus and Disagreement: Unsupervised On-Policy Self-Distillation with Minority-Trajectory Contrast
published: 2026-08-09T15:23:25Z
authors: Jiaxin Guo, Yanwei Yue, Xuanbo Fan, Chunyu Yang, Yan Zhang
url: http://arxiv.org/abs/2608.08764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Consensus and Disagreement: Unsupervised On-Policy Self-Distillation with Minority-Trajectory Contrast

## Abstract
On-policy self-distillation improves language-model reasoning by querying a teacher on states actually visited by the student. Recent methods create a powerful information asymmetry by exposing the teacher to privileged context, yet they fundamentally rely on external supervision---such as gold solutions or verifiers---to construct this advantage. We introduce CoDA (Consensus and Disagreement Alignment), a fully unsupervised framework that creates reliable privileged information entirely from the latent uncertainty structure of a model's own unlabeled rollouts. CoDA extracts two complementary signals. In the positive branch, answer-level consensus identifies a stable reasoning mode, which conditions a frozen self-teacher to provide dense distributional guidance on fresh student trajectories. However, because agreement does not guarantee correctness, positive-only distillation risks amplifying correlated errors into a false consensus. To break this harmful feedback loop, CoDA incorporates a negative branch that exploits disagreement: minority trajectories are treated as unstable alternatives and gently penalized via a reference-anchored, KTO-style calibration objective. This unpaired binary feedback provides robust regularization without requiring the strong assumption that the consensus is the absolute ground truth. Empirical evaluations on competition-level mathematical benchmarks demonstrate that CoDA significantly improves reasoning, outperforming self-generated baselines and effectively stabilizing training against erroneous consensus.

## Metadata
- **Published**: 2026-08-09T15:23:25Z
- **Authors**: Jiaxin Guo, Yanwei Yue, Xuanbo Fan, Chunyu Yang, Yan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08764v1)