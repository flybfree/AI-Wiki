---
title: Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems
published: 2026-08-12T10:05:29Z
authors: Natchanon Pollertlam, Witchayut Kornsuwannawit
url: http://arxiv.org/abs/2608.11879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems

## Abstract
Long-running conversational agents increasingly rely on a memory system to avoid resending the whole conversation each turn, yet how much that costs to serve has received little systematic benchmarking. We compare three memory systems (Mem0, Hindsight, and Mastra Observational Memory) against two reference strategies -- a fixed-size rolling window and resubmitting the full transcript -- across two backbones and conversations of up to 400 turns, pairing every cost measurement with answer accuracy on 665 LoCoMo questions. First, a memory system's serving cost cannot be predicted from conversation length and message size alone: a regression that tracks the two reference strategies closely misses the memory systems by 18-69%, their cost driven instead by internal memory behavior. Second, a break-even analysis shows that whether -- and when -- a memory system becomes cheaper to serve than the full transcript is highly sensitive to the system and the backbone, from the first tens of turns for the cheapest to never within 400 turns for the most expensive. Third, no system wins on both axes: accuracy spans 21-54%, and the backbone choice drives cost as much as the memory system does.

## Metadata
- **Published**: 2026-08-12T10:05:29Z
- **Authors**: Natchanon Pollertlam, Witchayut Kornsuwannawit
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11879v1)