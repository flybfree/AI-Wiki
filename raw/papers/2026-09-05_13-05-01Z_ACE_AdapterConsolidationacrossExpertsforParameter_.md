---
title: ACE: Adapter Consolidation across Experts for Parameter-Efficient Fine-Tuning of MoE LLMs
published: 2026-09-05T13:05:01Z
authors: Ahin Lee, Sehyun Yun, Joonha Park, Taesik Gong
url: http://arxiv.org/abs/2609.06072v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACE: Adapter Consolidation across Experts for Parameter-Efficient Fine-Tuning of MoE LLMs

## Abstract
Parameter-efficient fine-tuning (PEFT) of mixture-of-experts (MoE) models commonly attaches a separate low-rank adapter to each expert. This expert-wise design fragments adaptation in three ways: capacity is split across narrow low-rank updates, gradient supervision becomes sparse and imbalanced under sparse routing, and execution is decomposed into many small GEMMs. We find that such expert-wise separation is often unnecessary, as subsets of LoRA adapters become functionally similar during fine-tuning, revealing redundancy among expert-specific adapters. Based on this redundancy, we propose ACE (Adapter Consolidation across Experts), which groups redundant experts and replaces their expert-specific adapters with group-shared higher-rank LoRA modules under the same PEFT budget. ACE further introduces grouped adapter execution, which consolidates fragmented expert-wise adapter computations into fewer, larger group-level GEMMs. Across evaluations covering 12 datasets and four MoE backbones, ACE achieves the highest observed mean accuracy among the parameter-matched PEFT methods on the three backbones with complete baseline coverage, while providing $1.31\times$ to $1.48\times$ wall-clock training speedup over expert-wise LoRA without increasing peak memory. Our code is available at https://github.com/UbiquitousAILab/ACE.

## Metadata
- **Published**: 2026-09-05T13:05:01Z
- **Authors**: Ahin Lee, Sehyun Yun, Joonha Park, Taesik Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06072v1)