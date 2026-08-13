---
title: Instruction Alignment for Binary Code Representation Learning
published: 2026-08-12T08:07:26Z
authors: Huaijin Wang, Shuai Wang
url: http://arxiv.org/abs/2608.11766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instruction Alignment for Binary Code Representation Learning

## Abstract
Binary code representation learning is a fundamental problem in software security and reverse engineering. Existing methods mainly learn function-level embeddings that capture coarse-grained semantic relationships between binary functions, but they largely ignore fine-grained instruction-level correspondences. This limitation misses valuable supervision signals available from compiler debug information, which can support the learning of more accurate and interpretable binary code representations.   We propose to leverage instruction alignment knowledge to further improve binary code representation learning. Our preliminary study reveals that models finetuned for function-level binary code similarity exhibit substantially better instruction alignment than their pre-trained model, suggesting a strong correlation between instruction alignment and function-level embedding quality. Motivated by this observation, we design a training approach that explicitly incorporates instruction alignment as an auxiliary training objective. Our experiments show that instruction alignment training improves retrieval accuracy and provides more discriminative signal for the model's similarity judgments.

## Metadata
- **Published**: 2026-08-12T08:07:26Z
- **Authors**: Huaijin Wang, Shuai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11766v1)