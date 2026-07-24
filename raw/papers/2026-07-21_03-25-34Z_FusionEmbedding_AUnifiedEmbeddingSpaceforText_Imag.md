---
title: Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio
published: 2026-07-21T03:25:34Z
authors: Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Arman Luthra
url: http://arxiv.org/abs/2607.18666v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio

## Abstract
A single embedding space that covers text, images, video, and audio lets one index serve every query a user can pose. Embedding models built on vision-language backbones now lead text/image/video retrieval benchmarks but lack audio entirely, while audio-text retrieval is led by specialist systems that serve no other modality. We present the Fusion Embedding family, which adds audio to a frozen vision-language embedding base whose parameters are never updated: generation 1 (fusion-embedding-1) trains only a 16.4M-parameter connector between a frozen audio tower and the frozen base, and generation 2 (fusion-embedding-2) adds modality-gated deep adapters (44.2M parameters) whose branch never executes on text, image, or video inputs: their outputs are bit-for-bit those of the released base, verified after every training run. Because the base already binds text, images, and video, aligning audio to text alone makes audio-image retrieval emerge, with zero paired audio-visual training data. Alongside the recipe we map its design space with controlled negative results (rewriting training captions with an LLM, substituting a leaderboard-stronger audio tower, and widening the connector each reduce retrieval) and with training-protocol findings that we expect to transfer to any frozen decoder-LM embedding backbone. Both generations train in hours on a single GPU. Weights, code, and the evaluation harness are openly released.

## Metadata
- **Published**: 2026-07-21T03:25:34Z
- **Authors**: Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Arman Luthra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18666v1)