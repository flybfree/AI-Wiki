---
title: Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents
published: 2026-08-30T06:55:59Z
authors: Ming Wu, Pengyuan Zhu
url: http://arxiv.org/abs/2608.29606v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents

## Abstract
Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing structure (a fact store, a vector index, or a knowledge graph) and inherit its blind spots. We present Agent Zero Memory, a provenance-aware long-term memory system that distils a user's conversations, files, and connected sources into three parallel memory systems, each capturing a different facet of the same history: an episodic Memory Events timeline that makes when and what changed first-class, an associative entity-event knowledge graph that links people and projects across sessions, and a semantic, curated, citation-locked Hierarchical Documentary Memory (HDM) of durable facts. A retrieval turn runs an intent gate (so self-contained turns add no latency), a source router, and three concurrent agentic searches, one per system, each a tool-using loop over hybrid (embedding + lexical) search under agent-controlled filters; their grounded, cited answers are integrated into one answer with a single confidence. We formalize the reading discipline: every learned item is a provenanced item carrying its origin, timestamp, and evidence pointer, and every answer is read under a citation lock, so it may cite only evidence its reader actually opened; fabrication is structurally excluded and the system abstains rather than guesses. On two public benchmarks the system sets a new state of the art: 95.60% on LongMemEval and 93.60% on LoCoMo, improving over the strongest prior systems by +0.73 and +1.10 points. A controlled study across eight backbone LLMs characterizes the accuracy-cost-latency frontier: accuracy varies by only 3.4 points while per-query cost varies by ~30x, with near-state-of-the-art quality at up to 20x lower cost per query, the signature of memory-driven, rather than model-driven, quality.

## Metadata
- **Published**: 2026-08-30T06:55:59Z
- **Authors**: Ming Wu, Pengyuan Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29606v1)