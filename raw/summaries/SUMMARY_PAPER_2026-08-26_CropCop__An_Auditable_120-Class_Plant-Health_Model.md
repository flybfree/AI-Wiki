---
title: CropCop: An Auditable 120-Class Plant-Health Model from Benchmark Reconstruction to a Quantised Runtime Artifact
url: http://arxiv.org/abs/2608.25539v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_08-51-57Z_CropCop_AnAuditable120_ClassPlant_HealthModelfromB.md
generated_at: 2026-08-26 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
CropCop is a closed‑set plant‑health recognition system that spans 120 classes and provides an auditable evidence chain from image reconstruction to a quantised runtime artifact. The authors demonstrate that a MobileNetV4 Conv‑Medium model can achieve near‑state‑of‑the‑art accuracy (98.46% top‑1) while the final 22.6 MiB PTE runs with only six decision changes, confirming both leakage control and software‑runtime fidelity.

## Key Takeaways
- The benchmark reconstruction removed 3,233 duplicate relationships across split boundaries, leaving a trustworthy 109,107‑image set with zero crossings among trusted groups.  
- Quantisation to INT8 using ExecuTorch/XNNPACK PTE reduced model size to 22.6 MiB and kept macro‑F1 at 96.23%, showing that runtime inference does not degrade performance beyond negligible class‑balanced loss.  
- Only six of the 16,363 top‑1 predictions differ between the INT8 graph and the PTE, indicating high fidelity from model to execution artifact.

## Context
This work addresses a critical issue in AI deployment: hidden data leakage that inflates performance metrics without improving real‑world utility. By constructing an auditable pipeline from raw images to quantised inference, CropCop offers a template for transparent model evaluation and reproducible results.

## Implications
For industry practitioners, CropCop provides a practical framework to verify that model outputs are not compromised by unseen data or hardware quirks. It encourages the use of lightweight, quantised models while maintaining high accuracy, supporting efficient deployment on edge devices such as Android smartphones without sacrificing reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25539v1)
