---
title: TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval
published: 2026-08-13T17:24:23Z
authors: Yi-Chung Chen, Philip Jacobson, Tom Lampo, Yiren Lu, Jin Yao, David I. Inouye, Jing Gao, Danhua Guo, Burhan Yaman
url: http://arxiv.org/abs/2608.13495v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval

## Abstract
Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on shortcuts from static scene context and struggle to distinguish motion-centric events, such as turning left versus right or accelerating versus decelerating. In this work, we study how to adapt a general-purpose multimodal embedding model to driving-video retrieval. We first fine-tune Qwen3-VL-Embedding on paired clips and reasoning traces from nuReasoning using an InfoNCE objective. While this stage substantially improves overall retrieval, caption supervision alone remains insufficient for fine-grained motion understanding. We therefore introduce TraVEL (Trajectory-Guided Video Embedding Learning), a motion-aware fine-tuning framework that uses ego-trajectory similarity as a reward within Group Relative Policy Optimization. Trajectories serve only as privileged training supervision; retrieval still operates on single-vector video embeddings without ego poses, expert rules, or auxiliary perception outputs. We further construct a driving-video retrieval benchmark from nuReasoning. Experiments show that TraVEL improves motion-centric retrieval across model scales: relative to SFT, it raises longitudinal and lateral mAP by 9.8 and 4.7 points at 2B, with corresponding gains of 7.2 and 1.5 points at 8B. TraVEL thus combines physically grounded supervision with efficient embedding-based search.

## Metadata
- **Published**: 2026-08-13T17:24:23Z
- **Authors**: Yi-Chung Chen, Philip Jacobson, Tom Lampo, Yiren Lu, Jin Yao, David I. Inouye, Jing Gao, Danhua Guo, Burhan Yaman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13495v1)