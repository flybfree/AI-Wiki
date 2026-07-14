---
title: Evidence-Backed Video Question Answering
published: 2026-07-13T17:49:10Z
authors: Shijie Wang, Honglu Zhou, Ziyang Wang, Ran Xu, Caiming Xiong, Silvio Savarese, Chen Sun, Juan Carlos Niebles
url: http://arxiv.org/abs/2607.11862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Backed Video Question Answering

## Abstract
Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding. Existing explainability efforts rely on textual rationales or sparse bounding boxes, which struggle to capture complex video dynamics such as occlusions and non-rigid deformations. We propose Evidence-Backed Video Question Answering (E-VQA), a novel task requiring models to jointly output a semantic answer and precise spatio-temporal evidence: temporal segments and dense, tracked object segmentation masklets. To support this, we introduce ST-Evidence, the first human-verified benchmark for both discriminative and generative pixel-level grounding. Evaluations of state-of-the-art models reveal a critical decoupling between QA accuracy and true visual perception that scaling alone fails to bridge. To address this, we develop scalable, automated generation pipelines to create ST-Evidence-Instruct, a 160k-scale dataset bridging high-level reasoning with fine-grained grounding. Fine-tuning grounded Video LLMs on this data yields substantial gains over the corresponding size-matched UniPixel baselines (e.g., +27.2 t-mean and +13.8 J&F on a 7B model), establishing a robust baseline for explainable, evidence-backed video understanding. Code and data are available at https://github.com/SalesforceAIResearch/EVQA.

## Metadata
- **Published**: 2026-07-13T17:49:10Z
- **Authors**: Shijie Wang, Honglu Zhou, Ziyang Wang, Ran Xu, Caiming Xiong, Silvio Savarese, Chen Sun, Juan Carlos Niebles
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.11862v1)