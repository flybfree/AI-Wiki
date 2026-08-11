# Summary: 2026-08-10_15-22-37Z_PET_CTRadiogenomicMutationPredictioninNon_SmallCel.md
Saved: 2026-08-10 23:53
Source: 2026-08-10_15-22-37Z_PET_CTRadiogenomicMutationPredictioninNon_SmallCel.md
Model: None

---

## Summary  
The paper aims to develop PET/CT radiogenomic prediction of EGFR, TP53 and KRAS mutations in non‑small cell lung cancer using multi‑label deep learning. It introduces a novel UK‑based dataset and evaluates joint pre‑diction versus conventional single‑gene classification. Multi‑label learning improves the area under the ROC curve (AUC) for certain mutation pairs but not all, revealing that its effectiveness is context‑dependent. This work constitutes one of the first systematic investigations of multi‑label learning for radiogenomic prediction in NSCLC.

## Key Contributions  
- Joint pre‑diction of KRAS and TP53 improves AUC from 0.58 to 0.64 for KRAS and from 0.69 to 0.71 for TP53.  
- Only the EGFR/KRAS pair benefits from joint learning, while the EGFR/TP53 pair shows no improvement.  
- Multi‑label learning effectiveness depends on the specific combination of gene mutations being modelled, suggesting that mutation‑specific strategies may be preferable.

## Methodology  
The authors employed a deep‑learning framework for multi‑label classification, training models on PET/CT images and genomic data extracted from a UK radiogenomics cohort. They compared single‑gene classifiers with pairwise multi‑label models using AUC as the primary evaluation metric to assess the impact of joint pre‑diction.

## Results  
Joint pre‑diction yields higher AUCs for KRAS (0.64) and TP53 (0.71). The EGFR/KRAS pair benefits from learning, whereas the EGFR/TP53 pair does not show improvement over single‑gene baselines. These findings demonstrate that multi‑label approaches can be advantageous when the targeted mutations are co‑occurring.

## Significance  
This study provides a non‑invasive alternative to tissue biopsy for predicting actionable NSCLC mutations via PET/CT, and it highlights that predictive performance varies with mutation pairings, guiding clinicians toward tailored modeling strategies. The work advances radiogenomics by integrating imaging and genetics in a clinically relevant setting.

## Related Concepts  
- Radiogenomics  
- PET/CT imaging  
- Deep learning  
- Multi‑label classification  
- AUC (Area Under the ROC Curve)  
- NSCLC (non‑small cell lung cancer)  
- EGFR, TP53, KRAS mutations
