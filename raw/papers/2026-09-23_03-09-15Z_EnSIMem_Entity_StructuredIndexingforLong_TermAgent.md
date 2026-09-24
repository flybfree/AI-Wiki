---
title: EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory
published: 2026-09-23T03:09:15Z
authors: Xuanyu Meng, Xing Fan, Xinyi Fan, Chenlei Guo, Yixuan Xie, Jiawei Han
url: http://arxiv.org/abs/2609.27279v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory

## Abstract
An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes interactions into theme-coherent episodes and builds dialogue-grounded index entries of the form [entity][entity type][property:value]. Each entry preserves its source turns, temporal information, and available multimodal fields. During online interaction, the agent's request is decomposed into evidence requirements whose properties are aligned with the memory index. Entity-property lookup and adaptive retrieval then collect the evidence needed for point, temporal, compositional, and aggregation reasoning. The agent generates its response from the preserved source evidence rather than from lossy memory summaries. On long-term agent-memory benchmarks, EnSIMem achieves high answer accuracy while maintaining compact contexts and favorable online efficiency. These results show that entity-structured indexing and episode-level provenance provide a reliable foundation for long-term memory in agents. The code of our model is available at https://github.com/RamonMeng/EnSIMem.

## Metadata
- **Published**: 2026-09-23T03:09:15Z
- **Authors**: Xuanyu Meng, Xing Fan, Xinyi Fan, Chenlei Guo, Yixuan Xie, Jiawei Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27279v1)