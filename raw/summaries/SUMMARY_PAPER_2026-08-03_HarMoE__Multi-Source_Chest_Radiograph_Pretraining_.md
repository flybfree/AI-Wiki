---
title: HarMoE: Multi-Source Chest Radiograph Pretraining with Dataset-Disentangled Experts
url: http://arxiv.org/abs/2608.02252v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_14-00-16Z_HarMoE_Multi_SourceChestRadiographPretrainingwithD.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HarMoE, a dataset‑aware mixture‑of‑experts model for chest X‑ray understanding that combines multiple multi‑label classification datasets with image‑report alignment. By training on a unified disease vocabulary and masked supervision across heterogeneous sources, HarMoE learns shared medical semantics while isolating source‑specific noise to lightweight residual experts. Experiments demonstrate consistent gains in zero‑shot classification, out‑of‑distribution transfer, and grounding over strong baselines.

## Key Takeaways
- The model mitigates label ontology drift by training on a unified disease vocabulary that masks dataset identity during supervision, preventing false negatives from mismatched annotations.  
- HarMoE uses lightweight residual experts in deeper decoder layers to retain source‑specific variation without compromising the shared cross‑dataset knowledge base.  
- The approach yields higher zero‑shot performance and better generalization on large‑scale chest X‑ray benchmarks compared with single‑source image‑report aligned models.

## Context
Current radiology vision‑language models depend heavily on MIMIC‑CXR, which limits pathology coverage to diseases well documented in free‑text reports. Multi‑label classification datasets offer cleaner labels and broader disease representation but are rarely integrated due to semantic entanglement. HarMoE addresses this gap by constructing a harmonized knowledge base from heterogeneous sources.

## Implications
For the field, HarMoE shows that robust radiology VLMs benefit from structured knowledge construction rather than reliance on single‑source alignment. In industry, practitioners can leverage cleaner multi‑label data to improve model reliability and reduce false negatives in clinical deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02252v1)
