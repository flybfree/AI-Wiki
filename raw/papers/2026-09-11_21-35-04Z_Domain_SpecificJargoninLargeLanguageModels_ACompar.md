---
title: Domain-Specific Jargon in Large Language Models: A Comparative Analysis between General-Purpose and Specialist Models
published: 2026-09-11T21:35:04Z
authors: Darin Keng, Zhewei Sun
url: http://arxiv.org/abs/2609.13556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Domain-Specific Jargon in Large Language Models: A Comparative Analysis between General-Purpose and Specialist Models

## Abstract
Large Language Models (LLMs) have shown remarkable proficiency on general-purpose tasks, yet their performance often degrades in highly-specialized technical domains. Moreover, little is known about how parametric knowledge of domain-specific terms is encoded within these models. We address this gap by contributing two novel medical jargon evaluation benchmarks and evaluate a general-purpose Llama-3.1 model against a variant fine-tuned on medical-domain data. Surprisingly, the general-purpose model outperforms the medically fine-tuned model on both tasks. Using mechanistic interpretability tools, we find systematic patterns of miscalibration for the medically fine-tuned model. Instead of reorganizing parametric knowledge, the fine-tuned model places greater emphasis on a small subset of model components associated with jargon-favoring predictions. We find that applying component reweighting strategies against the benchmark tasks successfully suppresses these components and closes the gap with the general-purpose baseline. We also observe that some jargon-sensitive components transfer knowledge to the same tasks involving materials science jargon, suggesting they encode a partially domain-agnostic notion of specialized terminology. Our results provide a case study in which a medically fine-tuned checkpoint does not improve jargon comprehension over its general-purpose counterpart, highlighting that domain adaptation should not be assumed to yield better performance on specialized terminology.

## Metadata
- **Published**: 2026-09-11T21:35:04Z
- **Authors**: Darin Keng, Zhewei Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13556v1)