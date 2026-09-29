---
title: Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device
url: http://arxiv.org/abs/2609.35005v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_12-07-26Z_Sub_ModelShort_TermMemoryConvolutionsforKeywordSpo.md
generated_at: 2026-09-28 23:15
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces the application of Sub-Model Short-Term Memory Convolutions to adapt modular Convolutional Neural Networks for efficient, online inference in Keyword Spotting systems deployed on resource-constrained edge devices. The proposed method significantly reduces computational overhead by minimizing redundant calculations and power consumption while preserving the training stability inherent to CNN architectures. Experimental results demonstrate substantial efficiency gains, achieving up to 82% reduction in Million Computations Per Second compared to standard CNNs, with high accuracy maintained at 93.8% on the Google Speech Commands dataset.

## Key Takeaways
- The study leverages the STMC framework to transform a modular CNN into an online, LSTM-like inference model, enabling real-time processing suitable for edge deployment without sacrificing the structural simplicity of convolutional architectures.
- Performance evaluations reveal significant computational savings, with the approach reducing power consumption and redundant operations by up to 82% relative to equivalently frequent standard CNN execution and by 46% compared to vanilla STMC implementations.
- The optimized model achieves robust classification performance, reaching 93.8% accuracy on the standard 11-class Google Speech Commands task and improving to 97.1% when

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35005v1)
