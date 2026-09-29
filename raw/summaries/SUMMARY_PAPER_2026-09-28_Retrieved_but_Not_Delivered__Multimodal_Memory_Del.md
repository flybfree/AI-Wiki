---
title: Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents
url: http://arxiv.org/abs/2609.32590v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_13-05-56Z_RetrievedbutNotDelivered_MultimodalMemoryDeliveryf.md
generated_at: 2026-09-28 20:45
model: qwen3.6-35b-a3b
---

## Summary
This paper identifies and formalizes "delivery" as a critical, previously unexamined stage in multimodal memory systems for long-term agents, focusing on how retrieved information is actually transmitted to the model before answer generation. Through controlled experiments, the authors demonstrate that preserving original modalities, assigning clear identities, and providing temporal context significantly outperforms traditional retrieval optimization. Their proposed DeliverMem framework achieves state-of-the-art performance across established benchmarks without requiring any training or modifications to stored memory records.

## Key Takeaways
- Delivery of retrieved memory has a substantially larger impact on agent accuracy than improving retrieval precision alone, with delivering original pixel data boosting performance by 13.87 points compared to just 2.31 points for perfect retrieval.
- DeliverMem structures delivery through three core decisions: preserving the original modality, assigning readable identities to memory items, and specifying when each item was encountered, alongside a lightweight adapter to handle missing properties.
- The framework consistently outperforms existing state-of-the-art memory agents on both MemLens and DMV-Bench across all context lengths, achieving superior results while drastically reducing input overhead by up to 70 times without any training or record modifications.

## Context
As multimodal AI agents increasingly rely on long-term memory to maintain continuity and contextual awareness, research has heavily prioritized storage efficiency and retrieval accuracy. However, the intermediate step of how retrieved data is formatted and transmitted to the language model has remained largely unexamined in standard evaluation pipelines. This paper addresses that gap by isolating delivery as a distinct optimization target within the agent memory lifecycle, revealing that current benchmarks conflate retrieval quality with presentation fidelity.

## Implications
Practitioners building long-term multimodal agents should prioritize interface design between retrieval modules and generation models, ensuring raw modalities and metadata are preserved rather than heavily compressed or abstracted. System architects can adopt DeliverMem’s zero-training approach to immediately enhance performance across varying backbone sizes without retraining infrastructure or altering database schemas. Ultimately, this work shifts the field toward holistic memory pipeline optimization, emphasizing that what reaches the model matters as much as what is stored or retrieved.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32590v1)
