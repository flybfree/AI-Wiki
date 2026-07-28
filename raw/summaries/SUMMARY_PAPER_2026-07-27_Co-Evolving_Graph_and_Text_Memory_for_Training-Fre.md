---
title: Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering
url: http://arxiv.org/abs/2607.23278v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_16-29-38Z_Co_EvolvingGraphandTextMemoryforTraining_FreeMulti.md
generated_at: 2026-07-27 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Co-E, a training-free multi-hop question answering system that synchronizes bidirectional graph and textual memories to enable reasoning across relational and textual evidence without fine‑tuning. Evaluated on six benchmarks, Co-E outperforms comparable open‑backbone baselines and matches larger or trained models.

## Key Takeaways
- The system maintains two working memories—one for text and one for a knowledge graph—that are updated in each synchronization cycle.
- Relational triples extracted from the textual memory are inserted into the graph memory, creating a closed loop that feeds both retrieval and generation.
- This training‑free design eliminates the need for continual reconciliation between graph updates and new query contexts.

## Context
The work addresses a longstanding challenge in multi-hop QA: integrating heterogeneous knowledge sources without retraining large models. By treating graph and text as co‑evolving memories, Co-E offers a novel paradigm that could simplify deployment of reasoning agents.

## Implications
For industry practitioners, this approach reduces the complexity of building and maintaining external knowledge bases while preserving answer quality. Practitioners can adopt Co‑E to enhance chatbots or search assistants with richer, up‑to‑date information without costly fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23278v1)
