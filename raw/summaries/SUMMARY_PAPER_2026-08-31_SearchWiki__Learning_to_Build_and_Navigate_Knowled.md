---
title: SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking
url: http://arxiv.org/abs/2608.29953v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_18-36-13Z_SearchWiki_LearningtoBuildandNavigateKnowledgeWiki.md
generated_at: 2026-08-31 21:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents SearchWiki, a framework that transforms raw corpora into a hierarchical, typed wiki and trains WikiResearcher-9B to retrieve information through multi‑turn tool use. Experiments on ViDoRe‑V3, FinanceBench, LoCoMo, LongMemEval, and PersonaMem‑v2 show the RL‑tuned model outperforms flat retrieval baselines and matches or exceeds larger external models.

## Key Takeaways
- SearchWiki builds a three‑layer wiki—document overviews, cross‑domain topic pages, and source records—to preserve document hierarchy.
- The WikiResearcher‑9B agent employs on‑policy reinforcement learning with a reward that balances answer correctness, retrieval quality, and trajectory efficiency.
- Benchmarks demonstrate the model surpasses same‑size untrained baselines and matches or exceeds larger external models.

## Context
This research tackles the limitation of flat retrieval‑augmented generation by integrating document structure into knowledge navigation. It shows that structured, hierarchical corpora can yield higher answer relevance than treating text as a bag of chunks.

## Implications
For AI applications needing deep reasoning over domain data, SearchWiki provides a scalable way to augment LLMs with navigable knowledge graphs. Practitioners can adopt the framework to improve search accuracy and reduce hallucinations in enterprise tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29953v1)
