# Summary: 2026-07-31_16-14-24Z_RadPRISM_Schema_stratifiedradiology_reportsupervis.md
Saved: 2026-08-03 20:15
Source: 2026-07-31_16-14-24Z_RadPRISM_Schema_stratifiedradiology_reportsupervis.md
Model: None

---

## Summary  
RadPRISM tackles the limitation of vision‑language pretraining that collapses concept information into a single shared embedding, making it hard to interpret or use for clinical tasks. By treating a clinician‑defined radiology schema as a stratification axis and assigning each concept its own visual subspace, RadPRISM creates disentangled image representations that are both discriminative and transparent to clinicians. The method improves zero‑shot classification, visual grounding, and retrieval performance while preserving spatial faithfulness of the representations.

## Key Contributions  
- [Finding 1] RadPRISM introduces a schema‑stratified supervision framework that aligns each clinical concept with its own dedicated visual subspace, enabling true concept‑level disentanglement.  
- [Finding 2] The method achieves macro AUROC 0.868 on internal zero‑shot classification (up from 0.717) and outperforms the state‑of‑the‑art CARZero in pointing‑game visual grounding by up to 4.3×, with comparable external zero‑shot results.  
- [Finding 3] A radiologist reader study shows a concept‑stratified retrieval correctness rate of 0.78 within rank 3, surpassing fixed‑label vocabularies and report‑level retrieval.

## Methodology  
RadPRISM leverages an on‑premise large language model to extract per‑concept text spans from free‑text radiology reports. The extracted spans are paired with corresponding image patches, and a dedicated visual subspace is created for each concept. During training the model learns to map these patches into their respective subspaces, providing supervision that directly enforces concept‑level alignment. This stratification axis replaces generic caption‑image pairs, allowing the network to learn spatially faithful, concept‑specific representations.

## Results  
The internal dataset contains 203 602 chest radiographs and a 19‑concept schema. Macro AUROC for zero‑shot classification rose from 0.717 (baseline) to 0.868 (RadPRISM, 95% CI 0.863–0.872). External benchmarking shows RadPRISM matches CARZero’s zero‑shot performance while delivering up to a 4.3‑fold gain in visual grounding accuracy. The radiologist retrieval study reports a macro correctness rate of 0.78 within the top three retrieved concepts, indicating strong clinical interpretability.

## Significance  
By making concept stratification a first‑class training objective, RadPRISM bridges the gap between language and image semantics, delivering representations that are both high‑performing and clinically interpretable. The disentangled subspaces enable precise retrieval of specific findings, supporting decision support tools without sacrificing accuracy or spatial fidelity.

## Related Concepts  
vision‑language pretraining, schema stratification, concept disentanglement, visual grounding, zero‑shot classification, radiology report supervision, clinical interpretability.
