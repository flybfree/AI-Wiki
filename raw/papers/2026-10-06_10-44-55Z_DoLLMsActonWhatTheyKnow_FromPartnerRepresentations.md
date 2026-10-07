---
title: Do LLMs Act on What They Know? From Partner Representations to Cooperative Actions
published: 2026-10-06T10:44:55Z
authors: Yuhwan Jeong, Jinnyeong Yang, Kuk-Jin Yoon
url: http://arxiv.org/abs/2610.08129v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do LLMs Act on What They Know? From Partner Representations to Cooperative Actions

## Abstract
Cooperation with unfamiliar partners requires adapting to communication conventions that are not known in advance. We study this problem in a controlled Hanabi-derived environment with scripted hint generation, LLM-controlled receiving decisions, and frozen model weights. Across eight LLMs, linear probes recover intent conventions substantially more accurately than target conventions, yet receiving choices do not consistently agree with the sender's convention. We compare probe-predicted and ground-truth conventions presented either as general rules or as externally computed action recommendations. Rule statements yield modest and model-dependent changes in cooperation, whereas action translation produces larger gains on average. In a Qwen3-8B case study, matched-state statement reversals reveal much greater sensitivity to action recommendations than to rule statements. Activation transfers from oracle-action and non-oracle hint-restatement donors improve intent accuracy on both action classes, but the tested alternatives do not reliably reproduce these benefits. Together, these results distinguish convention decodability, sensitivity to convention information, and cooperative performance, and highlight limitations in turning available partner information into receiving decisions.

## Metadata
- **Published**: 2026-10-06T10:44:55Z
- **Authors**: Yuhwan Jeong, Jinnyeong Yang, Kuk-Jin Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08129v1)