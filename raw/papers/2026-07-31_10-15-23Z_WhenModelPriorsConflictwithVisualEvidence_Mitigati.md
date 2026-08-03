---
title: When Model Priors Conflict with Visual Evidence: Mitigating Commonsense-Driven Hallucinations by Selective Prior Calibration
published: 2026-07-31T10:15:23Z
authors: Kesheng Chen, Yamin Hu, Wenjian Luo
url: http://arxiv.org/abs/2607.29240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Model Priors Conflict with Visual Evidence: Mitigating Commonsense-Driven Hallucinations by Selective Prior Calibration

## Abstract
In vision--language models, commonsense-driven hallucination (CDH) occurs when a model's commonsense prior overrides clear visual evidence of an atypical state. For example, a model may report that a visibly six-fingered hand has five fingers. We show that these errors are systematically directed: when a model answers a question about a counterfactual (CF) image incorrectly, its answer often coincides with the candidate it prefers without access to the image. Suppressing this prior indiscriminately can repair CF errors, but may also disrupt correct answers on matched commonsense (CS) images, where the same prior is helpful. We therefore propose Selective Prior Calibration (SPC), which subtracts candidate-level prior-preference estimates from image-conditioned scores with an instance-dependent strength and revises the original prediction only when the resulting score pattern strongly supports an alternative. Extensive experiments demonstrate that SPC substantially improves accuracy on CF images while largely preserving accuracy on matched CS images. Furthermore, these gains generalize across CDH categories, candidate-answer permutations, and other conflict benchmarks, while SPC rarely alters predictions on benchmarks without such conflicts.

## Metadata
- **Published**: 2026-07-31T10:15:23Z
- **Authors**: Kesheng Chen, Yamin Hu, Wenjian Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29240v1)