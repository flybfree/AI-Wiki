---
title: GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models
url: http://arxiv.org/abs/2608.25375v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_04-58-40Z_GGSS_Geodesic_GatedSphericalSteeringforInference_T.md
generated_at: 2026-08-26 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces GGSS, a norm‑preserving inference‑time debiasing method for generative vision‑language models that corrects demographic bias by steering visual tokens along geodesic arcs on the unit hypersphere. It outperforms ten baselines and prompt‑based methods across four models in categorical, pairwise, occupation‑gender bias tests while maintaining image quality.

## Key Takeaways  
- GGSS discovers a counterfactual bias subspace on the unit hypersphere and steers visual tokens along geodesic arcs to neutralize demographic signals.  
- The adaptive gate focuses correction only on tokens that carry stronger demographic signal, preserving overall model performance.  
- Evaluation across four generative VLMs shows GGSS achieves the lowest average bias with significant improvements under paired permutation tests.

## Context  
Generative vision‑language models are central to human‑centered AI but often produce biased outputs despite controlled attribute differences. Existing debiasing techniques were largely designed for static embeddings or CLIP‑style models, leaving a gap in inference‑time mitigation for generative systems.

## Implications  
This work provides a scalable framework that can be applied to any generative VLMs without retraining, offering industry and researchers a practical tool to reduce bias while preserving visual‑language quality. The method’s simplicity and effectiveness could become standard practice as bias becomes a regulatory concern in AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25375v1)
