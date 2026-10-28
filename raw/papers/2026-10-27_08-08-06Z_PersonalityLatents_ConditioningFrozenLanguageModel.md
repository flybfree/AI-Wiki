---
title: Personality Latents: Conditioning Frozen Language Models on Individuals from Their Own Writing
published: 2026-10-27T08:08:06Z
authors: Gunhee Cho, Yun-Gyung Cheong
url: http://arxiv.org/abs/2610.36805v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personality Latents: Conditioning Frozen Language Models on Individuals from Their Own Writing

## Abstract
Controlling the personality of a language model usually relies on written profiles or named trait categories, so it can only express what an author writes down or what a taxonomy names. We instead propose Personality Latents (PL), which learn a latent for each person from their own writing, with no personality labels and no authored profile, and inject it into a frozen language model as a soft prefix. Following generative latent optimization, each training person receives a free latent that is optimized through the frozen model itself, while an encoder learns to predict these latents so that a new person needs only one forward pass, with optional refinement at test time. We evaluate on held-out people by having the conditioned model answer neutral and interview questions and reading personality from its answers with scorers trained on real human writing. On the MBTI axes PL reaches an AUC of , ahead of persona embedding and prompt-based baselines under identical settings, and the ranking holds when the answers are scored in three different embedding spaces. A latent learned with Qwen2.5-3B-Instruct also transfers personality to Llama-3.1-8B-Instruct through a new adapter alone.

## Metadata
- **Published**: 2026-10-27T08:08:06Z
- **Authors**: Gunhee Cho, Yun-Gyung Cheong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36805v1)