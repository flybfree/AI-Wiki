---
title: $π$-SUB: A Physics-Informed Synthetic Underwater Benchmark Dataset for Underwater Image Enhancement
url: http://arxiv.org/abs/2608.10589v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_07-16-53Z_π__SUB_APhysics_InformedSyntheticUnderwaterBenchma.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces π‑SUB, a physics‑informed synthetic underwater benchmark dataset that aims to close the gap between synthetic and real underwater images for enhancement tasks. The framework models depth‑dependent downwelling irradiance, biological absorption, scattering across ten Jerlov water types, enabling high‑resolution paired synthetic-reference pairs. Evaluation shows hyper‑realism improvements with 46 % lower FID than the current state‑of‑the‑art Syrea benchmark and notable gains in UIQM scores.

## Key Takeaways
- The dataset achieves a global Frechet Inception Distance that is 46% lower than the current state‑of‑the‑art Syrea benchmark, indicating superior realism. - It improves UIQM by 9.46% over Syrea and 4.18% over PHISWID, demonstrating strong generalizability across multiple AI models. - The framework reduces NIQE scores by up to 48.78%, highlighting efficient compression without quality loss.

## Context
Underwater image enhancement remains challenging due to the lack of diverse, realistic synthetic datasets that capture real‑world water physics and environmental variability. Existing benchmarks often rely on limited or unrealistic conditions, limiting model performance transfer to unseen scenarios.

## Implications
This benchmark enables researchers to train more robust underwater enhancement models with better generalization across different water types and depths. Practitioners can leverage the dataset for real‑time applications such as augmented reality navigation and remote sensing where image quality is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10589v1)
