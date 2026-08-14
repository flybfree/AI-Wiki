---
title: Demand Transfer Estimation at Scale via Restricted Logit Modeling
url: http://arxiv.org/abs/2608.12680v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_00-37-13Z_DemandTransferEstimationatScaleviaRestrictedLogitM.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method for estimating demand transfer (DT) coefficients at scale using restricted logit modeling, enabling accurate prediction of how customers might shift purchase intent when one item is removed from the shelf. The approach combines independent item forecasts with adjustments that account for substitution behavior among similar items, allowing efficient estimation across millions of SKUs without generating separate forecasts per possible assortment.

## Key Takeaways
- The method merges individual demand forecasts with systematic adjustments that reflect how the availability of other similar items influences a target item’s demand.  
- It enables the computation of DT coefficients for very large item universes, such as those containing over one million SKUs, by leveraging restricted logit modeling.  
- Experiments on both synthetic data and real historical transaction data show that under reasonable substitution assumptions, the procedure yields accurate DT estimates and improves overall demand forecasting accuracy.

## Context
In retail AI, forecasting demand for each possible assortment is computationally prohibitive as it requires a separate model per combination of items. This paper addresses the scalability challenge by proposing a unified statistical framework that captures cross‑item substitution effects without enumerating all possible assortments, aligning with broader trends toward efficient, high‑dimensional predictive modeling.

## Implications
Retailers and supply chain managers can use these DT coefficients to refine inventory policies, reduce stockouts, and optimize shelf space allocation across massive catalogs. The technique translates into tangible cost savings and better customer experience by ensuring that demand forecasts remain accurate even when items are frequently removed from shelves.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12680v1)
