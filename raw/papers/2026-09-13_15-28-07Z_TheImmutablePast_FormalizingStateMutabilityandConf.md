---
title: The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG
published: 2026-09-13T15:28:07Z
authors: Hamed HaddadPajouh, Amir AmiriTabat
url: http://arxiv.org/abs/2609.16073v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG

## Abstract
Retrieval-Augmented Generation (RAG) serves as the primary memory architecture for long-horizon autonomous agents. However, treating shared memory as an append-only stream introduces \textit{Semantic Shadowing}, a critical failure mode where conflicting historical observations accumulate and statistically dominate valid recent updates. In dynamic environments, this results in severe state divergence as agents retrieve and act upon obsolete facts. This paper formalizes the mechanics of State Mutability to prove that standard dense retrieval suffers from Asymptotic Recall Decay. Furthermore, we formally demonstrate a Majority Vote Trap, revealing that increasing the retrieval context window paradoxically degrades generation accuracy by diluting the attention mechanism under conditions of semantic equivalence. To resolve this, we introduce GC-Mem (Garbage Collection for Memory), a strict inference-time consistency protocol. Unlike heuristic time-decay mechanisms---which indiscriminately destroy valid long-term memory---GC-Mem relies purely on a temporal dominance operator ($Φ_{\mathcal{T}}$) paired with contradiction detection to surgically excise shadowed context. Evaluated across a rigorous, behaviorally inferred benchmark of 137,760 memory chunks and continuous accumulation sweeps, standard RAG and timestamp re-ranking baselines experience severe degradation. In contrast, GC-Mem empirically recovers $>90\%$ conflict resolution accuracy. We establish strict precision and recall deployment thresholds, ensuring state convergence where standard mutable RAG fundamentally fails.

## Metadata
- **Published**: 2026-09-13T15:28:07Z
- **Authors**: Hamed HaddadPajouh, Amir AmiriTabat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16073v1)