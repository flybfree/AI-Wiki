---
title: From Sweep to Seam: Interleaved Cross-Block Post-Training Quantization
published: 2026-08-10T13:28:23Z
authors: Achille Jacquemond, Yuma Ichikawa, Akira Sakai
url: http://arxiv.org/abs/2608.09595v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Sweep to Seam: Interleaved Cross-Block Post-Training Quantization

## Abstract
Compressing large language models to two bits or fewer is increasingly feasible through block-wise post-training quantization; cross-block variants reconstruct neighboring Transformer blocks within a moving window. In the fixed two-block setting studied here, the matched sequential baseline moves this window through the network once, so errors introduced early in the sweep are not revisited. We propose Interleaved Cross-Block Quantization (ICBQ), a scheduling modification that revisits the boundary pair between consecutive chunks. Each seam pair is refined twice: first at the end of one chunk and again at the start of the next. The method retains the local two-block objective and reuses the calibration inputs of existing block-wise PTQ pipelines. Under stated local contraction and smoothness assumptions, we derive a depth-wise upper-bound comparison in which seam revisits multiply the propagated term while the residual remains bounded independently of depth. In the reported experiments, ICBQ reduces ternary-quantization perplexity relative to the matched Sequential CBQ baseline, yields finite perplexity in configurations where the baseline has severe degradation, and can also be used with 3-bit and 2-bit GPTQ.

## Metadata
- **Published**: 2026-08-10T13:28:23Z
- **Authors**: Achille Jacquemond, Yuma Ichikawa, Akira Sakai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09595v1)