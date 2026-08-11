---
title: Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty
published: 2026-08-09T20:55:17Z
authors: Jennifer N. Kampe, Changwoo J. Lee, Xin Shen, Ari Lehtiö, Sandro von Brandenburg, Ossi Nokelainen, David B. Dunson, Otso Ovaskainen
url: http://arxiv.org/abs/2608.08911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty

## Abstract
Recent advances in Passive Acoustic Monitoring (PAM) offer an opportunity to obtain ecological spatial point-process data at unprecedented scale. However, realizing this opportunity necessitates the development of accurate and scalable localization methods. In real-world outdoor soundscapes, however, the assumptions underlying classical localization methods such as hyperbolic and score-based localization are routinely violated by multipath dominance, near-field effects, and complex propagation. Under these conditions, classical localization methods become brittle, with extreme errors possible even in small detection arrays. Rather than statistically replacing the underlying physics, we propose a method to refine it and increase robustness outside of ideal operating conditions: a learned model operating on physics-informed acoustic features corrects a fast hyperbolic solver where it produces implausible solutions, substantially reducing catastrophic worst-case errors while matching its median accuracy on field data. We further provide calibrated, geometry-aware uncertainty estimates suitable for propagation into downstream spatial models. Evaluating on distributed microphone arrays in real and simulated outdoor environments, we demonstrate that the proposed method yields robust, uncertainty-aware localization, providing a step toward scalable automated wildlife monitoring in complex acoustic environments.

## Metadata
- **Published**: 2026-08-09T20:55:17Z
- **Authors**: Jennifer N. Kampe, Changwoo J. Lee, Xin Shen, Ari Lehtiö, Sandro von Brandenburg, Ossi Nokelainen, David B. Dunson, Otso Ovaskainen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08911v1)