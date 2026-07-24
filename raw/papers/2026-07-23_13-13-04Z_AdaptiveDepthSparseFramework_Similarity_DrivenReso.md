---
title: Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs
published: 2026-07-23T13:13:04Z
authors: Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang
url: http://arxiv.org/abs/2607.21291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs

## Abstract
Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability. We present an Adaptive Depth Sparse Framework (AdaDSF) that converts off-the-shelf pre-trained LLMs into depth-sparse models without full retraining. Our key insight is that layers contribute unequally to representation transformation, characterized by the cosine similarity between layer input and output hidden states. Based on this, AdaDSF assigns layer-wise token retention ratios from similarity statistics, uses a lightweight router to select informative tokens at each layer, and introduces a feature-preserving alignment objective to match intermediate and final representations between sparse and dense models. On GPT-NeoX and Qwen2.5 over language modeling and commonsense reasoning, AdaDSF substantially reduces inference FLOPs while preserving performance close to dense counterparts. Under comparable sparsity, AdaDSF consistently yields smaller accuracy degradation than strong baselines including MoD, D-LLM, and DLO.

## Metadata
- **Published**: 2026-07-23T13:13:04Z
- **Authors**: Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21291v1)