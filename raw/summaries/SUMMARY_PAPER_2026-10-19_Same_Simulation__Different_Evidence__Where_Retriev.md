---
title: Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy
url: http://arxiv.org/abs/2610.26836v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_17-57-41Z_SameSimulation_DifferentEvidence_WhereRetrievedToo.md
generated_at: 2026-10-19 23:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how context-management strategies in LLM agent harnesses—specifically, retrieving long tool outputs via a section index rather than inlining them in the context window—affect agent accuracy. Using PHREEQC, a USGS geochemistry simulator with reports up to 846.8k characters, the authors demonstrate that GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 accuracy points under retrieval-based access, while Claude models show no detectable degradation. The core failure mode identified is "evidence substitution," where agents skip the authoritative simulator report and instead answer from their own higher-precision intermediate files, misrounding to a neighboring multiple-choice option.

## Key Takeaways
- Retrieval-based context management introduces a specific failure mode called "evidence substitution": agents compute the correct keyed value at roughly the same rate as before, but then skip the authoritative simulator report and answer from their own higher-precision output files, misrounding to a neighboring option. This means the accuracy loss is not a computation failure but an evidence-use failure, which is a fundamentally different problem than model capability limitations.
- The accuracy cost is model-dependent: GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 points respectively when reading PHREEQC reports through a section index rather than in context, while Claude Opus 4.6 and Claude Sonnet 4.6 show no detectable cost. For GPT-5.4, more frequent correct simulations mask an evidence-use loss of about ten points, producing a net change indistinguishable from zero—highlighting how aggregate accuracy metrics can hide underlying degradation.
- Mitigation strategies exist but are model-specific: explicitly naming the authoritative output file raises accuracy by 6.3–7.9 points over plain retrieval for the three GPT models, and inlining outputs that fit the context window works as well for GPT-5.1 and GPT-5.2. However, simply asking the agent to perform correct rounding does not resolve the problem, indicating the issue is structural rather than a prompting deficiency.

## Context
This work sits at the intersection of agentic AI systems, tool-augmented reasoning, and context-window management—areas that are increasingly central to production LLM deployments. As agent harnesses grow to handle long-running scientific, engineering, and data-analysis workflows, they routinely offload large tool outputs to files and rely on retrieval mechanisms to keep context windows manageable. The paper provides one of the first controlled, execution-verified studies isolating the accuracy cost of this architectural choice, using a deterministic scientific simulator to trace every printed value and distinguish computation errors from evidence-use errors.

## Implications
For practitioners building agentic pipelines around scientific simulators, database queries, or any tool producing large structured outputs, this paper argues that context-management decisions must be evaluated by diagnosing where accuracy is lost—computation versus evidence selection—rather than by aggregate accuracy scores alone. The finding that naming authoritative outputs or inlining manageable outputs can recover most of the lost accuracy offers concrete, actionable guidance for harness designers, while the model-dependent nature of the degradation warns against assuming a single retrieval strategy is safe across all frontier models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26836v1)
