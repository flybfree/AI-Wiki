# Summary: 2026-08-04_18-18-29Z_InterpretableFuzzyInferenceforUAVTargetTrackingUsi.md
Saved: 2026-08-05 23:11
Source: 2026-08-04_18-18-29Z_InterpretableFuzzyInferenceforUAVTargetTrackingUsi.md
Model: None

---

## Summary  
The paper proposes an interpretable fuzzy‑inference framework that enables a UAV to continuously estimate its yaw toward a ground target using only low‑dimensional features extracted from YOLO bounding boxes. By leveraging the centroid location, area, and aspect ratio of each box, the system generates a continuous yaw command without requiring explicit geometric models or large training datasets. The approach combines a Mamdani fuzzy system with a compact Takagi–Sugeno model, producing a 27‑rule structure that can be trained from quantiles of a motion‑capture dataset. This method promises real‑time, low‑compute guidance suitable for resource‑constrained aerial platforms.

## Key Contributions  
- [Finding 1] The framework uses only three simple geometric features—centroid position, area, and aspect ratio—extracted from YOLO boxes to infer yaw, eliminating the need for complex 3D reconstruction or external localization.  
- [Finding 2] It introduces a Mamdani‑Takagi–Sugeno hybrid that yields a compact 27‑rule Takagi–Sugeno model whose parameters are derived from training‑set quantiles, providing interpretability and data efficiency.  
- [Finding 3] The method achieves sub‑degree tracking errors (MAE ≈ 0.14°, RMSE ≈ 0.20°) with near‑perfect within‑threshold accuracies (±1°, ±3°, ±5°), demonstrating real‑time suitability.

## Methodology  
The authors first compute the target’s centroid in image coordinates, its bounding‑box area, and its aspect ratio (width/height). These three values feed a Mamdani fuzzy system that partitions the input space into “shoulder–triangle–shoulder” membership regions. The Mamdani output is then refined by a Takagi–Sugeno model with three antecedent terms per input, each corresponding to one of the features. Parameters are obtained as quantiles from 6 169 labeled samples in a VICON motion‑capture environment, resulting in a fixed‑size rule set that can be evaluated instantly on embedded hardware.

## Results  
Across five randomized train–test splits, the Takagi–Sugeno model yields a test‑set mean absolute error of 0.140° ± 0.003°, an RMS error of 0.200° ± 0.008°, and a maximum absolute error of 1.254° ± 0.121°. Within‑threshold accuracies are 99.676% ± 0.270% for ±1° and perfect (100%) accuracy for both ±3° and ±5° thresholds. Directional consistency between image‑plane horizontal displacement and predicted yaw sign reaches 90.254% ± 0.612%, confirming the model’s reliability.

## Significance  
This work bridges the gap between visual guidance and interpretable control, offering a lightweight, data‑efficient solution for UAV–UGV cooperation that can run on edge devices without sacrificing accuracy. By grounding inference in simple geometric features and a transparent fuzzy rule set, the method enhances trustworthiness and deployment readiness in real‑world aerial environments.

## Related Concepts  
- Fuzzy inference systems (Mamdani, Takagi–Sugeno)  
- YOLO bounding‑box extraction and feature engineering  
- Quantile‑based parameter estimation for rule generation  
- Real‑time perception‑control pipelines in autonomous robotics
