---
title: Interactive Training 2: Auditable Control Plane for Live Model Training
published: 2026-07-17T18:06:47Z
authors: Wentao Zhang, Xuanhe Pan, Han Zhou, Yang Lu, Yuntian Deng
url: http://arxiv.org/abs/2607.18314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interactive Training 2: Auditable Control Plane for Live Model Training

## Abstract
Experiment trackers show how training is progressing, but changing a live run still usually requires trainer-specific code. We present Interactive Training 2, an open-source control plane for steering training through a shared protocol. Training applications declare which settings and actions they expose, humans and automated controllers submit requests through the same interface, and the training loop validates and applies them at safe control points. A customized Aim workspace combines live metrics and controls with a chronological record of requests and outcomes. We demonstrate the system across five NLP and reinforcement-learning workflows. The released code and traces provide a reusable foundation for auditable human- and agent-guided training.

## Metadata
- **Published**: 2026-07-17T18:06:47Z
- **Authors**: Wentao Zhang, Xuanhe Pan, Han Zhou, Yang Lu, Yuntian Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18314v1)