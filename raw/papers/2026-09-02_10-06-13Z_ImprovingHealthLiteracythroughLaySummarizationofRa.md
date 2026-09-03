---
title: Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation
published: 2026-09-02T10:06:13Z
authors: Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız
url: http://arxiv.org/abs/2609.02396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation

## Abstract
Radiology reports are written primarily for clinicians, and their specialized terminology often makes them difficult for patients to interpret. As a result, many patients turn to publicly available Large Language Models (LLMs) to help explain their reports, despite well-documented risks of factual inaccuracies and hallucinations. Automated lay-summary generation has emerged as a promising alternative, yet the effectiveness of retrieval-enhanced and clinically informed approaches for radiology-specific communication remains underexplored. This study investigates the extent to which Retrieval-Augmented Generation (RAG) and Named Entity Recognition (NER) improve the quality, factual consistency, and readability of automatically generated lay summaries compared with standard LLM-based generation. We develop a framework combining NER-based extraction of clinically relevant findings with a RAG mechanism for contextual grounding, evaluated across few-shot and fine-tuned variants of two models (Qwen, BioBART). Results show that NER consistently improves readability and overall quality, while RAG alone offers no benefit and can introduce hallucinations from irrelevant retrieved terms. Combining RAG with NER degrades performance in few-shot settings but improves readability when fine-tuned. Fine-tuned BioBART with NER achieves the best overall performance, highlighting entity-aware extraction as the primary driver of improved patient-friendly summaries.

## Metadata
- **Published**: 2026-09-02T10:06:13Z
- **Authors**: Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02396v1)