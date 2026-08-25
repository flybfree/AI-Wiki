---
title: The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning
published: 2026-08-24T14:48:31Z
authors: Matthew Perlman, Atharva Nijasure, James Allan
url: http://arxiv.org/abs/2608.23338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning

## Abstract
LoRA fine-tuning is standard for adapting LLMs to reranking, but it remains unclear where in the network task-specific relevance behavior is learned and what attention-level changes accompany that learning. Through ablation and attention experiments, we identify where LoRA attention updates to RankLLaMA improve performance and whether those gains coincide with interpretable relevance-oriented attention patterns such as lexical matching, rarity sensitivity, and query-document interaction. We find that given LoRA fine-tuned MLPs throughout the network, restricting LoRA attention updates to a compact mid-network region is sufficient for recovering over half of the performance gained by applying LoRA to all attention layers, and that omitting attention fine-tuning in this region hurts performance more than elsewhere in the network. Additionally, we show that regions where applying LoRA affects performance the most overlap with regions where fine-tuning increased attention to axiomatic IR features. Rarity sensitivity, document-query interaction, and several compositional features are highly correlated with gains in ranking performance. Our results support an interpretable, correlational account of how relevance-oriented behavior emerges during LoRA fine-tuning and point toward improved strategies for adapting rerankers.

## Metadata
- **Published**: 2026-08-24T14:48:31Z
- **Authors**: Matthew Perlman, Atharva Nijasure, James Allan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23338v1)