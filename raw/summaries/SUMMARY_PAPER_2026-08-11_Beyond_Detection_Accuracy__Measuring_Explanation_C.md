---
title: Beyond Detection Accuracy: Measuring Explanation Cost, Stability, and Utility for Resource-Aware IoT Intrusion Detection
url: http://arxiv.org/abs/2608.10349v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_01-18-07Z_BeyondDetectionAccuracy_MeasuringExplanationCost_S.md
generated_at: 2026-08-11 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a joint evaluation framework that measures predictive accuracy, explanation cost, local stability, and selective usefulness for binary IoT intrusion detection. Experiments on a leakage‑safe CICIoT2023 dataset show XGBoost outperforms Random Forest in prediction while TreeSHAP incurs higher computational time.

## Key Takeaways
- TreeSHAP’s runtime is 700.759 seconds for Random Forest and only 1.471 seconds for XGBoost, indicating that explanation cost varies dramatically with model choice.
- Random Forest exhibits the highest base‑level explanation stability, whereas XGBoost retains high rank but suffers greater top‑feature turnover and attribution drift under perturbations.
- On balanced test data, achieving ~90% false‑negative coverage yields 28–32% compute savings, dropping to 15–23% under attack‑heavy natural prevalence.

## Context
Explainable AI for resource‑constrained IoT systems must balance detection performance with low‑latency explanations. Traditional approaches treat explanation generation as a free post‑processing step, ignoring its computational burden and stability across model variations.

## Implications
Practitioners should prioritize models that deliver both strong predictions and stable, cost‑effective explanations, especially when limited bandwidth or processing power is available. Selective invocation of explanations can further reduce overhead without sacrificing user trust in IoT security services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10349v1)
