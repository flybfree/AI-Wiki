---
title: Locating Sycophancy Across Training Stages in Open Language Models
published: 2026-10-27T18:08:55Z
authors: Jiarui Yao, Shweta Parihar, Nghia Tuan Bui, Guergana K Savova, Lijing Wang
url: http://arxiv.org/abs/2610.37788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locating Sycophancy Across Training Stages in Open Language Models

## Abstract
Language model assistants sometimes change a correct answer when the user suggests a wrong one. The behavior, called sycophancy, is usually attributed to preference-based post-training, yet early measurements found it in pretrained models. We ask where it comes from by measuring it at every available stage of training: 13 open checkpoints from 5 lineages, from base model through supervised fine-tuning and preference optimization to release. We separate how far an injected claim moves a model's answer from how firmly the answer was held, and vary who makes the claim, how reliable they are said to be, and how strongly they make it. Two sycophancy behaviors with different origins emerge, and both replicate across datasets. Deference to a claim in the prompt is already present in every base model, which ranks sources in the same order as its post-trained descendants. Capitulation in conversation, dropping a stated answer when the user objects, is largely absent from base models and present in every post-trained checkpoint. When the objection names an alternative, most post-trained models give up firmly held answers as often as loosely held ones. We discuss the implications of these measurements for evaluating sycophancy and approaches for addressing each behavior.

## Metadata
- **Published**: 2026-10-27T18:08:55Z
- **Authors**: Jiarui Yao, Shweta Parihar, Nghia Tuan Bui, Guergana K Savova, Lijing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.37788v1)