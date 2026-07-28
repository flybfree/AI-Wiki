---
title: Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting
published: 2026-07-24T20:01:33Z
authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois
url: http://arxiv.org/abs/2607.22890v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting

## Abstract
Domain Randomization (DR) is a standard technique for closing the Sim-to-Real gap, yet traditional DR pipelines rely on classical computer graphics rendering driven by polygon meshes. For complex organic subjects, such as insect specimens, extracting and rendering textured meshes is challenging. To address this issue, we propose a meshless DR framework that operates on the parameter space of 3D Gaussian Splatting (3DGS). Our method employs two independent perturbation pipelines to synthesize randomized training datasets. First, a Photometric DR pipeline alters the baked illumination and color balance by modulating the Spherical Harmonics (SH) coefficients. Second, a Procedural DR pipeline isolates the subject's geometric shape by replacing its original textures with 3D spatial noise. Finally, these perturbed radiance fields are composited over stochastically varied backgrounds using a rasterization engine. Our parameter manipulation provides a meshless alternative for generating robust datasets for complex geometries.

## Metadata
- **Published**: 2026-07-24T20:01:33Z
- **Authors**: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22890v1)