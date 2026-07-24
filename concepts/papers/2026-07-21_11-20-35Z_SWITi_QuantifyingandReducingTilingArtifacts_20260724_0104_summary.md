# Summary: 2026-07-21_11-20-35Z_SWITi_QuantifyingandReducingTilingArtifactswithSli.md
Saved: 2026-07-24 01:04
Source: 2026-07-21_11-20-35Z_SWITi_QuantifyingandReducingTilingArtifactswithSli.md
Model: None

---

## Summary  
SWITi is a test‑time method designed to reduce artifacts that appear when neural networks generate tiled predictions from posterior distributions. It addresses two main sources of tiling errors: tiles smaller than the network's receptive field and independent posterior samples. The core innovation is averaging overlapping sliding‑window predictions, which spreads discrepancies across tile boundaries rather than at fixed seams. SWITi also introduces new metrics for artifact detection without requiring reference images.  

## Key Contributions  
- [Finding 1] SWITi substantially attenuates stitching seams by averaging overlapping window predictions.  
- [Finding 2] The authors introduce two reference‑free metrics, Fraction of Rejected Tests (FRT) and Artifact Severity (ASV), to detect and quantify tiling artifacts via a per‑tile permutation test on pixel gradients.  
- [Finding 3] SWITi requires no additional forward passes because it leverages the MMSE estimate’s tile samples.  

## Methodology  
The authors address tiling artifacts by employing an inner sliding‑window approach where each tile’s prediction is combined with predictions from neighboring tiles. This overlapping averaging reduces seam formation at fixed coordinates. To evaluate artifact severity, they perform a permutation test that compares gradient distributions across tile seams to those of surrounding image content, yielding FRT and ASV scores.  

## Results  
Experiments on three fluorescence microscopy datasets in both 2D and 3D demonstrate that SWITi improves reconstruction fidelity and resolution while reducing seam artifacts. The Fraction of Rejected Tests drops significantly, indicating fewer erroneous pixel transitions, and the Artifact Severity metric declines across all conditions, confirming quantitative artifact reduction.  

## Significance  
Tiling artifacts can be misinterpreted as biological structures or boundaries in biomedical imaging, leading to downstream processing errors. By providing a test‑time correction that eliminates these false patterns without retraining, SWITi enhances the reliability of large‑scale image predictions and supports more accurate scientific analysis.  

## Related Concepts  
tiled predictions, posterior sampling, sliding window averaging, MMSE estimate, artifact detection, permutation testing, fluorescence microscopy, reconstruction fidelity.
