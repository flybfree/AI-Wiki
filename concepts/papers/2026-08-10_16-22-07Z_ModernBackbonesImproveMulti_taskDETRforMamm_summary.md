# Summary: 2026-08-10_16-22-07Z_ModernBackbonesImproveMulti_taskDETRforMammography.md
Saved: 2026-08-10 23:57
Source: 2026-08-10_16-22-07Z_ModernBackbonesImproveMulti_taskDETRforMammography.md
Model: None

---

## Summary  
The paper proposes a multi‑task DETR framework that jointly predicts image‑level malignancy in mammography and the precise location of lesions, leveraging shared representations to improve diagnostic support. It evaluates several state‑of‑the‑art CNNs on two benchmark datasets—OPTIMAM (biopsy‑confirmed) and SGM1k (clinical)—and shows that modern backbones consistently outperform older ResNet‑style features. ConvNeXtV2 leads the pack on OPTIMAM, while DINOv3 dominates on SGM1k, highlighting the importance of backbone selection for this task. The work advances AI‑assisted mammography by integrating classification and localization into a single model.

## Key Contributions  
- Modern backbones (ConvNeXtV2, DINOv3) outperform older ResNet features in joint multi‑task DETR for mammography.  
- ConvNeXtV2 achieves the highest overall metrics on OPTIMAM; DINOv3 provides the strongest performance on SGM1k.  
- MambaVision underperforms relative to other backbones, indicating it is less suitable for this application.

## Methodology  
The authors construct a shared representation network within DETR that serves two task heads: one for image‑level malignancy classification and another for lesion localization. They train the model jointly on both tasks using the OPTIMAM (biopsy‑confirmed) and SGM1k (clinical) datasets, selecting among ResNet‑50, ConvNeXtV2, DINOv3, and MambaVision as backbone candidates.

## Results  
On OPTIMAM, ConvNeXtV2 yields 97.96 % AUC, 99.89 % sensitivity, 25.08 % mAP@.5, and 74.38 % recall@.25. On SGM1k, DINOv3 achieves 90.97 % AUC, 86.28 % sensitivity, 82.00 % specificity, 27.04 % mAP@.5, and 77.32 % recall@.25.

## Significance  
These findings demonstrate that backbone quality is a critical factor in effective multi‑task mammography AI; integrating classification and localization improves diagnostic accuracy and enables more reliable clinical support systems.

## Related Concepts  
DETR (Detection Transformer), multi‑task learning, ConvNeXtV2, DINOv3, MambaVision, AUC, sensitivity, specificity, mAP@.5, recall@.25, ResNet, OPTIMAM dataset, SGM1k dataset.
