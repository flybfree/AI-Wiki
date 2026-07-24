---
title: Mixed-Timescale Differential Coding for Downlink Model Broadcast in Wireless Federated Learning
published: 2026-07-14T16:03:23Z
authors: Chung-Hsuan Hu, Zheng Chen, Erik G. Larsson
url: http://arxiv.org/abs/2607.13119v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mixed-Timescale Differential Coding for Downlink Model Broadcast in Wireless Federated Learning

## Abstract
In standard federated learning systems, the parameter server broadcasts the global model to the participating devices in every iteration. Motivated by the temporal correlation between consecutive global models, differential coding can be applied to global model dissemination to reduce the information magnitude, thereby enabling communication with fewer quantization bits. However, due to wireless link failures, devices may occasionally miss differential updates and consequently fail to reconstruct the global model. As a result, they either continue local training based on an outdated model or remain idle until the next full-model broadcast becomes available. To address this challenge, we propose a mixed-timescale differential coding (MTDC) scheme that performs differential coding at two different levels by adjusting the reference model. With MTDC, a device can reconstruct the latest global model between two full-model broadcasts even if it misses a differential update. We provide a convergence analysis that motivates the design of an age-aware variant of MTDC, along with a device scheduling policy to further improve communication efficiency. Simulation results demonstrate that the proposed MTDC schemes achieve superior learning performance compared to baseline methods under similar communication resource budgets in the presence of downlink transmission failures.

## Metadata
- **Published**: 2026-07-14T16:03:23Z
- **Authors**: Chung-Hsuan Hu, Zheng Chen, Erik G. Larsson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.13119v2)