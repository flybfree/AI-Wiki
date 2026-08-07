---
title: Does FLAIR super-resolution erase or hallucinate small white-matter lesions?
url: http://arxiv.org/abs/2608.06311v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-26-01Z_DoesFLAIRsuper_resolutioneraseorhallucinatesmallwh.md
generated_at: 2026-08-06 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether applying super-resolution to thin FLAIR scans erases or creates false white‑matter lesions. Using simulated thick slices from high‑resolution data, the authors compare lesion detection after reconstruction with the original high‑resolution segmentation and find that small real lesions are most often erased rather than hallucinated.

## Key Takeaways
- Small real WMH lesions are preferentially removed by super‑resolution, especially as slice thickness increases.  
- The error manifests as an erasure rate that rises with thicker simulated slices, though reconstruction still improves overall detection compared to raw thick slices.  
- Among the tested methods, ECHARLE outperforms cubic interpolation at preserving small lesion signal.

## Context
Super‑resolution techniques aim to recover isotropic resolution from clinical anisotropic scans, but their impact on pathological feature extraction remains unclear. This study addresses a critical gap by directly linking reconstruction quality to diagnostic segmentation performance in white matter hyperintensities.

## Implications
For neuroimaging analysts, the findings caution that SR may degrade lesion visibility rather than enhance it, influencing pipeline design and interpretation of automated segmentation tools. Practitioners should consider trade‑offs between resolution gain and sensitivity loss when selecting upsampling methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06311v1)
