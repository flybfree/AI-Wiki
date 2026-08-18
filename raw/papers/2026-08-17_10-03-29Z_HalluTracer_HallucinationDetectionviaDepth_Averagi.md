---
title: HalluTracer: Hallucination Detection via Depth-Averaging Truth Signals
published: 2026-08-17T10:03:29Z
authors: Zhihao Guo, Zonghan Wu, Huan Huo, DaYong Ye, Junwei Zhang, Weiran Yao, Zhiwei Liu, Qingsong Wen, Yilei Shao
url: http://arxiv.org/abs/2608.16353v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HalluTracer: Hallucination Detection via Depth-Averaging Truth Signals

## Abstract
Even well-aligned large language models confidently generate factually incorrect text, making hallucination a persistent reliability risk in high-stakes deployments. These models nonetheless carry linearly separable truthfulness signals in their internal representations. Existing white-box detectors, however, collapse this evidence to isolated components or a single depth, discarding discriminative information distributed across the full forward pass. We introduce HalluTracer, a detection framework that reads and aggregates truthfulness evidence across every layer of the forward pass before the model emits any answer token. A geometric analysis reveals that the per-layer signals are weakly correlated, so that simple depth averaging suppresses layer-specific noise and captures nearly all linearly accessible information. Across six open-source language models and five hallucination benchmarks, HalluTracer consistently outperforms matched white-box baselines, with gains ranging from one to fourteen points. Collectively, our work recasts hallucination detection from a layer-selection problem into a depth-aggregation problem governed by the geometric sparsity of the truthfulness signal.

## Metadata
- **Published**: 2026-08-17T10:03:29Z
- **Authors**: Zhihao Guo, Zonghan Wu, Huan Huo, DaYong Ye, Junwei Zhang, Weiran Yao, Zhiwei Liu, Qingsong Wen, Yilei Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16353v1)