# Summary: 2026-07-30_16-02-49Z_Negativecontrolsrevealvolume_drivenconfoundinginra.md
Saved: 2026-07-30 22:18
Source: 2026-07-30_16-02-49Z_Negativecontrolsrevealvolume_drivenconfoundinginra.md
Model: None

---

## Summary  
The paper introduces READII‑2‑ROQC, an open‑source framework that uses volume‑preserving negative controls to detect confounding in radiomics and imaging foundation model features caused by tumour volume or acquisition artefacts. It aims to assess whether extracted features reflect true spatial signals independent of volume changes. By generating voxel‑perturbed images across tumour, background, and whole‑image regions, the method compares feature behaviour between original and control images. The framework reveals that some models retain performance after spatial structure is destroyed, indicating volume‑driven confounding.

## Key Contributions  
- Introduces READII‑2‑ROQC, an open‑source framework for detecting volume‑driven or contextual confounding in radiomics and imaging foundation model features.  
- Demonstrates that multiple published survival and HPV‑status signatures persist after spatial perturbation, showing that some models are insensitive to volume changes (volume‑driven confounding).  
- Provides a scalable quality‑control strategy that can be applied across tumour volumes to improve interpretability of imaging biomarkers.

## Methodology  
The authors generate voxel‑perturbed images using READII‑2‑ROQC by applying configurable randomization strategies to tumour, background, and whole‑image regions while preserving overall volume. They extract PyRadiomics and foundation‑model features from original images and nine matched negative controls. Performance is evaluated on three public cancer imaging cohorts (3,552 tumour volumes), comparing feature stability and model predictions between original and control images.

## Results  
The framework shows that several models retain their predictive performance after spatial structure is destroyed, indicating volume‑driven confounding; others show significant degradation, suggesting context‑dependent signals. Reproducing published survival and HPV‑status signatures, the study confirms that some biomarkers are robust to volume changes while others are not.

## Significance  
This work addresses a critical problem of false biomarker discovery in radiomics and deep imaging by distinguishing true spatial signals from artefacts related to tumour volume or acquisition bias. By providing an open‑source QC tool, it enables reproducible pipelines and more biologically grounded biomarker development.

## Related Concepts  
Radiomics, imaging foundation models, negative controls, voxel‑perturbation, confounding, volumetric analysis, survival signatures, HPV status, PyRadiomics, spatial signal independence.
