---
title: Carryover Drafting: Recycling Rejected States for Speculative Decoding
published: 2026-09-13T18:20:31Z
authors: Jahyun Koo, Sunghyeon Woo, Jaeeun Kil, Jeongtae Lee, Sungjae Lee, Kyomin Jung, Minsub Kim
url: http://arxiv.org/abs/2609.14717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Carryover Drafting: Recycling Rejected States for Speculative Decoding

## Abstract
Speculative decoding accelerates LLM inference by verifying multiple drafted tokens in parallel, allowing a single target forward pass to accept several tokens. By construction, verification computes representations for both accepted and rejected tokens. Yet, conventional drafters retain only the representations of accepted tokens, leaving the substantial verifier computation spent on rejected tokens effectively wasted. We find that these discarded hidden states generated during target forward retain useful information about future tokens that can improve subsequent drafts. However, realizing this opportunity poses two distinct challenges. At inference, recycling overhead can increase drafting latency, diminishing the speedup gained from increased acceptance length. During training, standard parallel drafter training does not produce inference-aligned rejected states, while obtaining them through sequential rollouts would sacrifice parallelism across training positions. We introduce Carryover Drafting, which addresses both challenges. Carryover recycles rejected target hidden states as temporary KV context, allowing the drafter to selectively attend to them. It reuses the drafter's existing interface and adds only a single learned embedding to distinguish rejected states from committed context. The additional KV context is replaced each drafting round, keeping its length bounded by one proposal block. We introduce parallel draft--verify--draft training that exposes the drafter to inference-aligned rejected states while preserving parallelism across training positions. Experiments with DFlash and a DSpark-derived semi-autoregressive drafter across two target models show that this simple Carryover mechanism improves average acceptance length by 6.5--14.7% and end-to-end vLLM speedup by 7.9--14.4% over the corresponding baselines, with speedup gains reaching 28.8% on translation.

## Metadata
- **Published**: 2026-09-13T18:20:31Z
- **Authors**: Jahyun Koo, Sunghyeon Woo, Jaeeun Kil, Jeongtae Lee, Sungjae Lee, Kyomin Jung, Minsub Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14717v1)