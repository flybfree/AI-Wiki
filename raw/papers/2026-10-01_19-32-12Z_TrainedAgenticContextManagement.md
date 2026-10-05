---
title: Trained Agentic Context Management
published: 2026-10-01T19:32:12Z
authors: Bryce Sandlund
url: http://arxiv.org/abs/2610.02404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trained Agentic Context Management

## Abstract
We study long context language models. Instead of training long context natively, or designing a long context harness, we train a model over the simplest possible harness: a tool to call itself with any specified prompt and a tool to read tokens in a range from the input context. We finetune Qwen3.6-35B-A3B on a diverse synthetic dataset using this harness. With only 8,000 tokens of context, our small model is as strong as GPT-5.4 with 1M tokens of context on the OOLONG-synth benchmark when document length exceeds 40K tokens.

## Metadata
- **Published**: 2026-10-01T19:32:12Z
- **Authors**: Bryce Sandlund
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02404v1)