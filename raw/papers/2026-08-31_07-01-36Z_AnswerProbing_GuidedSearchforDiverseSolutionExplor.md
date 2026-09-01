---
title: Answer Probing-Guided Search for Diverse Solution Exploration of LLMs
published: 2026-08-31T07:01:36Z
authors: Yi Fang, Que Shen, Chengpeng Li, Boyi Deng, Wei Shi, Wenjie Wang, Fuli Feng, Fengli Xu, Dayiheng Liu
url: http://arxiv.org/abs/2608.30345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Answer Probing-Guided Search for Diverse Solution Exploration of LLMs

## Abstract
Generating multiple diverse and high-quality solutions is valuable for many applications, such as code-test generation and drug discovery. However, Large Language Models (LLMs) tend to converge on a single high-confidence solution during inference, limiting exploration of alternative valid solution paths. Existing test-time methods promote diversity through tree-like search and prune semantically similar branches using response-level semantic embeddings. However, we find that such embeddings are easily confounded by linguistic and stylistic similarities, making it difficult to distinguish genuinely distinct solution paths. To address this, we introduce Answer Probing, which probes the potential answer an LLM would reach from an intermediate reasoning path. We demonstrate that the hidden states of probed answers more effectively differentiate distinct solution paths than semantic embeddings, and the perplexity of probed answers serves as a practical proxy for reasoning correctness. Based on these findings, we propose Answer Probing-Guided Tree Search (APTS), which guides the tree search by the probed answers' hidden state similarity and perplexity. Experiments on three reasoning tasks across two LLMs show that APTS consistently enhances solution diversity, demonstrating its effectiveness and robustness.

## Metadata
- **Published**: 2026-08-31T07:01:36Z
- **Authors**: Yi Fang, Que Shen, Chengpeng Li, Boyi Deng, Wei Shi, Wenjie Wang, Fuli Feng, Fengli Xu, Dayiheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30345v1)