---
title: EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory
published: 2026-09-25T22:28:53Z
authors: Bhavyateja Potineni, Lohit Giri, Anu Jain, Vadim Kutsyy, Rajasekhar Pentakota
url: http://arxiv.org/abs/2609.32049v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory

## Abstract
As autonomous LLM agents are deployed across multi-session environments, conventional memory architectures suffer from Associative Blindness (inability to traverse multi-hop relational dependencies), Scaffolding Amnesia (temporal decay evicting core persona invariants), and Static Topology Stagnation (immutable graphs ignoring usage dynamics). Grounded in Complementary Learning Systems (CLS) principles, we propose EngramRAG, an adaptive memory architecture coupling a low-latency Waking State reflex with an asynchronous background Dreaming State consolidation cycle. EngramRAG introduces: (1) Usage-Modulated Personalized PageRank (U-PPR), where transition probabilities adapt via Hebbian plasticity to promote persistent entities into high-centrality Epistemic Macro-Hubs; (2) Consolidation-Activated Topology Decay (CATD), which scales retention half-life by topological load-bearing weight rather than wall-clock recency, protected by a cold-start grace period (N_grace >= 4); (3) Directed SUPERSEDES DAG filtering to suppress obsolete state during fact mutations; and (4) Triple-source hybrid retrieval fusing dense vectors, BM25, and U-PPR via dynamic Reciprocal Rank Fusion (RRF). Evaluating on all 1,982 QA pairs across 10 long-term conversations in the LoCoMo benchmark, EngramRAG achieves +38.9% relative improvement in Recall@5 (53.21% vs. 38.29%, p < 0.001) and +43.1% in MRR (0.4203 vs. 0.2937) over dense vector RAG, significantly outperforming Okapi BM25 (48.66%) and isolated static graph retrieval (8.50%). On temporal reasoning, EngramRAG reaches 62.33% Recall@5 (+16.67 points over dense vectors). In controlled mutation tests, SUPERSEDES suppresses split-brain hallucinations from 70.0% to 0.0%, while 90-day simulations show 100.0% scaffolding retention under a 26.21ms interactive retrieval reflex.

## Metadata
- **Published**: 2026-09-25T22:28:53Z
- **Authors**: Bhavyateja Potineni, Lohit Giri, Anu Jain, Vadim Kutsyy, Rajasekhar Pentakota
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32049v1)