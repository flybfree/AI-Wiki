---
title: Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips
published: 2026-08-26T01:23:01Z
authors: Huakang Lin, Tiancheng Zheng, Mingxuan Sun, Tianhong Xu, Fan Zhang, Yunsi Fei, Ruyi Ding
url: http://arxiv.org/abs/2608.25276v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips

## Abstract
Mixture-of-Experts (MoE) architectures enable scalable and efficient large language models (LLMs) by selectively activating expert sub-networks through a routing mechanism. However, this adaptive design introduces a new attack surface: specific experts become disproportionately correlated with certain tokens (e.g., end-of-sequence), allowing adversaries to manipulate model behavior via lightweight perturbations. In this work, we present \textbf{Groundhog Bit-Flip Attack (GBFA)}, the first bit-flip-based \textit{ Denial-of-Wallet availability attack} against MoE-based LLMs. By identifying and flipping routing-layer bits associated with related expert activations, we demonstrate that GBFA substantially extends the decoding token usage across three different LLM modes: conversational, reasoning, and agentic tasks, while largely preserving semantic fidelity. Across four main real-world MoE-based LLMs, manually deactivating on average fewer than \textbf{4 experts} drives average output inflation to $\mathbf{5912\%}$, with the majority of test samples reaching max tokens. These results reveal a robustness vulnerability of MoE architectures to bit flip, and highlight the potential of GBFA as an availability attack against LLMs.

## Metadata
- **Published**: 2026-08-26T01:23:01Z
- **Authors**: Huakang Lin, Tiancheng Zheng, Mingxuan Sun, Tianhong Xu, Fan Zhang, Yunsi Fei, Ruyi Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25276v1)