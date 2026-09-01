---
title: HiVe: Beyond Static Prompts for Multitask Learning via Hierarchy-based Vertical Mixture-of-Experts
published: 2026-08-30T13:35:42Z
authors: HyeonJik Bae, Minyeol Kim, Susik Yoon
url: http://arxiv.org/abs/2608.29790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiVe: Beyond Static Prompts for Multitask Learning via Hierarchy-based Vertical Mixture-of-Experts

## Abstract
As large language models (LLMs) continue to scale, parameter-efficient fine-tuning (PEFT) has become a practical alternative to full-parameter adaptation. Prompt tuning is effective, but existing approaches either use flat prompt structures or hierarchical structures with fixed prompt composition, limiting adaptive prompt specialization. To address this limitation, we propose HiVe, a prompt tuning framework that models prompts at multiple levels and enables input-dependent specialization. HiVe constructs a prompt hierarchy by leveraging inter-task relationships during training, and employs a vertical mixture-of-experts (V-MoE) mechanism at inference time to compose prompts up to the level of specialization required for each input. Experiments show that HiVe consistently outperforms strong prompt tuning baselines across diverse tasks.

## Metadata
- **Published**: 2026-08-30T13:35:42Z
- **Authors**: HyeonJik Bae, Minyeol Kim, Susik Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29790v1)