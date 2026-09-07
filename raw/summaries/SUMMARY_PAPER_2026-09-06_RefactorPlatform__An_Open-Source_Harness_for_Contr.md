---
title: RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents
url: http://arxiv.org/abs/2609.04898v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-58-10Z_RefactorPlatform_AnOpen_SourceHarnessforControlled.md
generated_at: 2026-09-06 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RefactorPlatform, an open‑source evaluation harness designed to isolate the design choices that affect repository‑scale refactoring agents. Experiments on 100 multi‑file tasks across four model families reveal that AST‑aware chunking improves performance by 25‑30% compared with naive token‑window methods, while retrieval‑augmented approaches can match or exceed baseline costs despite higher token usage.

## Key Takeaways
- AST‑aware chunking yields a 25‑30% performance boost over naive token‑window chunking across all prompt modes.  
- Retrieval‑augmented single agents achieve 86% success, outperforming sub‑agent configurations that reach only 66%, with no degradation in cost per successful refactoring.  
- Naive retrieval methods fall below the baseline, indicating that retrieval can be detrimental when not aligned with task requirements.

## Context
Repository‑scale refactoring remains a critical challenge for AI coding assistants because it demands precise propagation of changes across interdependent codebases without functional regression. Existing evaluations lack systematic isolation of design variables such as model backbones or prompt specificity, limiting reproducible insights into what truly drives success.

## Implications
RefactorPlatform provides a standardized framework that enables researchers and practitioners to audit, reproduce, and iterate on refactoring‑agent designs with confidence. By quantifying the impact of specific architectural choices, it guides more efficient deployment strategies in industry where cost and reliability are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04898v1)
