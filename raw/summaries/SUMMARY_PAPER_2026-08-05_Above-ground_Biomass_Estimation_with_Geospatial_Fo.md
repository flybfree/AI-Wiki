---
title: Above-ground Biomass Estimation with Geospatial Foundation Models
url: http://arxiv.org/abs/2608.04792v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-57-18Z_Above_groundBiomassEstimationwithGeospatialFoundat.md
generated_at: 2026-08-05 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a benchmark for evaluating geospatial foundation models (GFMs) in the task of global above‑ground biomass estimation using satellite imagery and the AGBD dataset. The authors compare 11 GFMs run as frozen encoders with pre‑computed embedding products AlphaEarth Foundations (AEF) and TESSERA against a supervised state‑of‑the‑art model, finding that embedding‑product approaches outperform raw encoder weights while also generalizing better across space and time.

## Key Takeaways
- Frozen GFM encoders used as model weights significantly underperform the fully supervised SOTA AGBD model.  
- Pre‑computed embedding products such as AEF enable an MLP to surpass the SOTA model when trained on these embeddings alone.  
- Combining the SOTA model with AEF embeddings (optionally augmented by raw features) yields the best overall accuracy and improved geographical and temporal generalization.

## Context
The emergence of foundation models in geospatial AI promises to replace traditional feature engineering pipelines, but their performance on quantitative regression tasks like biomass estimation has been under‑explored. This work fills that gap by systematically testing GFMs across diverse biomes, highlighting the importance of embedding products for reliable global predictions.

## Implications
For climate monitoring agencies and remote sensing companies, this research suggests that leveraging pre‑computed GFM embeddings can enhance model efficiency and accuracy without sacrificing generalization. Practitioners should prioritize using these embedding products as inputs to downstream regression models rather than relying solely on raw encoder outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04792v1)
