---
title: PathRIR: Physics-Guided Acoustic Path Selection and Late-Tail Compensation for Fast Room Impulse Response Simulation
published: 2026-07-25T17:05:04Z
authors: Shaoheng Xu, Chunyi Sun, Jihui Zhang, Amy Bastine, Prasanga N. Samarasinghe, Thushara D. Abhayapala
url: http://arxiv.org/abs/2607.23293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PathRIR: Physics-Guided Acoustic Path Selection and Late-Tail Compensation for Fast Room Impulse Response Simulation

## Abstract
Image-source-method (ISM)-based room impulse response (RIR) simulation is a useful and physically interpretable tool for acoustic scene modeling, but full-order ISM becomes computationally expensive as the reflection order and room complexity increase. We propose a physics-guided framework for fast RIR simulation that preserves the geometric structure of ISM while learning to retain only acoustically important image-source paths during online traversal. To recover energy removed by pruning, the proposed PathRIR uses a lightweight compensation multilayer perceptron to predict the missing late-tail energy envelope and generate a compensation tail whose energy follows that envelope. Experiments on irregular 3D rooms show that PathRIR reduces image-source computation and improves runtime efficiency over a full-order ISM simulator, while achieving low waveform- and decay-related errors. Ablation results show that adding the compensation tail improves waveform fidelity and reduces energy-decay-curve error, reverberation-time error, and direct-to-reverberant-ratio error, with modest runtime overhead.

## Metadata
- **Published**: 2026-07-25T17:05:04Z
- **Authors**: Shaoheng Xu, Chunyi Sun, Jihui Zhang, Amy Bastine, Prasanga N. Samarasinghe, Thushara D. Abhayapala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23293v1)