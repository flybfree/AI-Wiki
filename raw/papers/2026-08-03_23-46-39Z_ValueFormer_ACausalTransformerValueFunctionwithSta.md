---
title: ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies
published: 2026-08-03T23:46:39Z
authors: Inkyu Sa, Konstantin Stulov, Rajat Bhageria
url: http://arxiv.org/abs/2608.02958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies

## Abstract
Vision-Language-Action (VLA) policies trained by behavior cloning fail silently: from the action stream alone, a collapsing rollout looks much like one making clean progress, because imitation supplies no notion of progress. Reinforcement learning would supply one, but it is impractical here, where real-robot experience is costly and deformable food resists simulation. The cheap alternative, a terminal success / failure bit, is learnable in principle yet far too sparse to say when a rollout went wrong. We argue that the per-frame label, not the architecture, is the hard part: to be useful it must be dense, continuous, and correctly shaped. We present ValueFormer, a compact policy-agnostic causal transformer over a frozen DINOv3 backbone that emits two per-frame signals in one forward pass: a smooth Monte Carlo value, V_mc, for advantage estimation and a sharp binary value for online mistake detection, targets that pull in opposite directions by design. Failed episodes are labeled with a stage-aware, success-then-decay return that preserves the success curve before the failure stage, and detection is supervised from mistake intervals rather than a single failure time, so mistakes the policy recovers from also carry signal. On a real-robot bimanual sandwich-assembly task 1,427 episodes), a critic-derived per-frame training weight lifts task completion from 70% to 85% (within noise at n=20), and a batched bf16 encoder cuts the live serving cost 3~5 times so the critic runs at 2 Hz alongside the policy on a single GPU.

## Metadata
- **Published**: 2026-08-03T23:46:39Z
- **Authors**: Inkyu Sa, Konstantin Stulov, Rajat Bhageria
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02958v1)