---
title: EuroAlpaca: Task-Preserving Localisation of Instruction Data for European Languages
published: 2026-09-04T12:05:53Z
authors: Aleix Sant, Jordi Luque, Carlos Escolano
url: http://arxiv.org/abs/2609.05043v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EuroAlpaca: Task-Preserving Localisation of Instruction Data for European Languages

## Abstract
Machine translation (MT) offers a scalable way to extend English instruction-tuning data to multiple languages, but it can distort task-critical constraints and required outputs, creating corrupted training examples and degrading models trained on such data. We introduce EuroAlpaca, a task-preserving localisation pipeline and near-parallel resource covering 50 European languages and regional varieties, together with European-IFEval, a multilingual benchmark for verifiable instruction following. Depending on the example, our pipeline applies field-wise MT while preserving task-critical content or reconstructs a task-equivalent target-language instance, followed by validation of cross-field coherence and target-language consistency. Across LoRA experiments with four LLMs, training on directly translated data improves ROUGE-L and F-BERT on the Aya Evaluation Suite, but reduces accuracy on European-IFEval by 29.8% relative to the unadapted baseline. In contrast, adaptation with EuroAlpaca improves accuracy by 12.9% over the same baseline, reversing the degradation caused by direct MT, while also achieving the highest ROUGE-L and F-BERT scores on Aya. These results show that preserving task semantics is essential for multilingual instruction tuning.

## Metadata
- **Published**: 2026-09-04T12:05:53Z
- **Authors**: Aleix Sant, Jordi Luque, Carlos Escolano
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05043v1)