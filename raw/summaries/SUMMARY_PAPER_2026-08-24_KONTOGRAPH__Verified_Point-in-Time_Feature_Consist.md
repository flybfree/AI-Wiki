---
title: KONTOGRAPH: Verified Point-in-Time Feature Consistency and Amortised Explanation for Real-Time Anti-Money Laundering under a 200 ms Decision Budget
url: http://arxiv.org/abs/2608.22389v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_12-28-26Z_KONTOGRAPH_VerifiedPoint_in_TimeFeatureConsistency.md
generated_at: 2026-08-24 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KONTOGRAPH, an end‑to‑end anti‑money‑laundering pipeline for SEPA instant credit transfers that must decide within a 200 ms budget. Empirical testing on 1.56 million simulated payments shows three major results: a graph network with per‑node memory boosts PR‑AUC from 0.0053 to 0.1717, point‑in‑time violations are revealed after exporting the model to ONNX despite negligible score change, and 32‑bit accumulation amplifies small perturbations that affect decisions.

## Key Takeaways
- A temporal graph network with per‑node memory improves PR‑AUC from 0.0053 to 0.1717, a paired day‑blocked bootstrap difference of +0.166 with 95% CI [0.105, 0.241], and per‑node memory alone more than doubles the score.
- Property‑based tests that perturb future data expose three point‑in‑time violations that code review had missed; these would have inflated reported performance if not caught.
- Exporting the tree ensemble to ONNX changes only $7.4×10⁻⁸$ in mean score but alters 0.26% of decisions and inflates alert volume by 12%, due to 32‑bit accumulation perturbing scores across a cost‑optimal threshold of $3.98×10⁻⁴.

## Context
This work addresses the regulatory pressure for real‑time AML detection in payment systems, where latency budgets are tight and model fidelity must be preserved. It demonstrates how graph‑based representations and careful serving formats can boost performance while exposing hidden data‑drift issues that traditional tabular models miss.

## Implications
For practitioners, the findings stress that serving‑format conversion is a model change until its impact is measured, and that explainability metrics may be unreliable with small neighbourhoods. The industry must adopt rigorous testing pipelines to catch point‑in‑time violations early and avoid inflated alert volumes caused by numerical precision issues.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22389v1)
