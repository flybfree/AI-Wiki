---
title: From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference
published: 2026-07-30T12:07:56Z
authors: Tianyang Zhu
url: http://arxiv.org/abs/2607.28097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference

## Abstract
Mathematically equivalent expert-reduction orders can produce observably different sparse-MoE executions. We isolate this effect in native DeepSeek-V4-Flash by freezing local MoE state and varying only aggregation semantics. Four schemes separate operand representation from accumulator precision. At one layer-5 fork, 720 A-mode orders yield 10 continuation basins; 720 B-mode orders form 360 exact structural classes and 11 basins. Under one Chinese prompt, the B classes split into 202 layoffs, 113 hiring, and 45 other continuations. Maximum-L-infinity B-branch selection separates 12, 24, and 36 of 50 prompts by 8, 16, and 32 tokens. Across 192 persistent trajectories per scheme, P32, A, and B change every native-reference route trajectory, while C preserves routes, token sequences, and texts. A separate 192-trajectory C check matches native MoE, post-mHC, next-router, and LM states bitwise. For one controlled B branch, exact post-mHC endpoint reconstruction reproduces the measured downstream trajectory. At the next decode boundary, exact FP64 reconstruction of the branch's full persistent state yields agreement for 301 downstream post-mHC states, 301 persistent-state checkpoints, 301 routes, predictions, and text over seven steps, given the same naturally generated next input. These controls identify post-mHC as an intra-token boundary and full persistent state as a cross-token continuation boundary. Identical tokens need not imply identical autoregressive state: divergence can survive a token boundary and become visible later. These results make expert operand conversion, accumulator precision, and reduction order part of a numerical compatibility contract for sparse-MoE runtimes and hardware backends. They establish controlled causal possibility, not deployment incidence; C's order invariance is limited to evaluated six-term states and schedules.

## Metadata
- **Published**: 2026-07-30T12:07:56Z
- **Authors**: Tianyang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28097v1)