---
title: BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents
published: 2026-09-08T10:56:17Z
authors: Yanhong Qian, Xuanying He, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin
url: http://arxiv.org/abs/2609.08566v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents

## Abstract
KV cache is evolving from a serving optimization into an external memory substrate for long-term LLM agents. In a shared multi-user deployment, however, reusable KV blocks introduce a missing access-control question: semantic relevance alone cannot determine whether a memory block is authorized for the current physical user. We propose Bio-MemArt, a biometric-aware KV-cache memory framework for multi-user LLM agents. Bio-MemArt attaches a normalized biometric template to each stored KV memory block, filters the shared memory pool with the current user's biometric probe, and then runs the original MemArt retrieval and KV reuse pipeline only inside the authorized candidate pool. This design preserves latent-space retrieval, direct cache reuse, and decoupled position encoding while adding physical-user access control to shared KV memory. We evaluate Bio-MemArt under Owner and Non-owner query conditions on long-term dialogue QA with face and palmprint benchmarks. Across face benchmarks, the average owner and non-owner biometric success rates are 95.71% and 0.86%; across palmprint benchmarks, they are 97.60% and 2.00%. In the efficiency study, average prefill tokens drop from 18,781.96 under full-context prompting to 28.57 with Bio-MemArt, showing that biometric gating preserves the low-token operating regime of KV-cache memory.

## Metadata
- **Published**: 2026-09-08T10:56:17Z
- **Authors**: Yanhong Qian, Xuanying He, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08566v1)