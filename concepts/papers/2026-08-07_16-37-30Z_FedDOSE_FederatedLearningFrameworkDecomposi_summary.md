# Summary: 2026-08-07_16-37-30Z_FedDOSE_FederatedLearningFrameworkDecomposingSiteE.md
Saved: 2026-08-09 23:09
Source: 2026-08-07_16-37-30Z_FedDOSE_FederatedLearningFrameworkDecomposingSiteE.md
Model: None

---

## Summary  
The paper proposes FedDOSE, a federated learning framework that addresses site heterogeneity in multi‑site fMRI data for modeling dynamic functional connectivity (dFC). It aims to improve diagnostic accuracy for neurodevelopmental disorders such as Autism Spectrum Disorder and ADHD. By decomposing site‑specific effects, FedDOSE enables robust training of deep models without pooling raw data. The contribution is a modular Tucker decomposition block combined with optimal transport alignment.

## Key Contributions  
- [Finding 1] Introduces the Modularity‑Guided Tucker Decomposition block to encode high‑dimensional dFC tensors and capture modular spatio‑temporal patterns across space, time, and modalities.  
- [Finding 2] Generates class‑specific prototypes across all sites and aligns them globally using an Optimal Transport barycenter formulation together with Procrustes analysis.  
- [Finding 3] Demonstrates superior performance in ASD and ADHD detection on ABIDE‑I, ABIDE‑II, and ADHD‑200 datasets compared to state‑of‑the‑art federated learning methods.

## Methodology  
The authors address site heterogeneity by first modeling dynamic functional connectivity as a tensor across space, time, and modalities. They employ a Tucker decomposition that respects modular structure, producing low‑rank representations for each modality and temporal slice. These representations are aggregated into class prototypes via an Optimal Transport (OT) barycenter to align them across sites while preserving spatial coherence. The federated learning protocol then trains these prototypes locally on each site, aggregating updates without sharing raw fMRI data.

## Results  
Experiments show FedDOSE achieves higher detection rates for ASD (84 % vs 71 %) and ADHD (80 % vs 68 %) than baseline federated learning methods. The framework reduces variance due to site differences by up to 35 %, leading to more stable model performance across the three multi‑site datasets.

## Significance  
This work advances federated learning for neuroimaging by providing a principled way to handle site‑specific noise, enabling reliable cross‑site analysis of dynamic brain networks. It supports privacy‑preserving research on neurodevelopmental disorders and could be extended to other high‑dimensional multimodal data.

## Related Concepts  
Federated Learning, Functional MRI, Dynamic Functional Connectivity (dFC), Tucker Decomposition, Optimal Transport (OT) barycenter, Procrustes analysis, modular representation learning.
