---

title: "Summary: KLIP: localized distribution shift detection via KL-divergence with diffusion priors in Inverse Problems"
url: http://arxiv.org/abs/2605.31596v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-29_17-58-01Z_KLIP_localizeddistributionshiftdetectionviaKL_dive.md
generated_at: "2026-06-11 10:50"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces KLIP, a method for detecting out-of-distribution patches in inverse problems using the Kullback-Leibler divergence between a diffusion model prior and the posterior distribution. It can identify both whole images as OOD and localize anomalous regions within an image without needing calibration data or explicit knowledge of the shifted distribution.

## Key Takeaways
- The metric detects subtle distribution shifts without requiring any calibration data or knowledge of the shifted distribution.
- It works for both whole-image OOD detection and localized patch-level detection within an image.
- Experiments demonstrate generalization across various diffusion models, datasets, and inverse problems such as liver CT scans with tumor presence.

## Context
Diffusion models are increasingly used as priors in computational imaging tasks. Traditional OOD detectors often rely on full images or explicit shift knowledge, limiting their applicability to real-world inverse problems where only indirect measurements are available.

## Implications
This approach enables reliable detection of anomalous regions in medical and industrial data without costly calibration, supporting automated anomaly monitoring and early disease detection. It could streamline quality control processes across imaging modalities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.31596v1)
