# Summary: 2026-08-02_02-55-32Z_GraRe_GraspCandidateRe_RankingforFrozen6_DoFGraspD.md
Saved: 2026-08-03 21:30
Source: 2026-08-02_02-55-32Z_GraRe_GraspCandidateRe_RankingforFrozen6_DoFGraspD.md
Model: None

---

## Summary  
The paper demonstrates that frozen 6‑DoF grasp detectors often rank high‑quality grasps low because their confidence scores are misaligned with actual grasp quality. To remedy this, the authors introduce GraRe, a dedicated re‑ranking module that estimates grasp quality from candidate attributes, local geometry, and object context without modifying the detector itself. By fusing these three feature types with a Transformer and combining the predicted quality with detector confidence, they obtain a more accurate ordering of grasp candidates.

## Key Contributions  
- Finding 1: Detector confidence is frequently poor at reflecting true grasp quality in frozen 6‑DoF detectors.  
- Finding 2: A separate re‑ranking task can improve candidate ordering without altering the detector or its input representations.  
- Finding 3: The GraRe model, built on a Transformer that fuses attribute‑conditioned local geometry and object context, yields up to 13.60 points gain in Average AP.

## Methodology  
The authors treat grasp candidate re‑ranking as an auxiliary downstream task. For each candidate they compute three representations: (i) attributes that condition the representation, (ii) shell‑stratified local geometry extracted from the detector output, and (iii) object context derived from the surrounding scene. A Transformer encoder fuses these heterogeneous features into a unified quality embedding. The predicted grasp quality is then added to the original detector confidence to produce the final ranking score.

## Results  
Experiments on GraspNet‑1Billion with three frozen detectors show consistent improvements, achieving gains of up to 13.60 points in Average AP compared with baseline re‑ranking methods. Real‑robot tests in cluttered scenes confirm that the improved ordering enables robust grasping without additional hardware or retraining.

## Significance  
Improving candidate ranking is a practical way to enhance frozen grasp detectors, allowing higher‑quality grasps to be selected even when the detector cannot be updated. This approach reduces reliance on expensive fine‑tuning and can be applied across diverse datasets and robot platforms.

## Related Concepts  
- 6‑DoF grasp detection  
- Detector confidence scoring  
- Grasp candidate re‑ranking  
- Transformer fusion of heterogeneous features  
- Local geometry extraction  
- Object context modeling  
- Grasp quality estimation
