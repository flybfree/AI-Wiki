# Summary: 2026-07-21_02-15-33Z_DeepLearningEstimationofSex_Age_Height_andWeightfr.md
Saved: 2026-07-24 00:46
Source: 2026-07-21_02-15-33Z_DeepLearningEstimationofSex_Age_Height_andWeightfr.md
Model: None

---

## Summary  
This paper presents a deep learning ensemble model designed to estimate adult sex, age, height, and weight from coronal digitally reconstructed radiographs (DRRs) derived from diagnostic CT scans. The study demonstrates that combining three state-of-the-art vision transformers—ConvNeXt-Base, ViT-Base/16, and MaxViT-Base—into a weighted averaging ensemble significantly improves estimation accuracy across multiple clinical parameters. The model was validated on a large Japanese cohort of 80,044 adults and further tested for generalizability to non-Japanese datasets, showing robust performance with minimal error propagation. This work bridges the gap between high-resolution CT imaging and rapid anthropometric assessment without requiring additional patient measurements.

## Key Contributions  
- [Finding 1] The ensemble model achieves near-perfect sex classification (99.7% accuracy) and low MAEs for age, height, and weight estimation, outperforming individual models through improved generalization.  
- [Finding 2] BSA-corrected heart and liver volume trends align precisely with estimated height and weight values, confirming the physiological relevance of the model’s outputs.  
- [Finding 3] The model maintains high accuracy (100%) on examinations covering chest to pelvis, with MAEs as low as 2.28 cm for height and 3.18 kg for weight, highlighting its clinical utility across full-body DRR views.

## Methodology  
The authors developed a multitask deep learning ensemble using coronal DRRs from 128,621 CT scans of adults aged 18–90 at nine Japanese institutions. Three transformer-based models—ConvNeXt-Base, ViT-Base/16, and MaxViT-Base—were fine-tuned on the training set (7 institutions) to predict sex classification and regression outputs for age, height, and weight. A tuning set was used for hyperparameter optimization, while a test set from one institution evaluated final performance. Accuracy was measured via correct sex prediction and MAE for continuous variables. Generalizability was tested on two non-Japanese datasets, with fine-tuning applied to reduce ethnic bias.

## Results  
In the test set (median age 69.9 years; 48.2% male), sex classification accuracy reached 0.997 with a 95% CI of 0.996–0.998, MAE for age was 3.57 years, height 2.59 cm, and weight 3.40 kg. On full-body DRR views (chest to pelvis), accuracy improved to 1.000 with lower MAEs: 3.15 years, 2.28 cm, and 3.18 kg. BSA-calculated from estimated values reproduced true age-related trends in heart and liver volumes, validating the model’s physiological consistency. On non-Japanese datasets, height error increased but was mitigated through fine-tuning.

## Significance  
This study enables rapid, accurate anthropometric estimation directly from CT-derived DRRs, reducing reliance on manual measurements or patient self-reporting. The ensemble approach improves diagnostic and therapeutic decision-making in fields such as pediatrics, oncology, and cardiology by providing objective estimates of growth, disease progression, and metabolic health.

## Related Concepts  
- Digital Reconstructed Radiographs (DRR)  
- Vision Transformers (ViT), ConvNeXt  
- Multitask Learning  
- Body Surface Area (BSA)  
- Generalizability in AI models  
- CT-derived imaging  
- Age-related organ volume trends
