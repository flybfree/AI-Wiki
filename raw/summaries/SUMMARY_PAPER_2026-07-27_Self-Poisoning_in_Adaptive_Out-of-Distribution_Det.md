---
title: Self-Poisoning in Adaptive Out-of-Distribution Detection: A Sharp-Threshold Theory and Certified Label-Free Calibration
url: http://arxiv.org/abs/2607.21673v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-23_09-43-46Z_Self_PoisoninginAdaptiveOut_of_DistributionDetecti.md
generated_at: 2026-07-27 00:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper studies adaptive out-of-distribution detection where detectors maintain a memory bank updated from unlabeled data and shows that the system follows a provable dynamical law, becoming poisoned when a reproduction number exceeds one. It also introduces a label‑free calibrated admission gate that prevents collapse and a CDC protocol to handle drift.

## Key Takeaways
- The adaptive detector’s impurity evolves according to a generalized Pólya urn model, converging almost surely to an equilibrium whose slope equals a reproduction number; below one the system remains benign while above one it is fully poisoned leading to detector collapse.
- Empirical results across 96 settings show the admission kernel has R² ≥0.996 and its slope stays just under one, indicating the detector operates near a critical threshold where performance degrades sharply as contamination increases up to an AUROC loss of 0.163.
- A certified label‑free admission gate that reads only a frozen reserve breaks the feedback loop, eliminating the transition at any contamination rate even in adversarial settings while keeping false positives low.

## Context
Adaptive out-of-distribution detectors are crucial for robust AI systems that must reject inputs from unfamiliar data without relying on labels. Recent work has shown that unsupervised memory banks can be vulnerable to poisoning, but theoretical guarantees and practical safeguards remain scarce.

## Implications
This theory provides a sharp threshold framework that helps practitioners anticipate when adaptive detectors will fail, enabling proactive design of label‑free calibration mechanisms. The results also highlight an inherent information barrier between drift and contamination in unlabeled settings, guiding future research on closed‑form performance limits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21673v1)
