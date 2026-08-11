---
title: Integrating spectral and morphological plant features with decision-tree models for early-season cotton biomass and nitrogen status estimation from multi-year UAV data
url: http://arxiv.org/abs/2608.07801v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_22-46-06Z_Integratingspectralandmorphologicalplantfeatureswi.md
generated_at: 2026-08-11 13:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study integrated spectral and morphological plant features with decision‑tree models to estimate cotton dry biomass weight, plant nitrogen uptake, plant nitrogen concentration, critical N dilution, and nitrogen nutrition index from multi‑year UAV multispectral data. The best performing models—random forest regression with trial‑held‑out validation (RFRTHO) and extreme gradient boosting with trial‑held‑out validation (XGBTHO)—achieved high correlation coefficients (R² ≈ 0.85–0.88) and low mean absolute percentage errors for all target variables.

## Key Takeaways
- RFRTHO and XGBTHO models using spectral reflectance, plant height, and fractional canopy cover produced the most accurate estimates of dry biomass weight with R² values above 0.85 and MAPE below 23 %.  
- The nitrogen nutrition index derived from XGBTHO outperformed that from RFRTHO in detecting N‑deficient plots and multi‑level N‑stress categories, highlighting its value for early warning.  
- Critical N dilution was successfully calculated by combining model‑estimated dry biomass weight with plant nitrogen concentration, providing a reliable indicator of fertilizer timing.

## Context
The integration of machine learning with remote sensing is increasingly used to automate agronomic decision support in precision agriculture. By leveraging UAV‑derived multispectral imagery and morphological traits, this work demonstrates how AI can replace labor‑intensive ground measurements for monitoring nitrogen status throughout the growing season.

## Implications
Farmers can apply these models to schedule fertilizer applications precisely when needed, reducing input waste and improving yields. The high accuracy of the NNI also enables early detection of nutrient stress, supporting sustainable cotton production in regions like the Texas Coastal Plains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07801v1)
