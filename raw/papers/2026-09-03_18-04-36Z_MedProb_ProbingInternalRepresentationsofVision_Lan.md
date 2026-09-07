---
title: MedProb: Probing Internal Representations of Vision-Language Models for Medical Question Answering
published: 2026-09-03T18:04:36Z
authors: Erfan Nourbakhsh, Ke Yang, Anthony Rios
url: http://arxiv.org/abs/2609.04336v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedProb: Probing Internal Representations of Vision-Language Models for Medical Question Answering

## Abstract
Medical visual question answering (Med-VQA) is often assumed to require medical fine-tuning, large models, or complex multi-agent pipelines. We revisit this assumption with \textbf{MedProb}, a lightweight probing framework that predicts multiple-choice Med-VQA answers from frozen VLM representations without free-text generation. Across PATH-VQA, SLAKE, and VQA-RAD, MedProb recovers substantially more answer-relevant signal than prompting and performs stronger than medical VLMs and agentic systems. Probing also reduces the apparent gap between small and large models compared to prompting, suggesting that smaller VLMs contain more recoverable Med-VQA signal than generation-based evaluation reveals. Across 14 matched general-purpose and medical VLM pairs, medical adaptation does not consistently improve this linear decodability. Finally, free-text generation exhibits an answer-position bias of up to 10 percentage points, whereas MedProb also has positional bias, however, it is impacted differently than prompting. Our main results target the multiple-choice/multiclass Med-VQA setting; we additionally show the probe can be extended to open-ended generation via a rejection-sampling scoring procedure.

## Metadata
- **Published**: 2026-09-03T18:04:36Z
- **Authors**: Erfan Nourbakhsh, Ke Yang, Anthony Rios
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04336v1)