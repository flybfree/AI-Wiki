---
title: Contextual Deconvolution for Variance-Stable Demand Sensing: Kernel-Modulated Operators in Promotional Retail
published: 2026-07-28T12:49:59Z
authors: Mohammad Forouhesh
url: http://arxiv.org/abs/2607.25664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contextual Deconvolution for Variance-Stable Demand Sensing: Kernel-Modulated Operators in Promotional Retail

## Abstract
Machine learning demand forecasts optimize statistical accuracy yet leave excess operational volatility that inflates safety stock and amplifies the Bullwhip effect. We introduce \textbf{Contextual Deconvolution} (CD), a two-stage estimator that reframes demand sensing as a convex decomposition: a kernel-modulated banded operator separates transient promotion-driven shocks from a smooth structural baseline, and hierarchical partial pooling enables catalog-scale deployment without per-SKU training. The operator is data-derived, not imposed---it reduces to the identity wherever the promotional response is impulsive (most of M5, all of Favorita) and contributes only where genuine multi-day carryover exists, so the gains rest on the structural decomposition itself. Evaluating strictly out-of-sample on 30,490 M5 SKUs and 2,845 Favorita items, with calendar-aware baselines given CD's identical future calendar, we anchor the contribution on a full inventory-cost accounting: CD lowers safety stock, holding cost, and order variance but under-provisions event spikes, reducing total cost only when holding costs exceed $\sim$20\% of stockout costs (95\% CI $[17\%,25\%]$); otherwise it is an operational-stability and inventory-capital layer, not an expected-cost minimizer. Its accuracy contribution is reliability rather than central tendency: across eleven baselines, CD attains the lowest cross-sectional dispersion of per-SKU error and mis-forecasts by more than 200\% on 0.8\% of SKUs versus 9.9--20.6\% for every baseline, ranking first on both in all four M5 draws. Because the Variance Ratio and std-based safety stock are minimized by any sufficiently smooth forecast, we treat them as diagnostics, not objectives. A supporting analysis shows the learned demand operators are non-normal, yet CD's compact parametric kernel matches their operational performance interpretably.

## Metadata
- **Published**: 2026-07-28T12:49:59Z
- **Authors**: Mohammad Forouhesh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25664v1)