---
title: How Fragile Is On-Device Language Model Safety? Localizing Safety-Critical Parameters for Sparse Fault Analysis
published: 2026-10-06T18:56:14Z
authors: Muhammad Zeeshan Karamat, Christiana Chamon Garcia
url: http://arxiv.org/abs/2610.09000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Fragile Is On-Device Language Model Safety? Localizing Safety-Critical Parameters for Sparse Fault Analysis

## Abstract
As small language models (SLMs) are increasingly deployed on resource-constrained and on-device platforms, including as components of agentic systems, the integrity of locally stored model parameters becomes an important safety concern. We investigate whether safety-sensitive behavior in LLaMA-2-7B-Chat is concentrated within a sparse subset of parameters, creating a reduced fault surface for targeted analysis. We study two complementary localization methods: low-rank safety-associated subspace analysis and parameter-level safety--utility importance filtering. Both approaches reveal highly non-uniform safety sensitivity across the network, with the MLP down_proj consistently emerging as a prominent safety-sensitive component and o_proj providing a smaller contribution. Using parameter-level localization, modifying only 0.19% of model weights in down_proj yields 53% Basic ASR and 56% GCG ASR, while tinyBenchmarks accuracy remains at 51.6% compared with a 52.2% unmodified baseline. These results motivate targeted fault analysis and selective integrity protection for language models deployed in resource-constrained, on-device, and agentic settings.

## Metadata
- **Published**: 2026-10-06T18:56:14Z
- **Authors**: Muhammad Zeeshan Karamat, Christiana Chamon Garcia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09000v1)