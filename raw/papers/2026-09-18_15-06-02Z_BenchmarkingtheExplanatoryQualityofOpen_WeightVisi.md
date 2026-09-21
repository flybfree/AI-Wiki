---
title: Benchmarking the Explanatory Quality of Open-Weight Vision-Language Models in Face Recognition
published: 2026-09-18T15:06:02Z
authors: Laurent Colbois, Sébastien Marcel
url: http://arxiv.org/abs/2609.21879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking the Explanatory Quality of Open-Weight Vision-Language Models in Face Recognition

## Abstract
Vision-Language Models (VLMs) have recently been proposed as promising tools for face recognition, as they can produce natural language explanations alongside similarity scores. This capability is considered appealing for face comparisons in forensic contexts, which require decisions to be transparent and auditable. However, existing evaluations of VLMs for that use case focus mostly on recognition accuracy, while the validity of generated explanations remains unquantified. In this work, we introduce a benchmarking framework for VLM-based face recognition that treats explanation quality as a core evaluation axis. We propose two criteria that explanations should satisfy: relevance, i.e., reliance on identity-stable facial features; and faithfulness, i.e., alignment with the visible image content without hallucinated features. We jointly develop a methodology enabling the quantification of relevance and faithfulness of evaluated models, based on constraining model outputs to a structured explanation format that supports automated querying and auditing. Using this framework, we benchmark several families of open-weight VLMs, jointly evaluating face verification accuracy and explanation quality. Our results highlight remaining shortcomings of produced explanations, and emphasize the need for such explanation quality metrics to get a complete picture of model performance. The proposed benchmark and open-source evaluation harness provide a foundation for proper benchmarking and future fine-tuning of explainable face recognition systems.

## Metadata
- **Published**: 2026-09-18T15:06:02Z
- **Authors**: Laurent Colbois, Sébastien Marcel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21879v1)