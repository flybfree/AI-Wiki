---
title: What Emerges and What Breaks in Self-Play Driving
published: 2026-08-31T14:01:32Z
authors: Laur Sisask, Ardi Tampuu, Tambet Matiisen
url: http://arxiv.org/abs/2608.30819v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Emerges and What Breaks in Self-Play Driving

## Abstract
Training autonomous driving policies through pure self-play has recently shown promising results. Following Gigaflow and Puffer- Drive, we train driving policies in a similar self-play fashion, but extend the models from MLPs to Transformers and train on the high-definition map of a real city, where we ultimately aim to deploy them. On the CARLA and Waymax benchmarks, our policies fall short of Gigaflow, and we trace the gap to specific failure modes, including reward hacking at traffic lights and a missing incentive to stop at stop signs. We further analyze which traffic rules emerge from self-play and how closely they match human driving, and we confirm that reward conditioning yields the intended diversity of driving behaviors. A demonstration of a trained policy is available at https://laursisask-ut.github.io/eccvdemo.

## Metadata
- **Published**: 2026-08-31T14:01:32Z
- **Authors**: Laur Sisask, Ardi Tampuu, Tambet Matiisen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30819v1)