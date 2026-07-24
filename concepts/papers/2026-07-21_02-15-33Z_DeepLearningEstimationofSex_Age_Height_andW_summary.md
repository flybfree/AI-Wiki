# Summary: 2026-07-21_02-15-33Z_DeepLearningEstimationofSex_Age_Height_andWeightfr.md
Saved: 2026-07-24 00:29
Source: 2026-07-21_02-15-33Z_DeepLearningEstimationofSex_Age_Height_andWeightfr.md
Model: None

---

## Summary  
This study aimed to create a deep‑learning ensemble capable of estimating adult sex, age, height, and weight directly from coronal digitally reconstructed radiographs (DRRs) derived from diagnostic CT scans. By training multiple state‑of‑the‑art multitask models—ConvNeXt‑Base, ViT‑Base/16, and MaxViT‑Base—and combining their predictions with weighted averaging, the authors achieved high‑precision estimates that closely match measurements obtained from body‑surface area (BSA) correction of true height and weight. The approach also reproduced age‑related trends in heart and liver volumes, suggesting a potential clinical utility for non‑invasive patient stratification.

## Key Contributions  
- [Finding 1] An ensemble of three fine‑tuned multitask deep‑learning models attains sex‑classification accuracy of 0.997 and regression MAEs of 3.57 years, 2.59 cm, and 3.40 kg on a test set of 10,169 examinations.  
- [Finding 2] BSA‑corrected heart and liver volume trends derived from the true height/weight values are reproduced by the estimated values, indicating that the model captures underlying physiological relationships.  
- [Finding 3] Fine‑tuning the ensemble on non‑Japanese datasets reduces height error despite a modest increase in overall error, demonstrating improved generalizability.

## Methodology  
The authors performed a retrospective analysis of 128,621 CT examinations from 80,004 adults across nine Japanese institutions. Three convolutional and transformer‑based multitask models were fine‑tuned on coronal DRRs to predict sex (binary), age (continuous), height (continuous), and weight (continuous). Predictions from each model were combined via weighted averaging. The dataset was stratified into training (114,147 exams; seven institutions), tuning (4,305; one institution) and test (10,169; one institution) sets to evaluate generalizability. Accuracy measured sex classification accuracy; mean absolute error (MAE) evaluated age, height, and weight regressions.

## Results  
In the Japanese test set (median age 69.9 years), sex‑classification accuracy was 0.997 with a 95 % CI of 0.996–0.998; MAEs were 3.57 years for age, 2.59 cm for height, and 3.40 kg for weight. When examinations covered the chest through pelvis, sex accuracy reached 1.000 with lower MAEs of 3.15 years, 2.28 cm, and 3.18 kg. BSA‑calculated from estimated height/weight reproduced age‑dependent heart and liver volume trends observed using true values. On two non‑Japanese datasets, height error increased but was mitigated by additional fine‑tuning.

## Significance  
The ensemble provides a fast, non‑invasive method for estimating vital anthropometric parameters directly from CT‑derived DRRs, enabling clinical decision support such as patient stratification and risk assessment without the need for manual measurement. Its ability to reproduce physiological volume trends suggests that the model may also serve as a surrogate for organ health monitoring.

## Related Concepts  
- Deep learning ensemble  
- Multitask learning (sex classification + regression)  
- Digital reconstruction radiograph (DRR) from CT  
- Body‑surface area (BSA) correction  
- Heart and liver volume trends  
- Generalizability across populations  
- Weighted averaging of model outputs
