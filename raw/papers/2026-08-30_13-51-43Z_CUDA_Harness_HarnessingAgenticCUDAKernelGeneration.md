---
title: CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language
published: 2026-08-30T13:51:43Z
authors: Qi Fan, An Zou, Yehan Ma
url: http://arxiv.org/abs/2609.00058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language

## Abstract
Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential. Meanwhile, the general-purpose code generation capability of Large Language Models (LLMs) prompts a series of works exploring LLM-based CUDA kernel generation. They mainly focus on transpilation from high-level frameworks such as PyTorch to CUDA (Torch2CUDA) rather than Text2CUDA, where models must understand the high-level input semantics and handle low-level kernel implementation and validation. Additionally, these methods are vulnerable to reward hacking due to reliance on predefined test inputs. In this paper, we propose CUDA-Harness, a framework for harnessing agentic CUDA kernel generation and optimization from natural language. Specifically, we introduce Intermediate-Structured Generation to connect high-level semantic understanding with low-level kernel generation. To dilute reward hacking in Text2CUDA, we construct Synthesis-Based Verification to provide isolated test data and progressive validation. Furthermore, we propose Feedback-Adaptive Evolution, a kernel evolution strategy that prioritizes correctness while optimizing performance. Finally, through extensive experiments, we demonstrate the effectiveness of CUDA-Harness, with further evaluations illustrating generalization across LLMs, hardware platforms, and to C-to-CUDA transpilation.

## Metadata
- **Published**: 2026-08-30T13:51:43Z
- **Authors**: Qi Fan, An Zou, Yehan Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00058v1)