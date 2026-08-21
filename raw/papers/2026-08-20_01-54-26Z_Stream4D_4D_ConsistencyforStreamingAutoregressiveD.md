---
title: Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models
published: 2026-08-20T01:54:26Z
authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
url: http://arxiv.org/abs/2608.19556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

## Abstract
Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion. Recent bidirectional approaches address this problem using rewards signals built upon 3D Gaussian-Splatting reconstruction. However, a single rigid 3d reconstruction cannot model a dynamic scene, so this critic penalizes genuine object motion as reconstruction error and is maximized by freezing the video. This shortcut is especially detrimental in the AR setting, where each chunk can propagate an already-static configuration. In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards. To further guide motion magnitude and quality, we add a motion prior that rewards natural scene-flow magnitude while penalizing jitter and non-rigid artifacts. Our final recipe combines these two terms with a lightweight perceptual anchor. Across various autoregressive video backbones and various generation horizons, Stream4D improves 4D reconstruction quality, preserves motion more effectively, and achieves higher human-aligned preference. Project page: https://banyuanhao.github.io/Stream4D/

## Metadata
- **Published**: 2026-08-20T01:54:26Z
- **Authors**: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19556v1)