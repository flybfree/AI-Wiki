---
title: D2PO: Optimizing Diffusion Samplers via Dynamic Preference
published: 2026-07-07T06:05:42Z
authors: Jinkyu Kim, Jinyoung Choi, Bohyung Han
url: http://arxiv.org/abs/2607.06609v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D2PO: Optimizing Diffusion Samplers via Dynamic Preference

## Abstract
We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with perceptual quality. D2PO addresses this challenge by reformulating sampler optimization as a preference-based alignment problem, leveraging the Direct Preference Optimization (DPO) framework. To make DPO applicable to diffusion samplers, we model the sampling policy as an energy-based model (EBM), transforming preference comparisons into tractable energy differences. We further introduce a novel energy formulation derived directly from the pretrained score network, enabling preference evaluation in perturbed spaces that jointly capture structural consistency and fine-grained details. Moreover, we introduce dynamic preferences, where the preferred samples used for alignment progressively improve as the sampling policies are learned. This self-improving mechanism replaces rigid static teacher supervision with an iterative, preference-guided refinement process, providing progressively stronger alignment signals. Extensive experiments demonstrate that D2PO aligns diffusion samplers with perceptual quality more faithfully, unlocking the full potential of high-quality teachers and consistently outperforming conventional regression-based schedulers under low-NFE constraints.

## Metadata
- **Published**: 2026-07-07T06:05:42Z
- **Authors**: Jinkyu Kim, Jinyoung Choi, Bohyung Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.06609v1)