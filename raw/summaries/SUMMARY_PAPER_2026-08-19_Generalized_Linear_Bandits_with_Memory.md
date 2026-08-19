---
title: Generalized Linear Bandits with Memory
url: http://arxiv.org/abs/2608.15848v1
type: paper-summary
date: 2026-08-19
source_paper: 2026-08-16_16-39-09Z_GeneralizedLinearBanditswithMemory.md
generated_at: 2026-08-19 11:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses generalized linear bandits with memory, where rewards depend on past actions via a finite memory matrix. It refines the existing \(\tilde{O}(T^{3/4})\) regret bound to achieve a \(\tilde{O}(\sqrt{T})\) rate for linear models and extends this improvement to nonlinear generalizations using a block‑wise algorithm based on shrunken confidence bounds.

## Key Takeaways
- The previous \(\tilde{O}(T^{3/4})\) regret analysis is loose; the authors recover a \(\tilde{O}(\sqrt{T})\) bound through a sharper analysis of the linear case.  
- Their method extends to generalized linear models, employing block‑wise updates and shrunken confidence bounds to handle memory effects.  
- The resulting regret bound \(\tilde{O}\left(\sqrt{mT} + d\sqrt{T} + \sqrt{κ}\,d^{2}m^{1/4}T^{1/4}+ κd^{2}\right)\) attains a \(\sqrt{T}\)-type rate even with nonlinear rewards and memory, independent of link‑function curvature.

## Context
Memory in bandits introduces non‑stationarity that complicates standard online learning methods. Generalized linear models allow for flexible link functions, yet their performance is often limited by the same \(\tilde{O}(T^{3/4})\) regret gap observed in linear settings. This work bridges those gaps by providing a unified framework that treats both memory and nonlinearity together.

## Implications
For practitioners designing adaptive systems such as recommendation engines or clinical trial allocation, this algorithm offers near‑optimal regret performance across diverse reward structures. The \(\sqrt{T}\) scaling reduces long‑term loss dramatically compared with earlier approaches, enabling more reliable outcomes in real‑world applications where data is collected over time and subject to evolving patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15848v1)
