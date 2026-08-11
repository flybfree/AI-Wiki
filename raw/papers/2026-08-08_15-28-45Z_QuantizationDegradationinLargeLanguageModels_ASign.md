---
title: Quantization Degradation in Large Language Models: A Signal-Noise Perspective
published: 2026-08-08T15:28:45Z
authors: Chenxi Zhou, Pengfei Cao, Jinyu Ye, Bohan Yu, Haida Yu, Jiang Li, Jun Zhao, Kang Liu
url: http://arxiv.org/abs/2608.08188v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantization Degradation in Large Language Models: A Signal-Noise Perspective

## Abstract
Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone. We systematically study weight-only post-training quantization across bit-widths, quantization methods, model scales and downstream tasks on multiple model families. We observe that such degradation varies substantially across these factors: 4-bit quantization usually preserves performance, 2-bit often causes broad degradation, and at 3-bit, degradation becomes apparent but varies markedly with task type, quantization method and model scale. To explain this variability, we use the signal-to-noise ratio (SNR) to measure how strongly quantization perturbs full-precision representations. We trace degradation back to two linked processes: how quantization errors arise within individual modules, and how they accumulate across layers. First, a source SNR decomposition shows that newly introduced errors depend on three factors: the magnitude of the weight error, the strength of the task-specific signal, and how strongly the quantization error aligns with task-specific activations. Different factors affect these components in distinct ways. Second, a cross-layer propagation analysis shows that these errors can be attenuated, preserved, or amplified as they pass across layers, and that larger models benefit from weaker error amplification. Together, these results establish that quantization degradation is governed by how errors are introduced at the source and how they accumulate across the network.

## Metadata
- **Published**: 2026-08-08T15:28:45Z
- **Authors**: Chenxi Zhou, Pengfei Cao, Jinyu Ye, Bohan Yu, Haida Yu, Jiang Li, Jun Zhao, Kang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08188v1)