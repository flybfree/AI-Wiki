# Summary: 2026-08-04_06-08-21Z_Tactus_Open_VocabularyObjectRecognitionfromLow_Cos.md
Saved: 2026-08-05 20:17
Source: 2026-08-04_06-08-21Z_Tactus_Open_VocabularyObjectRecognitionfromLow_Cos.md
Model: None

---

## Summary  
Tactus is an open‑vocabulary object recognition system that works from low‑cost pressure arrays without any optical imaging. It achieves performance comparable to supervised CNNs on the STAG benchmark using only pressure data and a small model that requires no trained classifier head. The approach relies on masked autoencoder pretraining and the sensor’s calibration affine transform, delivering robust results across paraphrased or bare‑name queries.

## Key Contributions  
- [Finding 1] Tactus reaches top‑1 accuracy of 0.771 ± 0.062 (top‑3 0.935) on the STAG benchmark with no trained classifier head.  
- [Finding 2] The model’s errors are limited to contact‑ambiguous classes, uncorrelated with text‑target geometry (Spearman ρ ≤ 0.05), and survive paraphrased or bare‑name queries within one point.  
- [Finding 3] Releasing the full model—including weights, code, and a plug‑in memory layer—enables open‑source deployment; alternative pretraining (cross‑sensor pooling) yields no gain.

## Methodology  
The authors trained a small neural network on 187 recordings of each of 27 objects. First, they pretrained it via masked autoencoder on 144 k unlabeled frames from the same sensor to learn latent representations. Then they fine‑tuned with the sensor’s calibration affine transform. The model is designed as a memory layer that can be inserted into existing pipelines.

## Results  
On STAG, Tactus achieves 0.771 top‑1 (4 runs) and 0.935 top‑3, matching or exceeding the supervised CNN benchmark of 0.76. Accuracy remains stable across paraphrased queries; two diverse frames recover 89% of eight‑frame accuracy. The released model’s errors are concentrated in a few ambiguous classes.

## Significance  
Tactus demonstrates that low‑cost pressure arrays can support open‑vocabulary object recognition, reducing reliance on expensive optical sensors and eliminating the need for a classifier head. By releasing the full model, it promotes reproducibility and further research on tactile perception.

## Related Concepts  
- Resistive pressure arrays  
- Masked autoencoder pretraining  
- Open‑vocabulary semantic search  
- Sensor calibration affine transform  
- STAG benchmark
