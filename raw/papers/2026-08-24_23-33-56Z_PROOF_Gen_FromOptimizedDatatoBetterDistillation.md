---
title: PROOF-Gen: From Optimized Data to Better Distillation
published: 2026-08-24T23:33:56Z
authors: Anh Ta, Junjie Zhu, Shahin Shayandeh
url: http://arxiv.org/abs/2608.23911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PROOF-Gen: From Optimized Data to Better Distillation

## Abstract
Supervised fine-tuning on teacher-generated trajectories is the standard first stage for distilling tool-calling capabilities into deployable models. Post-training pipelines that drive shipped tool-calling agents re-run this stage on a daily or weekly cadence, paying the frontier-teacher cost each cycle, yet the mechanism is generate-and-filter (keep the teacher's passing trajectories, discard the rest) and each cycle leaves behind the same hard scenarios because failures supply no signal. On τ2-bench, 57% of teacher trials fail, two-thirds of them near-misses (most tool calls correct, undone by one decisive error).   We introduce PROOF-Gen (Per-scenario Reflective Optimization to Overcome FailedGeneration), which recovers golden trajectories from these failures via per-scenario prompt optimization. For each failed task, a reflector analyzes the execution trace and evaluation feedback, then writes corrective guidance that steers the teacher to a passing trajectory. The guidance is stripped before training, so the student learns from clean demonstrations with no task-specific scaffold.   On τ2-bench, per-scenario optimization recovers 93% of failed scenarios. Fine-tuned on the combined data, Qwen3-4B-Instruct-2507 improves from Pass^1=0.132 to 0.529 and Gemma 4 E4B-it gains +7.2pp on BFCL v4 multi-turn. In a deployed pipeline, the method lifts trajectory quality by +6.3pp goal completion and transfers to a deployed on-device model (+1.5pp goal completion; +1.7 to +5.0pp across response-quality metrics), with positive transfer in every locale (non-English average +1.48pp).

## Metadata
- **Published**: 2026-08-24T23:33:56Z
- **Authors**: Anh Ta, Junjie Zhu, Shahin Shayandeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23911v1)