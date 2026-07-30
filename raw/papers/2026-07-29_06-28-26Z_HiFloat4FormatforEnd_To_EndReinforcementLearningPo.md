---
title: HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models
published: 2026-07-29T06:28:26Z
authors: Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Yaoyuan Wang, Yao Wang, Junsong Wang, Tianchi Hu, Fengchen He, Guipeng Hu, Tanzila Rahman, Anandharaju Durai Raju
url: http://arxiv.org/abs/2607.26515v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models

## Abstract
We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision. A systematic study reveals that the dominant source of degradation in FP4 RL is not training-side quantization error but rollout activation quantization: outliers stretch the dynamic range so far that a large number of activation values underflow to zero under FP4. Counterintuitively, restoring the training policy to higher precision while keeping the rollout in FP4 makes accuracy worse than full FP4 baseline, exposing rollout-training mismatch as the principal failure mode and ruling out standard pretraining-style fixes. We address this with Rollout Residual Quantization (Rollout-ResQ): a single residual correction term constrained to a hardware-friendly sparsity pattern, added only to the FP4 rollout matmul -- a lightweight correction that recovers most of the precision lost to outlier-driven underflow without inflating the rollout's compute footprint. On Qwen2.5-3B and Qwen2.5-Math-7B, Rollout-ResQ paired with the HiFloat4 (HiF4) format -- whose three-level hierarchical scaling preserves resolution under FP4's tight 4-bit budget -- closes the accuracy gap to BF16 from 4.9% to 1.1%, bringing fully quantized FP4 RL within striking distance of full precision. Applied to the open-standard MXFP4, the same recipe narrows the gap from 13.6% to 5.3%, revealing that FP4 format choice is a key factor that determines the ceiling on recoverable accuracy. Together, these results establish HiF4 as the enabling format for end-to-end FP4 RL post-training, and Rollout-ResQ as the activation-side mechanism that makes the gap to BF16 closable.

## Metadata
- **Published**: 2026-07-29T06:28:26Z
- **Authors**: Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Yaoyuan Wang, Yao Wang, Junsong Wang, Tianchi Hu, Fengchen He, Guipeng Hu, Tanzila Rahman, Anandharaju Durai Raju
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26515v1)