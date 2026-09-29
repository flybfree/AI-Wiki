---
title: Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs
published: 2026-09-26T05:30:18Z
authors: Vincent-Daniel Yun, Woosang Lim, Haneul Yoo, Sungjoo Yoo, Sai Praneeth Karimireddy, Murali Annavaram
url: http://arxiv.org/abs/2609.32259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs

## Abstract
Recent multi-agent LLM systems increasingly combine heterogeneous models for specialized agent roles. However, text-based communication requires each receiver to prefill shared context already processed by the sender. Reusing the sender's key-value (KV) cache avoids this redundancy, but prefill-free transfer across model families must handle differences in tokenization, model depth, and KV representations. To address these issues, we propose \textit{HeteroFold}, a prefill-free cross-family KV cache transfer method that keeps both the sender and receiver frozen. HeteroFold aligns model structures, maps the sender cache into the receiver space, and calibrates it to preserve receiver behavior. Across six transfer directions, HeteroFold achieves the best cache-transfer performance on all four long-context benchmarks and most short-context settings. It also matches text-based communication on the multi-agent benchmark. At 32K context length, Llama-3.1-8B$\rightarrow$Ministral-3-14B transfer is $10.7\times$ faster than Native Prefill and $1.18$--$1.47\times$ faster than the state-of-the-art prefill-free baselines, Dense Latent and KV Ridge. These results show that HeteroFold enables efficient cross-family KV reuse without receiver prefill.

## Metadata
- **Published**: 2026-09-26T05:30:18Z
- **Authors**: Vincent-Daniel Yun, Woosang Lim, Haneul Yoo, Sungjoo Yoo, Sai Praneeth Karimireddy, Murali Annavaram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32259v1)