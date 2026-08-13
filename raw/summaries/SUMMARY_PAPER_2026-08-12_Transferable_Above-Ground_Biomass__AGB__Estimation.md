---
title: Transferable Above-Ground Biomass (AGB) Estimation Model from Multi-Sensor Data with Sparse Field Calibration
url: http://arxiv.org/abs/2608.11638v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_04-36-26Z_TransferableAbove_GroundBiomass_AGB_EstimationMode.md
generated_at: 2026-08-12 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a transferable convolutional neural network that estimates forest above‑ground biomass using multi‑sensor data from Sentinel‑2, Sentinel‑1, ALOS‑2 PALSAR‑2 and DEM. The global model is fine‑tuned with a few field plots to correct scale and bias, achieving higher accuracy than existing products.

## Key Takeaways
- The CNN combines optical and SAR inputs plus terrain data into a single 10 m grid, producing biomass predictions that are calibrated locally through Random Forest fine‑tuning.  
- Field calibration reduces RMSE from about 22 Mg/ha to roughly 15 Mg/ha while improving R² from 0.78 to 0.82 on validation plots.  
- The approach outperforms both the uncalibrated global model and the ESA CCI Biomass product, demonstrating a practical workflow for sparse field inventories.

## Context
The need for continuous forest biomass monitoring is driven by climate accounting and carbon markets, where spatial gaps in field data limit reliability. Deep learning models can exploit large satellite datasets to fill those gaps, but they often require extensive retraining per region. This work shows that a one‑time global training combined with minimal local calibration can deliver consistent performance across diverse landscapes.

## Implications
Practitioners can now generate high‑resolution biomass maps without costly repeated field campaigns, accelerating carbon accounting and forest management decisions. The framework also offers a template for other remote sensing applications where multi‑sensor fusion and sparse ground truth are required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11638v1)
