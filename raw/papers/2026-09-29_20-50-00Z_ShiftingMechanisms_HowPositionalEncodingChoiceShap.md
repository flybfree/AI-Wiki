---
title: Shifting Mechanisms: How Positional Encoding Choice Shapes In-Context Retrieval
published: 2026-09-29T20:50:00Z
authors: Eric Enouen, Sainyam Galhotra
url: http://arxiv.org/abs/2609.38530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shifting Mechanisms: How Positional Encoding Choice Shapes In-Context Retrieval

## Abstract
Language models increasingly use architectures that vary attention span and positional encoding across layers, such as applying RoPE with sliding-window attention and NoPE with global attention (SWA NoPE). However, how these choices shape in-context retrieval remains unclear. To study this question, we take a mechanistic view, tracing how positional encoding (PE) choice shapes the internal mechanisms models use for in-context retrieval. Across 22 open-weight models spanning eight families, we find that standard RoPE models rely primarily on positional retrieval, while PE hybrids shift toward semantic retrieval. We further show on a controlled pre-training ablation that confining positional encoding to local layers produces this semantic shift, degrading representations of positional information. Finally, we show that the reported long-context gains of PE hybrids mask a retrieval trade-off: SWA NoPE improves over RoPE on multiple-target retrieval and QA, but degrades when distinguishing competing keys. We show that these behavioral differences better track the mechanism shift from positional toward semantic mechanisms than a uniform improvement in long-context retrieval.

## Metadata
- **Published**: 2026-09-29T20:50:00Z
- **Authors**: Eric Enouen, Sainyam Galhotra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38530v1)