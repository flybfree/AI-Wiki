---
title: When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters
url: http://arxiv.org/abs/2608.05207v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_07-48-35Z_WhenDoCorrectiveFeaturesHelp_AnAgentforCorrectiveF.md
generated_at: 2026-08-06 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CRAFTER, a corrective feature discovery agent that works on frozen black‑box forecasters by mining interpretable features from their residuals. It combines a compositional search over input channels with a large language model to propose features and code, validates each candidate through a single gate, and applies accepted corrections to improve forecasts. Across six datasets and backbones CRAFTER outperforms existing feature‑engineering systems, roughly doubling the improvement of the corrector alone and cutting error on weak models by up to 27%.

## Key Takeaways
- The agent’s source‑agnostic pipeline lets any prior feature‑engineering system be evaluated under identical conditions, isolating improvements to that specific source.  
- CRAFTER’s dual generators—raw channel compositional search and an LLM proposing features or code—enable diverse candidate generation without bias toward one method.  
- Validation‑grounded gating ensures every candidate is judged uniformly, making the process robust across different LLM backends.

## Context
Current AI forecasting systems often rely on frozen pretrained models that degrade in systematic ways, requiring costly fine‑tuning. Automated feature engineering has become a standard remedy, but its performance varies with model architecture and data distribution. This work bridges the gap by treating model failure as a separate problem to be corrected after the fact.

## Implications
For practitioners, CRAFTER offers a lightweight tool that can boost forecast accuracy without retraining heavy models, reducing operational costs. The framework also provides a clear attribution mechanism for feature improvements, enabling better resource allocation and accountability in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05207v1)
