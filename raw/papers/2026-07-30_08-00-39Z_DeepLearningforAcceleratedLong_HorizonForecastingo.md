---
title: Deep Learning for Accelerated Long-Horizon Forecasting of Multicomponent Multiphase Microstructure Evolution in High-Entropy Alloys
published: 2026-07-30T08:00:39Z
authors: Hamidreza Razavi, Nele Moelans
url: http://arxiv.org/abs/2607.27820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep Learning for Accelerated Long-Horizon Forecasting of Multicomponent Multiphase Microstructure Evolution in High-Entropy Alloys

## Abstract
Phase-field modeling provides a powerful approach for predicting microstructure evolution but becomes computationally prohibitive for multicomponent and multiphase systems over large spatial and temporal scales. This work presents an AE-GCN-LSTM surrogate framework for long-horizon forecasting of microstructure evolution in the multicomponent AlCrFeNi high-entropy alloy system containing coexisting BCC and FCC phases. A multi-head autoencoder compresses the four elemental concentration fields and phase-field order parameter into latent representations, which are formulated as graphs for learning their spatial and temporal evolution. The framework accurately forecasts microstructure evolution over horizons extending to 3,000,000 simulation timesteps. Its robustness is systematically evaluated under previously unseen conditions without retraining, fine-tuning, or parameter adaptation. These evaluations include variations in FCC precipitate size and initial position, microstructures containing one, two, and five FCC precipitates, and complex phase interactions involving precipitate merging and splitting. Although trained only on 100 x 100 computational domains containing a single nominal alloy composition, the framework is successfully transferred to larger 256 x 256 and 512 x 512 systems and to previously unseen AlCrFeNi compositions. Across the evaluated configurations, the model preserves the dominant phase morphology and compositional evolution while providing computational speedups ranging from approximately 7200 to 62300 relative to conventional phase-field simulations. These results demonstrate that latent graph-based AE-GCN-LSTM forecasting provides a scalable and computationally efficient surrogate for long-horizon simulation of multicomponent, multiphase microstructures and offers a promising foundation for high-throughput alloy design.

## Metadata
- **Published**: 2026-07-30T08:00:39Z
- **Authors**: Hamidreza Razavi, Nele Moelans
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27820v1)