---
title: Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing
published: 2026-07-22T20:51:28Z
authors: Sadegh Majidi, Niloofar Mireshghallah, Kazem Taram
url: http://arxiv.org/abs/2607.20723v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing

## Abstract
This work presents LeakyLMs, a set of attacks that leak proprietary model, architecture, and deployment information from production language models. LeakyLMs is the first to demonstrate that key model and deployment details can be inferred using only token generation timing, even when interacting through remote APIs. LeakyLMs introduces two core attacks. The first attack targets inference optimizations and deployment strategies. For example, our attack detects whether a provider uses speculative decoding, a widely deployed inference-time optimization, and further identifies the context length of the draft model used in the pipeline. Our measurements show that Google Gemini Flash 2.5 uses speculative decoding with a draft context window of approximately 128K tokens. The second attack recovers key architectural properties, including the number of transformer layers, hidden dimension size, and number of attention heads. To achieve this, LeakyLMs builds a detailed and accurate model of token-generation timing on modern NVIDIA GPUs, characterizing how latency scales with model configuration and hardware parameters. The attack then performs a search over the architecture space using this timing model. In experiments with Llama models, the near-correct architectural configuration appears in the top-10 guesses more than 90% of the time.

## Metadata
- **Published**: 2026-07-22T20:51:28Z
- **Authors**: Sadegh Majidi, Niloofar Mireshghallah, Kazem Taram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20723v1)