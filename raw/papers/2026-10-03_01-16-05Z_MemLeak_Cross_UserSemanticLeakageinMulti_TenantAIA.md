---
title: MemLeak: Cross-User Semantic Leakage in Multi-Tenant AI Agent Memory
published: 2026-10-03T01:16:05Z
authors: Priyanka Mudgal, Kai Zhao, Guilin Zhang, Andy Olsen, Ezekiel Miller, Xu Chu, Aletta Johanna Blanken
url: http://arxiv.org/abs/2610.04195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemLeak: Cross-User Semantic Leakage in Multi-Tenant AI Agent Memory

## Abstract
Personal AI agents in enterprise multi-tenant deployments share a common vector store for long-term memory. Shared embedding spaces create a surface for cross-user memory leakage: a user's query can retrieve semantically adjacent memories belonging to another user through ordinary cosine-similarity retrieval, without any exploit. We formalize this as cross-user admissibility failure and evaluate it across six experiments, plus follow-up ablations, under both sparse (TF-IDF) and production-faithful (MiniLM-L6-v2) retrieval. Non-adversarial, incidental leakage reaches 70--100\% under pooled {same-team} retrieval; adversarially crafted memories achieve 90--100\% top-$k$ placement, exceeding weaker keyword-based attacker baselines, with score lifts of $+0.416$ to $+0.511$ under production-faithful dense retrieval (Config B); and end-to-end response contamination reaches 5.00/5 under a production retrieval path and 4.67/5 with Claude Sonnet~4.5, with contaminated responses often scoring as helpful or more helpful than clean ones, a gap validated against human judgment. Among three architectural mitigations, only hard post-retrieval ownership gating consistently restores the clean baseline (1.00/5) across {two generation models, at a measured latency overhead of roughly 1.4~ms per query.

## Metadata
- **Published**: 2026-10-03T01:16:05Z
- **Authors**: Priyanka Mudgal, Kai Zhao, Guilin Zhang, Andy Olsen, Ezekiel Miller, Xu Chu, Aletta Johanna Blanken
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04195v1)