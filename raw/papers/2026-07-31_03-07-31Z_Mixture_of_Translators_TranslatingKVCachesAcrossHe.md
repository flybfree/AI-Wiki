---
title: Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models
published: 2026-07-31T03:07:31Z
authors: Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Soyoung Park, Gwangseon Jang, Sungsu Lim
url: http://arxiv.org/abs/2607.28979v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models

## Abstract
Heterogeneous Large Language Model (LLM) systems increasingly rely on shared contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or store caches for the same context, limiting the scalability of multi-model reasoning and long-context generation. We propose Mixture-of-Translators(MoT), a cache translation framework that maps context KV caches from a source LLM into the cache space of a target LLM. Unlike prior approaches that depend on a single projection path or global shared latent space, MoT uses multiple translator modules to capture diverse source--target mappings. To further reduce residual translation error, we introduce a Context Correction Loss that aligns the replayed target trajectory with the native target trajectory. We reveal two competing failure modes in cache translation: propagated translation shift from early injection and last-state shift from late injection. MoT addresses them through translator mixtures and target-side correction. Across homogeneous and heterogeneous translations among Qwen2.5, GPT-2, and OPT models, MoT preserves downstream QA performance, including Qwen2.5-7B-scale translation with 51.0% average closed-set QA accuracy and 0.43 average extractive QA F1. In practical case studies, MoT enables quality-preserving memory reuse for multi-agent reasoning and retains 96.3% of direct-context quality in long-context cache-augmented generation, demonstrating scalable KV cache reuse across heterogeneous LLMs.

## Metadata
- **Published**: 2026-07-31T03:07:31Z
- **Authors**: Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Soyoung Park, Gwangseon Jang, Sungsu Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28979v1)