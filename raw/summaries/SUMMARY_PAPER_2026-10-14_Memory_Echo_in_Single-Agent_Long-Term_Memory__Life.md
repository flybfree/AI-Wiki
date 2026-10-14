---
title: Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation
url: http://arxiv.org/abs/2610.17763v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_05-44-32Z_MemoryEchoinSingle_AgentLong_TermMemory_LifecycleE.md
generated_at: 2026-10-14 00:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies and formalizes a phenomenon called "Memory Echo," where a single historical claim from one source accumulates multiple retrieval positions in an agent's long-term memory, artificially inflating its influence on current answers without independent corroborating evidence. The authors introduce MEchoBench to evaluate how this echo effect emerges, resists correction, persists over time, and contaminates agent decisions. They propose the Family-Provenance-Authority (FPA) framework, which deduplicates records by source family, gates old records behind verified corrections, and constrains final answers to authoritative evidence, yielding substantial accuracy improvements across multiple memory frameworks.

## Key Takeaways
- Memory Echo is defined as the excess retrieval exposure gained by historical information from the same source without additional independent evidence. This phenomenon is motivated by social cognition and memory psychology research on repeated exposure, retrieval, and revision, and it represents a previously underexplored failure mode distinct from standard retrieval or updating errors in agent memory systems.
- The FPA framework addresses Memory Echo through three mechanisms: selecting one representative record per source family to prevent same-source accumulation, conditioning the eligibility of old records on verified corrections to combat post-correction persistence, and constraining final answers with authoritative evidence. In paired replay experiments on 190 fixed questions across four memory frameworks, FPA raised accuracy from 0.825 to 0.920 with DeepSeek V4 Flash and from 0.782 to 0.916 with Kimi K2.6, while reducing mean Decision Contamination Effect from roughly 0.106–0.109 down to 0.030–0.038.
- MEchoBench provides a benchmark specifically targeting the lifecycle of memory echo—its emergence, correction resistance, persistence, and downstream effect on answers—filling a gap left by existing work that focuses on retrieval, updating, and question answering without examining same-source record accumulation or post-correction persistence.

## Context
As large language model agents increasingly rely on persistent long-term memory to maintain coherence across sessions, the integrity of retrieved information becomes a critical reliability concern. Prior research has concentrated on retrieval accuracy, memory updating strategies, and question-answering performance, but has largely overlooked how a single source can proliferate across memory stores and create a false sense of evidential consensus. This paper bridges memory psychology insights about repeated exposure and revision with practical agent architecture design, addressing a failure mode that can silently degrade decision quality in deployed systems.

## Implications
For practitioners building agent systems with persistent memory, Memory Echo represents a subtle but high-impact failure mode: a single outdated or incorrect claim can dominate retrieval results simply because it has been written back multiple times, not because it is well-supported. The FPA framework offers a concrete, implementable mitigation strategy that preserves traceable history while preventing redundant historical information from governing current decisions, making it directly applicable to production agent deployments. The public availability of MEchoBench and the accompanying code provides the community with a standardized tool to audit and harden memory pipelines against this class of contamination errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17763v1)
