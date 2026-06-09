# Summary: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md
Saved: 2026-05-07 22:08
Source: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md
Model: None

---

## Summary
PALACE is a closed-form adaptive-landmark kernel method for certified point-cloud and graph classification. It uses a small amount of cross-validation to tune a few discrete knobs, then derives theoretical guarantees and prediction-time certificates without gradient training.

## Key Takeaways
- Provides closed-form guarantees for distortion, classification rate, and per-prediction certification.
- Uses adaptive landmark placement and latent-variable decomposition instead of predictor duplication.
- Reports strong performance on several graph and diagram benchmarks, including Orbit5k, COX2, MUTAG, and DHFR.
- Maintains performance under domain inflation where a uniform grid collapses.

## Context
The method sits in the intersection of topological data analysis, kernel methods, and certified learning. It is motivated by the need for efficient classification on point clouds and graphs with provable behavior.

## Implications
The paper suggests that carefully designed closed-form methods can be both theoretically certifiable and empirically competitive. Its adaptive placement strategy appears especially useful when data geometry shifts beyond the training regime.

## Original Reference
- Title: A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification
- Authors: Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi
- URL: http://arxiv.org/abs/2605.04046v1
- Published: 2026-05-05T17:59:18Z