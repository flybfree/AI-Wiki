# Summary: 2026-08-07_16-11-11Z_MeasurementsAutomaticallyExtractedfromZeroEchoTime.md
Saved: 2026-08-09 23:11
Source: 2026-08-07_16-11-11Z_MeasurementsAutomaticallyExtractedfromZeroEchoTime.md
Model: None

---

## Summary  
This study aimed to develop a fully automated pipeline that extracts femoroacetabular impingement (FAI) angles from zero‑echo time (ZTE) MRI using deep learning segmentation and geometric modeling, and to evaluate how well the results match those of expert manual measurements. By training an nnU‑Net on curated hip images and applying custom algorithms to compute six key FAI angles, the authors demonstrated that automated morphometry can be performed with high accuracy and comparable reliability to human readers.

## Key Contributions  
- [Finding 1] The segmentation model achieves Dice scores exceeding 0.96 for bone structures and ranging from 0.65 to 0.83 for osseous landmarks, indicating excellent delineation of the femur, pelvis, and three key landmarks.  
- [Finding 2] Model‑vs‑rater agreement is excellent (ICC ≥ 0.82) for acetabular version, coronal center‑edge, and Tonnis angles; it is good for mid‑acetabular sagittal center‑edge and fair for alpha and femoral neck‑shaft angles.  
- [Finding 3] The automated Bland‑Altman limits of agreement are narrower than the interrater limits for most angles, suggesting that the model’s estimates are more precise than human variability.

## Methodology  
The researchers employed nnU‑Net, a deep learning network trained on 100 manually curated ZTE MRI scans to segment the femur, pelvis, and three osseous landmarks (lateral acetabulum, medial acetabulum, greater trochanter). Custom geometric algorithms then computed the six FAI angles: alpha, femoral neck‑shaft, Tonnis, coronal center‑edge, sagittal center‑edge, and acetabular version. A cross‑sectional study enrolled 73 participants (135 hips), with a test set of 35 hips compared to the mean of two radiologists’ manual measurements using intraclass correlation (ICC) and Bland‑Altman analysis.

## Results  
Dice coefficients for bone segmentation were >0.96, while landmark Dice ranged from 0.65 to 0.83. Median landmark errors were 0.38 mm (femoral head), 0.82 mm (lateral acetabulum), and <2.5 mm for the medial acetabulum and greater trochanter. ICC values ranged from 0.45 to 0.96, with excellent agreement (≥0.82) for three angles and fair agreement (≈0.45–0.55) for two others. Bland‑Altman limits of agreement were consistently narrower than the interrater limits, especially for acetabular version, coronal center‑edge, and Tonnis.

## Significance  
Fully automated FAI angle extraction from ZTE MRI reduces reliance on ionizing radiation from CT, shortens clinical workflows, and improves reproducibility. The high Dice scores and narrow Bland‑Altman intervals indicate that the model can serve as a reliable adjunct to expert assessment for most coverage and version angles.

## Related Concepts  
ZTE MRI, nnU‑Net deep learning segmentation, geometric modeling of FAI angles (alpha, femoral neck‑shaft, Tonnis, coronal center‑edge, sagittal center‑edge, acetabular version), Dice coefficient, intraclass correlation (ICC), Bland‑Altman analysis, osseous landmarks.
