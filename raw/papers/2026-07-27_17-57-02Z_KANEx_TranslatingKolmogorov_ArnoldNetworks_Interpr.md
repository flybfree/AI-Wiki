---
title: KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability
published: 2026-07-27T17:57:02Z
authors: Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V., Sowmya S. Sundaram, Gokul S. Krishnan, Aditi Anand, Balaraman Ravindran
url: http://arxiv.org/abs/2607.24730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability

## Abstract
Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are increasingly paired with Vision-Language Models (VLMs) to generate natural-language explanations. However, these systems add linguistic fluency without addressing the underlying opacity of the visual model. With the emergence of Kolmogorov-Arnold Networks (KANs), whose spline-based components provide inherently interpretable functional units, we investigate whether this architectural transparency can be leveraged to produce more trustworthy textual explanations. We introduce KANEx, the first ever framework that leverages the symbolic transparency of KANs to ground VLM reasoning. This interpretability also made it possible to design KAN-Map, a novel heatmap generation method derived directly from KAN models rather than gradient approximations. We feed these grounded contexts into downstream VLMs for enhanced explainability. Benchmarked on the MIMIC-CXR dataset, we demonstrate that KAN-based architectures with ResNet/ViT baselines demonstrate improved semantic similarity while producing significantly more faithful saliency maps. KAN architectures improve visual localization and downstream reasoning quality by 10%. Our findings suggest that grounding linguistic explanations and visual attributions in mathematically interpretable units is a necessary step toward trustworthy medical AI.

## Metadata
- **Published**: 2026-07-27T17:57:02Z
- **Authors**: Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V., Sowmya S. Sundaram, Gokul S. Krishnan, Aditi Anand, Balaraman Ravindran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24730v1)