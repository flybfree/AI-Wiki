---
title: FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos
url: http://arxiv.org/abs/2609.00377v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_21-09-22Z_FoldingAgent_InferringParametricOrigamiProceduresf.md
generated_at: 2026-09-01 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
FoldingAgent is an agentic framework that infers explicit parametric origami programs from demonstration videos. It uses a pre‑trained vision‑language model combined with specialized tools to simulate folding steps, check physical plausibility, and re‑plan actions when errors occur. The approach converts unstructured visual demonstrations into executable, physically plausible folding procedures.

## Key Takeaways
- FoldingAgent leverages a Vision‑Language Model equipped with geometric simulation, plausibility verification, visual retrieval, and self‑evaluation tools to transform video content into parametric folding programs.
- Unlike static crease pattern predictors, the agent operates sequentially and can re‑plan its actions, reducing compounding errors in multi‑step origami folds.
- The framework is evaluated on PurelandFold, a benchmark of diverse Pureland origami videos with ground‑truth geometry and action labels, showing successful conversion to executable folding procedures.

## Context
This work addresses the gap between human origami knowledge—primarily visual demonstrations—and computational methods that rely on structured parametric representations. By integrating VLM reasoning with specialized simulation tools, FoldingAgent demonstrates a path toward more flexible, error‑resilient origami generation in AI.

## Implications
For researchers, FoldingAgent opens avenues to create generative models that can handle unstructured input and produce executable plans without pre‑defined crease patterns. In industry, it could enable automated design of paper structures for crafts, packaging, or medical origami, reducing manual planning effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00377v1)
