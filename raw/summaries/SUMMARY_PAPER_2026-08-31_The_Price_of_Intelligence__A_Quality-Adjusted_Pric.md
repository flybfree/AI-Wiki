---
title: The Price of Intelligence: A Quality-Adjusted Price Index for AI Services
url: http://arxiv.org/abs/2608.29843v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_15-17-14Z_ThePriceofIntelligence_AQuality_AdjustedPriceIndex.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper builds a quality‑adjusted price index for AI inference services using public posted prices and benchmark scores. It finds that while token prices fell about 0.10 log points per year, the overall quality‑adjusted index declined only 0.73 log points, indicating most of the decline is invisible to current methods.

## Key Takeaways
- The matched‑model approach yields a price decline of 0.10 log points annually while the quality‑adjusted index falls at 0.73 log points, showing that 87% of the observed drop reflects hidden quality changes.
- Buyer and seller prices diverge because reasoning models consume more tokens faster than token prices fall, making counted per‑task price static.
- A pre‑registered validity audit improves benchmark reliability, leaving model rankings stable at 0.998 but moving the index by 0.49 log points when contamination is removed.

## Context
AI inference markets are characterized by rapid price drops that are often attributed solely to cost reductions, yet quality improvements or deteriorations can mask these trends. This study addresses the gap between observable pricing and latent service quality in a large‑scale dataset.

## Implications
Practitioners must recognize that benchmark stability does not protect economic statistics from quality shifts, affecting competition analysis and productivity estimates. The index provides a transparent, reproducible metric for assessing AI service value without proprietary tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29843v1)
