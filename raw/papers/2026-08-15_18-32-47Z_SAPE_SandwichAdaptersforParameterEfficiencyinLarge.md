---
title: SAPE: Sandwich Adapters for Parameter Efficiency in Large Language Model Fine-Tuning
published: 2026-08-15T18:32:47Z
authors: Mohammad Aref Jafari-Raddani, Morteza Mohajjel Kafshdooz
url: http://arxiv.org/abs/2608.15360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAPE: Sandwich Adapters for Parameter Efficiency in Large Language Model Fine-Tuning

## Abstract
While Parameter-Efficient Fine-Tuning (PEFT) has substantially reduced the hardware cost of adapting Large Language Models (LLMs) by decreasing the number of trainable parameters, recent studies have sought to further improve PEFT through parameter sharing. However, these approaches either employ uniform parameter sharing across layers, which can delay convergence, or rely on dynamic masking strategies, which add computational overhead. The potential of sharing patterns inspired by the inherent hierarchical structure of Transformer architectures remains unexplored in PEFT. To address this gap, we introduce SAPE (Sandwich Adapters for Parameter Efficiency), a PEFT framework based on a sandwich-style hard weight-sharing topology. SAPE routes intermediate Transformer layers through balanced shared group adapters while strictly isolating the input embedding and final projection boundary transformations to prevent gradient interference. This design significantly reduces memory consumption while eliminating the computational overhead associated with dynamic parameter-sharing methods. Extensive evaluations across encoder-only and causal decoder architectures demonstrate that SAPE achieves state-of-the-art performance in low-parameter regimes. On natural language understanding, SAPE outperforms proPETL on RoBERTa-large while utilizing only 10% of the baseline's parameter budget. On natural language generation and world knowledge reasoning with LLaMA-3.2 (3B) under a strict ~0.6M parameter constraint, SAPE outperforms AdaLoRA, yielding absolute improvements of +4.85% on GSM8K and +3.11% on CommonsenseQA. Furthermore, through comprehensive topological ablations, we formalize an inherent capacity trade-off: while hard parameter sharing strongly regularizes semantic generalization, it slightly smooths the sharp layer-wise transformations required for rigid multi-step arithmetic reasoning.

## Metadata
- **Published**: 2026-08-15T18:32:47Z
- **Authors**: Mohammad Aref Jafari-Raddani, Morteza Mohajjel Kafshdooz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15360v1)