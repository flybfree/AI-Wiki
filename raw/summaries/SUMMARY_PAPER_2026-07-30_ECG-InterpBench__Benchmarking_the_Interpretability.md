---
title: ECG-InterpBench: Benchmarking the Interpretability of ECG Foundation Models with Matched-Scale Sparse Autoencoders
url: http://arxiv.org/abs/2607.27404v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_19-20-50Z_ECG_InterpBench_BenchmarkingtheInterpretabilityofE.md
generated_at: 2026-07-30 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ECG‑InterpBench, a benchmark that measures how well electrocardiogram foundation models can reproduce their internal representations using sparse autoencoders with matched capacity. The study evaluates six frozen models across multiple encoder depths and dictionary widths, revealing distinct interpretability profiles and confirming that reconstruction fidelity and clinical accessibility highlight different leading performers.

## Key Takeaways
- The benchmark produces a 450‑cell interpretability atlas that includes exactly six model comparison blocks, each with matched sparse autoencoder capacity.  
- Reconstruction fidelity and single‑feature accessibility differ across models, indicating that these dimensions capture separate aspects of representation interpretability.  
- Patient‑sampling uncertainty, depth dependence, seed variation, and sparsity parameterization all influence the benchmark results.

## Context
Interpretability is a growing concern in AI, especially for medical imaging where trust and clinical relevance are paramount. Existing ECG benchmarks focus on predictive accuracy, leaving gaps in understanding how internal models can be decomposed or reproduced. This work fills that gap by providing a capacity‑controlled, reproducible framework for comparing interpretability across diverse model configurations.

## Implications
For researchers, ECG‑InterpBench offers a standardized tool to assess whether new foundation models retain meaningful structure when compressed, guiding design choices toward clinically useful representations. For industry and clinicians, the benchmark highlights which models are more transparent, potentially accelerating adoption of AI in cardiac diagnostics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27404v1)
