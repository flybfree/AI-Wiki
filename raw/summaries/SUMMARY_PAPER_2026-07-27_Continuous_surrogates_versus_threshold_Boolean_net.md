---
title: Continuous surrogates versus threshold Boolean networks for modeling Arabidopsis ISR gene regulation
url: http://arxiv.org/abs/2607.23289v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_16-57-09Z_ContinuoussurrogatesversusthresholdBooleannetworks.md
generated_at: 2026-07-27 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper compares continuous surrogate models such as Random Forest regression and Multi‑Layer Perceptron with a threshold Boolean network on Arabidopsis induced systemic resistance gene data, evaluating both prediction performance and interpretability across time points.

## Key Takeaways
- Random Forest achieved the best one‑step numerical accuracy with an MAE of 1.910 and RMSE of 2.836, outperforming MLP which had MAE 2.089 and RMSE 3.106.
- The threshold Boolean network obtained the highest binary one‑step quality, delivering a binary accuracy of 0.550 and Hamming distance 3.600, compared with RF (0.500, 4.000) and MLP (0.495, 4.040).
- In recursive rollout the threshold Boolean network reproduced the observed binarized trajectory exactly, while the MLP showed near‑perfect fidelity (binary accuracy 0.986), whereas RF accumulated larger deviation with binary accuracy 0.708.

## Context
This study highlights a fundamental trade‑off in AI modeling of biological networks: quantitative prediction can be high without guaranteeing mechanistic interpretability, and vice versa. The results underscore the need for methods that balance both aspects when dealing with gene regulatory data.

## Implications
Practitioners should view continuous surrogates and threshold Boolean networks as complementary tools rather than competing alternatives, enabling more robust and interpretable models of complex biological regulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23289v1)
