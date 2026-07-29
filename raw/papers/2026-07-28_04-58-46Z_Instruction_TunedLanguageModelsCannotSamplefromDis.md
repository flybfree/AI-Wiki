---
title: Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe
published: 2026-07-28T04:58:46Z
authors: Chaemin Jang, Dongman Lee, Jihee Kim
url: http://arxiv.org/abs/2607.25292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe

## Abstract
Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. The same persona on the same question returns the same answer on more than half of items in a public-opinion benchmark. The collapse is sharp: the model's internal probabilities concentrate on a single option, and the failure is substantially amplified by instruction tuning: across three model families with materially different post-training pipelines, every instruction-tuned model fails on every task we test, while base models fail far less often. Strikingly, the same model that cannot sample from a distribution can describe it accurately in a single call. We call this gap the KNOWS/DOES split, and trace it to a degenerate sampling primitive visible in the logits and induced by alignment training. Exploiting this split, asking the model to describe the response distribution in one call more than halves the error against human survey data compared to persona aggregation. For applications that require per-persona outputs, we propose Prompt-Perturbed Argyle (PPA), which reduces the same error by 21% at no added cost.

## Metadata
- **Published**: 2026-07-28T04:58:46Z
- **Authors**: Chaemin Jang, Dongman Lee, Jihee Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25292v1)