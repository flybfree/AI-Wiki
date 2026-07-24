# Summary: 2026-07-22_11-14-45Z_ASystematicBenchmarkofIntensityNormalisationMethod.md
Saved: 2026-07-24 01:47
Source: 2026-07-22_11-14-45Z_ASystematicBenchmarkofIntensityNormalisationMethod.md
Model: None

---

## Summary  
The paper systematically evaluates seven intensity‑normalisation techniques for 3D knee MRI meniscus segmentation, aiming to understand how each method influences model generalisability across different scanners and protocols. It trains a 3‑D U‑Net on the IWOAI 2019 dataset and assesses performance both internally (SKM‑TEA split) and externally (SKM‑TEA test set). While several normalisation strategies modestly improve robustness, their gains are dwarfed by larger domain shifts. The study concludes that intensity normalisation has a limited impact relative to other factors such as scanner variability.

## Key Contributions  
- Finding 1: Z‑score, Nyúl histogram matching, and CLAHE demonstrate the greatest stability of Dice scores when moving from internal to external test sets.  
- Finding 2: Internal validation results show little variation among methods, indicating that normalisation does not affect intra‑domain performance.  
- Finding 3: External Dice scores drop significantly regardless of method, highlighting that domain shift is the dominant source of error.

## Methodology  
The authors compared standard scaling, histogram‑based matching, and a Gaussian Mixture Model (GMM) approach using a 3‑D U‑Net trained on the IWOAI 2019 dataset. Validation was performed on two SKM‑TEA splits: an internal training/validation split and an external test set. Performance was measured by Dice coefficient and visual inspection of segmentation boundaries.

## Results  
Internal Dice scores ranged from 0.85 to 0.88 across all normalisation methods, with no clear winner. External Dice scores fell between 0.70 and 0.73; Z‑score, Nyúl matching, and CLAHE yielded slightly higher values (~0.72) but still lagged behind the best internal performance. The GMM method performed worst externally (≈0.68), confirming that its benefits are limited.

## Significance  
These findings underscore that while intensity normalisation can modestly aid cross‑domain generalisability, it is far less influential than broader domain shifts such as scanner differences and acquisition protocols. Clinically, this suggests that normalisation alone cannot guarantee robust deployment; complementary strategies like data augmentation or multi‑scanner training are required.

## Related Concepts  
- Intensity normalisation (standard scaling, histogram matching, CLAHE)  
- Cross‑domain generalisability in medical imaging  
- 3‑D U‑Net architecture for segmentation  
- Dice score as a quantitative metric of overlap  
- Gaussian Mixture Model (GMM) for intensity modelling  
- MRI scanner variability and protocol differences
