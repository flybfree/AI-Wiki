---
title: Restoring Without Forgetting: Continual Learning Across Image Degradations
published: 2026-08-24T20:04:18Z
authors: Alif Ashrafee, Bartosz Krawczyk
url: http://arxiv.org/abs/2608.23799v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Restoring Without Forgetting: Continual Learning Across Image Degradations

## Abstract
Recent progress in image restoration has converged on all-in-one architectures that jointly handle multiple degradations within a single network. These methods are effective on static benchmarks but target a closed-world setting that assumes simultaneous access to every target degradation at training time. In practice, degradations are encountered sequentially as field-deployed systems progressively face new environmental conditions, and historical training data is often unavailable due to privacy or storage constraints. Accommodating a new degradation then requires either retraining on the union of all prior data, which is often costly or infeasible, or fine-tuning, which causes catastrophic forgetting. We formulate multi-degradation image restoration as a continual domain-incremental learning problem, in which degradations arrive incrementally and prior data is unavailable. Our proposed Restoring without Forgetting (RwF) framework learns a lightweight adapter for each new degradation, eliminating forgetting by construction at a fraction of the cost of dedicated per-domain networks. To isolate degradation learning from dataset variation, we construct a benchmark spanning five degradation domains under shared image content. At test time, an unsupervised routing mechanism identifies the appropriate restoration path for unknown inputs without requiring domain labels. Across the five-domain sequence, RwF improves final average PSNR over naive sequential fine-tuning by 15.25 dB and 11.83 dB on the Restormer and NAFNet backbones, respectively. The framework transfers to eleven canonical real-degradation benchmarks (3,465 images) at 89.5% routing accuracy with only a +0.94 dB oracle PSNR gap, establishing, to our knowledge, the first systematic baseline for continual multi-degradation image restoration.

## Metadata
- **Published**: 2026-08-24T20:04:18Z
- **Authors**: Alif Ashrafee, Bartosz Krawczyk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23799v1)