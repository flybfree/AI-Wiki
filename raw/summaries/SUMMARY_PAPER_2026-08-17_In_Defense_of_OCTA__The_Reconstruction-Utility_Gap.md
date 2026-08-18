---
title: In Defense of OCTA: The Reconstruction-Utility Gap in OCT-to-OCTA Synthesis
url: http://arxiv.org/abs/2608.15626v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_08-45-34Z_InDefenseofOCTA_TheReconstruction_UtilityGapinOCT_.md
generated_at: 2026-08-17 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates whether OCT‑to‑OCTA synthesis tools preserve the clinical measurements that OCTA is designed to capture. Using a frozen real‑OCTA segmenter as a probe on two synthesizers, it shows that while large vessel reconstruction remains intact, fine capillary detail degrades dramatically, and neither tool reliably reproduces neovascular lesions.

## Key Takeaways
- Large vessel Dice scores drop modestly (0.862 → 0.831) whereas fine capillary Dice collapses sharply (0.798 → 0.635), a five‑fold loss.
- The TransPro synthesizer exhibits worse performance across all metrics compared to XOCT, with paired Wilcoxon p < 1e‑3 indicating significant differences.
- A blur control confirms that the loss is not due to simple blurring but reflects fabricated fine structures.

## Context
The study addresses a gap between reconstruction fidelity and downstream clinical utility in OCTA synthesis. While PSNR and SSIM metrics are high, they do not guarantee that the synthetic images retain the detailed perfusion information needed for diagnosing diabetic retinopathy. This highlights a broader issue of evaluating AI models by their real‑world impact rather than isolated image quality.

## Implications
For researchers, this work calls for evaluation frameworks that prioritize task‑specific performance over traditional reconstruction scores. For industry and clinicians, adopting such metrics could prevent deployment of synthetic OCTA images that mislead diagnostic decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15626v1)
