---
title: When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents
published: 2026-09-03T07:24:33Z
authors: Wen-Yu Chang, Yun-Nung Chen
url: http://arxiv.org/abs/2609.03467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents

## Abstract
Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems. However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage. We introduce LOCOMO-CONV, a conversa- tional memory benchmark derived from Lo- CoMo with four query styles: dialog, implicit, counterfactual, and composed. Across five rep- resentative memory systems, we evaluate both retrieval recall and end-to-end response qual- ity. Our experiments show that conversational framing exposes substantial retrieval gaps over- looked by QA benchmarks, especially on im- plicit and composed queries, which multi-facet query rewriting narrows for raw-turn mem- ory but not abstractive memory. We further find that strong retrieval does not fully trans- late into response quality, and that implicit queries exhibit silent grounding, where mem- ory improves contextual grounding without ex- plicitly surfacing the gold fact. These results point to reasoning-based memory elaboration as a promising direction, and we release aux- iliary supportive_memory annotations captur- ing conversationally useful context beyond the original gold evidence.

## Metadata
- **Published**: 2026-09-03T07:24:33Z
- **Authors**: Wen-Yu Chang, Yun-Nung Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03467v1)