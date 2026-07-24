---
title: Now We Know? A Systematic Comparison of TerraMind and THOR
published: 2026-07-20T20:55:06Z
authors: Frederick Schindlegger, Kenzo Bounegta, Eva Gmelich Meijling, Johannes Jakubik, Arnt-Børre Salberg, Theodor Forgaard, Nicolas Longepe, Valerio Marsocci
url: http://arxiv.org/abs/2607.18504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Now We Know? A Systematic Comparison of TerraMind and THOR

## Abstract
Benchmarks for Geospatial Foundation Models (GFMs) increasingly rank models by aggregate score, but such rankings obscure why models differ: how much of the gap is architecture, how much is decoder capacity, and how much is a use-case-specific artefact? This study addresses that gap through a controlled comparison of two GFMs developed under European Space Agency's $Φ$-lab with contrasting design philosophies: THOR, which introduces a compute-adaptive architecture supporting variable patch sizes and unifies Sentinel-1, -2, and -3 data at their native resolutions; and TerraMind, a multimodal generative GFM pretrained with a dual-scale token/pixel objective that enables any-to-any cross-modal generation (Thinking-in-Modalities) to infer missing sensors at inference time. Rather than reporting a single leaderboard, we investigate the axes along which the two architectures actually differ - patch size, decoder complexity, finetuning regime, input modality, and model scale - across ten use cases spanning segmentation and regression in diverse domains, including climate disaster response, methane leak detection, snow monitoring, or sea ice mapping. We find that architectural design choices - patch size and decoder type in particular - explain more performance variance than model identity itself, that the two models embody complementary investment strategies (pretraining-time scale for TerraMind versus inference-time tokenisation for THOR), and that correctly interpreting results requires dataset-level characterisation. The resulting picture is not a single winner but a set of hypotheses and a diagnostic ablation methodology that we expect to generalise to future GFMs beyond THOR and TerraMind.

## Metadata
- **Published**: 2026-07-20T20:55:06Z
- **Authors**: Frederick Schindlegger, Kenzo Bounegta, Eva Gmelich Meijling, Johannes Jakubik, Arnt-Børre Salberg, Theodor Forgaard, Nicolas Longepe, Valerio Marsocci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18504v1)