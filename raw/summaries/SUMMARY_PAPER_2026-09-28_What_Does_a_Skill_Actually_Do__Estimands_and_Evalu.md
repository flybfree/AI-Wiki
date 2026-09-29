---
title: What Does a Skill Actually Do? Estimands and Evaluation Validity for Tool and Skill Use in LLM Agents: A Critical Review
url: http://arxiv.org/abs/2609.33153v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_03-26-34Z_WhatDoesaSkillActuallyDo_EstimandsandEvaluationVal.md
generated_at: 2026-09-28 23:21
model: qwen3.6-35b-a3b
---

## Summary
This critical review examines the validity and ambiguity in evaluating tool and skill use within large language model agents. The authors argue that claims of performance improvements often conflate distinct concepts such as retrieval recall, success rate changes, or budget-constrained gains. By introducing an estimand-based framework across six axes—including treatment contrast, target population, outcome, budget constraint, summary measure, and identification assumptions—the paper clarifies what different study designs actually measure and provides a reporting checklist to standardize evaluation transparency.

## Key Takeaways
- Claims that a retriever or skill library "improves" an agent are frequently ambiguous; they may refer to retrieval recall, the change in success from enabling a library, a paired contrast restricted to triggered tasks, or efficiency gains under budget constraints, necessitating precise definitions for valid comparison.
- The review decomposes tool and skill designs along six analytical axes: treatment contrast, target population, outcome, budget constraint, summary measure, and identification assumptions, allowing researchers to explicitly distinguish between total effects of module deployment and budget-constrained efficiency metrics.
- Analytical counterexamples demonstrate that pairing on the task does not identify an invocation effect, paired gain measures protocol-specific discordance rather than the share of tasks with worsened outcomes, and comparisons across studies must account for differences in triggered subsets versus all-task outcomes to avoid misleading conclusions.

## Context
As LLM agents increasingly rely on external tools and reusable skills selected from vast libraries at runtime, the field faces challenges in comparing agent architectures and evaluation methodologies. The proliferation of diverse design choices and reporting standards has made it difficult to synthesize empirical results or determine whether observed gains stem from better retrieval, routing, or skill utility. This paper addresses a critical gap by providing a rigorous methodological lens to assess evaluation validity across the growing body of agent research.

## Implications
Researchers and practitioners must carefully distinguish between different evaluation metrics when interpreting agent performance, as total deployment effects answer fundamentally different questions than budget-constrained efficiency. The proposed reporting checklist offers a practical tool for authors to communicate clear estimands, enhancing reproducibility and enabling meaningful comparisons across studies. Ultimately, adopting these distinctions will help the community avoid conflating retrieval quality with skill utility and ensure that claims of improvement are grounded in specific, well-defined experimental conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33153v1)
