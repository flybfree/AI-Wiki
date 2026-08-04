---
title: When Extreme Darkness Meets Motion Blur: MeanFlow for Unified RAW Restoration
published: 2026-08-03T05:38:47Z
authors: Zepu Wang, Jingze Liang, Weijie Xiao, Kexin Chen
url: http://arxiv.org/abs/2608.01720v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Extreme Darkness Meets Motion Blur: MeanFlow for Unified RAW Restoration

## Abstract
Extremely low-light RAW enhancement aims to recover severely attenuated sensor signals, yet existing methods often focus on illumination and noise while overlooking the motion-induced degradations inherent in practical low-light imaging. We present a framework for robust extremely low-light RAW enhancement under realistic acquisition degradations. First, we introduce See in the Degraded Extremely Dark (SIDED), a new dataset that applies controlled motion degradation to extremely low-light RAW pairs while retaining their original sensor noise. Second, we propose a unified RAW tokenizer equipped with explicit domain-conditioned representation calibration to align extremely low-light and well-exposed RAW data, followed by a MeanFlow that performs enhancement in a single function evaluation. To our knowledge, this is the first work to formulate extremely low-light RAW enhancement under realistic motion-degraded acquisition and address it with MeanFlow. We further introduce a physics-guided refinement model to strengthen illumination--reflectance consistency, pixel fidelity, and color preservation without incurring additional inference cost. Extensive experiments demonstrate that our framework achieves state-of-the-art performance in extremely low-light RAW enhancement, and robustly handles coupled motion and noise degradations.

## Metadata
- **Published**: 2026-08-03T05:38:47Z
- **Authors**: Zepu Wang, Jingze Liang, Weijie Xiao, Kexin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01720v1)