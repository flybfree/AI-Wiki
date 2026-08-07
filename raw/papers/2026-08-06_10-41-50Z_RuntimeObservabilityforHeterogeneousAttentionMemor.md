---
title: Runtime Observability for Heterogeneous Attention Memory
published: 2026-08-06T10:41:50Z
authors: Fanzhe Wei, Li Liu, Ziyang Wang, Chenyu Wang
url: http://arxiv.org/abs/2608.05863v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Runtime Observability for Heterogeneous Attention Memory

## Abstract
Modern models no longer keep a plain KV cache: latent caches, learned sparse selectors and recurrent states each carry the model's memory in a different form, and each fails differently under compression. We give a runtime observability contract that covers all four memory classes with three operators, instantiate it on six model configurations across five architecture families, and compose the per-stage bounds into an executable request-level risk ledger. Contracts carry their error metric as a type -- composition is only defined when metrics match, and this check rejected our own first composed chain; the repaired chain crosses metrics through two proved bridges, and whatever no formal system can certify is measured instead, dropping the composed tier to empirical automatically: every claim is certified, partially certified, or empirical, composition inherits the weakest tier, and the tier is decided by the machine. Replayed over $12.4$M entry reads and run under eight-way concurrency with per-request budgets and fail-closed identity attribution, the ledger quantifies the honest trade-off on today's witness and holds its risk budget with zero violations. A fused always-on probe observes a declared one-layer subset under CUDA graphs inside the serving noise floor. Applied to a served DeepSeek-V4 stack with a packed compressed-KV prototype, the same machinery localizes a silent corruption to a precise structural boundary -- exact in the eviction-free, identity-isolated regime, with every observed failure in an eviction or slot-reuse regime -- through a machine-adjudicated discrimination campaign whose calculus rejected two of our own confounded inferences along the way. All artifacts, guards, and the Lean development are released at https://github.com/metask-ai/witprobe-attention-memory; every number in this paper regenerates from the shipped artifacts by one command.

## Metadata
- **Published**: 2026-08-06T10:41:50Z
- **Authors**: Fanzhe Wei, Li Liu, Ziyang Wang, Chenyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05863v1)