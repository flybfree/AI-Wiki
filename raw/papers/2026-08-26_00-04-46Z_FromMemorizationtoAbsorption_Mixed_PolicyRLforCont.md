---
title: From Memorization to Absorption: Mixed-Policy RL for Continual Knowledge Injection
published: 2026-08-26T00:04:46Z
authors: Zhibo Hou, Fan Zhao, Zhiyu An, Wan Du
url: http://arxiv.org/abs/2608.25243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Memorization to Absorption: Mixed-Policy RL for Continual Knowledge Injection

## Abstract
Continual knowledge injection is essential for keeping large language models up-to-date in a fast-evolving world. Existing methods rely on supervised fine-tuning (SFT), which memorizes injected facts in their training format but fails to generalize across paraphrasing, document combinations, and reasoning. To address this, we propose Golden-GRPO Injection (GRIN), a three-stage self-learning framework for continual knowledge injection. Golden-GRPO is a mixed-policy reinforcement learning algorithm designed specifically for knowledge injection, which injects a golden answer to provide learning signal even when on-policy rollouts fail on novel facts. We further introduce Blank and Counter, two document-level benchmarks targeting novel acquisition and counterfactual overwrite respectively, each evaluating single-fact recall, multi-source retrieval, and inferential reasoning. Our experiments establish a clear empirical claim: mixed-policy reinforcement learning enables knowledge absorption beyond what supervised fine-tuning can achieve. GRIN substantially outperforms SFT and mixed-policy RL baselines on the harder question types while matching them on basic fact recall.

## Metadata
- **Published**: 2026-08-26T00:04:46Z
- **Authors**: Zhibo Hou, Fan Zhao, Zhiyu An, Wan Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25243v1)