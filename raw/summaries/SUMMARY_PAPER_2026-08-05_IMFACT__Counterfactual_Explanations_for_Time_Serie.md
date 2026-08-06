---
title: IMFACT: Counterfactual Explanations for Time Series via Intrinsic Mode Function Substitution
url: http://arxiv.org/abs/2608.04777v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-43-33Z_IMFACT_CounterfactualExplanationsforTimeSeriesviaI.md
generated_at: 2026-08-05 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IMFACT, a model‑agnostic method that creates counterfactual explanations for time series classifiers by working in the Empirical Mode Decomposition (EMD) space. It replaces selected Intrinsic Mode Functions with Nearest Unlike Neighbour functions until the classifier switches to a target class, evaluating strategies on two benchmark datasets.

## Key Takeaways
- The framework operates in decomposition space, preserving temporal structure while allowing counterfactual perturbations that are physically plausible.
- A variance‑based IMF selection combined with three NUN substitutions achieves high reliability and plausibility compared to baselines.
- Cycling through three NUNs yields the best proximity metrics on both FaultDetectionA and FruitFlies.

## Context
Time series classification often relies on raw feature space, where counterfactual explanations can break temporal coherence. This work addresses that limitation by leveraging IMF decomposition, a technique widely used for signal analysis, to generate more interpretable and realistic alternatives.

## Implications
For practitioners, IMFACT offers a scalable approach to explainable AI in sensor data, improving trust in model outputs. The method could be integrated into industry pipelines where physical plausibility is critical, such as vibration monitoring or medical signal analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04777v1)
