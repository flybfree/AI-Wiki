---
title: Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization
published: 2026-10-05T23:41:48Z
authors: Yan Scholten, Rachel Lawrence, James Hensman, Stephan Günnemann, Alicia Curth, Riccardo Grazzi
url: http://arxiv.org/abs/2610.07522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization

## Abstract
Post-training quantization is a powerful tool for compressing large language models. The most scalable methods quantize every layer in parallel, but quantization errors then compound through the residual stream, as no layer corrects for the errors of the layers before it. Sequential quantization accounts for this error compounding by re-calibrating each layer on the already-quantized outputs of its predecessors, yielding stronger results but at the cost of a serial schedule that becomes a bottleneck at scale. As a solution, we propose parallel quantization with activation denoising, which recovers much of the sequential benefit while keeping quantization fully parallel. Rather than re-calibrating layer-by-layer, we take a robustness perspective and model the upstream error as noise, regularizing to be robust to it through a preprocessing step followed by metric-weighted rounding. Applied at every layer, this regularization forms a depth-compounding smoothness penalty that dampens how strongly quantization errors amplify through the model. Unlike orthogonal rotations commonly used in quantization, which must preserve the model's function, we multiply the weights by a more general linear transformation. We find that the two are complementary and their effects compound. Empirically, our robustness regularization recovers a significant part of sequential quantization's benefit in a single parallel pass, at a fraction of its time. Overall, by treating compounding quantization errors as a robustness problem, we offer a principled foundation for more efficient and accurate LLM quantization at scale.

## Metadata
- **Published**: 2026-10-05T23:41:48Z
- **Authors**: Yan Scholten, Rachel Lawrence, James Hensman, Stephan Günnemann, Alicia Curth, Riccardo Grazzi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07522v1)