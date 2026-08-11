---
title: Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis
published: 2026-08-09T21:53:37Z
authors: Kalelo Dukuray, Israel Pina, Evan Perez, Erika Ardiles-Cruz, Jie Wei
url: http://arxiv.org/abs/2608.08935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis

## Abstract
This work presents a unified multimodal AI system for damage assessment that integrates retrieval-augmented generation (RAG) models, thermal spectrum perception, vision foundation model pipelines, and exploratory wireless signal sensing. A RAG component is developed to ground a locally hosted language model in project-specific documentation, including specialized damage level classification criteria to mitigate hallucinations during inference. Controlled comparisons against static few-shot prompting demonstrate that dynamic retrieval improves grounding and factual consistency. We further compare vector-based RAG with a knowledge graph variant constructed via entity-relation extraction, and show that graph-based retrieval produces stronger responses for damage assessment queries requiring cross-document reasoning, motivating hybrid dense, sparse, and graph-aware retrieval. To address limitations of EO imagery under adverse lighting and weather conditions, infrared (IR)/thermal sensing is employed for object detection and segmentation. Our detectors generate candidate detections, yielding improved segmentation of a broad array of objects. Paired IR versus visible spectrum tracking experiments reveal failure modes, motivating multimodal fusion for robust object detection and damage analysis. Vision foundation and vision-language models are leveraged to generate synthetic damage imagery and classify damage severity with high accuracy, supporting training and validation of downstream damage assessment models. Finally, exploratory Wireless-based sensing demonstrates potential to detect presence, motion, and post-event environmental changes where EO and IR sensing are ineffective.

## Metadata
- **Published**: 2026-08-09T21:53:37Z
- **Authors**: Kalelo Dukuray, Israel Pina, Evan Perez, Erika Ardiles-Cruz, Jie Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08935v1)