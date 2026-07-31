---
title: $Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems
url: http://arxiv.org/abs/2607.27958v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_10-05-50Z_Σ__Mem_AnOnlineReliabilityMemoryforLLM_basedMulti_.md
generated_at: 2026-07-30 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Σ‑Mem, an online reliability memory that records competence evidence for individual peers and the trustworthiness of peer relationships in LLM‑based multi‑agent systems. By updating these symmetric states from post‑decision correctness feedback, Σ‑Mem enables stable adaptation without retraining underlying models and delivers readouts that improve over traditional voting methods.

## Key Takeaways
- Σ‑Mem maintains both individual peer competence evidence and peer relationship evidence as real symmetric states that are updated from post‑decision correctness feedback.  
- The spectral change caused by each event‑level update is bounded using Weyl’s inequality, allowing stable online adaptation without retraining the models.  
- Direct memory readouts outperform majority voting and the best fixed peer over the full OOD evaluation set.

## Context
Reliability in long‑horizon LLM agents remains a challenge because existing memory systems focus on preserving interaction content rather than modeling trustworthiness. This work addresses that gap by introducing a structured, feedback‑driven memory that can be read and written online across diverse tasks and unseen peers.

## Implications
Σ‑Mem provides a reusable foundation for adaptive coordination in LLM‑based multi‑agent environments, enabling industries to build systems that continuously learn from correctness signals without costly retraining. Practitioners can leverage its write‑read interface to improve decision quality and scalability in complex collaborative AI setups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27958v1)
