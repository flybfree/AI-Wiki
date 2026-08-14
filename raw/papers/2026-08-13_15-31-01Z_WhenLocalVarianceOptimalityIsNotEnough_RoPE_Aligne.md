---
title: When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation
published: 2026-08-13T15:31:01Z
authors: Shuhan Wang, Yilin Luo, Nan Xu, Chi Wang Cheung
url: http://arxiv.org/abs/2608.13365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation

## Abstract
Rotation-based post-training quantisation commonly applies an orthogonal transform across an entire attention head to reduce outlier-induced error. RoPE instead partitions each head into two-dimensional frequency pairs, raising the question of whether a transform respecting this decomposition can improve on full-head mixing. Prior work has established the per-pair rotations that commute with RoPE. We state the converse result that, for distinct frequencies, no other single-head orthogonal map commutes with RoPE. For the head-shared parameterisation used in our experiments, we then derive the rotation angle that minimises the larger channel variance under a pooled-covariance, position-averaged surrogate and verify that the implementation attains its analytic minimum. The evaluated head-shared pairwise configuration does not improve accuracy in the tested dynamic W4A4KV4 setting. Across four checkpoints, replacing the full-head Hadamard with this configuration increases perplexity at both short and long context lengths. Composing the pairwise rotation with the Hadamard satisfies the selected $\pm0.05$-PPL interval criterion under the default estimator. Estimating the shared angle from K alone improves pairwise-only on every checkpoint but does not close its gap to full-head mixing. The analytic objective controls a position-averaged second moment of a pooled calibration covariance, whereas the dynamic quantiser sets its step from a tokenwise group range. The pairwise transform also has only two-channel mixing support. Along a controlled interpolation from two-channel to full-head mixing, K range, relative quantisation error, and perplexity degradation decrease as support increases. These results show that optimality for a structured surrogate need not reduce quantisation error when the surrogate and mixing support are misaligned with the quantiser's scale-setting statistic.

## Metadata
- **Published**: 2026-08-13T15:31:01Z
- **Authors**: Shuhan Wang, Yilin Luo, Nan Xu, Chi Wang Cheung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13365v1)