---
title: FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier Coupon Allocation
url: http://arxiv.org/abs/2608.11675v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_05-32-33Z_FunnelCausalNet_Funnel_awareJointConversion_Revenu.md
generated_at: 2026-08-12 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FunnelCausalNet, a joint conversion-revenue uplift estimator that respects the deterministic funnel structure of coupon campaigns and handles zero-inflated GMV. It combines a binary conversion head with a nonnegative conditional-value head using μ_gmv = μ_conv * μ_val. On multi-tier Criteo-MT7 data it matches or slightly exceeds leading feature-interaction baselines while reducing pointwise variance in certain regimes.

## Key Takeaways
- The estimator’s MSE advantage is heuristic and not guaranteed for the shared‑representation neural model.
- It uses marginal split‑conformal CATE summaries with Bonferroni audit bands to control error across heads.
- Ablation shows 18–48% lower GMV effect error versus direct GMV regression in zero‑inflation regimes.

## Context
This work advances causal uplift estimation by integrating funnel dynamics into neural architectures, addressing the variance problem inherent in heavy‑tailed GMV. It demonstrates that funnel composition can improve pointwise uncertainty bounds, a concept relevant to multi‑stage marketing optimization.

## Implications
Practitioners can leverage FunnelCausalNet for budgeted coupon allocation with ROI‑aware subsidies while maintaining rigorous statistical audit bands. The method sets a benchmark for combining conversion and revenue heads in real‑world e‑commerce settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11675v1)
