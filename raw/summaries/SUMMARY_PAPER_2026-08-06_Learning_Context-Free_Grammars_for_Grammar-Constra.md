---
title: Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees
url: http://arxiv.org/abs/2608.05493v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_00-44-46Z_LearningContext_FreeGrammarsforGrammar_Constrained.md
generated_at: 2026-08-06 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Autogrammar, a declarative agent that automatically learns context‑free grammars from DSL documentation and execution traces to enforce syntax constraints during language model decoding. Experiments on three third‑party DSLs show that the generated grammars achieve near‑perfect precision on unseen data while reducing execution time by 3.8× without significant loss of accuracy, outperforming existing LM baselines and formal techniques.

## Key Takeaways
- Autogrammar learns context‑free grammars directly from execution data, making documentation optional for grammar generation.
- The generated grammars produce near‑perfect precision on unseen test sets while cutting runtime by 3.8× thanks to temporal constraints enforced via linear temporal logic.
- Grammar‑constrained decoding using these grammars improves end‑to‑end LM performance on eight of ten real tasks, matching or exceeding professional grammars.

## Context
This work addresses a longstanding challenge in AI‑assisted code generation where low‑resource DSLs hinder reliable model output. By automating grammar construction, the approach reduces reliance on manual linguistic expertise and aligns with broader trends toward self‑learning system components.

## Implications
For industry practitioners, Autogrammar offers a scalable way to enforce syntax without dedicated linguists, accelerating deployment of domain‑specific AI agents. The method also demonstrates that declarative constraints can be learned automatically, opening pathways for continuous improvement as execution data accumulates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05493v1)
