---
title: Scale Weight Decay and Train Better
url: http://arxiv.org/abs/2607.23777v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_17-55-40Z_ScaleWeightDecayandTrainBetter.md
generated_at: 2026-07-27 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces scaling weight decay by the fraction of peak learning rate to improve training stability and convergence. It proves that this scaled decay preserves asymptotic stationarity for stochastic gradient descent and the non‑Euclidean spectral optimizer Muon, avoiding bias from constant weight decay. Experiments on mixture‑of‑experts models show faster validation loss reduction.

## Key Takeaways  
- Scaled weight decay equals η/ηmax, keeping the norm roughly constant instead of shrinking steadily.  
- The method retains asymptotic stationarity guarantees for both SGD and Muon, eliminating extra bias from fixed decay.  
- In MoE training at large scales (72–930M parameters) Muon‑SW achieves 30% lower validation loss faster.

## Context  
The field of neural scaling laws has driven research into efficient pre‑training regimes where data and model size grow together. Traditional weight decay is often applied uniformly, but its steady shrinkage can hinder convergence at massive scales. This work offers a principled alternative that aligns regularization with the learning dynamics.

## Implications  
Practitioners can implement Muon‑SW with minimal code changes to accelerate pre‑training of frontier models without sacrificing stability. Faster training reduces compute costs and shortens time‑to‑market for large language systems, benefiting both research labs and industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23777v1)
