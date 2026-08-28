---
title: Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models
published: 2026-08-27T03:57:52Z
authors: Saksham Khatwani, He Cheng, Majid Afshar, Dmitriy Dligach, Yanjun Gao
url: http://arxiv.org/abs/2608.26587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models

## Abstract
Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question. We present a systematic study spanning five KG task formulations, three training paradigms, two KGs, and three base LLMs. At the task level, all paradigms improve over the non-finetuned baseline, but methods with comparable in-domain accuracy show substantially different knowledge transfer behavior. We introduce Gradient Intervention Density (GID) and Gradient Distortion (GD) to measure how broadly an optimizer modifies the pretrained model. GID and GD together reveal a clear divide: KG-judgment training under KL regularization produces sparse, localized updates (a regime we term as surgical alignment), while task-specific SFT produces dense ones. A controlled ablation shows that the objective and KL contribute to sparsity independently, and the paradigms that produce sparse updates also improve reasoning quality, even when their in-domain accuracy is lower than task-specific SFT. Assessing KG-LLM integration thus requires complementing accuracy with optimization-geometry diagnostics. Our implementation can be found at https://github.com/LARK-NLP-Lab/Surgical-Alignment.

## Metadata
- **Published**: 2026-08-27T03:57:52Z
- **Authors**: Saksham Khatwani, He Cheng, Majid Afshar, Dmitriy Dligach, Yanjun Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26587v1)