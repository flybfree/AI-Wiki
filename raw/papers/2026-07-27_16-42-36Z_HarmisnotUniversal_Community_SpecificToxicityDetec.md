---
title: Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed
published: 2026-07-27T16:42:36Z
authors: Xinnuo Xu, Anja Thieme, Daniela Massiceti, Ioana Tanase, Rita Marques, Melanie Fernandez Pradier, Martin Grayson, Camilla Longden, Cecily Morrison
url: http://arxiv.org/abs/2607.24898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed

## Abstract
State-of-the-art toxicity detectors for text-to-image generation adopt a one-size-fits-all approach: a single universal model applying fixed safety guidelines to all users. Our empirical evidence shows that these detectors fail to shield marginalized communities: approximately 35% of generated images labeled safe are considered harmful by disability communities. In this position paper, we argue for community-specific toxicity detection (CTD). To demonstrate its feasibility, we collaborate with disability experts to develop safety guidelines for two communities: dwarfism and blind/low vision. Using a dataset of 2,400 annotated T2I-generated images we demonstrate that both large vision-language models and existing general-purpose toxicity detectors catastrophically fail to recognize harmful content under these guidelines in zero-shot settings with F1 score lower than random guessing (F1 0.32 and 0.37). Promisingly, prompt-based adaptation methods (ICL, VQA) substantially improve harm detection performance (GPT-4o: F1 0.50 and 0.78), while parameter-efficient fine-tuning improves smaller models (0.5b-7b with best F1 0.48 and 0.59) with less than 100 demonstrations, but remains sensitive to evolving guidelines. Despite these gains, CTD performance remains far below F1 $\approx 0.9$ achieved for general-purpose toxicity detection, highlighting the challenge and the need for sustained research effort.

## Metadata
- **Published**: 2026-07-27T16:42:36Z
- **Authors**: Xinnuo Xu, Anja Thieme, Daniela Massiceti, Ioana Tanase, Rita Marques, Melanie Fernandez Pradier, Martin Grayson, Camilla Longden, Cecily Morrison
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24898v1)