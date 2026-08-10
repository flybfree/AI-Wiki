# Summary: 2026-08-07_16-37-30Z_FedDOSE_FederatedLearningFrameworkDecomposingSiteE.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_16-37-30Z_FedDOSE_FederatedLearningFrameworkDecomposingSiteE.md
Model: None

---

## Summary  
The paper proposes FedDOSE, a federated learning framework that decomposes site‑specific effects to model dynamic functional connectivity in fMRI for psychiatric diagnosis. It addresses the statistical heterogeneity between multi‑site data while preserving privacy and capturing spatio‑temporal patterns. By integrating modular decomposition and optimal transport alignment, FedDOSE enables robust classification of Autism Spectrum Disorder (ASD) and Attention‑Deficit Hyperactivity Disorder (ADHD).

## Key Contributions  
- [Finding 1] FedDOSE introduces a Modularity‑Guided Tucker Decomposition block that efficiently encodes high‑dimensional dynamic functional connectivity tensors into modular components.  
- [Finding 2] The framework generates class‑specific prototypes across sites and aligns them globally using an optimal transport barycenter formulation combined with Procrustes analysis, mitigating site effects.  
- [Finding 3] FedDOSE outperforms state‑of‑the‑art methods in diagnosing ASD and ADHD on ABIDE‑I, ABIDE‑II, and ADHD‑200 datasets.

## Methodology  
The authors tackled the challenge of statistical heterogeneity across multi‑site fMRI data by first decomposing dynamic connectivity tensors into modular patterns using Tucker decomposition tailored to site‑specific variability. They then created class prototypes per site and aligned them globally via an optimal transport barycenter that minimizes transport cost, followed by Procrustes alignment for orientation correction. This modular encoding reduces dimensionality while preserving spatial‑temporal structure, enabling federated training where each site updates its own representation without sharing raw data.

## Results  
Experiments on three multi‑site resting‑state fMRI datasets—ABIDE‑I (autism), ABIDE‑II (autism), and ADHD‑200 (ADHD)—showed that FedDOSE achieved higher diagnostic accuracy than baseline federated methods, with AUC improvements of up to 12 % for ASD and 9 % for ADHD. The modular prototypes captured distinct network patterns per condition, and the alignment step reduced site‑to‑site variance, leading to more consistent predictions across sites.

## Significance  
FedDOSE demonstrates that decomposing site effects is crucial for reliable federated analysis of dynamic brain connectivity. By preserving privacy while improving diagnostic performance, it offers a scalable solution for large‑scale neuroimaging consortia seeking actionable insights without compromising data security.

## Related Concepts  
- Federated Learning (FL)  
- Dynamic Functional Connectivity (dFC)  
- Optimal Transport (OT) barycenter formulation  
- Procrustes analysis  
- Tucker Decomposition  
- Modularity‑guided representation learning
