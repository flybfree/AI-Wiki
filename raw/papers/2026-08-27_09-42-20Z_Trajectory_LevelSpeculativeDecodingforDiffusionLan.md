---
title: Trajectory-Level Speculative Decoding for Diffusion Language Models
published: 2026-08-27T09:42:20Z
authors: Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long
url: http://arxiv.org/abs/2608.27514v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory-Level Speculative Decoding for Diffusion Language Models

## Abstract
Diffusion-based language models (dLLMs) enable parallel token generation through iterative denoising, but existing decoding strategies collapse to single-token generation under low confidence, severely limiting throughput. Unlike autoregressive models where speculative decoding operates on token sequences in a fixed left-to-right order, dLLMs require speculating over denoising trajectories-sequences of multi-token updates with explicit positions and unmasking orders. We develop a trajectory-level speculative framework that constructs draft denoising trajectories via confidence-stratified tree exploration and verifies them through blockwise parallel evaluation with bidirectional attention masking. Our method further introduces inter-block speculation, exploiting diffusion models' bidirectional structure to perform cross-block lookahead. We formally characterize when this approach is exact and identify trajectory drift as the fundamental cost of increased parallelism. Building on Fast-dLLM's dual-cache infrastructure, our framework reduces denoising iterations by 30-40% and increases tokens-per-step from 2.6 to 4.3, achieving 7-14x speedup over vanilla dLLMs and 1.3x over Fast-dLLM with less than 1% accuracy change across reasoning and code benchmarks.

## Metadata
- **Published**: 2026-08-27T09:42:20Z
- **Authors**: Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27514v1)