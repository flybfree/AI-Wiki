# Summary: 2026-07-30_17-43-46Z_VAD_AttributingVisualEvidenceforTargetReconstructi.md
Saved: 2026-07-30 22:23
Source: 2026-07-30_17-43-46Z_VAD_AttributingVisualEvidenceforTargetReconstructi.md
Model: None

---

## Summary  
The paper addresses the challenge of multimodal on‑policy distillation where teacher corrections are source‑mixed, making it hard to attribute which visual evidence supports a correction. They propose Visual Attribution Distillation (VAD), a counterfactual target‑reconstruction method that estimates the visually attributable part of each correction. By comparing teacher outputs with and without specific visual evidence, VAD creates a signed proxy for evidence direction, guiding reconstruction of student‑anchored targets. The approach replaces source‑mixed supervision with this reconstructed target while using the privileged teacher only as a weak regularizer.  

## Key Contributions  
- [Finding 1] VAD introduces a counterfactual target‑reconstruction framework that separates visually attributable corrections from linguistic priors, enabling precise attribution of visual evidence.  
- [Finding 2] The method uses centered log‑probability differences between teacher outputs with and without specific evidence to generate a proxy that quantifies how evidence supports or refutes candidate tokens.  
- [Finding 3] Experiments on six fine‑grained benchmarks at 4B and 9B scale show VAD outperforms both direct privileged‑view distillation and visual‑advantage weighting, delivering stronger token‑level target shifts especially when evidence contradicts the teacher.  

## Methodology  
The authors evaluate each student‑generated prefix by applying the same fixed teacher model twice: once with the relevant visual evidence present in the input and once with that evidence removed. The difference in centered log‑probabilities (CLP) between these two runs is interpreted as a signed proxy, ut, indicating the direction of visual influence on the correction. VAD then projects the original teacher correction onto this proxy to obtain an intervention‑aligned component, while the residual is considered unexplained. This aligned component is used to reconstruct a target that aligns with the student’s prefix and the evidence, which serves as primary supervision; the privileged teacher provides only a weak regularizer.  

## Results  
Across six fine‑grained visual benchmarks (e.g., ImageNet‑1K, Visual Genome), VAD achieves higher token‑level accuracy than baseline methods. Controlled‑target analyses reveal that the proxy‑aligned component is enriched in task‑relevant visual corrections and produces larger target shifts when evidence refutes a teacher’s answer. The improvement is consistent at both 4B and 9B parameter scales, demonstrating scalability.  

## Significance  
VAD advances multimodal on‑policy distillation by replacing opaque source‑mixed supervision with interpretable counterfactual reconstruction, improving model alignment and reducing overfitting to non‑visual priors. This method provides a principled way to attribute visual evidence to specific corrections, which is crucial for robust vision‑language models.  

## Related Concepts  
- Multimodal on‑policy distillation (OPD)  
- Privileged‑view teacher  
- Centered log‑probability difference  
- Counterfactual reasoning  
- Visual attribution  
- Target reconstruction
