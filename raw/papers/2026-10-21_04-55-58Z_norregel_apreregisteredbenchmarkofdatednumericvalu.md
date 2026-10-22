---
title: norregel: a preregistered benchmark of dated numeric values in Norwegian law
published: 2026-10-21T04:55:58Z
authors: Eirik Botten Nicolaysen
url: http://arxiv.org/abs/2610.29207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# norregel: a preregistered benchmark of dated numeric values in Norwegian law

## Abstract
norregel asks language models for numeric values in Norwegian statutes, regulations and parliamentary decisions (NOK amounts, percentages, multiples of the National Insurance basic amount (G) and age limits), each at a stated date. The 916 items were extracted mechanically from Lovdata's open data, and each carries the dated history of its provision, so an answer can be classed as correct, outdated, wrong or uninterpretable. We report a first and a second preregistered run on the same items. In the first run (five models, listed publicly only after local analysis), H1, that outdated answers are more frequent for values that took effect after a model's cutoff, could not be tested in substance, and H2 and H3 were inconclusive; Opus 5.5 and Sonnet 4.6 answered 46.7% and 40.2% of the 880 primary items correctly. The second run was preregistered and published before any of its calls, and eight models were analysed. Its pooled primary test supported H1 under the preregistered decision rule (d = 17.8 percentage points, 95% interval [7.7, 28.9], p = 0.0001). In the preregistered sensitivity analysis S8, which counts as outdated only the most recent value that differs from the key, d was 3.9 [-3.6, 12.7] (p = 0.1754), an interval that contains 0. H1 was supported in every other preregistered sensitivity analysis, but S8 is the only one that gives both groups one target value, so we do not regard the support for H1 as robust. The share of outdated answers equal to that most recent value (H2) was 56.1% [46.6, 65.0], an interval that contains 0.5, and the pooled test of a lower share correct in Nynorsk than in Bokmål (H3) was inconclusive. Several models, among them Haiku 4.5, gave mostly uninterpretable answers. Items and keys are withheld; item IDs, per-answer classes, code and results are on Zenodo.

## Metadata
- **Published**: 2026-10-21T04:55:58Z
- **Authors**: Eirik Botten Nicolaysen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29207v1)