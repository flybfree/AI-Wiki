---
title: SCAPES: Semantically Conditioned Autoregressive Prior for Environmental Sounds
published: 2026-09-04T02:11:46Z
authors: Esteban Gutiérrez, Lonce Wyse, Frederic Font, Xavier Serra
url: http://arxiv.org/abs/2609.04634v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCAPES: Semantically Conditioned Autoregressive Prior for Environmental Sounds

## Abstract
As generative audio models grow in complexity, the computational and ecological costs of synthesizing everyday sounds have become increasingly prohibitive, often requiring industrial-scale resources and massive datasets. In this paper, we present SCAPES: a Semantically Conditioned Autoregressive Prior for Environmental Sounds. SCAPES is a lightweight, resource-efficient generative model designed to synthesize high-fidelity environmental textures through high-level semantic control. By operating on the continuous latent manifold of a neural audio codec, our approach bypasses the rigid structural constraints inherent to discrete tokenization. We propose a segmentation strategy that decomposes audio into overlapping segments, enabling a Continuous Normalizing Flow (CNF) to model the evolution of latent trajectories using Flow Matching. Our experiments demonstrate that a 36-million parameter instance of SCAPES can be trained on limited, uncurated datasets using a single consumer-grade GPU. Notably, convergence is achieved after training for approximately twice the source audio duration, yielding high-fidelity outputs with robust long-term stability and semantic consistency. Furthermore, we showcase the model's capacity for smooth semantic interpolation, providing a flexible and accessible tool for open research and creative sound design. Code, pretrained weights, audio examples, and an interactive demo are publicly available on our project page https://cordutie.github.io/projects/scapes.html

## Metadata
- **Published**: 2026-09-04T02:11:46Z
- **Authors**: Esteban Gutiérrez, Lonce Wyse, Frederic Font, Xavier Serra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04634v1)