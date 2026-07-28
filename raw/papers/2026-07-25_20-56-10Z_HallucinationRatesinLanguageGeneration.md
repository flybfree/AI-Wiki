---
title: Hallucination Rates in Language Generation
published: 2026-07-25T20:56:10Z
authors: Debmalya Panigrahi, Fan Wei, Ian Zhang
url: http://arxiv.org/abs/2607.23361v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hallucination Rates in Language Generation

## Abstract
Language generation in the limit is an elegant model introduced by Kleinberg and Mullainathan [KM24] to formally study language generation by an algorithm that learns solely based on example strings. In this model, an algorithm is said to correctly generate from a language if it never makes an error after some finite time. In contrast, even sophisticated language models are known to regularly hallucinate in practice. In this paper, we initiate the study of language generation in the limit with (infinite) hallucination, i.e., the algorithm may generate incorrect strings infinitely often, but the errors occur at a limited rate (possibly even with 0-measure).   We first show that hallucination, even at rate 0, makes generation in the limit strictly more powerful: there are language collections that cannot be generated with finite error but can be generated with infinite error, even when errors occur on a 0-measure set of time-steps. Furthermore, while all countable collections are generatable with finite error, we show a strict hierarchy of (uncountable) language collections characterized by the hallucination rate. This hierarchy extends to breadth, the fraction of the target language generated. While all countable collections can attain the optimal breadth of 1/2 [KW26b], we show strict separation at every breadth and hallucination rate.   Finally, we study generation in the limit without repetition, where the algorithm may not repeat strings. This lets us compare the sets of correct and incorrect strings generated, rather than the fractions of correct and incorrect time-steps. Once again, we demonstrate a strict hierarchy at every hallucination rate and breadth. Taken together, these results reveal rich structure in language collections generatable in the limit with hallucination and establish hallucination rate as an important parameter in the theoretical study of language generation.

## Metadata
- **Published**: 2026-07-25T20:56:10Z
- **Authors**: Debmalya Panigrahi, Fan Wei, Ian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23361v1)