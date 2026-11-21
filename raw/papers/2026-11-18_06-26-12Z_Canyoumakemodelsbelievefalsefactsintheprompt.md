---
title: Can you make models believe false facts in the prompt?
published: 2026-11-18T06:26:12Z
authors: Ananya Sutradhar, Fabien Roger
url: http://arxiv.org/abs/2611.23938v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can you make models believe false facts in the prompt?

## Abstract
Making LLMs believe false facts is useful for alignment evaluations and for building model organisms. Previous work explored doing so with Synthetic Document Finetuning (SDF). But SDF requires fine-tuning one new model for each set of injected false beliefs. To enable larger scale SDF-powered alignment evaluations, we attempt to produce a single model that believes any fact placed in a <facts> tag in the prompt. To do so, we explore doing prompt-conditioned SDF: fine-tuning a model on synthetic documents covering thousands of facts, with each document conditioned on a fact presented in the prompt. We evaluate how deeply the model believes the facts provided in the prompt using evaluations from prior work and a new Jacobian lens evaluation. We find that the belief depth on unseen facts scales roughly log-linearly with the number of training facts, making this a cheap, promising avenue for making models believe false facts, though preliminary experiments on applying it to alignment audits on the small model we studied showed negative results due to these small models often already acting as if they believed facts provided in regular honeypot system prompts. Using RL to reduce the rate at which models verbalize following a false fact in the prompt, on top of prompt-conditioned SDF, generalizes to held-out evals and almost matches SDF on some evaluations. But training against one of our metrics for belief depth makes it harder to trust those evaluations.

## Metadata
- **Published**: 2026-11-18T06:26:12Z
- **Authors**: Ananya Sutradhar, Fabien Roger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.23938v1)