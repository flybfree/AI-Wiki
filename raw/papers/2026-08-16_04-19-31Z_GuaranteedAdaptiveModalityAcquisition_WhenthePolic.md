---
title: Guaranteed Adaptive Modality Acquisition: When the Policy Chooses Its Own Calibration Group
published: 2026-08-16T04:19:31Z
authors: Melika Baghi
url: http://arxiv.org/abs/2608.15520v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Guaranteed Adaptive Modality Acquisition: When the Policy Chooses Its Own Calibration Group

## Abstract
A multimodal system may begin inference holding only some of its inputs and may acquire the rest at a cost. With adaptive acquisition, the policy determines which inputs are ultimately observed, so we state the guarantee conditional on that terminal input pattern. Conditional calibration normally assumes the grouping map is fixed independently of the calibration sample, which policy-induced grouping does not satisfy. We characterize when pattern-conditional guarantees remain valid and give two finite-sample constructions: threshold-free routing with calibration applied at the terminal pattern, and simultaneous certification of complete policy-pattern pairs, which lets calibration data select the deployed policy. A counterexample shows that a guarantee proved for a calibration-independent grouping map need not transfer once the policy makes the terminal group calibration-dependent. We call the resulting method RouteCert. On a clinical electrocardiogram task with a staged, cost-ordered lead protocol, the certified policy answers 71.2% of held-out patients at an observed 7.4% disagreement with the cardiologist's diagnosis at 48.8% of the prespecified ordinal cost of acquiring every stage, and all three acquisition stages carry their own certificate. On masked multimodal benchmarks, certifying pointwise at each terminal pattern holds observed worst-pattern selective risk, measured against the full-information reference decision rather than the true label, at 0.034 where a pooled design reaches 0.145 against a 0.10 cap, at a comparable answered fraction (0.350 vs 0.342); under the budget-matched simultaneous comparison the answered fraction falls to 0.305.

## Metadata
- **Published**: 2026-08-16T04:19:31Z
- **Authors**: Melika Baghi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15520v1)