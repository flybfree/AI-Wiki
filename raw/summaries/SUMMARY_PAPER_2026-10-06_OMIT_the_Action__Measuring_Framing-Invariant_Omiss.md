---
title: OMIT the Action: Measuring Framing-Invariant Omission Bias under Philosophical Disagreement
url: http://arxiv.org/abs/2610.07847v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_06-54-19Z_OMITtheAction_MeasuringFraming_InvariantOmissionBi.md
generated_at: 2026-10-06 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces OMIT, a benchmark for measuring omission bias in LLMs under framing-sensitive moral conflicts. It constructs 218 paired-frame scenarios across 10 conflict types using disagreement patterns from a five-perspective philosophical persona panel, then evaluates eight LLMs and four inference-time interventions. The main findings are that omission bias is widespread, tends to decrease as model size increases within model families, and can be reduced by prompting models to consider moral principles before answering, though such mitigation may also increase action-biased responses.

## Key Takeaways
- OMIT operationalizes omission bias as a framing-invariant evaluation problem by pairing scenarios so that equivalent framings reverse substantive outcomes, allowing researchers to test whether models prefer inaction inconsistently rather than making stable moral judgments.
- The benchmark is built from philosophical disagreement across utilitarianism, deontology, virtue ethics, care ethics, and contractualism, which broadens the evaluation beyond simple utilitarian-deontological conflicts and captures more complex moral disagreement patterns.
- Evaluating eight LLMs shows that omission bias is pervasive but inversely correlates with model size within families, and interventions that encourage principle-based reasoning before yes/no decisions reduce omission bias and improve frame consistency, while sometimes shifting models toward action bias.

## Context
As LLMs are increasingly used for moral reasoning and decision support, small framing changes can reveal hidden preferences for inaction that may distort recommendations. Existing LLM evaluations have largely underexplored omission bias and often focus on narrow moral conflicts, so OMIT addresses a gap by using diverse philosophical perspectives to create framing-sensitive benchmarks. This matters because reliable moral evaluation requires testing whether model preferences remain stable when morally equivalent situations are described differently.

## Implications
For AI researchers, OMIT provides a methodology for using philosophical disagreement signals to evaluate framing-sensitive inaction preferences and to measure how mitigation strategies change model behavior. For practitioners building LLM-based advisory systems, the results suggest that prompting models to reason about moral principles before committing to a decision can reduce omission bias, but developers must monitor whether this creates new action-bias risks. Overall, the work supports more robust evaluation and safer deployment of LLMs in complex moral decision-making contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07847v1)
