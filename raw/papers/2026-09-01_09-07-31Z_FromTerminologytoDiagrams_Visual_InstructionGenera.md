---
title: From Terminology to Diagrams: Visual-Instruction Generation for Scientific Diagram Understanding
published: 2026-09-01T09:07:31Z
authors: Raul Ortega, José Manuel Gómez-Pérez
url: http://arxiv.org/abs/2609.00948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Terminology to Diagrams: Visual-Instruction Generation for Scientific Diagram Understanding

## Abstract
Vision-language models (VLMs) have demonstrated strong performance in visual question answering with natural images. However, they continue to struggle with scientific diagrams, which are designed to convey functional or relational meaning rather than literal scenes. We therefore introduce a framework for generating large-scale diagram-grounded instruction data by leveraging terminology derived from scientific curricula. Our approach systematically extracts domain concepts, synthesizes atomic facts, retrieves relevant diagrams from the web, and generates multimodal supervision in the form of diagram captions and multiple-choice questions. Using this pipeline, we construct SciGram, a dataset of over 194K diagrams and 1.4M visual instructions across life, earth, and physical sciences. Despite relying on noisy web data and synthetic annotations, models fine-tuned on SciGram achieve substantial improvements on diagram-centric benchmarks, including TQA, ScienceQA, and AI2D, outperforming or matching state-of-the-art VLMs while using fewer training instances. Furthermore, augmenting existing models such as LLaVA OneVision with SciGram establishes new state-of-the-art performance on diagram question answering. Our results highlight the effectiveness of terminology-grounded instruction generation as a general strategy for improving vision-language reasoning in scientific domains. To support future research in scientific diagram understanding, we release both the SciGram dataset and models.

## Metadata
- **Published**: 2026-09-01T09:07:31Z
- **Authors**: Raul Ortega, José Manuel Gómez-Pérez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00948v1)