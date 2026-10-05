---
title: APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory
published: 2026-10-01T20:51:45Z
authors: Chin-Lun Fu, Anagha Kulkarni, Hong Ni, Behrouz Madahian
url: http://arxiv.org/abs/2610.02472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory

## Abstract
Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity. We introduce APDMem (Agent-controlled Progressive Disclosure Memory), a hierarchical long-term memory architecture that applies progressive disclosure to memory retrieval. Rather than relying on a flat memory store or fixed retrieval granularity, APDMem represents conversation history as four progressively detailed layers: thematic summaries, personalized key facts, turn-level evidence notes, and raw messages. At inference time, a controller applies progressive disclosure to the memory hierarchy: it first reads high-level summaries and drills into finer evidence only when needed. This creates an adaptive cost-fidelity trade-off: simple queries can terminate early, while complex temporal, multi-hop, or exact-evidence queries trigger deeper inspection. A note synthesizer converts retrieved evidence into a query-focused structure that consolidates facts, orders events, and flags contradictions before final answer generation. Experiments on LongMemEval show that APDMem achieves strong performance for long-context memory reasoning while accessing only 8% of the total conversations.

## Metadata
- **Published**: 2026-10-01T20:51:45Z
- **Authors**: Chin-Lun Fu, Anagha Kulkarni, Hong Ni, Behrouz Madahian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02472v1)