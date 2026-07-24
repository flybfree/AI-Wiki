---
title: Real-time optimal control with shallow recurrent decoder networks
published: 2026-07-21T17:13:49Z
authors: Matteo Tomasetto, Francesco Braghin, J. Nathan Kutz, Andrea Manzoni
url: http://arxiv.org/abs/2607.19302v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Real-time optimal control with shallow recurrent decoder networks

## Abstract
Controlling dynamical systems in real-time across multiple scenarios is critical to enabling adaptive control strategies, ensuring stability and efficiency. However, to tailor control actions in response to varying scenarios, traditional optimal control problems typically require several system simulations, which are often computationally demanding due to the high-dimensionality of the underlying spatio-temporal dynamics. In this work, we exploit SHallow REcurrent Decoder networks-based Reduced Order Modeling (SHRED-ROM) to synthesize a real-time closed-loop controller for high-dimensional and parametric dynamics, relying solely on limited state sensor readings. After training the model on a few optimal examples given by an expert demonstrator, SHRED-ROM mimics the expert behavior with effective distributed control actions in new scenarios, alleviating the curse of dimensionality. Moreover, a sensor forecaster is synthesized and used to close the loop at the latent level, thus efficiently mitigating possible sensor failures or delays. The performance of the proposed optimal control strategy is finally assessed on three challenging high-dimensional cases dealing with either parametric density control or fluid flow control.

## Metadata
- **Published**: 2026-07-21T17:13:49Z
- **Authors**: Matteo Tomasetto, Francesco Braghin, J. Nathan Kutz, Andrea Manzoni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19302v1)