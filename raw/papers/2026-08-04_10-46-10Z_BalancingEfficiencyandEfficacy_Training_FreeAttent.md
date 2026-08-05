---
title: Balancing Efficiency and Efficacy: Training-Free Attention-Guided Switching Between Explicit and Latent Thoughts for MLLMs
published: 2026-08-04T10:46:10Z
authors: Haoqian Kang, Liupeng Li, Kuofeng Gao, Jinpeng Wang, Zhenyu Lu, Bin Chen, Ke Chen, Yaowei Wang
url: http://arxiv.org/abs/2608.03450v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Balancing Efficiency and Efficacy: Training-Free Attention-Guided Switching Between Explicit and Latent Thoughts for MLLMs

## Abstract
Reasoning in Multimodal Large Language Models (MLLMs) requires both fine-grained visual perception and rigorous logical deduction. Explicit text-based Chain-of-Thought (CoT) is computationally expensive and prone to visual hallucinations, while existing latent reasoning methods typically require costly training. Furthermore, directly adapting training-free LLM reasoning mechanisms to the multimodal setting yields unstable performance. We identify that this failure stems from their reliance on token-level entropy, which fundamentally conflates perceptual ambiguity (e.g., unclear visual details) with logical uncertainty (e.g., complex reasoning steps). To overcome this bottleneck, we present a novel training-free inference strategy for MLLMs that explicitly decouples perception and reasoning. We propose a novel metric, the vision-to-text attention ratio, to dynamically gauge the model's cognitive focus. Guided by this metric, our proposed framework, Attention-Guided Switching (AGS), adaptively triggers latent reasoning for perceptual tokens to preserve high-fidelity visual information in the continuous space, while enforcing explicit text generation for logical tokens to maintain structural anchoring. Extensive experiments demonstrate that our method achieves state-of-the-art performance, significantly improving both accuracy and inference efficiency by reducing autoregressive steps and latency. Code is released at https://github.com/swordAndSnow/MM26-AGS.

## Metadata
- **Published**: 2026-08-04T10:46:10Z
- **Authors**: Haoqian Kang, Liupeng Li, Kuofeng Gao, Jinpeng Wang, Zhenyu Lu, Bin Chen, Ke Chen, Yaowei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03450v1)