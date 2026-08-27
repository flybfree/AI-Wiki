---
title: Training Alignment Auditors via Reinforcement Learning
published: 2026-08-26T07:28:09Z
authors: Paul Rosu, Rowan Wang
url: http://arxiv.org/abs/2608.25460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Alignment Auditors via Reinforcement Learning

## Abstract
Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistically compares the policy's investigation to a reference investigation to determine the reward. With systematic ablations, we find that pairwise rewards yield more robust training compared to pointwise rewards, and that adding targets without planted behaviors helps maintain a low false positive rate. Training improves investigation quality against targets with planted behaviors, the rate of concerning behaviors surfaced in unmodified production models, and audit realism, while false-positive rates stay below 1%. Furthermore, auditing capabilities generalize across scaffolds: performance on AuditBench's adversarially fine-tuned targets substantially improves [Sheshadri et al., 2026].

## Metadata
- **Published**: 2026-08-26T07:28:09Z
- **Authors**: Paul Rosu, Rowan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25460v1)