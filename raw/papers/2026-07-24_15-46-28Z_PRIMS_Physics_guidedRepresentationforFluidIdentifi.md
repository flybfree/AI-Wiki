---
title: PRIMS: Physics-guided Representation for Fluid Identification in Multimodal Sensing
published: 2026-07-24T15:46:28Z
authors: Hai-Long Nguyen, Trung Thanh Nguyen, Lars Holm, Dennis Alveringh, Duc Viet Le
url: http://arxiv.org/abs/2607.22422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRIMS: Physics-guided Representation for Fluid Identification in Multimodal Sensing

## Abstract
Accurate on-device fluid identification is essential for microfluidic applications, yet maintaining reliability under varying flow, pressure, and temperature remains a key challenge. Existing learning-based methods often treat sensor signals as domain-agnostic features, neglecting the underlying physical relationships that govern fluid behavior, thereby limiting generalization and interpretability. To address this, we propose PRIMS, a physics-aware multimodal Transformer that integrates physical knowledge into representation learning and attention mechanisms through three dedicated modules: (1) Physics-based Token Vectorization transforms raw Coriolis and pressure sensor signals into physically meaningful token embeddings; (2) Physical Component Synthesizer models viscosity-related dependencies among flow, pressure, and density; and (3) Physics-guided Fusion captures cross-physical correlations through attention-based integration. By embedding these physics-based relationships directly into the model architecture, PRIMS bridges analytical fluid mechanics and deep learning, enabling interpretable, data-efficient, and resilient fluid classification. Evaluations on a five-fluid benchmark under dynamic flow, pressure, and temperature conditions show that PRIMS achieves 98.92% average F1-score with only 0.46 million parameters, a 14 times reduction compared to state-of-the-art Transformer-based methods. PRIMS also consistently outperforms prior SOTA models under out-of-distribution shifts to unseen temperature ranges and unseen flow-rate ranges, indicating strong robustness to operating conditions not observed during training. These findings suggest that designing architectures that explicitly mirror governing physical relationships can make them learn transferable, environment-independent representations, improving real-world reliability for microfluidic sensing.

## Metadata
- **Published**: 2026-07-24T15:46:28Z
- **Authors**: Hai-Long Nguyen, Trung Thanh Nguyen, Lars Holm, Dennis Alveringh, Duc Viet Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22422v1)