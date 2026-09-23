---
title: From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs
published: 2026-09-22T04:04:53Z
authors: Zhentao Tan, Chang Liu, Yao Liu, Yue Wu, Jieping Ye
url: http://arxiv.org/abs/2609.25655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs

## Abstract
As large language models (LLMs) scale rapidly, dense full-parameter adaptation becomes increasingly expensive, motivating sparse and modular architectures such as Mixture-of-Experts (MoE) models. This shift raises a key question for parameter-efficient fine-tuning (PEFT): at what granularity should parameters be selected and updated? Existing PEFT methods such as LoRA operate on predefined weight matrices, while expert-level sparse tuning methods update entire selected experts. However, we observe that activated experts are internally sparse, with only a small fraction of intermediate channels strongly responding to downstream tasks, indicating that expert-level adaptation is still too coarse. We propose NSFT (Neural Sub-expert Fine-Tuning), a fine-grained PEFT framework that refines MoE adaptation from experts to sub-experts. NSFT decomposes each expert along the intermediate dimension into structured channel groups and selects task-relevant sub-experts by combining routing importance with intra-expert activation saliency. To optimize sparse partial updates, NSFT further introduces learning-rate scaling and dynamic gradient scaling to compensate for the reduced effective update magnitude. Experiments on OLMoE and Ling-mini-2.0 across challenging domain-specific tasks and general benchmarks show that NSFT consistently outperforms representative PEFT and expert-level sparse tuning baselines, while using substantially fewer trainable parameters and preserving competitive general capability. These results suggest that sub-expert-level adaptation is a more precise and efficient PEFT paradigm for MoE LLMs.

## Metadata
- **Published**: 2026-09-22T04:04:53Z
- **Authors**: Zhentao Tan, Chang Liu, Yao Liu, Yue Wu, Jieping Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25655v1)