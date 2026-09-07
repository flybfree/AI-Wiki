---
title: Large Language Models with At Most One Spike per Neuron
published: 2026-09-04T13:53:28Z
authors: Zhuoya Zhao, Parsa Omidi, Aref Jafari, Richard Naud
url: http://arxiv.org/abs/2609.05151v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large Language Models with At Most One Spike per Neuron

## Abstract
Leveraging their inherent sparse event-driven computation, spiking neural networks (SNNs) offer a promising path toward energy-efficient large language models (LLMs). Time-to-first-spike (TTFS) coding generates at most one spike per neuron within a time window, yielding extremely low firing rates. However, conventional TTFS SNNs are restricted to specific structures, making it challenging to encode certain blocks in LLM -- such as layer normalization and matrix multiplication --using TTFS. To overcome this limitation, we introduce a reference-based strategy specifically to encode the four core LLM components: embedding layers, layer normalization, attention-related operations and dropout. We construct a fully TTFS-based SNN architecture and train it end-to-end. Experiments on modern LLMs like BERT and GPT-2 demonstrate that our approach achieves performance comparable to ANN counterparts on natural language understanding and common-sense reasoning, while a clear gap remains on language modeling perplexity. To the best of our knowledge, this is the first work to scale a spiking LLM to 1.5 billion parameters using TTFS coding. We also report an estimate of spike-related energy; this is a spike-count proxy under an established cost model rather than a measurement on neuromorphic hardware.

## Metadata
- **Published**: 2026-09-04T13:53:28Z
- **Authors**: Zhuoya Zhao, Parsa Omidi, Aref Jafari, Richard Naud
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05151v1)