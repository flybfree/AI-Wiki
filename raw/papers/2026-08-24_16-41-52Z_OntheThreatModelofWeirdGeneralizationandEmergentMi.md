---
title: On the Threat Model of Weird Generalization and Emergent Misalignment
published: 2026-08-24T16:41:52Z
authors: Miriam Wanner, Mark Dredze, William Walden
url: http://arxiv.org/abs/2608.23476v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Threat Model of Weird Generalization and Emergent Misalignment

## Abstract
Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely on small question sets that assess the extent of the generalization, we also analyze how sensitive this measurement is to the set of questions used. Experiments with three open-weight models on four datasets show that the degree of WG (1) depends heavily on dataset composition and language (more than on size); (2) is greater for data familiar from pretraining than for novel data; and (3) is sensitive to the set of evaluation questions used. Collectively, these results indicate that WG is a product of quite fragile properties of both training and evaluation data. As such, we argue that WG is more plausible as an adversarial threat-requiring careful data engineering-rather than as a significant hazard inherent to routine fine-tuning.

## Metadata
- **Published**: 2026-08-24T16:41:52Z
- **Authors**: Miriam Wanner, Mark Dredze, William Walden
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23476v1)