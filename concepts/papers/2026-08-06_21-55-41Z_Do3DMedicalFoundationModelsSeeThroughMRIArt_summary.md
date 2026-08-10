# Summary: 2026-08-06_21-55-41Z_Do3DMedicalFoundationModelsSeeThroughMRIArtifacts_.md
Saved: 2026-08-09 22:25
Source: 2026-08-06_21-55-41Z_Do3DMedicalFoundationModelsSeeThroughMRIArtifacts_.md
Model: None

---

## Summary  
The paper investigates whether 3D medical foundation models are robust to MRI artifacts and proposes a controlled study that evaluates representation robustness across five pretrained encoders under seven different corruption settings using the BraTS‑Africa dataset. It finds that robustness is strongly dependent on both model architecture and the type of artifact, with some models showing minimal degradation while others collapse dramatically.

## Key Contributions  
- Finding 1: Robustness varies markedly by model and artifact type, not merely by pretraining scale or domain.  
- Finding 2: 3DINO exhibits the most consistently stable representations, whereas BrainIAC is highly sensitive to ghosting and Rician noise.  
- Finding 3: Linear centered kernel alignment (CKA) drops substantially under many corruptions while RankMe remains comparatively stable, indicating geometry distortion without full dimensional collapse.

## Methodology  
The authors generated BraTS‑Africa cases with four MRI sequences and applied seven frequency‑ and image‑domain artifacts at five predefined corruption levels. Robustness was measured using linear centered kernel alignment (CKA), RankMe, UMAP visualizations, and an independent segmentation‑consistency analysis across the five pretrained 3D encoders.

## Results  
Robustness is model‑dependent: 3DINO shows high stability, BrainIAC degrades sharply with ghosting and Rician noise, NeuroVFM, BrainFM, and Neuro‑SimCLR show intermediate but distinct profiles. CKA decreases under many conditions while RankMe stays relatively constant; segmentation consistency also degrades—especially for ghosting and Rician noise—but only partially aligns with representation‑level robustness.

## Significance  
These findings demonstrate that larger scale or domain‑specific pretraining alone does not guarantee artifact invariance, underscoring the need for explicit robustness evaluation before deploying 3D foundation models in heterogeneous MRI settings. This guides future research toward more robust and reliable medical AI systems.

## Related Concepts  
- 3D medical foundation models; self‑supervised learning; representation robustness; MRI artifacts (ghosting, Rician noise); kernel alignment metrics (CKA, RankMe); UMAP visualizations; segmentation consistency.
