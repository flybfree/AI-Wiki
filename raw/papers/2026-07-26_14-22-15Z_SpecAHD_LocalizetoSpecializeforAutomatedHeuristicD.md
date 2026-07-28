---
title: SpecAHD: Localize to Specialize for Automated Heuristic Design in Large-Scale Routing Problems
published: 2026-07-26T14:22:15Z
authors: Kezhao Lai, Yutao Lai, Hai-Lin Liu
url: http://arxiv.org/abs/2607.23676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecAHD: Localize to Specialize for Automated Heuristic Design in Large-Scale Routing Problems

## Abstract
LLM-based automated heuristic design (AHD) typically scores executable programs on complete instances or within fixed solver components. In large-scale routing problems, localized reconstruction reduces the size of each optimization task, but repair regions within the same incumbent can exhibit substantially different structures. One construction rule must therefore compromise across them. In this paper, we propose SpecAHD, a coupled bilevel framework for within-instance specialization. An upper-level search learns where to expose bounded repair regions, while a lower-level search evolves a complementary repertoire of executable heuristics for the induced repair tasks. The upper-level program determines the repair tasks seen by the lower level, while checked repair outcomes determine how upper-level programs are evaluated. The lower-level objective favors heuristics that perform well on average or solve tasks that the current repertoire handles poorly. For the repair tasks induced by a fixed upper-level program and a fixed lower-level candidate pool, this objective is monotone submodular, allowing greedy repertoire selection with a (1-1/e) approximation guarantee. Across four routing problems and multiple LLM backbones, SpecAHD reduces held-out objective cost by up to 57.7% against the strongest competing AHD baseline and outperforms the per-instance baseline envelope on most public instances.

## Metadata
- **Published**: 2026-07-26T14:22:15Z
- **Authors**: Kezhao Lai, Yutao Lai, Hai-Lin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23676v1)