---
title: Reflection-aware Generative Novel View Synthesis
published: 2026-09-04T17:33:45Z
authors: GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh
url: http://arxiv.org/abs/2609.05382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflection-aware Generative Novel View Synthesis

## Abstract
We propose Ref-GeNVS, a training-free, reflection-aware method for generative novel view synthesis (NVS) in mirror scenes. Existing multi-view diffusion models often fail to recognize the mirror in the scene and cannot exploit reflected content for scene generation. To fix this issue without additional training, our key idea is to treat a mirror image as two complementary views. From input images, we estimate the mirror plane and reflect camera poses to form virtual views. Based on this virtual view setup, we propose a two-stage generation method consisting of Mirror-gated attention and Reflection injection, which enables reflection-consistent NVS by explicitly leveraging reflection relationships in a multi-view diffusion model. Ref-GeNVS inherits the strong generalizability of the multi-view diffusion backbone, while it does not require finetuning. On synthetic and real scenes including mirrors, Ref-GeNVS outperforms recent generative NVS methods by generating reflection-consistent and contextually coherent novel views, revealing scene structure visible only through mirrors. Project page: https://kim-geonu.github.io/Ref-GeNVS/

## Metadata
- **Published**: 2026-09-04T17:33:45Z
- **Authors**: GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05382v1)