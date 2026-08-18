---
title: Do Geometry-Aware Positional Encodings Help Transformers in Spatial Imperfect-Information Games?
published: 2026-08-15T02:20:10Z
authors: Wenji Fu
url: http://arxiv.org/abs/2608.14982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Geometry-Aware Positional Encodings Help Transformers in Spatial Imperfect-Information Games?

## Abstract
Transformers applied to spatial imperfect-information games must represent map geometry while tracking hidden entities through time. We ask whether geometry-aware positional encodings improve these capabilities, without claiming a new positional encoding. We construct a four-level benchmark on a hexagonal naval pursuit game: controlled geometry and topology probes, an exact-Bayes hidden-target tracking task, offline policy imitation at 1k and 10k games, and 7,200 fixed-seed games against three legacy opponents. Across matched Transformer backbones, HexRoPE reduces exact-belief posterior cross-entropy relative to no positional encoding by 0.278 on D6-transformed test orbits and 0.329 on a larger map; both hierarchical-bootstrap confidence intervals exclude zero, and both Holm-adjusted p-values are below 0.001. At 1k games, HexRoPE improves policy action accuracy by 4.63 percentage points over no encoding and 2.05 points over rectangular relative bias; the gains shrink to 1.55 and 0.41 points at 10k games. However, HexRoPE does not improve aggregate gameplay win rate: its paired effect over no encoding is -1.56 percentage points (95% CI [-4.50, 1.17]). Rectangular relative bias is strongest on D6 belief consistency but fails sharply when extrapolating from radius 3 to radius 4, while graph bias provides only a small blocked-edge gain. The results show that geometric inductive bias improves belief estimation and data-efficient imitation, but those representation gains do not automatically produce stronger closed-loop play.

## Metadata
- **Published**: 2026-08-15T02:20:10Z
- **Authors**: Wenji Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14982v1)