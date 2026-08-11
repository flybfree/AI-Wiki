# Summary: 2026-08-08_01-54-03Z_DistillingCTFoundationModelsintoEditableConceptBot.md
Saved: 2026-08-10 22:44
Source: 2026-08-08_01-54-03Z_DistillingCTFoundationModelsintoEditableConceptBot.md
Model: None

---

## Summary  
The authors propose a novel approach to make CT foundation‑model predictions interpretable by distilling them into eight radiologist‑defined pulmonary‑nodule concepts that can be edited and used for malignancy prediction. By training concept bottleneck models on two frozen embeddings—CT-FM (whole‑CT self‑supervised) and FMCIB (nodule‑focused contrastive)—they map these representations to nodule attributes and size, then predict malignancy using ridge regression heads. The method achieves discrimination comparable to nodule size alone while providing transparent feature contributions that can be altered through concept interventions. This work bridges the gap between high‑performing deep models and clinically interpretable diagnostic tools.  

## Key Contributions  
- [Finding 1] Concept bottleneck models improve interpretability by extracting eight radiologist‑defined attributes from frozen CT foundation‑model embeddings, enabling explainable malignancy predictions.  
- [Finding 2] FMCIB (nodule‑focused contrastive encoder) yields higher concept fidelity than CT-FM for subtlety, spiculation, texture, and lobulation, indicating that representation choice matters for bottleneck performance.  
- [Finding 3] The additive nature of the model allows controlled manipulation of concept predictions, demonstrating that feature contributions can be modified without retraining.  

## Methodology  
The authors first built two frozen CT foundation‑model encoders: CT-FM using a 96³‑voxel nodule‑centered patch for whole‑CT self‑supervision, and FMCIB using a 50 mm crop with contrastive learning. Both embeddings are then projected onto eight radiologist‑defined pulmonary‑nodule attributes (subtlety, spiculation, texture, lobulation, etc.) via ridge‑regression concept heads trained on the LIDC‑IDRI dataset of 2,610 nodules. Malignancy is predicted by regressing these concepts and nodule size with a simple linear model. The pipeline was evaluated internally on LUNA25 (held‑out test) and externally on DLCS cohort.  

## Results  
Internally, the concept+size models achieved AUROCs of 0.86 (95% CI 0.80–0.92) for both CT-FM and FMCIB, comparable to nodule size alone (0.73). Externally, AUROCs were 0.72 (0.68–0.75) for CT‑FM and 0.73 (0.70–0.76) for FMCIB, exceeding the size‑only probes (0.73) and embedding‑only probes (0.60, 0.67). Concept fidelity measured by five‑fold cross‑validated R² was modest but higher for FMCIB than CT‑FM across all attributes: subtlety 0.24 vs 0.11, spiculation 0.17 vs 0.08, texture 0.17 vs 0.07, lobulation 0.15 vs 0.05.  

## Significance  
By replacing opaque deep embeddings with transparent concept bottlenecks, the method enables clinicians to understand and intervene on prediction drivers, potentially improving trust and facilitating targeted interventions such as biopsy targeting. The findings also highlight that representation selection (whole‑CT vs nodule‑focused) critically influences bottleneck performance, guiding future foundation‑model integration in radiology.  

## Related Concepts  
- CT foundation models  
- Radiologist‑defined pulmonary‑nodule attributes  
- Concept bottleneck models  
- Ridge regression heads  
- Self‑supervised encoder (CT‑FM)  
- Contrastive encoder (FMCIB)  
- AUROC, R², bootstrap resampling
