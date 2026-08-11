# Summary: 2026-08-09_03-13-51Z_MGMCL_Multi_GranularityManifoldContrastiveLearning.md
Saved: 2026-08-10 23:11
Source: 2026-08-09_03-13-51Z_MGMCL_Multi_GranularityManifoldContrastiveLearning.md
Model: None

---

## Summary  
The paper aims to improve cross‑subject EEG emotion recognition by learning continuous representations on Riemannian manifolds that preserve affective continuity across subjects and individuals. It introduces MGMCL, a multi‑granularity manifold contrastive learning framework anchored in neural ODEs, which aligns subject‑specific manifolds via Gromov‑Wasserstein distance while respecting semantic ordering of valence, arousal, and dominance dimensions. By modeling emotions as trajectories on symmetric positive definite manifolds, the method enables weakly supervised prediction from discrete labels. The approach achieves state‑of‑the‑art accuracy improvements across three benchmark datasets.

## Key Contributions  
- Multi‑granularity manifold contrastive learning that operates at instance, emotion, and trajectory levels while preserving semantic ordering.  
- Neural ordinary differential equations on Riemannian manifolds to model continuous emotion dynamics.  
- Gromov‑Wasserstein manifold alignment for cross‑subject generalization in weakly supervised settings.

## Methodology  
The authors first embed each EEG recording into a high‑dimensional vector space that is mapped onto a symmetric positive definite (SPD) Riemannian manifold using a learned embedding. They then construct three contrastive objectives: one aligning individual samples within the same emotion, another aligning emotional states across subjects at the trajectory level, and a third preserving the ordering of valence, arousal, and dominance dimensions. Neural ODEs are employed to generate smooth trajectories on these manifolds, which serve as features for contrastive loss functions. The manifold alignment is performed via Gromov‑Wasserstein distance minimization between subject embeddings, ensuring that the learned representations respect the intrinsic geometry of emotion dynamics.

## Results  
On three public EEG datasets—SEED (91.23% accuracy), SEED‑IV (73.82%), and DEAP (76.38%)—MGMCL outperforms prior methods by 1.89%, 1.66%, and 1.28% respectively, establishing a new state‑of‑the‑art benchmark for cross‑subject emotion recognition.

## Significance  
This work bridges the gap between discrete emotional labels and continuous affective dynamics, enabling more robust and generalizable emotion classifiers that respect human perception of valence, arousal, and dominance as an ordered continuum. By leveraging Riemannian geometry and neural ODEs, MGMCL provides a principled framework for learning on manifolds where Euclidean assumptions fail.

## Related Concepts  
Riemannian manifold, SPD embedding, neural ordinary differential equations (Neural ODE), Gromov‑Wasserstein distance, contrastive learning, valence‑arousal‑dominance space, weakly supervised classification.
