---
title: Context-Aware Distillation and Ablation for Text2DSL
url: http://arxiv.org/abs/2606.22578v1
type: paper-summary
date: 2026-06-22
source_paper: 2026-06-21_16-27-24Z_Context_AwareDistillationandAblationforText2DSL.md
generated_at: 2026-06-22 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces context‑aware distillation for Text2DSL, replacing prompt‑only generation with a teacher model operating under a structured context that includes BNF grammar, API specifications, and a closed identifier vocabulary. The approach yields a verified PolkitBench corpus of 10,073 natural‑language‑to‑Polkit‑rule pairs with near‑perfect validation scores, while ablation studies reveal that the full context (C7) is essential for high performance.

## Key Takeaways
- The new harder corpus collapses baseline mode accuracy to 58.5% and combined score to 0.252, whereas context‑enhanced mode retains near‑optimal scores of 97.4% syntax validity and 0.750 combined, showing structured context is a load‑bearing mechanism.
- The best absolute condition is the full context C7 across all metrics; partial conditions C5 (BNF + Vocabulary) and C6 (API + Vocabulary) both include the vocabulary, indicating its critical role.
- Shapley decomposition assigns the largest semantic‑quality effect to the vocabulary (+0.198), followed by API (+24.7 pp) and BNF (+22.3 pp).

## Context
The work advances automatic DSL generation by integrating formal language specifications into large language models, moving beyond simple prompt engineering toward verifiable, production‑grade outputs. This aligns with trends in AI safety and reliability, where model behavior must be constrained by domain constraints.

## Implications
For practitioners, this method provides a scalable pipeline to generate correct DSL code that passes both static and runtime checks, reducing errors in automated systems. In industry, it enables more trustworthy integration of natural‑language specifications into production pipelines, enhancing robustness and maintainability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.22578v1)
