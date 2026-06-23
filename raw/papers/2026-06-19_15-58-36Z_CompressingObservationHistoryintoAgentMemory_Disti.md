---
title: Compressing Observation History into Agent Memory: Distilling Transformers into Recurrent Transformers
published: 2026-06-19T15:58:36Z
authors: Philippe Weinzaepfel, Christian Wolf, Bülent Mert Sariyildiz, Guillaume Bono, Gianluca Monaci
url: http://arxiv.org/abs/2606.21562v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compressing Observation History into Agent Memory: Distilling Transformers into Recurrent Transformers

## Abstract
Transformers are AI's workhorse with strong performance in modeling sequential data, but their computational cost becomes prohibitive when processing long sequences. We target long-horizon streaming vision and robotics applications like map-free pose estimation, where it is particularly impractical to store and maintain a history of observations. Recurrent Transformers address this limitation by maintaining fixed-size memory but their performance lags behind that of transformers operating over the full observation history. We argue that this gap does not stem from architectural limitations, but from differences in how these models learn to compress past information. Without access to an observation history, recurrent models must explicitly decide what to retain in memory at each step, a significantly harder learning problem. In this work, we propose a distillation approach that transfers the compression strategy of a classical full-history transformer to a recurrent variant. We enable this by designing a teacher model that explicitly compresses its observation history into a fixed-size bottleneck representation. By directly supervising the student's memory with this bottleneck representation, we align the two compression mechanisms. We show that this approach allows to train a recurrent latent robotic memory with linear-time complexity while substantially narrowing the performance gap to full-history transformers.

## Metadata
- **Published**: 2026-06-19T15:58:36Z
- **Authors**: Philippe Weinzaepfel, Christian Wolf, Bülent Mert Sariyildiz, Guillaume Bono, Gianluca Monaci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.21562v1)