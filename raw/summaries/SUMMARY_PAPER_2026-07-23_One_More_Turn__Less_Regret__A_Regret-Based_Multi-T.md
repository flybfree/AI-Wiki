---
title: One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies
url: http://arxiv.org/abs/2607.21143v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
generated_at: 2026-07-23 22:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RegretBench, a multi‑turn benchmark that evaluates how language models handle ambiguous user requests by measuring the regret they incur relative to an optimal clarification policy. The study shows that simply achieving high accuracy is not enough; models must ask the right question at the right time and stop when the user’s intent becomes clear. Experiments on open‑domain QA and product recommendation tasks reveal differences in efficiency, robustness, and stopping decisions among models with comparable performance.

## Key Takeaways
- RegretBench treats clarification as a sequential decision problem that depends on timing, question choice, and stopping criteria rather than isolated query quality.  
- The hidden‑intent formulation of ambiguity allows the benchmark to track semantic state across turns, enabling evaluation of how well a model resolves user intent over multiple interactions.  
- Models can have similar final success rates yet differ markedly in interaction cost, effectiveness of clarification, and regret accumulation.

## Context
The rapid growth of conversational AI has highlighted that users often need follow‑up questions to achieve desired outcomes, making efficient clarification crucial for usability. Traditional benchmarks focus on single‑turn accuracy, which overlooks the nuanced trade‑offs between asking too many or too few clarifying queries. This paper addresses that gap by modeling clarification as a policy problem.

## Implications
For developers and practitioners, RegretBench provides a concrete metric to assess whether a model’s clarification strategy is truly useful rather than merely correct. It guides design choices around timing and specificity of follow‑up questions, ultimately improving user experience in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21143v1)
