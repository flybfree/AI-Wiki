---
title: ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection
published: 2026-09-03T10:05:45Z
authors: Taewoo Kim, Young Han Lee, Nam In Park, Chanwoo Kim
url: http://arxiv.org/abs/2609.03620v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection

## Abstract
Audio deepfake detection is commonly formulated as clip-level binary classification of single-domain audio. However, real-world manipulated audio can exhibit mixed authenticity, where genuine and manipulated cues coexist across temporal transitions, overlapping sources, or both. This setting requires not only detecting manipulated audio but also localizing the components that provide evidence for the decision. We propose ToolDF, a tool-integrated reasoning framework for mixed-authenticity audio deepfake detection. ToolDF employs an audio large language model as an orchestrator trained with supervised tool-use trajectories. It adaptively analyzes the audio scene, selectively performs source separation, routes components to domain-specific experts, and aggregates their evidence into an interpretable verdict. We further introduce a mixed-authenticity ADD benchmark covering temporal transitions, acoustic overlaps, and hybrid mixtures. Experimental results show that ToolDF achieves the best overall performance on composite-type detection, achieving macro-F1 gains of 3.72 and 14.39 points over the strongest monolithic baseline and a fixed pipeline, respectively, while providing interpretable evidence localized to temporal regions and acoustic sources. Our source code and dataset are publicly available online.

## Metadata
- **Published**: 2026-09-03T10:05:45Z
- **Authors**: Taewoo Kim, Young Han Lee, Nam In Park, Chanwoo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03620v1)