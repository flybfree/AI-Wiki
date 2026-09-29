---
title: Can Open-Weight Large Language Models (LLMs) Simulate Human Survey Populations? A Cross-Instrument Calibration Study
published: 2026-09-26T14:01:34Z
authors: Grandee Lee, Wang Yue
url: http://arxiv.org/abs/2609.32638v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Open-Weight Large Language Models (LLMs) Simulate Human Survey Populations? A Cross-Instrument Calibration Study

## Abstract
Large language models (LLMs) are increasingly used to generate synthetic survey respondents and digital twins of real people, but whether their output preserves real human statistical structure, rather than surface plausibility, remains unresolved, and most existing evidence comes from proprietary models rather than open-weight ones. We evaluate three open-weight LLM families on a cross-instrument calibration task: conditioning personas on real respondents' verbatim answers to one psychometric instrument and measuring them on a second, construct-distance-controlled instrument, checked against a 2,058-person human panel. Across a 139-pair grid, the simulated cross-instrument correlation tracks the real human correlation at r = 0.70 - 0.73 in every model, driven mainly by correct sign rather than precise magnitude and concentrated in pairs of moderate construct distance. A correlation of this magnitude, obtained from untuned open-weight models conditioned only on individual-level survey data, is a substantively encouraging result for LLM-based behavioral simulation and digital-twin applications: specific model families and releases already reproduce a meaningful share of real human cross-instrument structure without any fine-tuning. This capability does not, however, improve monotonically across model releases: on a matched panel, the newest of three tested Llama releases performs worst on two of three headline metrics, so realizing its promise in practice requires release-specific, distance-aware verification rather than a one-time benchmark.

## Metadata
- **Published**: 2026-09-26T14:01:34Z
- **Authors**: Grandee Lee, Wang Yue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32638v1)