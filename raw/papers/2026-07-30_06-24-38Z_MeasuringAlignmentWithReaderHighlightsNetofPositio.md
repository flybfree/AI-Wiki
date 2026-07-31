---
title: Measuring Alignment With Reader Highlights Net of Position and Length
published: 2026-07-30T06:24:38Z
authors: Kazuki Nakayashiki, Keisuke Watanabe
url: http://arxiv.org/abs/2607.27739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Alignment With Reader Highlights Net of Position and Length

## Abstract
Context compression discards most of a document before a language model reads it, and is normally evaluated by downstream task accuracy - which makes another model the judge of what mattered. Naturalistic social highlighting offers a non-circular reference: many people independently marking passages on the same page. But the obvious metric, the fraction of crowd-marked sentences a compressor keeps, is confounded twice: crowd marks are front-loaded and crowd-marked sentences are longer, so any method favouring early or long sentences scores well regardless of readers. We remove both by matching each marked sentence against unmarked sentences of the same document at equal relative depth and equal within-document length rank, and we calibrate every estimator on synthetic nulls built from position and length alone - a step that matters, since depth-only stratification returns a false positive on 20-36% of nulls containing no effect. On 120 web documents (at least 12 independent readers each), a language-model importance ranking keeps 38.4% of crowd-marked sentences against 19.9% of their matched neighbours: an enrichment of +0.196 [+0.148, +0.239], at p = 0.0005 under an exact randomization test that assumes nothing about clustering, and replicated cross-vendor. Naive truncation, whose keep rule is position, correctly falls to +0.003. To give the number a scale: scored identically, on the same budget, against a crowd label recomputed to exclude them, a single human reader reaches +0.182 - indistinguishable from GPT-5.4 (+0.002 [-0.081, +0.088]) and below Claude Opus 5. Classical methods are not null - Luhn's 1958 heuristic reaches +0.088 - so reader selection is partly recoverable by counting words; conditioning additionally on lexical centrality removes only 0.010, so the agreement is not centrality. We also report that a claim in our own prior work does not reproduce on this corpus.

## Metadata
- **Published**: 2026-07-30T06:24:38Z
- **Authors**: Kazuki Nakayashiki, Keisuke Watanabe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27739v1)