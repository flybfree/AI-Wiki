---
title: The Learning Objective Governs Perceptual Narrowing: A Cross-Lingual, Layer-Wise, Ten-Seed Study of Self-Supervised Speech Encoders
published: 2026-08-01T08:02:35Z
authors: Sejin Yoo
url: http://arxiv.org/abs/2608.00507v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Learning Objective Governs Perceptual Narrowing: A Cross-Lingual, Layer-Wise, Ten-Seed Study of Self-Supervised Speech Encoders

## Abstract
Perceptual narrowing---the developmental loss of non-native phoneme discrimination in the first year of life \citep{werker1984}---is a canonical developmental finding, yet \emph{what learning objective produces it} remains open. We train a \(\sim\)7\,M-parameter Transformer encoder on child-directed and read speech and evaluate phoneme ABX in English, French, and Mandarin over ten seeds, the seed as the unit of replication. Six results. \textbf{(1)}~The objective sets the direction of cross-lingual transfer: reconstruction (masked mel-prediction) degrades non-native discrimination, prediction (frame-contrastive) improves it---a same-encoder, same-data gap of \(+0.051\) in first-layer Mandarin ABX (\(p=3\times10^{-8}\)), unanimous in sign across twenty runs. \textbf{(2)}~That decline combines a large arm-intrinsic difficulty gradient with a smaller language-specialization effect (matched vs.\ mismatched \(+0.022\), \(p=10^{-4}\), all four layers). \textbf{(3)}~Against a language-symmetric raw-mel floor, reconstruction pushes the first layer \emph{below} the discriminability of its input; prediction pushes it \emph{above}. \textbf{(4)}~Read speech gives a \(3.6\times\) steeper non-native decline than child-directed speech. \textbf{(5)}~The customary three-seed budget cannot see this reliably: an effect unambiguous at ten seeds is called significant by as few as 70\% of three-seed subsets. \textbf{(6)}~Six objective configurations---sharpening, compression, consolidation, their composition, and word-level semantic grounding in two forms---fail to produce the full developmental signature (native improves \emph{and} non-native declines): a single objective moves both languages the same way because it acts on a shared representation. We conclude that the objective, not the architecture, is the first-order determinant of narrowing-shaped representational change.

## Metadata
- **Published**: 2026-08-01T08:02:35Z
- **Authors**: Sejin Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00507v1)