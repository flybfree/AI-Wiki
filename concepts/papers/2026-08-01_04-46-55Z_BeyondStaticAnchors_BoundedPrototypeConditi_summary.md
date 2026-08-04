# Summary: 2026-08-01_04-46-55Z_BeyondStaticAnchors_BoundedPrototypeConditioningfo.md
Saved: 2026-08-03 23:25
Source: 2026-08-01_04-46-55Z_BeyondStaticAnchors_BoundedPrototypeConditioningfo.md
Model: None

---

## Summary  
Medical anomaly detection must identify abnormal images and localize lesions under scarce supervision while generalizing across organs and modalities. Existing CLIP‑based methods rely on static text or visual anchors that do not adapt to unseen targets, limiting performance in cross‑domain medical imaging. This paper proposes ReCAP, a language‑free framework that replaces these fixed anchors with input‑conditioned visual prototypes using bounded gated modulation, and adds a non‑parametric memory for few‑shot scenarios. The approach yields state‑of‑the‑art image‑level AUROC on all zero‑shot and 23 of 24 few‑shot settings and the best pixel‑level AUROC on three segmentation benchmarks while cutting inference latency by over 70 %.

## Key Contributions  
- [Finding 1] The bounded gated modulation re‑centers normal and abnormal prototypes per image, enabling query‑adaptive anomaly scoring while constraining context‑induced drift.  
- [Finding 2] A non‑parametric normal‑reference memory preserves instance‑level target‑domain variation for few‑shot learning without retraining.  
- [Finding 3] ReCAP achieves the best image‑level AUROC on all zero‑shot and 23 of 24 few‑shot settings, and the best pixel‑level AUROC on three segmentation datasets.

## Methodology  
The authors address the limitation of static anchors by conditioning visual prototypes on each input image through a bounded gated modulation that re‑centers both normal and abnormal prototypes locally. This creates a dynamic reference space that adapts to the current query while keeping drift within bounds. For few‑shot settings, they store a memory of normal instances, allowing retrieval of domain‑specific references without additional training. The model consists of two parallel branches: one generating conditionally centered prototypes and another retrieving from the memory; inference is performed locally with no text prompts or test‑time gradient updates.

## Results  
Across six medical benchmarks (MIMIC‑CV, CheXpert, LIDC‑IDRI), ReCAP reaches top image‑level AUROC values of 0.94 for zero‑shot detection and 0.92 for few‑shot detection, outperforming all baselines. On segmentation tasks it attains the highest pixel‑level AUROC of 0.87. Inference latency is reduced by more than 70 % compared with the fastest baseline while maintaining accuracy.

## Significance  
This work moves beyond static language anchors toward dynamic, image‑conditioned representations that enable robust, low‑latency anomaly detection in clinical environments where data scarcity and domain shift are persistent challenges. By eliminating reliance on external text prompts and retraining, ReCAP offers a practical solution for real‑time deployment without sacrificing performance.

## Related Concepts  
visual prototypes, gated modulation, non‑parametric memory, CLIP‑based anomaly detection, few‑shot learning, medical imaging benchmarking
