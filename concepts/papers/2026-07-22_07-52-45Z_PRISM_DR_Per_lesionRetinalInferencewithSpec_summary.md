# Summary: 2026-07-22_07-52-45Z_PRISM_DR_Per_lesionRetinalInferencewithSpecialistM.md
Saved: 2026-07-24 01:36
Source: 2026-07-22_07-52-45Z_PRISM_DR_Per_lesionRetinalInferencewithSpecialistM.md
Model: None

---

## Summary  
Diabetic retinopathy screening suffers from small, low‑contrast lesions that are hard to detect with a single multi‑class model, which tends to favor common classes over rare ones. This paper introduces PRISM‑DR, a lesion‑specific pipeline that trains four separate detectors—one per non‑proliferative DR lesion type—to improve detection of each class individually. The system combines region cropping, fundus preprocessing, YOLO detections, tiling, cross‑validation ensembling, and per‑lesion selection to achieve higher accuracy on difficult lesions like hard exudates. By treating each lesion as an independent problem, PRISM‑DR offers a practical alternative to conventional multi‑class approaches.  

## Key Contributions  
- The authors demonstrate that training separate single‑class detectors for microaneurysms, hemorrhages, hard exudates, and soft exudates yields higher AP50 scores than a shared model.  
- A per‑lesion ensembling strategy using five cross‑validation folds improves robustness and selects the best detection per lesion.  
- Bayesian optimization tunes augmentation parameters for each detector, enhancing generalization across imaging scales.  

## Methodology  
The pipeline begins with raw fundus images, applying region of interest cropping to focus on the retinal area and performing fundus‑specific preprocessing such as histogram equalization. Four parallel YOLO detectors are then trained—one per lesion class—to detect their respective features. The full image is tiled into overlapping patches to ensure coverage of small lesions. Each patch generates detections from all four models, which are aggregated; the best detection for each lesion across five cross‑validation folds is chosen as the final result. An inter‑lesion suppression step resolves overlaps by applying physical size constraints and clinical priority, prioritizing high‑confidence predictions. Bayesian optimization selects augmentation strategies that maximize validation performance while preserving diagnostic quality.  

## Results  
Trained on IDRiD with stratified five‑fold cross‑validation, PRISM‑DR achieves a test mAP50 of 0.527 and F1 of 0.529 overall. The hard exudate detector reaches the highest AP50 at 0.561, outperforming other lesion detectors. When fine‑tuning is omitted, models retain transferability when the field of view and resolution are close to IDRiD; however, performance degrades with larger FOVs or lower resolution. These results reflect modest absolute gains due to limited single‑source data and a challenging task, yet they validate the value of lesion‑specific modeling.  

## Significance  
Treating diabetic retinopathy lesions as distinct detection problems can lead to more reliable screening, especially for rare and visually subtle classes like hard exudates that are often missed by shared models. By enabling per‑lesion optimization, PRISM‑DR contributes a practical framework for future multi‑task retinal AI systems, potentially reducing false negatives and improving early diagnosis.  

## Related Concepts  
- Lesion‑specific detection  
- Single‑class object detectors (YOLO)  
- Cross‑validation ensembling  
- Bayesian optimization of augmentation  
- IDRiD dataset
