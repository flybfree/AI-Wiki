---
title: KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems
published: 2026-07-27T10:51:38Z
authors: Shuo Wang, Fang Xi, Wenyuan Huang, Qing Wang, Junming Su
url: http://arxiv.org/abs/2607.24260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems

## Abstract
Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serialized into a prompt, the backend observes only a flat token sequence, forcing dense and uniform consumption of the full key-value (KV) state during decoding. We term this architectural mismatch the Knowledge Selection-Runtime Consumption (KSRC) gap: richer contexts enlarge the full-prompt KV footprint and decode-time memory traffic, increasing latency and degrading throughput even when reasoning depends on only a small fraction of the context. To bridge the gap, we propose Knowledge Access Planning (KAP), a paradigm-shifting execution abstraction that elevates structured knowledge priors from passive prompt-construction hints into first-class physical execution artifacts. KAP establishes a universal intermediate representation (IR)-the runtime access plan-which compiles structured knowledge signals to govern physical KV access without altering logical prompt semantics, model weights, or training procedures. Through this IR, KAP shifts LLM serving from token-aware context consumption to plan-driven, knowledge-aware runtime consumption. We instantiate KAP with GraphSpec, a compiler-executor realization connecting structured knowledge selection to an LLM serving backend. We derive a phase-boundary model for the positive-speedup regime of plan-guided execution. Across 4K-128K long-context QA workloads, GraphSpec maintains answer quality comparable to full-context decoding while decoupling physical KV consumption from prompt length, reducing proposal-time KV access to 5.5% of source KV state at 128K, and fundamentally shifting the scaling trajectory of long-context generation.

## Metadata
- **Published**: 2026-07-27T10:51:38Z
- **Authors**: Shuo Wang, Fang Xi, Wenyuan Huang, Qing Wang, Junming Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24260v1)