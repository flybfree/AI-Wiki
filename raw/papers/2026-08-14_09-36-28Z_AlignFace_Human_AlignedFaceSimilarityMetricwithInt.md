---
title: AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept Relations
published: 2026-08-14T09:36:28Z
authors: Ying Huang, Wencan Zhang, Brian Y. Lim
url: http://arxiv.org/abs/2608.14130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept Relations

## Abstract
Computer vision models for generated facial content, such as face editing and privacy protection, increasingly affect people, requiring similarity metrics that serve as faithful proxies for human perception. While perceptual evaluation has progressed from signal-based heuristics to representation-based metrics, current approaches are limited to behavioral modeling without cognitive alignment. They rely on implicit and spurious relations while assuming a universal observer, failing to account for inherent variations across diverse human populations. This leads to inaccurate evaluative models of stakeholders and misleading guidance for generative model debugging. Rather than treating perception as a black box, we leverage scientific findings from cognitive psychology of human face similarity perception: dependence on facial featural and configural attributes, nonlinear psychophysical response scaling, and own-group biases. We introduce the FACETS dataset and propose AlignFace, an interpretable, human-aligned, face similarity metric that encodes these cognitive principles through ante-hoc modeling. It employs visual-language modeling (VLM) to encode paired face images and text-based attributes, gated cross-attention (CA) to extract attribute-specific facial difference representations, concept bottleneck modeling (CBM) to constrain reasoning via interpretable face attributes, and neural generalized additive model (GAM) to model their nonlinear influence. Experiments found AlignFace significantly improves alignment with human subpopulation perceptions compared to baseline metrics, including recent domain-free learned perceptual metrics. By bridging learned representations and human cognitive processes, this work enables more transparent and aligned perceptual evaluation metrics for face images.

## Metadata
- **Published**: 2026-08-14T09:36:28Z
- **Authors**: Ying Huang, Wencan Zhang, Brian Y. Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14130v1)