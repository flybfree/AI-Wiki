---
title: Spatially explicit feature importance for building height estimation using research-access high-resolution SAR and optical sensors
url: http://arxiv.org/abs/2608.17822v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_14-20-53Z_Spatiallyexplicitfeatureimportanceforbuildingheigh.md
generated_at: 2026-08-18 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper aims to estimate individual building heights at the footprint scale using freely accessible high‑resolution SAR and optical imagery from TerraSAR‑X StripMap, PlanetScope, and Sentinel‑1. By integrating features from these sensors into a geographically weighted random forest model, the authors achieve an RMSE of 5.34 m and R² of 0.756 against a LiDAR reference dataset in a Brazilian city.

## Key Takeaways
- Local feature importance varies with building height: footprint geometry dominates for low‑rise structures, shadow‑derived height predicts taller isolated buildings, while spectral reflectance is key for the tallest ones.  
- Sentinel‑1 backscatter and InSAR data occupy complementary spatial niches, meaning no single sensor provides a uniformly superior prediction across all contexts.  
- The study demonstrates that machine learning models can leverage research‑access satellite products to deliver city‑scale height estimates where airborne LiDAR is unavailable.

## Context
The integration of heterogeneous remote sensing data into AI‑driven geospatial models reflects the growing trend toward open, scalable solutions for urban analytics. This work illustrates how non‑commercial sensors can be combined with advanced algorithms to fill gaps left by expensive or inaccessible LiDAR coverage in many regions.

## Implications
For urban planners and disaster responders, these results provide a practical optioneering guide that balances sensor availability, cost, and predictive performance. Practitioners can select the most relevant data sources for their specific building height needs without relying on proprietary high‑resolution imagery or costly LiDAR surveys.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17822v1)
