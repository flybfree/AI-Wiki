---
title: Janus: An Algorithm-Evaluator Co-Evolution Framework for LLM-Driven Discovery under Expensive Evaluation Budgets
url: http://arxiv.org/abs/2608.08189v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_15-31-12Z_Janus_AnAlgorithm_EvaluatorCo_EvolutionFrameworkfo.md
generated_at: 2026-08-10 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Janus, a framework that co‑evolves target programs and executable proxy evaluators using large language models to reduce the cost of expensive scientific evaluations. In experiments across five design tasks, Janus improves the area under the best‑so‑far curve by 99 % of a matched baseline while cutting real evaluations by 59.1 %.

## Key Takeaways
- Cheap surrogates are vulnerable to search‑induced distribution shift and hard to fit from sparse labels; Janus generates task‑specific evaluator programs from LLMs and calibrates them with real outcomes.
- Evolving evaluators alongside targets mitigates this shift through a promotion‑aligned objective, region‑conditioned portfolios, and online credit updates.
- Proxy predictions are used only for candidate prioritization; candidates must undergo real validation before entering the target population or updating the incumbent.

## Context
LLM‑driven discovery benefits from cheap feedback, yet many scientific tasks require high‑fidelity simulations or hardware runs that are costly. Existing methods either rely on fixed surrogates or lack mechanisms to keep them aligned with evolving targets, limiting performance under expensive evaluation budgets.

## Implications
This work demonstrates that trustworthy evaluator evolution can dramatically lower real‑world validation costs while preserving discovery quality, offering a scalable approach for industries where high‑fidelity testing is impractical. Practitioners can adopt Janus to balance speed and accuracy in LLM‑guided design processes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08189v1)
