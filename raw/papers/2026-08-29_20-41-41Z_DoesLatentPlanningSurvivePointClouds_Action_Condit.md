---
title: Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations
published: 2026-08-29T20:41:41Z
authors: Fabio F. Oberweger, Michael Schwingshackl
url: http://arxiv.org/abs/2608.29434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations

## Abstract
JEPA world models make latent-space planning a practical route to control, but they are built almost exclusively on images. Whether latent prediction survives geometric observations is unclear: point clouds are sparse, unordered, and self-occluded, and with 0.3-15% of scene points moving, the slow-feature optimum of latent prediction compounds with the geometric shortcut of 3D self-supervision. We lift three canonical JEPA designs to point clouds, frozen-encoder, distribution-prior, and action-sensitive, and re-sense the stable-worldmodel benchmark so that only the observation differs from the image baselines. All three plan without collapse: the distribution-prior model is statistically equivalent to its re-evaluated image counterpart on every benchmark, and the action-sensitive model attains the strongest result in our controlled comparison where the most geometry moves. Probing explains why: object positions are almost perfectly linearly decodable and attention falls on the few moving points. Planning withstands heavy dropout never seen in training, though range noise defeats the thinnest scene. Geometry finally makes a commanded 3D target a natural goal interface: we construct the goal latent from the target and the current latent, at no cost in success rate, without a goal observation.

## Metadata
- **Published**: 2026-08-29T20:41:41Z
- **Authors**: Fabio F. Oberweger, Michael Schwingshackl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29434v1)