---
title: Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges
published: 2026-09-04T06:16:49Z
authors: Chenqi Li, Minghui Min, Dusit Niyato, Wei Ni
url: http://arxiv.org/abs/2609.04778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges

## Abstract
Diffusion language models (DLMs) offer a non-autoregressive alternative for mobile edge agentic artificial intelligence (AI) by refining tokens through iterative denoising rather than left-to-right decoding. Compared with autoregressive Transformer-based large language models (LLMs), DLMs can update multiple uncertain tokens in parallel and exploit bidirectional context throughout the generation process, enabling more flexible quality-latency trade-offs beyond fixed sequential decoding. These properties are particularly attractive for edge agents, where partial refinement, early exit, and constraint-guided correction can reduce response delay and communication overhead while improving robustness under noisy, incomplete, or dynamic contexts. This survey reviews DLM foundations and analyzes their suitability for edge settings under latency, memory, energy, bandwidth, privacy, and reliability constraints. We cover resource-efficient architectures, training and inference acceleration, compression, edge/cloud deployment, communication-aware serving, Internet of Things (IoT)/wireless applications, and evaluation of DLM-based agents. We further discuss open issues in long-context state management, split inference, trustworthy execution, multimodal grounding, and reproducible benchmarking. The goal is to connect DLM modeling properties, including bidirectionality, parallel refinement, controllability, and quality-latency elasticity, with system-level requirements of future mobile edge intelligence.

## Metadata
- **Published**: 2026-09-04T06:16:49Z
- **Authors**: Chenqi Li, Minghui Min, Dusit Niyato, Wei Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04778v1)