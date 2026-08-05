---
title: Double Descent in Gradient Boosting Decision Trees via Split-Candidate Scaling
url: http://arxiv.org/abs/2608.03111v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_04-32-08Z_DoubleDescentinGradientBoostingDecisionTreesviaSpl.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces split-candidate scaling as a capacity parameter for gradient boosting decision trees and demonstrates that test error can peak then decline at larger budgets, revealing double descent behavior. Experiments on XGBoost LightGBM CatBoost show this pattern while random forests improve monotonically. The analysis links the phenomenon to geometry induced by candidate-induced paths.

## Key Takeaways
- Increasing split-candidate budget refines feature quantization and expands root-to-leaf path dictionary which can cause test error to peak before decreasing at larger budgets.
- The empirical tree-kernel diagnostic shows kernel rank growing toward sample size with small positive eigenvalues indicating noise-sensitive directions that trigger the double descent.
- Experiments across XGBoost LightGBM CatBoost confirm intermediate split-candidate budgets produce peak test errors, contrasting with monotonic improvement in random forests.

## Context
Double descent is a well‑studied phenomenon in deep learning where model performance improves then worsens as capacity increases. GBDTs lack an explicit single‑axis capacity knob, so this work provides a new operational metric that clarifies how boosting dynamics interact with candidate‑induced geometry.

## Implications
Practitioners can use split-candidate scaling to tune model complexity and avoid overfitting in noisy settings. The insight helps researchers design more robust training regimes for GBDTs across diverse datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03111v1)
