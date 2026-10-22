---
title: Retrieval Augmented Generation Compositionality
url: http://arxiv.org/abs/2610.29722v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_13-30-29Z_RetrievalAugmentedGenerationCompositionality.md
generated_at: 2026-10-21 23:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the individual performance gains of modern RAG pipeline components—such as embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification—actually compose when combined into a full system. The authors introduce LASAGNA, an open-source framework for controlled RAG evaluation, and test 450 configurations across eight benchmarks with corpora ranging from 5K to 200K documents. Their central finding is that isolated gains from individual techniques are unreliable predictors of end-to-end performance, and that optimal pipeline configurations shift as corpus scale increases.

## Key Takeaways
- Individually strong retrieval techniques do not compose additively: three techniques that each predicted a combined +47% improvement delivered only +17% when used together, demonstrating that interaction effects between pipeline stages can severely diminish expected gains and that researchers must evaluate full stacks rather than isolated components.
- Retrieval quality and answer faithfulness are not aligned objectives within a RAG pipeline: component gains stack differently for these two metrics, meaning that optimizing for better retrieval can actively degrade faithfulness, and vice versa, creating a fundamental design tension that practitioners must navigate explicitly rather than assuming a single configuration serves both goals.
- The optimal RAG configuration is corpus-size-dependent: the combination of techniques that performs best on a small corpus (5K documents) may no longer be the best choice at larger scales (200K documents), implying that benchmark results from small-scale evaluations cannot be safely extrapolated to production deployments with large document collections.

## Context
Modern RAG systems have evolved into complex multi-stage pipelines where each component is developed and evaluated in isolation by different research groups, creating a fragmented evidence base about what actually works in practice. This paper addresses a critical methodological gap in the RAG literature: the near-universal practice of ablation studies that measure single-component improvements without testing whether those gains survive interaction with the rest of the pipeline. By pre-declaring hypotheses and running 450 controlled configurations, the authors provide a rare systematic study of compositionality in RAG systems, a problem analogous to the well-known challenges of combining techniques in other multi-stage ML pipelines.

## Implications
For practitioners deploying RAG systems in production, this work warns against naively stacking individually validated techniques and instead demands end-to-end evaluation on realistic corpus scales before committing to a pipeline architecture. For the research community, the authors call for a new standard of testing new RAG techniques within the full surrounding stack rather than in isolation, and they supply LASAGNA as an open-source tool to make such comprehensive experiments more accessible. Industry teams building retrieval systems should treat corpus-size sensitivity as a design constraint, re-validating their chosen configuration whenever document collections grow significantly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29722v1)
