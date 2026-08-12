---
title: DEFT: Data-Efficient Frequency-domain Top-k Sampling via Inverse Discrete Fourier Transform for Spatiotemporal Dynamical Systems Modeling
url: http://arxiv.org/abs/2608.11019v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-00-46Z_DEFT_Data_EfficientFrequency_domainTop_kSamplingvi.md
generated_at: 2026-08-11 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DEFT, a data-efficient frequency-domain sampling technique for spatiotemporal dynamical systems modeled by PDEs. It generates training data by varying amplitudes and phases of dominant Fourier modes using the inverse discrete Fourier transform while providing a generalization bound and a theoretical criterion for selecting K. Experiments show DEFT reduces data needs by 40%, maintains predictive accuracy, and yields high R^2 scores on battery degradation models.

## Key Takeaways
- DEFT identifies dominant Fourier modes and systematically varies their amplitudes and phases to create physically consistent training data via inverse discrete Fourier transform.
- The method provides a theoretical generalization bound and a principled criterion for selecting K, improving efficiency over traditional approaches.
- Experiments demonstrate a 40% reduction in required data while preserving predictive accuracy below 2%, with R^2 exceeding 0.99 on battery degradation PDEs.

## Context
Spatiotemporal modeling of physical systems often suffers from high computational cost or insufficient training data, limiting the use of deep learning for operator learning. DEFT addresses these bottlenecks by leveraging frequency-domain properties to generate representative samples without costly simulations.

## Implications
This approach enables faster and cheaper training pipelines for complex PDE-based models, making them accessible in resource-constrained settings such as industrial process control or energy management. Practitioners can adopt DEFT to reduce data acquisition costs while maintaining high predictive performance across diverse operating conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11019v1)
