---
title: ReVA: A Region-Aware Visual Assistant for Visually Grounded Question Answering
published: 2026-08-27T20:33:13Z
authors: Anoop Senthil
url: http://arxiv.org/abs/2608.28707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReVA: A Region-Aware Visual Assistant for Visually Grounded Question Answering

## Abstract
Multimodal Large Language Models (MLLMs) have achieved remarkable progress in Visual Question Answering (VQA), yet they continue to struggle with questions requiring precise spatial reasoning and fine-grained visual understanding. These limitations often manifest as object, attribute, and spatial hallucinations, where models generate confident but visually unsupported responses due to insufficient region-level and fine-grained visual grounding. To address this challenge, we propose ReVA, a region-aware VQA model that employs a frozen CLIP ViT-L/14 Vision Transformer (ViT) and a Qwen2.5-7B-Instruct large language model (LLM) connected through a dual bridge that aligns both whole-image and region-level representations with the LLM's embedding space. The image bridge maps final transformer block features into image tokens. The region bridge maps cropped features from enriched intermediate features across ViT blocks so early texture and later object cues are more evident, into K region tokens for every bounding box. ReVA uses a detector stack that supplies automatic zero-shot bounding boxes that are both question-agnostic and question-dependent, using RAM++ (Recognize Anything Model), spaCy, and Grounding DINO. The image tokens and region tokens are concatenated as an LLM prompt prefix to jointly encode scene-level context and fine-grained regional evidence when answering questions. Evaluated on VQAv2, MMBench, POPE, and SEED-Bench, ReVA achieves 82.85% mean F1 on POPE, compared with 81.14% for an image-token baseline without region tokens. These results demonstrate that explicit region-aware visual representations reduce object hallucination and improve the factual grounding of MLLMs.

## Metadata
- **Published**: 2026-08-27T20:33:13Z
- **Authors**: Anoop Senthil
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28707v1)