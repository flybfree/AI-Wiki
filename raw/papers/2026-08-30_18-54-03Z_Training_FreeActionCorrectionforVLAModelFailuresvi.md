---
title: Training-Free Action Correction for VLA Model Failures via Language Feedback
published: 2026-08-30T18:54:03Z
authors: Owen Kwon, Pablo Ortega-Kral, Arthur Bucker, Jean Oh
url: http://arxiv.org/abs/2608.29967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-Free Action Correction for VLA Model Failures via Language Feedback

## Abstract
Vision-Language-Action (VLA) models demonstrate strong semantic understanding yet exhibit systematic failures during deployment. The conditions under which these failures occur, and whether they can be corrected without retraining, remain poorly understood. In this paper, we take steps toward addressing this gap. We present CorrectVLA, a framework that translates task-level natural language corrections into additive action magnitude adjustments without modifying policy weights. A human provides a single task-level correction, applied uniformly across all rollouts without per-episode intervention. In simulation, CorrectVLA recovers execution misalignment failures across both in-distribution and OOD tasks. In real-robot experiments on a UFactory xArm7 under environment shift, CorrectVLA restores near-perfect success where the base policy almost entirely breaks down, generalizing across object locations and identities. Through a taxonomy of failure modes on LIBERO-90, we find that execution misalignment failures, where the policy reaches the correct target but miscalibrates action magnitudes, represent the correctable subset, while other failure modes where semantic comprehension itself breaks down are not amenable to this approach. The approach succeeds when policies possess strategic correctness and fails when fundamental comprehension is absent, establishing a practical operational boundary for inference-time correction.

## Metadata
- **Published**: 2026-08-30T18:54:03Z
- **Authors**: Owen Kwon, Pablo Ortega-Kral, Arthur Bucker, Jean Oh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29967v1)