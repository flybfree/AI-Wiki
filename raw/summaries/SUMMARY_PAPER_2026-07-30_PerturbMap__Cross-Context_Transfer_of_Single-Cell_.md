---
title: PerturbMap: Cross-Context Transfer of Single-Cell Perturbation Responses
url: http://arxiv.org/abs/2607.28090v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-58-52Z_PerturbMap_Cross_ContextTransferofSingle_CellPertu.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PerturbMap, a method that predicts missing perturbation responses across different cellular contexts by leveraging low-rank representations and ridge experts trained on paired perturbations. On the melanoma dataset, PerturbMap outperforms several baseline approaches in full-effect mean squared error (MSE) while maintaining high specificity for condition-mean similarity retrieval.

## Key Takeaways
- The method predicts missing recipient-context effects using a recipient-local low‑rank base augmented with ridge experts that transport measured source responses through calibrated pathways.  
- PerturbMap reduces MSE by 4.1 % compared to the low‑rank baseline and beats FedAvg, zero‑response, raw copy, calibrated copy, and identity‑shuffled affine controls.  
- Its performance is only slightly lower than a centralized token‑matched pooled reference (2.82×10⁻⁶ MSE), indicating strong alignment with the strongest training interface.

## Context
In single‑cell perturbation atlases, experimental evidence is often incomplete across contexts, leading to biased or inaccurate cross‑context predictions. AI techniques that combine local context knowledge with global transfer mechanisms are needed to fill these gaps while preserving signal fidelity and avoiding unintended propagation of noise.

## Implications
PerturbMap offers a scalable framework for generating reliable perturbation maps in multi‑tissue studies, reducing reliance on costly re‑measurement across contexts. Practitioners can leverage its improved specificity to make more informed biological inferences and accelerate drug discovery pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28090v1)
