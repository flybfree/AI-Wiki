---
title: </think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination
published: 2026-09-03T10:25:23Z
authors: Seunghee Koh, Sungjae Choi, Minchan Kwon, Sunghyun Baek, Junmo Kim
url: http://arxiv.org/abs/2609.03633v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# </think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination

## Abstract
Chain-of-thought (CoT) reasoning improves large reasoning models (LRMs) on complex tasks but often produces long, redundant traces. Recent training-free early-exit methods shorten these traces by choosing an intermediate point to stop reasoning. We study one such strategy that injects an end-of-think token (EoT, </think>) at this point to trigger the reasoning-to-answering transition, and find that the injected EoT does not always induce a clean answering phase. Answering-phase generation can continue before the model regenerates another EoT, with the span preceding this regenerated EoT scaling with the reasoning tokens saved by early exit and exhibiting continued reasoning behavior. We call this spurious CoT termination, where reasoning-like generation continues into the answering phase. We hypothesize that insufficient attention to the injected EoT contributes to spurious CoT termination and probe this hypothesis with Exit-token Attention Biasing (EAB). Across four LRMs, five benchmarks, and two early-exit methods, increasing attention to the injected EoT reduces spurious CoT termination and answering-phase length. These results reveal a limitation of controlling LRMs by externally matching their explicit think-block format. Inserting the EoT token conforms to this format but does not by itself guarantee the intended reasoning-to-answering transition. Our code is available at https://github.com/Seunghee-Koh/Spurious-CoT-Termination.

## Metadata
- **Published**: 2026-09-03T10:25:23Z
- **Authors**: Seunghee Koh, Sungjae Choi, Minchan Kwon, Sunghyun Baek, Junmo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03633v1)