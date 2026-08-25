---
title: Retrieval-Augmented Classification of Environmental Mitigations in Hydropower Licensing Documents
published: 2026-08-24T13:27:18Z
authors: Hong-Jun Yoon, Tom Ruggles, Joanna Lee, Debjani Singh
url: http://arxiv.org/abs/2608.23241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-Augmented Classification of Environmental Mitigations in Hydropower Licensing Documents

## Abstract
Identifying and classifying environmental mitigation obligations in Federal Energy Regulatory Commission hydropower licensing documents is a labor-intensive task requiring deep domain expertise. We formulate this as a multi-label classification problem over a structured 135-category taxonomy and address the central challenge of severe label scarcity: 40 of 135 categories have no training examples, and 26 have fewer than five. A supervised Bidirectional Encoder Representations from Transformers (BERT)-based pipeline, while effective on well-represented categories, achieves F1 of zero on unseen classes regardless of augmentation strategy. We introduce a Retrieval-Augmented Generation (RAG) pipeline that conditions classification on retrieved category definitions, enabling zero-shot generalization across the full label space. We further propose a hybrid system that combines BERT detection with RAG classification, exploiting the high recall of fine-tuned detection and the zero-shot coverage of retrieval-augmented reasoning. Evaluated on the full set of 2017 license documents (5,860 paragraphs, 135 categories), the hybrid achieves a Micro F1 of 0.524, outperforming the BERT-only pipeline (0.477) and the RAG-only pipeline (0.416) across all training-support buckets.

## Metadata
- **Published**: 2026-08-24T13:27:18Z
- **Authors**: Hong-Jun Yoon, Tom Ruggles, Joanna Lee, Debjani Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23241v1)