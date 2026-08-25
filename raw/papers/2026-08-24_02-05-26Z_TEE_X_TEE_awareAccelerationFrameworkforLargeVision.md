---
title: TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge
published: 2026-08-24T02:05:26Z
authors: Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky, Sadat Shahriyar, Souvik Kundu, Zhishan Guo, Abdullah Al Arafat, Adnan Siraj Rakin
url: http://arxiv.org/abs/2608.22716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge

## Abstract
Despite their remarkable success, machine learning models, particularly in vision applications, are alarmingly vulnerable to a range of security threats. One key factor in the attack landscape is the distinction between white-box and black-box threat models, as the latter poses challenges that limit attack effectiveness when access to model information is limited. As a result, using Trusted Execution Environments (TEEs) enhances security for machine learning applications by protecting model confidentiality and execution integrity, effectively shifting the execution environment from the white-box to the black-box side of the threat model spectrum. While adopting TEEs for large vision models, e.g., Vision Transformers (ViTs), is crucial for enhancing security and privacy, significant challenges related to memory constraints and increased computational latency must be addressed, especially in time-sensitive edge applications where safety and privacy are paramount. The objective of this work is to enable large vision models to be fully hosted within TEEs, achieving GPU-level inference latency for time-sensitive edge vision applications while maintaining performance. To this end, we propose TEE-X, a TEE-aware acceleration framework that introduces a sensitivity-aware modularization technique and enables vectorization in TEE inference. This design is validated on OP-TEE for Arm TrustZone, configured to optimize performance on the NVIDIA Jetson AGX Xavier for efficient edge vision applications using ViT models. The findings reveal that TEE-X delivers an effective TEE-aware acceleration framework that achieves minimal accuracy-latency trade-offs while ensuring fast and secure edge inference for vision models.

## Metadata
- **Published**: 2026-08-24T02:05:26Z
- **Authors**: Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky, Sadat Shahriyar, Souvik Kundu, Zhishan Guo, Abdullah Al Arafat, Adnan Siraj Rakin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22716v1)