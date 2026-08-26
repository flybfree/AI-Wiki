---
title: Retrieval-augmented generation vs. deterministic tax computation in multi-agent financial advisory: A 2x2 factorial experiment
url: http://arxiv.org/abs/2608.23908v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-23-02Z_Retrieval_augmentedgenerationvs_deterministictaxco.md
generated_at: 2026-08-25 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents a 2x2 factorial experiment comparing retrieval‑augmented generation (RAG) with a deterministic tax computation engine within a multi‑agent financial advisory system. The results show that the tax optimization engine significantly reduces tax savings by about 55 percentage points, while RAG alone yields modest improvements and does not interact meaningfully with the engine.

## Key Takeaways
- The custom capital gains calculation engine lowers overall tax savings to roughly half of what is achieved without it, indicating a substantial negative impact on portfolio performance.  
- Retrieval‑augmented generation provides only marginal benefit; its main effect is non‑significant and does not interact with the engine’s output.  
- The RAG‑only condition achieves the highest mean tax savings (47.7%), suggesting that pre‑trained language models can already perform competent tax‑loss harvesting recommendations without explicit tooling.

## Context
The study contributes to AI research by testing how specialized computation tools interact with large language models in real‑world advisory workflows, highlighting the complexity of integrating domain‑specific logic into generative systems. It aligns with broader efforts to balance LLM capabilities with precise financial calculations for accurate tax advice.

## Implications
For practitioners, the findings caution against assuming that adding computational engines will always improve outcomes and may instead create conflicting optimization signals. This underscores the need for careful evaluation of tool integration in AI‑driven advisory services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23908v1)
