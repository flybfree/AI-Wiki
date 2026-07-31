---
title: MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians
published: 2026-07-30T14:41:02Z
authors: Pouya Ardekhani, Zahra Dehghanian, Morteza Abolghasemi, Hamid R. Rabiee
url: http://arxiv.org/abs/2607.28300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians

## Abstract
Open vocabulary 3D scene understanding is essential for next-generation interactive systems, empowering users to intuitively query and navigate reconstructed environments using natural language. However, current 3D Gaussian frameworks are often bottlenecked by restrictive multiview capture requirements, costly scene-specific optimization, and the massive memory overhead of storing dense language features. We present a novel, training-free pipeline that fundamentally reimagines this paradigm by explicitly decoupling 3D geometric reconstruction from semantic integration. Given a standard monocular video sequence as input, our method efficiently outputs a compact, highly interpretable, and fully searchable object-level semantic Gaussian map. Rather than entangling heavy language embeddings within the mapping loop, we extract geometry independently and ground semantics through a lightweight, modular post-processing framework. Extensive evaluations on the Replica dataset demonstrate that this decoupled architecture preserves strong rendering fidelity and competitive segmentation accuracy. Crucially, by replacing dense per-Gaussian storage with modular, object-level semantic embeddings, our approach delivers an order-of-magnitude reduction in memory usage compared to SOTA baselines. This provides a highly efficient, scalable, and practical solution for open-vocabulary 3D retrieval and question answering directly from everyday monocular video.

## Metadata
- **Published**: 2026-07-30T14:41:02Z
- **Authors**: Pouya Ardekhani, Zahra Dehghanian, Morteza Abolghasemi, Hamid R. Rabiee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28300v1)