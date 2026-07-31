---
title: Metaphor Tracer: A Theory-Informed Analysis of Hidden States
url: http://arxiv.org/abs/2607.28434v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-12-13Z_MetaphorTracer_ATheory_InformedAnalysisofHiddenSta.md
generated_at: 2026-07-30 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Metaphor Tracer, a theory‑informed framework that interprets hidden states from a single forward pass of language models as evidence for two properties: an aggregator and a differentiator. It demonstrates that the aggregator scores token positions by their role in consolidating the text’s structure, while the differentiator tracks transient metaphorical or semantic carryover across tokens.

## Key Takeaways
- The aggregator is not a conventional information measure; it remains stable for repeated signifiers yet marks a token’s place within the specific text.  
- Across unrelated models, the model that carries lexical type transfers reads singular discourse poorly, indicating that hidden states encode relational rather than essentialist meaning.  
- Ground‑truth validation comes from both an engineered register (6/6 cells) and psychoanalytic marking of clinical transcripts (34/36 cells), confirming the aggregator’s predictive power.

## Context
This work situates hidden‑state analysis within a broader effort to move beyond token‑level metrics toward understanding how models represent text structure. By linking model outputs to pre‑existing theoretical constructs, it offers a novel lens for evaluating representation quality without retraining.

## Implications
For practitioners, Metaphor Tracer suggests that fine‑tuning can improve textual fidelity by preserving the relational dynamics captured in hidden states rather than merely adjusting classification scores. The methodology could inform the design of interpretable AI systems where interpretability is as important as performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28434v1)
