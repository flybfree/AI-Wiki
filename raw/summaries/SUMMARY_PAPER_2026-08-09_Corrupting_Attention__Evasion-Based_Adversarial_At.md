---
title: Corrupting Attention: Evasion-Based Adversarial Attacks on Encoder Attention in Detection Transformers
url: http://arxiv.org/abs/2608.06674v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_00-42-25Z_CorruptingAttention_Evasion_BasedAdversarialAttack.md
generated_at: 2026-08-09 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an adversarial attack that directly manipulates the encoder attention mechanism of detection transformers, showing a severe degradation in performance under imperceptible perturbations. It achieves a fourfold drop in mAP for DETR-R50 on COCO and similar drops across other models, demonstrating that corrupting attention is more disruptive than perturbing output alone.

## Key Takeaways
- The attack optimizes an encoder-attention objective with bounded l_infty perturbation, causing the model to focus attention on a corrupted target without visible patches. 
- Across four distinct corruption objectives—dispersion, re-ranking, permutation, and peak-suppression—the detection mAP falls below three, indicating that breaking attention structure is sufficient for failure. 
- The method achieves state-of-the-art results against existing attacks on both dense and deformable attention variants, showing broad applicability.

## Context
Attention mechanisms are central to modern transformer-based detectors, but their robustness has not been systematically evaluated under adversarial conditions. This work highlights a previously overlooked vulnerability that could undermine real‑world safety‑critical applications where subtle input changes lead to catastrophic misclassifications.

## Implications
For practitioners, the findings call for rigorous attention‑level testing and mitigation strategies in deployment pipelines. Industry reliance on transformer detectors must incorporate defenses against attention corruption to maintain reliability and trustworthiness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06674v1)
