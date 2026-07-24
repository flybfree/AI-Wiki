---
title: SWITi: Quantifying and Reducing Tiling Artifacts with Sliding Window Inner Tiling
url: http://arxiv.org/abs/2607.18990v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_11-20-35Z_SWITi_QuantifyingandReducingTilingArtifactswithSli.md
generated_at: 2026-07-23 23:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
SWITi is a test‑time technique that reduces artifacts in tiled neural network predictions, especially for models that generate posterior distributions at inference time. By averaging overlapping sliding‑window predictions, the method spreads discrepancies across tile boundaries instead of concentrating them at fixed seams. Experiments on fluorescence microscopy datasets show that SWITi markedly improves seam quality and overall reconstruction fidelity.

## Key Takeaways
- SWITi eliminates stitching seams by averaging neighboring tile samples, preventing artifacts from accumulating at predetermined borders.
- The method requires no extra forward passes because it uses only the number of tile samples needed for an MMSE estimate.
- Two reference‑free metrics—Fraction of Rejected Tests (FRT) and Artifact Severity (ASV)—detect and quantify tiling artifacts via per‑tile permutation tests.

## Context
Tiled predictions are essential for processing large images, yet they introduce visual seams that can be mistaken for biological structures. Existing solutions often require costly re‑training or additional inference steps, limiting practical deployment in real‑time biomedical applications.

## Implications
For researchers and industry practitioners, SWITi offers a lightweight way to clean up tiled outputs without sacrificing computational efficiency. This directly enhances the downstream processing of large image predictions, especially in medical imaging where artifact removal is critical for accurate diagnosis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18990v1)
