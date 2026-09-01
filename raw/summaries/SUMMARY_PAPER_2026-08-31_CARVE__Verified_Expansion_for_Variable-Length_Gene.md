---
title: CARVE: Verified Expansion for Variable-Length Generation in Diffusion Language Models
url: http://arxiv.org/abs/2608.30922v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-00-30Z_CARVE_VerifiedExpansionforVariable_LengthGeneratio.md
generated_at: 2026-08-31 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CARVE, a training‑free method that dynamically expands the masked positions in diffusion language models to improve generation length without retraining. It uses counterfactual predictions and Jensen–Shannon divergence to verify stability of added masks. Across code and math tasks, CARVE outperforms fixed‑length baselines while cutting inference cost.

## Key Takeaways
- CARVE grows response by inserting additional [MASK] positions during decoding from a shorter canvas.
- It tests candidate expansions with counterfactual questions about model predictions on unresolved positions to ensure low Jensen–Shannon divergence, making length growth a verified stability decision.
- The method works without retraining and applies to both full‑canvas and blockwise diffusion decoders.

## Context
Variable‑length decoding is needed for tasks where the answer can be of varying size, yet most diffusion models are limited by fixed inference pipelines that waste resources or truncate outputs. CARVE addresses this limitation by providing a flexible, runtime‑adaptive strategy. This approach aligns with trends toward dynamic inference and resource‑aware model deployment.

## Implications
For practitioners, CARVE enables more efficient generation without sacrificing quality, reducing computational overhead in real‑time applications. It also sets a precedent for counterfactual verification in model inference, opening new avenues for robust AI systems. Future work could explore extending this verification framework to other generative modalities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30922v1)
