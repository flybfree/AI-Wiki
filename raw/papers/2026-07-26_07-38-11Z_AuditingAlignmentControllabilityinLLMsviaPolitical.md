---
title: Auditing Alignment Controllability in LLMs via Political Axes
published: 2026-07-26T07:38:11Z
authors: Bartol Bućan, Nikola Sočec, Sarah Isufi, Morena Granić, Luka Hobor, Agneza Krajna, Mihael Kovac, Mario Brcic
url: http://arxiv.org/abs/2607.23519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Alignment Controllability in LLMs via Political Axes

## Abstract
Political audits of large language models (LLMs) usually reduce each to one point on a political compass. But that resting point barely matters in deployment: a model must land somewhere, and what counts is how far, and in which directions, its answers can be steered. That steering runs through the system prompt: the personalization layer a platform sets, or one induced from a user's history, not necessarily written by hand. We run a dispersion-first stress test of prompt-based controllability across 12 ideological personas plus an unsteered baseline, 70 Political Compass items, ten replicates, and seven leading LLMs: GPT-5, Claude, Grok, Gemini, DeepSeek, Kimi, and Qwen (63,700 responses). Contextual framing explains roughly 88%-93% of variance on the economic and society axes, model identity under 3%: responses are highly instruction-adjustable. Models do not shift alike: some move more, and some saturate under extreme framings. Conflicting directional-steering results in prior audits resolve once baselines are recognized as non-centered: displacement and proximity diverge, so the effect is geometric, not differential compliance. Under authoritarian prompts, models produce similar shifts on the same questions. Political-coordinate audits therefore need steerability audits reporting dispersion, symmetry, saturation, and refusal floors. We release prompts, benchmark data, and code.

## Metadata
- **Published**: 2026-07-26T07:38:11Z
- **Authors**: Bartol Bućan, Nikola Sočec, Sarah Isufi, Morena Granić, Luka Hobor, Agneza Krajna, Mihael Kovac, Mario Brcic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23519v1)