---
title: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations
published: 2026-08-11T12:01:59Z
authors: Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca, Ethan Fetaya, Yftah Ziser, Gal Chechik, Haggai Maron
url: http://arxiv.org/abs/2608.10835v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations

## Abstract
Large Vision-Language Models (LVLMs) achieve impressive visual reasoning and dialogue capabilities, yet frequently hallucinate content unsupported by the visual input. Effective mitigation requires token-level localization, enabling targeted intervention without discarding the entire response. Existing detectors require expensive full-model fine-tuning, rely on external verifiers that ignore the model's generation process, or reduce internal signals to isolated features and hand-crafted statistics, discarding spatial, sequential, and relational structure. We introduce \textbf{UniProbe}, a lightweight, unified, learnable detector that models a frozen LVLM's heterogeneous computational trace from a single forward pass. UniProbe constructs a directed graph over image patches, query tokens, and generated tokens, with attention weights encoding their relations. It processes this trace with alternating structure-aware modules: a GNN for relational evidence, a ViT for 2-D visual geometry, and a GRU for response order. Interleaving them allows spatial, relational, and sequential evidence to interact throughout the detector. We further develop a streaming variant for hallucination-aware decoding, which detects and resamples hallucinated tokens during generation, and a self-adaptation strategy aligning the detector with the LVLM's own generations. Across diverse LVLM backbones, UniProbe achieves state-of-the-art token-level and object-hallucination detection. During decoding, it reduces object hallucinations by up to 55\% at $1.06\times$ the latency of standard generation.

## Metadata
- **Published**: 2026-08-11T12:01:59Z
- **Authors**: Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca, Ethan Fetaya, Yftah Ziser, Gal Chechik, Haggai Maron
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10835v1)