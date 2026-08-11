---
title: LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems
published: 2026-08-08T17:05:08Z
authors: Heng Zhou, Lian Zhang, Yutao Fan, Tiancheng He, Siki Chen, Hejia Geng, Philip Torr, Zhenfei Yin
url: http://arxiv.org/abs/2608.08236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems

## Abstract
Multi-agent LLM systems often fail not for lack of candidate answers, but because they have no persistent mechanism for deciding which incompatible claim should currently be trusted. Majority vote, debate, and judge-based selection choose an output without recording which claim wins, which is contested, or why a later update supersedes it. We present \term{LatticeMind}, a conflict-aware structured memory that handles contradiction at write time. It maintains explicit item status, applies cheap symbolic conflict checks, and invokes LLM reconciliation only for unresolved semantic cases. On a label-blind ConflictBank evaluation that removes source-name hints, LatticeMind reaches 0.97 accuracy versus 0.61 for the strongest aggregation baseline, with the gap significant at $p<10^{-6}$ by paired McNemar test. Ablations show that removing the checker or the reconciler costs 12 to 14 points. On four secondary planning benchmarks the picture is mixed: LatticeMind beats naive merge on three of four, but does not replace deliberation methods on tasks rewarding iterative search.

## Metadata
- **Published**: 2026-08-08T17:05:08Z
- **Authors**: Heng Zhou, Lian Zhang, Yutao Fan, Tiancheng He, Siki Chen, Hejia Geng, Philip Torr, Zhenfei Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08236v1)