---
title: A Triple-Robustness Analysis of Retrieval-Augmented Generation for Multi-Hop Requirements Traceability
url: http://arxiv.org/abs/2608.00705v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_15-05-45Z_ATriple_RobustnessAnalysisofRetrieval_AugmentedGen.md
generated_at: 2026-08-03 20:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts a triple‑robustness analysis of Retrieval‑Augmented Generation (RAG) by fixing the five‑pipeline architecture and systematically varying embedder, corpus, and judge across 5 000+ judgments. The study resolves prior disagreements between GraphRAG and vector RAG by showing that citation quality depends on which component is measured. Results reveal that GraphRAG’s graph walk floods context windows while its synthesizer cites selectively, and that faithfulness varies with query hop distance and corpus type.

## Key Takeaways
- GraphRAG’s precision‑0.12 to 0.23 graph walks cause citation sets to be inflated at low recall, but the synthesizer’s selective citations raise precision to 0.48–0.65, flipping ranking when attribution is defined by retrieved set versus citation quality.  
- Answer‑level citation winners are corpus and stratum conditional yet embedder robust: GraphRAG ties vanilla on short‑hop DO‑178C queries but dominates MuSiQue strata; agentic pipelines succeed only on 3‑plus hop requirements.  
- Faithfulness is corpus‑conditional: it declines with hop distance on DO‑178C (p < 0.05 in most judge‑embedder combos) while Wikipedia chains show no collapse, and single‑judge LLM reliability drops sharply over time.

## Context
The paper addresses a longstanding debate about RAG performance by exposing that results are not universal but hinge on specific retrieval‑generation pipelines and measurement points. By isolating embedders, corpora, and judges, it provides a methodological benchmark for evaluating claims of superiority in AI systems.

## Implications
For practitioners, the findings stress that architecture rankings must be validated across diverse components to avoid overstated performance. Industry stakeholders should adopt triple‑robustness testing as a standard practice before deploying RAG solutions in safety‑critical domains like DO‑178C requirements traceability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00705v1)
