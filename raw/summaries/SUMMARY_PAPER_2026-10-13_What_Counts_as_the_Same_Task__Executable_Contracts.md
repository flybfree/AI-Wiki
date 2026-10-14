---
title: What Counts as the Same Task? Executable Contracts for Robustness Evaluation of Tool-Using Agents
url: http://arxiv.org/abs/2610.14477v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_02-18-56Z_WhatCountsastheSameTask_ExecutableContractsforRobu.md
generated_at: 2026-10-13 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical flaw in how robustness evaluations of tool-using agents validate perturbed test cases: current methods rely on weak heuristics such as embedding-space proximity or well-formedness checks, which can both admit invalid edits that fundamentally alter the task and reject legitimate adversarial perturbations. The authors propose "executable task contracts"—formal specifications that define which facts constitute a task, which edits are permissible, and what constitutes successful completion—and demonstrate through analysis of 14,336 stored agent runs that existing validity rules systematically misclassify test cases, producing misleading vulnerability assessments.

## Key Takeaways
- Embedding-based validity rules are fundamentally unreliable for distinguishing task-preserving edits from task-altering ones: across four different encoders tested, embedding thresholds permitted 75–100% of edits that genuinely changed the task (such as swapping the payee on an invoice) while simultaneously rejecting 24–45% of valid hostile-note perturbations that should have been accepted as legitimate adversarial tests.
- The false-positive/false-negative pattern produces distorted agent vulnerability profiles: using a MiniLM cosine similarity threshold, the Mistral model appeared vulnerable on all 64 evaluation tasks, yet only 26 of those tasks contained a genuinely valid successful attack, meaning roughly 60% of the apparent vulnerabilities were artifacts of the flawed validity check rather than real agent weaknesses.
- Alternative ad-hoc strategies such as replaying a saved solution or permitting edits to benchmark metadata fields exhibit failure modes similar to embedding thresholds, confirming that no simple heuristic can substitute for a principled, executable specification of what constitutes the same task.

## Context
As tool-using agents are increasingly deployed in high-stakes domains such as finance, legal document processing, and customer service, robustness evaluations that perturb inputs (e.g., inserting adversarial notes into invoices) have become standard practice for measuring agent reliability. However, the field has largely assumed that any syntactically valid or embedding-close perturbation automatically constitutes a fair test of the original task, without formally verifying that the perturbed instance still exercises the same underlying capability. This paper addresses that gap by formalizing task identity as a checkable contract, contributing to the broader effort in AI evaluation science to make benchmarking methodology as rigorous as the models being evaluated.

## Implications
For practitioners building agent evaluation pipelines, this work signals that current robustness scores may be substantially inflated or deflated depending on the validity rule chosen, meaning published vulnerability rankings across models could be unreliable artifacts of evaluation methodology rather than true capability differences. For the research community, the executable task contract framework provides a concrete, implementable standard that evaluation suites can adopt to ensure perturbed test cases genuinely stress the intended task, which is essential before agent robustness claims are used to guide deployment decisions, regulatory compliance, or model selection in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14477v1)
