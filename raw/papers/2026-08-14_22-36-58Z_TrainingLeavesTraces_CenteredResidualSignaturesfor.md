---
title: Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification
published: 2026-08-14T22:36:58Z
authors: Aman Singh Thakur, Rayan Khoury
url: http://arxiv.org/abs/2608.14929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification

## Abstract
Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented. We study data-free white-box lineage verification: can weights alone reveal whether two compatible model checkpoints share ancestry?   Residual training produces a shared identity-aligned component in branch products, so this structure alone cannot establish ancestry. We remove it and compare checkpoint-specific structure across residual blocks, yielding a symmetric lineage score calibrated against independent checkpoints. On residual-MLP and GPT-2 benchmarks, the score separates fine-tuned, LoRA-merged, pruned, and quantized descendants from independent and distilled models (AUROC=1.0), distinguishing weight ancestry from behavioral similarity. Under function-preserving checkpoint laundering experiments, weight-space baselines lose margin or fail; our score remains unchanged and runs 76x faster than the nearest robust baseline on GPT-2. The projection-pairing signal appears across six language-model families and beyond, and a case study correctly identifies 3 related and 7 unrelated LLaMA-2 public checkpoints. Collectively, these results establish a passive, data-free provenance signal for compatible open-weight language-model checkpoints

## Metadata
- **Published**: 2026-08-14T22:36:58Z
- **Authors**: Aman Singh Thakur, Rayan Khoury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14929v1)