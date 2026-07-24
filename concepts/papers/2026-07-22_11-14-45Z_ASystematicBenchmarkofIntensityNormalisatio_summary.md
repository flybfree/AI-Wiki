# Summary: 2026-07-22_11-14-45Z_ASystematicBenchmarkofIntensityNormalisationMethod.md
Saved: 2026-07-24 01:44
Source: 2026-07-22_11-14-45Z_ASystematicBenchmarkofIntensityNormalisationMethod.md
Model: None

---

## Summary  
The paper aims to systematically benchmark intensity normalisation methods for 3D knee MRI meniscus segmentation and assess their impact on cross‑domain generalisability. It compares seven normalisation techniques using a 3D U‑Net trained on the IWOAI 2019 dataset, evaluating both internal and external test sets (SKM‑TEA). The study finds that while some methods improve robustness, the effect is modest compared to larger domain shifts. Overall, intensity normalisation contributes limited but measurable gains in generalisability.

## Key Contributions  
- Finding 1: Z‑score, Nyúl histogram matching, and CLAHE provide better external performance than simple scaling.  
- Finding 2: The impact of intensity normalisation is small relative to the large drop observed when moving from IWOAI to SKM‑TEA datasets.  
- Finding 3: A GMM‑based method shows intermediate results but does not outperform histogram matching.

## Methodology  
The authors trained a 3D U‑Net on the IWOAI 2019 dataset and evaluated it on two test sets: an internal split of IWOAI (to measure overfitting) and the external SKM‑TEA set. They applied seven normalisation methods—standard Z‑score scaling, Nyúl histogram matching, CLAHE, Gaussian Mixture Model (GMM), intensity clipping, linear scaling, and adaptive normalization—and recorded Dice scores for each combination.

## Results  
Internal Dice scores were comparable across all normalisations (average ~0.84). On the external SKM‑TEA set, Z‑score and Nyúl histogram matching yielded Dice ≈0.71–0.73, CLAHE slightly higher (~0.75), while GMM performed around 0.68. Simple scaling dropped to ~0.62. The performance gap between internal and external sets was significant (≈0.12–0.14 absolute difference). No normalisation method fully closed the gap, indicating limited generalisability benefit.

## Significance  
Understanding how intensity normalisation affects model generalisability helps clinicians choose preprocessing pipelines that balance speed and robustness. The study suggests that while simple methods may suffice for modest domain shifts, more sophisticated techniques offer marginal gains but cannot overcome fundamental data distribution differences.

## Related Concepts  
- Intensity normalisation  
- Cross‑domain generalisability  
- Dice score  
- 3D U‑Net segmentation  
- MRI scanner drift  
- Histogram matching (Nyúl)  
- CLAHE (Contrast Limited Adaptive Histogram Equalization)
