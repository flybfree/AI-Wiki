---
title: PURPOSE: Poisoning Conflict Resolution in RAG via Proxy-Fact-Grounded Updates
url: http://arxiv.org/abs/2608.04756v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-23-24Z_PURPOSE_PoisoningConflictResolutioninRAGviaProxy_F.md
generated_at: 2026-08-05 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PURPOSE, a black‑box poisoning attack for Retrieval‑Augmented Generation that reframes the injection as a conflict‑minimizing update rather than a direct contradiction. Across three QA benchmarks, five generators, and three conflict‑resolution methods, PURPOSE achieves the highest attack success rate in 35 of 45 settings and exceeds prior attacks by nine point seven mean ASR points.

## Key Takeaways
- PURPOSE reframes poisoning as an update that minimizes conflict rather than a frontal contradiction.  
- The method extracts query‑related facts approximating the resolver’s possible reference to keep the injection consistent with what the resolver might verify.  
- Across diverse settings, PURPOSE attains the highest attack success rate and outperforms the strongest prior attack by nine point seven mean ASR points.

## Context
In AI systems that rely on external knowledge sources, poisoning attacks can corrupt outputs without being detected. This work demonstrates how subtle updates can bypass detection mechanisms in RAG pipelines.

## Implications
For practitioners, this shows conflict resolution is a vulnerable point that attackers can exploit to manipulate answers. It calls for more robust evaluation of resolver behavior against adversarial inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04756v1)
