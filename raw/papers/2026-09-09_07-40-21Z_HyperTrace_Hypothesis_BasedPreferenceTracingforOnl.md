---
title: HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization
published: 2026-09-09T07:40:21Z
authors: Jianzhi Shen, Keyu Mao, Minghao Shao, Chuanyang Jin, Yusong Wang, Ailiang Lin, Kotaro Funakoshi, Manabu Okumura, Tianmin Shu, Muhammad Shafique
url: http://arxiv.org/abs/2609.09835v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization

## Abstract
Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction. Existing training-free methods rely on stored histories or retrieved memories, but they often struggle to reconcile long- term preferences with short-term topic-specific needs. To address this issue, we propose HyperTrace, a training-free framework that formulates online personalization as latent preference tracing. HyperTrace maintains interpretable natural-language hypotheses over short-term intent and long-term preferences, and updates them through an SMC-style reweight process using an LLM-based surrogate choice model. By updating these hypotheses across turns and sessions, HyperTrace enables personalization without parameter updates. Experiments on PRISM and PersonaMem-v2 show that HyperTrace improves response alignment, preference prediction, and profile consistency over strong online baselines, demonstrating the effectiveness of tracing latent user preferences for robust personalization. Code and scripts are available in the repository: https://github.com/jiseshen/HyperTrace.

## Metadata
- **Published**: 2026-09-09T07:40:21Z
- **Authors**: Jianzhi Shen, Keyu Mao, Minghao Shao, Chuanyang Jin, Yusong Wang, Ailiang Lin, Kotaro Funakoshi, Manabu Okumura, Tianmin Shu, Muhammad Shafique
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09835v1)