---
title: Quantize with Confidence? An Empirical Study of Quantization for Code Generation
published: 2026-07-15T14:05:33Z
authors: Saima Afrin, Md. Zahidul Haque, Antonio Mastropaolo
url: http://arxiv.org/abs/2607.14181v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantize with Confidence? An Empirical Study of Quantization for Code Generation

## Abstract
The growing adoption of local inference frameworks such as Ollama has made it increasingly common for developers to run large code models on laptops and other resource-constrained hardware. In these settings, post-training quantization is essential for reducing memory footprint and enabling practical deployment, yet its impact on generated code remains insufficiently understood. We empirically evaluate six state-of-the-art quantization methods (GPTQ, AWQ, QuIP#, AQLM, BitsAndBytes, and GGUF) on two representative large code model families, Qwen2.5-Coder and CodeLlama, using the multilingual McEval and CoderEval benchmarks for Python and Java. We assess functional correctness (pass@1) together with maintainability, reliability, security, and structural complexity. We also introduce a novel analysis of robustness under varying prompt complexity, characterized by Shannon entropy and token length. Our results show that quantization techniques differ meaningfully in their impact on correctness and code quality. AQLM consistently matches or exceeds the full-precision baseline, whereas QuIP# exhibits the largest correctness degradation, particularly on complex prompts. Security attributes remain stable across models, benchmarks, and programming languages, while robustness to prompt complexity varies across techniques. These findings provide practical guidance for selecting quantization strategies for deploying large code models on resource-constrained hardware and highlight the importance of evaluating quantized models beyond functional correctness.

## Metadata
- **Published**: 2026-07-15T14:05:33Z
- **Authors**: Saima Afrin, Md. Zahidul Haque, Antonio Mastropaolo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14181v1)