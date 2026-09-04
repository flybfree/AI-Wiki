---
title: BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training
published: 2026-09-02T20:33:23Z
authors: Bigyan Ghimire, Jon C. Calhoun
url: http://arxiv.org/abs/2609.03151v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training

## Abstract
Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements. Sequence parallelism has emerged as an essential technique for addressing bottlenecks in long sequence LLM training. However, we observe that existing sequence parallelism methods are batch-agnostic and apply uniform sequence partitioning across all batch sizes, resulting in inefficient communication. In this paper, we introduce Batch- Aware Sequence Parallelism (BASP), a sequence parallelism approach that leverages batch structure to reduce communication overhead. BASP exploits batch structure by partitioning GPUs into disjoint sequence-parallel groups according to the micro- batch size. This design reduces the all-to-all communication group size, thereby localizing communication and improving training efficiency. Experimental results on an NVIDIA A100 cluster show that BASP improves end-to-end training time by up to 1.17 - 1.31x in Llama and Qwen models compared to standard sequence parallel baselines, while preserving identical model accuracy and memory usage.

## Metadata
- **Published**: 2026-09-02T20:33:23Z
- **Authors**: Bigyan Ghimire, Jon C. Calhoun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03151v1)