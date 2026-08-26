---
title: Mechanistic Circuit Identification for Controllable Data Generation
published: 2026-08-25T04:53:19Z
authors: Nakyung Lee, Sangwoo Hong, Jungwoo Lee
url: http://arxiv.org/abs/2608.24065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mechanistic Circuit Identification for Controllable Data Generation

## Abstract
While recent advances in data synthesis aim to curate high-quality datasets, most generation pipelines still rely on heuristic prompt-based control. This black-box paradigm provides limited insight into how individual samples interact with a model's underlying learning dynamics. To bridge this gap, we propose a circuit-grounded framework that connects training-dynamics-based data valuation with mechanistic interpretability (MI). Specifically, we conceptualize data quality along three complementary utility axes, learnability, challenge, and alignment. First, we uncover specialized model-internal circuits that causally govern these utility signals. Then, moving beyond heuristic prompting toward mechanistic control, we leverage these circuits as controllable interfaces, actively steering generation to produce utility-targeted data. Building on this capability, we introduce SAMS (Stage-Aware Mechanistic Scheduling), which schedules circuit-steered data according to the model's evolving optimization needs. Experiments on multiple-choice QA tasks demonstrate that our approach yields precisely controlled data with greater diversity than prompt-based baselines, consistently improving downstream performance and calibration. Ultimately, this work establishes a principled white-box paradigm for interpretable data generation, pioneering the use of MI not just as an analytical tool, but as a practical, controllable interface.

## Metadata
- **Published**: 2026-08-25T04:53:19Z
- **Authors**: Nakyung Lee, Sangwoo Hong, Jungwoo Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24065v1)