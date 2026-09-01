---
title: Benchmark Contamination: A Taxonomy Organized by Defeated Mitigation
published: 2026-08-29T23:04:09Z
authors: Johanna Angulo, Víctor Yeste, Hector Espinos-Morato
url: http://arxiv.org/abs/2608.29463v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmark Contamination: A Taxonomy Organized by Defeated Mitigation

## Abstract
A benchmark score is a joint property of the model, the evaluation harness, the elicitation budget, the sampled population, and contamination status. Leaderboards publish the model and the score, so capability and leakage stay observationally equivalent. Existing taxonomies classify contamination for automated detection, not the question a reporter faces at publication: given the mitigations already applied, which validity threats remain open? We introduce a taxonomy organized by the mitigation each type defeats -- direct, derivative, temporal, distributional, and acquired -- spanning training-time and evaluation-time leakage. Holding out a private test set closes the first alone. The fifth is acquired during the evaluation itself; because it is a property of one run, it must be recorded with the reported score rather than with the benchmark release. We operationalize it as a four-field disclosure protocol in which "unknown" is a valid entry, released under CC BY 4.0 with a JSON Schema, a validator, and worked examples. Two coders external to the design team applied a pre-registered instrument to 41 documents. Per-variable linear-weighted $κ$ runs from 0.00 to 0.35 (median 0.21) over 29 main-pass documents against a single-coder test-retest ceiling of 0.84, collapsing under the class skew the registration anticipated; pooling raises it to 0.46 through chance correction rather than better agreement. Two variables fall below the prevalence-robust threshold registered in advance: strata reporting and the acquired type introduced here. Disagreement concentrates on when a variable applies rather than on what a document states. Elicitation budgets are reported in 13% of documents, and no document addresses all five types. The contribution is the taxonomy, the score-side artifact that follows from it, and a pre-registered measurement of instrument reliability and current disclosure.

## Metadata
- **Published**: 2026-08-29T23:04:09Z
- **Authors**: Johanna Angulo, Víctor Yeste, Hector Espinos-Morato
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29463v1)