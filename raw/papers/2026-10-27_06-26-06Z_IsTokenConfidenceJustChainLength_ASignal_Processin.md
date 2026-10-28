---
title: Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces
published: 2026-10-27T06:26:06Z
authors: Pragna Mallappa
url: http://arxiv.org/abs/2610.36709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces

## Abstract
Reasoning language models answer math problems by writing long chains of thought, and sampling many chains per problem and taking a majority vote raises accuracy at a large cost in generated text. A popular way to cut that cost scores each chain by the model's confidence in each token it writes, where a token is a word or part of a word. The method averages this confidence over a sliding window of 2048 tokens and keeps or stops chains based on the lowest average. We treat the confidence, recorded token by token, as a signal in the sense of audio or radio, and examine the method with standard signal-processing tools such as spectral analysis and statistical tests for detecting a sudden change. We sampled 16 chains for each of 500 problems from two math benchmarks with a small open reasoning model. The windowed-minimum score turns out to measure mostly how long a chain is. Ranking chains by length alone does as well as or better than the confidence score, and once length is accounted for the score carries no information about correctness. Signal processing explains why: the minimum of a longer stretch of a slowly drifting signal is lower by chance alone, and the confidence signal drifts slowly enough that this effect dominates. The spectrum does hold a small signal that length does not explain, since incorrect chains carry more rapid token-to-token fluctuation, but it is too weak to improve the vote. For stopping chains early, neither the sliding average nor a classical change detector beats the simpler choice of sampling fewer chains.

## Metadata
- **Published**: 2026-10-27T06:26:06Z
- **Authors**: Pragna Mallappa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36709v1)