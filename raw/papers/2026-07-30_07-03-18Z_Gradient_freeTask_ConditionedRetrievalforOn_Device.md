---
title: Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning
published: 2026-07-30T07:03:18Z
authors: Xinyu Luo, Hui Liu, Yihua Shao, Junyi Yang, Arindam Basu, Haoliang Li
url: http://arxiv.org/abs/2607.27766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning

## Abstract
On-device in-context learning (ICL) relies on pre-inference retrieval to select demonstrations for useful context before downstream model inference. This retrieval must exploit task-specific information while operating over local memories under limited computation, memory, and data-exposure budgets. We propose Conditional Retrieval Alignment (CoRA), a gradient-free framework that converts a frozen encoder into a task-conditioned retriever using paired candidate inputs and outputs. CoRA selects complementary encoder layers, constructs an output-derived conditioning space from candidate memory, and aligns candidate input representations to this space through closed-form ridge regression. Low-rank factorization then produces a compact retrieval basis where candidate outputs are used only during offline index construction, whereas query-time retrieval requires only the query input and precomputed index. We show that CoRA's rank-constrained basis is the optimal low-rank compression of the output-conditioned fitted representation, and derive an exact two-pass streaming construction that avoids materializing the full fitted matrix. We further extend the framework to multimodal exemplar retrieval by incorporating visual representations into the conditioning and retrieval spaces. Experiments across ten textual datasets and four multimodal benchmarks with Llama-3.2-1B, MobileLLM-Pro, OpenFlamingo-3B, and Qwen3.5-2B, as well as end-to-end Raspberry Pi~5 deployment demonstrate that CoRA supports effective task-conditioned retrieval without retriever fine-tuning, backpropagation, or target-model calls.

## Metadata
- **Published**: 2026-07-30T07:03:18Z
- **Authors**: Xinyu Luo, Hui Liu, Yihua Shao, Junyi Yang, Arindam Basu, Haoliang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27766v1)