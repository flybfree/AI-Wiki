---
title: LOCUS-DT: Localization via Observation-Conditioned Uncertainty Scoring with Digital Twins
published: 2026-08-01T03:02:15Z
authors: Haozhe Lei, Roberto Bomfin, Marwa Chafii, Sundeep Rangan
url: http://arxiv.org/abs/2608.00406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LOCUS-DT: Localization via Observation-Conditioned Uncertainty Scoring with Digital Twins

## Abstract
Accurate indoor localization is essential for emerging applications in robotic navigation and search and rescue. While classical methods typically focus on single-point estimates, complex indoor environments with heavy blockage and multipath propagation often lead to multimodal likelihood surfaces where a single estimate is insufficient. This paper proposes LOCUS-DT (Localization via Observation-Conditioned Uncertainty Scoring with Digital Twins), a framework that treats snapshot localization as posterior inference over the transmitter location. By leveraging a ray-tracing-based digital twin (DT) of the known environment, LOCUS-DT generates synthetic multipath profiles for candidate locations and compares them against the measured channel profile. Central to our approach is a novel learned scoring function designed to compare a fixed number of dominant specular paths, providing robustness against errors in both the DT environment model and the physical channel estimation. Importantly, LOCUS-DT is trained over an ensemble of environments to ensure generalization to unseen layouts. We evaluate the system using a Sionna-based ray-tracing backend, demonstrating that LOCUS-DT captures the sharp, multimodal posterior structures inherent in indoor settings more accurately than standard Gaussian or Gaussian-mixture benchmarks.

## Metadata
- **Published**: 2026-08-01T03:02:15Z
- **Authors**: Haozhe Lei, Roberto Bomfin, Marwa Chafii, Sundeep Rangan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00406v1)