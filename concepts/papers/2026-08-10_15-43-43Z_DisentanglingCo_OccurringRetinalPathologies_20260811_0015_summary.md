# Summary: 2026-08-10_15-43-43Z_DisentanglingCo_OccurringRetinalPathologieswithSal.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-43-43Z_DisentanglingCo_OccurringRetinalPathologieswithSal.md
Model: None

---

## Summary  
Retinal fundus images often contain multiple co‑occurring pathologies that standard classifiers ignore. The paper proposes a sparse conditional computation framework that routes feature tokens to domain‑specific experts, producing an interpretable decomposition of disease presence. This approach enables the model to allocate computational resources only where they are needed, improving both efficiency and diagnostic insight. The proposed architecture is evaluated on a five‑class, patient‑disjoint benchmark and shows state‑of‑the‑art performance.

## Key Contributions  
- Finding 1: A Guided Context Gating (GCG) spatial attention front‑end provides disease‑aware saliency maps that guide expert routing.  
- Finding 2: Sparse Mixture‑of‑Experts (MoE) routing yields an interpretable, data‑driven decomposition with disease‑dependent expert allocation (p < 0.001).  
- Finding 3: The model achieves macro AUC = 0.912 ± 0.008 and macro F1 = 0.653 ± 0.014 on a five‑class, patient‑disjoint cross‑validation set.

## Methodology  
The authors address multi‑pathology detection by introducing conditional computation: each feature token is evaluated only by a subset of expert modules whose selection is driven by saliency scores computed with GCG. This sparsely‑routed MoE block reduces redundant calculations while preserving the ability to isolate distinct pathologies such as Normal, ERM, and AMD. The routing decision is learned jointly from image data and gradient saliency, ensuring that experts are allocated where lesions are most salient.

## Results  
On a five‑class, patient‑disjoint 5‑fold cross‑validation benchmark, our model achieves 0.912 ± 0.008 macro AUC and 0.653 ± 0.014 macro F1. These metrics surpass typical single‑pathology detectors by over 10% in AUROC, indicating robust performance across disease combinations. Grad‑CAM++ visualizations and post‑MoE t‑SNE plots confirm that expert routing aligns with localized lesions and correctly maps co‑occurring cases between their constituent clusters.

## Significance  
This interpretable routing enables clinicians to trust the model’s decomposition, supporting clinical decision‑making and facilitating future integration into automated screening pipelines. By allocating computation only to relevant disease regions, the approach improves both diagnostic accuracy and computational efficiency in real‑world settings.

## Related Concepts  
- Sparse Mixture‑of‑Experts (MoE)  
- Conditional computation  
- Guided Context Gating (GCG) spatial attention  
- Gradient saliency maps  
- t‑SNE visualization
