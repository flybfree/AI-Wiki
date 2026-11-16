---
title: Show Your Work in Swahili: Reinforcement Learning for Native-Language Mathematical Reasoning
published: 2026-11-11T23:25:01Z
authors: Jessica Lundin, Katherine Rosenfeld, David Adelani, Geoffrey Mosoti Nyakiongora, Halfan Ngowo, Sloan Coffin, Ralph Abboud, Guillaume Chabot-Couture
url: http://arxiv.org/abs/2611.16104v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Show Your Work in Swahili: Reinforcement Learning for Native-Language Mathematical Reasoning

## Abstract
We present Fikiria, a two-stage SFT+GRPO recipe for Swahili mathematical reasoning. Its reward multiplies a format gate by a weighted sum of answer accuracy and the ChrF\texttt{++} similarity of the Swahili reasoning to an in-language reference chain of thought, so that training targets the surface fidelity of the reasoning trace and not only the final answer. We train on a 2.3k-problem Swahili dataset created by translating GSM8K with GPT-4.1 and filtering with SSA-COMET. On AfriMGSM Swahili, Fikiria-AfriqueQwen-14B reaches 79.2\%. Under the same fixed prompt and strict answer-format scoring, GPT-4o reaches 68.0\%, partly because it often fails the required answer format; IrokoBench reports 78.8\% for GPT-4o using a best-per-model prompt, a figure numerically close to ours but not directly comparable. In a small human evaluation with co-author annotators, GPT-4o's outputs were preferred overall. ChrF\texttt{++} measures surface fidelity, not the validity of individual reasoning steps.

## Metadata
- **Published**: 2026-11-11T23:25:01Z
- **Authors**: Jessica Lundin, Katherine Rosenfeld, David Adelani, Geoffrey Mosoti Nyakiongora, Halfan Ngowo, Sloan Coffin, Ralph Abboud, Guillaume Chabot-Couture
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.16104v1)