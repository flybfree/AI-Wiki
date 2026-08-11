# Summary: 2026-08-08_03-43-58Z_AuditingInstruction_TrajectoryMismatchesinMultimod.md
Saved: 2026-08-10 22:48
Source: 2026-08-08_03-43-58Z_AuditingInstruction_TrajectoryMismatchesinMultimod.md
Model: None

---

## Summary  
The paper addresses the problem of instruction‑trajectory mismatches (ITMs) in multimodal robot demonstrations where a behaviorally correct action is paired with an incorrect language label, potentially corrupting policy learning. It proposes a training‑free auditing framework called Multimodal Probabilistic Fusion (MMPF) to detect and correct these mismatches by leveraging modality‑specific expert models.

## Key Contributions  
- [Finding 1] ITMs are subtle but harmful failure modes that can mislead multimodal policies.  
- [Finding 2] MMPF provides a training‑free auditing framework that estimates task‑label distributions using local neighborhood agreement and global prototype similarity across modalities.  
- [Finding 3] Empirical results show MMPF achieves the highest detection and correction accuracy on LIBERO benchmarks, improves downstream policy learning when language is needed for disambiguation, and demonstrates real robot performance gains.

## Methodology  
The authors treat each modality (vision, language, action) as an expert that predicts a task label. They first compute local agreement by measuring similarity of neighboring demonstrations in the same modality and globally estimate prototype similarity across all demonstrations. Using these distributions, MMPF fuses modalities with predictive‑entropy weighting, producing a product of experts to generate a unified probability distribution over labels. The framework is applied post‑hoc without retraining the policy; it flags mismatched instruction‑trajectory pairs for correction.

## Results  
Across LIBERO benchmark datasets containing both injected ITMs and noisy real robot data, MMPF outperforms baseline methods in detecting mismatches (average detection rate 92 % vs. 78 %) and correcting labels (accuracy 89 % vs. 65 %). The corrected policies achieve a 4.3 % increase in success rate on downstream tasks requiring language cues. Real robot experiments show improved performance with MMPF‑filtered demonstrations compared to simple relabeling, while maintaining comparable training time.

## Significance  
This work highlights that instruction‑trajectory mismatches are a critical failure mode for multimodal robot learning pipelines, and introduces a scalable, model‑free auditing technique that can be integrated into existing training loops. By correcting these errors before policy deployment, MMPF enhances safety, reliability, and performance of robotic demonstrations.

## Related Concepts  
- Instruction‑Trajectory Mismatch (ITM)  
- Multimodal Probabilistic Fusion (MMPF)  
- Expert fusion in machine learning  
- Prototype‑based representation learning  
- Post‑hoc auditing
