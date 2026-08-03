---
title: Small Is Enough: Per-User Style Rewriting of AI-Edited Text via LoRA Adapters
published: 2026-07-31T10:14:28Z
authors: Antorweep Chakravorty
url: http://arxiv.org/abs/2607.29238v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Small Is Enough: Per-User Style Rewriting of AI-Edited Text via LoRA Adapters

## Abstract
InMyStyle is a privacy first, single user system that adapts small language models to rewrite AI-edited text towards an individual user's writing style without an instruction prompt at inference. Given a user's documents, it uses multiple local helper LLMs to construct paired training examples and fine tunes LoRA adapters on base models ranging from 0.5B to 7B parameters. Length aware generation budgets and automatic chunking support inputs of different lengths. On 219 evaluation pairs from a scientific-paper corpus, the automatic composite score plateaus at 0.69 [scale 0-1] across all model sizes under both greedy and sampled decoding. This observed plateau suggests that small models are sufficient for the measured rewriting task, with model size determining trade-offs rather than a stable quality ranking. As a secondary evaluation, 400 ratings from five LLM judges give InMyStyle outputs a mean perceived AI-ness score over 20% lower than their helper-AI generated inputs, while mean perceived AI-ness scores decrease with model size within InMyStyle.

## Metadata
- **Published**: 2026-07-31T10:14:28Z
- **Authors**: Antorweep Chakravorty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29238v1)