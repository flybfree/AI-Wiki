# Summary: 2026-08-07_00-42-25Z_CorruptingAttention_Evasion_BasedAdversarialAttack.md
Saved: 2026-08-09 22:33
Source: 2026-08-07_00-42-25Z_CorruptingAttention_Evasion_BasedAdversarialAttack.md
Model: None

---

## Summary  
This paper introduces a novel class of adversarial attacks that target the encoder‑attention mechanism within detection transformers, rather than merely perturbing the final detection output. By optimizing an encoder‑attention objective under imperceptible, bounded ℓ∞ perturbations, the authors demonstrate that corrupting attention can cause a dramatic collapse in object‑detection performance. Their attack achieves a four‑fold reduction of DETR‑R50 mAP (from 42.1 to 0.97) and drives detection below three percent across multiple corruption objectives, establishing a new state‑of‑the‑art result for both dense and deformable attention models.

## Key Contributions  
- [Finding 1] The first attack directly optimizes an encoder‑attention objective under imperceptible, bounded ℓ∞ perturbation without using a visible sink token.  
- [Finding 2] The attack reduces DETR‑R50 mAP from 42.1 to 0.97—a ~4× drop—while also dropping detection below 3 mAP for four distinct corruption targets (dispersion, re‑ranking, permutation, peak‑suppression).  
- [Finding 3] The vulnerability generalizes across attention formulations; DINO‑Swin‑L mAP falls from 56.8 to 1.44 against the strongest prior attack of 7.3.

## Methodology  
The authors formulate an adversarial optimization problem that maximizes a corruption objective while minimizing L∞ norm changes, forcing the model’s own attention weights toward a corrupted target. The perturbation is applied uniformly across the encoder’s attention layers, making it imperceptible to human observers yet sufficient to disrupt spatial reasoning. Experiments compare this approach against existing sink‑token attacks and measure impact on standard detection metrics (mAP) under identical iteration budgets.

## Results  
Across four qualitative corruption objectives, DETR‑R50 mAP is reduced from 42.1 to 0.97, a ~4× degradation. All targets cause detection scores below 3 mAP, indicating a fundamental breakdown in attention rather than a single target. The same attack reduces DINO‑Swin‑L mAP from 56.8 to 1.44, outperforming the best prior (7.3). These results hold for both dense and deformable attention variants.

## Significance  
The work reveals that encoder attention is a critical yet vulnerable component of detection transformers, with attacks on it causing far more severe performance loss than output‑only perturbations. This insight has implications for safety‑critical systems where subtle attentional failures could lead to missed detections or false positives.

## Related Concepts  
- Adversarial robustness in neural networks  
- Object detection transformers (e.g., DETR, DINO)  
- Encoder attention mechanisms and their role in spatial reasoning  
- ℓ∞ bounded perturbations and imperceptibility constraints  
- Sink‑token adversarial attacks as a baseline method
