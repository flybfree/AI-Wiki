---
title: Represent, Then Generate: Multimodal-Conditioned Time-Series Generation under Irregular Missingness
url: http://arxiv.org/abs/2608.12592v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_21-04-44Z_Represent_ThenGenerate_Multimodal_ConditionedTime_.md
generated_at: 2026-08-13 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReCoGen, a two‑stage framework for generating missing physiological time series from multimodal conditions and static covariates despite irregular missingness. Experiments on glucose monitoring and blood pressure data show that ReCoGen outperforms six existing conditional generators across all dataset‑task‑metric combinations and matches or exceeds the utility of real signals in thirteen cases.

## Key Takeaways
- ReCoGen decouples condition representation from generation by training separate masked autoencoders for each modality, producing missingness‑tolerant token sequences.  
- The generator uses flow‑matching to fuse these tokens with static conditions and employs learnable cross‑attention over frozen per‑modality encoders.  
- Ablations reveal that the dual token‑plus‑AdaLN route for static covariates is crucial, enabling the model to synthesize signals even when some modalities are absent.

## Context
Current clinical monitoring relies heavily on invasive or unavailable measurements, creating a need for synthetic surrogates generated from routine data streams. Existing models often fail because they assume homogeneous conditioning and cannot handle the heterogeneous pattern of missing time‑varying signals seen in real hospitals.

## Implications
This work paves the way toward less invasive, cost‑effective continuous monitoring by turning routinely collected data into reliable proxies for missing measurements. Practitioners can leverage ReCoGen to improve diagnostic accuracy without additional hardware, aligning AI with broader goals of equitable and affordable healthcare delivery.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12592v1)
