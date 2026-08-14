---
title: Non-Degenerate Risk Certification for Automated Security Decisions: A Decision-Contract Theory with ATT\&CK-Aligned Triage as a Worked Instance
published: 2026-08-12T16:59:19Z
authors: Zhenpeng Li
url: http://arxiv.org/abs/2608.12444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Non-Degenerate Risk Certification for Automated Security Decisions: A Decision-Contract Theory with ATT\&CK-Aligned Triage as a Worked Instance

## Abstract
An unconditional risk bound on automated decisions can be satisfied without automating anything, since a selector that never acts drives the bound to zero. We show this is structural: any risk certificate is defined over a decision contract, the inputs a system acts on plus the semantic relation under which an output counts correct, and weakening either hides base-classifier error. We develop a decision-contract theory: an error-conservation law showing error is only reassigned among harmful automation, human deferral, and semantic masking; a label-free singleton capacity certifying structural incapacity, with a risk-feasible refinement separating recoverable threshold misalignment from risk-constrained incapacity; and a non-degenerate actionability certificate excluding all-abstain solutions by construction. We instantiate this on ATT\&CK-aligned alert triage for LLM-based intrusion detection, the setting that exposed the vacuity failure. Across 3 IDS datasets, 6 LLMs, and 4 error-rate thresholds, empirical false-attribution risk stays at or below target in 90.3% of configurations, with 83.4% mean correct automation. The capacity diagnostic explains every low-utility configuration; its refinement separates genuine misalignment from risk-constrained incapacity, confirmed by an exhibited alternative threshold; a training-stability re-run finds no confirmed structural-incapacity instance; and real fine-grained attack-subtype labels confirm the coarsening-transfer identity under a genuine many-to-one map, with small but non-zero masking mass.

## Metadata
- **Published**: 2026-08-12T16:59:19Z
- **Authors**: Zhenpeng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12444v1)