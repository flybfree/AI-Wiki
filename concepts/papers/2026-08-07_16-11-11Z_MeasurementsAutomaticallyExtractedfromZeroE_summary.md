# Summary: 2026-08-07_16-11-11Z_MeasurementsAutomaticallyExtractedfromZeroEchoTime.md
Saved: 2026-08-09 23:09
Source: 2026-08-07_16-11-11Z_MeasurementsAutomaticallyExtractedfromZeroEchoTime.md
Model: None

---

## Summary  
This study aimed to develop an automated pipeline that extracts femoroacetabular impingement (FAI) angles from zero‑echo time (ZTE) MRI without ionizing radiation, thereby matching the accuracy of expert manual measurements. The authors combined a deep‑learning image segmentation model with custom geometric algorithms to compute multiple angular parameters and evaluated their reliability against two radiologists’ assessments in a cross‑sectional cohort. By achieving high Dice similarity for bone structures and modest landmark errors, the method demonstrates that fully automated morphometric assessment from ZTE MRI is feasible and clinically comparable to manual reading.

## Key Contributions  
- [Finding 1] The nnU‑Net segmentation model attains Dice coefficients >0.96 for cortical bone and 0.65–0.83 for osteological landmarks, indicating robust delineation of the femur, pelvis, and key FAI landmarks.  
- [Finding 2] Automated angle calculations (alpha, femoral neck‑shaft, Tonnis, coronal and sagittal center‑edge, acetabular version) show median landmark errors <2.5 mm for most structures, with acceptable interrater ICC values (≥0.82) for several angles.  
- [Finding 3] Model versus rater‑mean agreement is excellent (ICC 0.92–0.96) for acetabular version, coronal center‑edge, and Tonnis, while model Bland‑Altman limits of agreement are narrower than interrater limits for most angles.

## Methodology  
The authors acquired pelvic ZTE MRI from 73 participants (mean age 36.8 ± 18.5 years) and used nnU‑Net, a convolutional neural network trained on 100 manually curated hip images, to segment the femur, pelvis, and three osseous landmarks. Custom geometric algorithms then derived the FAI angles from these inferred structures. Measurements were extracted from 35 test hips and compared with the mean of two expert radiologists using intraclass correlation (ICC) and Bland‑Altman analysis.

## Results  
Dice similarity exceeded 0.96 for bone segmentation and ranged from 0.65 to 0.83 for landmarks, indicating high precision. Median landmark errors were 0.38 mm (femoral head), 0.82 mm (lateral acetabulum), and <2.5 mm for medial acetabulum and greater trochanter. Interrater ICC was excellent (≥0.82) for acetabular version, coronal center‑edge, and Tonnis angles but poor for alpha and femoral neck‑shaft. Model versus rater‑mean agreement was excellent (0.92–0.96) for acetabular version, coronal center‑edge, and Tonnis; good for mid‑acetabular sagittal center‑edge (0.74); fair for alpha (0.45) and femoral neck‑shaft (0.55). Model Bland‑Altman limits of agreement were narrower than interrater limits for most angles.

## Significance  
This work eliminates the need for ionizing radiation in FAI assessment, reduces measurement time, and provides a reproducible automated tool that matches expert accuracy for key clinical parameters, potentially improving diagnostic consistency and patient care.

## Related Concepts  
- Zero echo time (ZTE) MRI  
- nnU‑Net deep learning segmentation  
- Dice coefficient for image quality  
- Intraclass correlation (ICC)  
- Bland‑Altman analysis  
- Femoroacetabular impingement (FAI) angles
