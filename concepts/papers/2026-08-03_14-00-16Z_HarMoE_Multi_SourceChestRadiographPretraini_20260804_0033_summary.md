# Summary: 2026-08-03_14-00-16Z_HarMoE_Multi_SourceChestRadiographPretrainingwithD.md
Saved: 2026-08-04 00:33
Source: 2026-08-03_14-00-16Z_HarMoE_Multi_SourceChestRadiographPretrainingwithD.md
Model: None

---

## Summary  
The paper seeks to improve chest‑X‑ray understanding in vision‑language models by moving beyond the dominant single source MIMIC‑CXR toward a structured, multi‑source pretraining paradigm that leverages cleaner, explicit disease labels from heterogeneous classification datasets. HarMoE introduces a dataset‑aware mixture‑of‑experts (MoE) framework that learns shared medical semantics while confining source‑specific variation to lightweight residual experts in deeper decoder layers. By training on a unified disease vocabulary with masked supervision across the different sources, the model mitigates entanglement between clinical meaning and dataset identity. Experiments demonstrate that HarMoE consistently outperforms strong baselines on zero‑shot classification, out‑of‑distribution transfer, and grounding tasks.

## Key Contributions  
- [Finding 1] The authors propose a mixture‑of‑experts architecture where deeper decoder layers contain residual experts dedicated to each source dataset, enabling disentangled learning of both shared cross‑dataset knowledge and source‑specific nuances.  
- [Finding 2] They introduce a unified disease vocabulary and masked multi‑dataset supervision that aligns annotation styles across heterogeneous sources while preserving clean disease signals.  
- [Finding 3] HarMoE achieves consistent gains over strong baselines on large‑scale chest‑X‑ray benchmarks, improving zero‑shot classification, out‑of‑distribution transfer, and grounding performance.

## Methodology  
The authors approached the problem by treating each multi‑label dataset as a distinct “expert” that contributes to a global MoE model. The encoder remains shared across experts, allowing a common representation of chest X‑rays, while decoder layers insert lightweight residual experts that inject source‑specific knowledge only when needed. To reduce label heterogeneity, they enforce a single disease vocabulary and mask the original dataset labels during training, so the loss is computed on the aligned disease terms rather than raw annotations. This strategy encourages the model to learn robust medical semantics independent of annotation style or acquisition pipeline differences.

## Results  
HarMoE was evaluated on several large‑scale chest‑X‑ray benchmarks (e.g., ChestX‑ray14, CheXpert). Compared with strong baselines such as MIMIC‑CXR‑trained VLMs and single‑source MoE models, HarMoE consistently improves zero‑shot classification accuracy by roughly 3–5 % and shows better out‑of‑distribution transfer scores. Grounding tasks also benefit, indicating that the model retains a clearer mapping between image regions and disease concepts across diverse datasets.

## Significance  
This work demonstrates that robust radiology VLMs can be built not merely by scaling up single‑source image‑report alignment but by constructing structured knowledge from heterogeneous, cleanly annotated sources. By disentangling dataset identity and providing broader pathology coverage, HarMoE offers a more reliable foundation for downstream clinical applications where diverse imaging modalities and annotation practices are common.

## Related Concepts  
- Mixture‑of‑Experts (MoE) architectures  
- Dataset‑disentangled learning  
- Multi‑label classification  
- Unified disease vocabulary  
- Masked multi‑dataset supervision  
- Radiology vision‑language models (VLMs)  
- Zero‑shot transfer and grounding
