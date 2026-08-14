---
title: Sustaining Plasticity via Learnable Wavelet Activations in Continual Learning
url: http://arxiv.org/abs/2608.12874v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_06-38-04Z_SustainingPlasticityviaLearnableWaveletActivations.md
generated_at: 2026-08-13 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a learnable wavelet activation to combat plasticity loss in continual learning by balancing low‑frequency stability and high‑frequency plasticity. It introduces dynamic wavelet injection and regularization to preserve prior knowledge while enabling new task adaptation. Experiments show improved trainability and state‑of‑the‑art performance across benchmarks.

## Key Takeaways
- The hybrid wavelet architecture explicitly decouples low‑frequency components for stable memory retention and high‑frequency components that can be updated, mitigating spectral bias.
- Dynamic wavelet injection is triggered by loss signals to adaptively boost plasticity only when new information outweighs forgetting risk.
- A regularization strategy ensures the network’s learned knowledge remains stable while allowing controlled updates, providing rigorous L2 approximation guarantees.

## Context
Continual learning struggles with forgetting as models accumulate knowledge over time. Traditional activation functions often bias toward low frequencies, limiting adaptation to high‑frequency task variations. This work addresses that limitation by designing a flexible wavelet activation that can be tuned per task.

## Implications
Practitioners can implement this framework to maintain model performance across long training sequences without manual retraining. The method’s theoretical guarantees offer confidence in its stability and efficiency, encouraging adoption in real‑world applications where data streams evolve continuously.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12874v1)
