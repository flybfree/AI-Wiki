---
title: Towards Autonomous Aircraft Surveillance from Nanosatellites through On-Board Inference and Generative Data Augmentation
url: http://arxiv.org/abs/2607.28470v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-26-38Z_TowardsAutonomousAircraftSurveillancefromNanosatel.md
generated_at: 2026-07-30 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a workflow that merges on‑board inference with generative data augmentation to overcome the limited downlink and class‑imbalance problems in nanosatellite surveillance. By running a low‑power edge detector on a 6U CubeSat and generating synthetic minority‑class images with a diffusion model, the system creates a balanced training set that improves detection performance. The results show a rise from global mean average precision of 77.9 % to 82.2 %, with minority‑class F1 increasing from 0.683 to 0.811, and the quantised detector processes 25–30 frames per second on orbit.

## Key Takeaways
- The integration of on‑board inference reduces reliance on high‑bandwidth downlink by processing images locally within a CubeSat’s limited compute resources.
- Generative data augmentation creates synthetic minority‑class imagery, effectively balancing the dataset and enabling standard detectors to learn robust representations.
- The quantised detector fits on‑chip memory and achieves 25–30 frames per second, demonstrating real‑time autonomous operation.

## Context
In satellite AI research, the bottleneck of downlink bandwidth versus computational capability remains a key challenge. This work addresses both by performing inference locally while supplementing data with synthetic samples, illustrating how edge AI can complement cloud processing for remote sensing tasks.

## Implications
For industry and practitioners, this approach enables cost‑effective autonomous surveillance from low‑Earth orbit without needing massive ground stations or high‑resolution raw imagery. It also provides a template for balancing scarce training data in other domains where class imbalance is problematic.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28470v1)
