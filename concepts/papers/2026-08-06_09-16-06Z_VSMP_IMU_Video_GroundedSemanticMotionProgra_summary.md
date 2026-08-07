# Summary: 2026-08-06_09-16-06Z_VSMP_IMU_Video_GroundedSemanticMotionProgramsforSe.md
Saved: 2026-08-06 22:10
Source: 2026-08-06_09-16-06Z_VSMP_IMU_Video_GroundedSemanticMotionProgramsforSe.md
Model: None

---

## Summary  
The paper introduces VSMP‑IMU, a video‑grounded framework that generates synthetic IMU signals for human activity recognition by separating semantics from label preservation. It leverages structured Semantic Motion Programs (SMPs) to create controllable motion data grounded in actual activities. By grounding the synthesized IMUs to wearable domains, it addresses limitations of existing synthetic data methods. The study evaluates VSMP‑IMU on multiple datasets and shows significant gains over real‑only training.

## Key Contributions  
- Structured Semantic Motion Program (SMP) separates activity semantics from label‑preserving variation.  
- Video‑grounded generation yields sensor‑aware IMUs that are both controllable and realistic.  
- Demonstrated consistent performance improvements across low‑resource, long‑tail, and imbalanced settings.

## Methodology  
The authors extract an SMP from a given video using deep pose estimation and semantic segmentation, then augment the program to generate motion trajectories. These trajectories are converted into virtual IMU signals via physics‑based simulation and subsequently calibrated to match wearable sensor characteristics through domain grounding.

## Results  
VSMP‑IMU achieves an average Macro‑F1 of 78.33% on five public IMU‑HAR datasets, outperforming real‑only training by 9.77%, the strongest prior synthetic baseline by 4.04%, low‑resource training by 18.54%, and the prior baseline by >6%. In long‑tail evaluation it lifts tail‑class Macro‑F1 by 19.86% over real data and 4.76% over SOTA.

## Significance  
This work provides a practical, controllable source of wearable‑relevant synthetic sensor data that can alleviate labeling bottlenecks in HAR, especially for rare or imbalanced activities.

## Related Concepts  
Synthetic IMU generation, Semantic Motion Program (SMP), video grounding, wearable domain calibration, Macro‑F1 metric, low‑resource learning, long‑tail evaluation.
