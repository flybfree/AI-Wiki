---
title: Beyond Field Accuracy: Two-Axis Diagnosis of Inverse-PINN Parameter Error
url: http://arxiv.org/abs/2608.15373v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_18-54-12Z_BeyondFieldAccuracy_Two_AxisDiagnosisofInverse_PIN.md
generated_at: 2026-08-17 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a two-axis diagnostic framework for inverse PINNs that separates finite-sample resolution errors from signed parameter preferences. It shows how the learned field and residual metrics can mislead despite accurate field reconstruction. Experiments on synthetic PDEs reveal mean absolute relative errors up to 17.46% while displacement tracks correct sign in most fresh-noise runs.

## Key Takeaways
- The first axis measures finite-sample resolution under a specific observation protocol, yielding MARE errors between 2.34% and 17.46% across three scalar PDEs.
- The second axis captures signed parameter preference by freezing the field view and measuring displacement toward residual minima, with correct direction in 237 of 240 fresh-noise RBA runs.
- Endpoint consistency validates that joint training aligns both axes under identical final views, confirming complementary diagnostic coordinates.

## Context
Inverse PINNs aim to recover physical parameters from noisy data but often fail to provide reliable parameter estimates. Existing diagnostics either add error components or require oracle feedback, limiting practical use. This work offers an oracle-free, two-axis approach that clarifies the source of bias in parameter inference.

## Implications
Practitioners can now diagnose whether errors stem from limited observations or biased learned preferences without additional data. The method guides future research toward robust training protocols and endpoint delivery, improving trust in inverse modeling applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15373v1)
