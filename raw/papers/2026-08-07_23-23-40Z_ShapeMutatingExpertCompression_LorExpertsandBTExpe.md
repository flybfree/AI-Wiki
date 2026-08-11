---
title: Shape Mutating Expert Compression:LorExperts and BTExperts
published: 2026-08-07T23:23:40Z
authors: Inesh Chakrabarti, Sourjya Roy, Bowen Bao, Thiago Crepaldi, Spandan Tiwari, Ashish Sirasao
url: http://arxiv.org/abs/2608.07814v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shape Mutating Expert Compression:LorExperts and BTExperts

## Abstract
Mixture-of-Experts (MoE) language models deliver high capacity at low per-token compute, but deploying them cheaply requires compressing their many expert weight matrices. Expert pruning (e.g., REAP) and merging reduce cost but sacrifice accuracy and require retraining the router; low-rank delta decomposition of experts (e.g., D^2-MoE) preserves all experts and the router, but degrades sharply as the expert count grows because a single shared component cannot approximate many near-orthogonal experts.   Because MoE expert weights are near-orthogonal, a single shared component (as in prior delta decomposition) scales poorly with the expert count; we show that experts nonetheless organize into functional co-activation communities that are decoupled from weight similarity. Building on this, we introduce LorExperts, a router-preserving compression method that clusters experts, keeps one full-precision dominant per cluster, and represents the remaining members as low-rank corrections to their local dominant. LorExperts retains all experts and the original router (no router retraining). At ~50% expert compression on Qwen3-30B-A3B and Gemma-4-26B-A4B, LorExperts preserves downstream accuracy and perplexity better than the baselines on most of the tasks; the margin over D^2-MoE grows with expert count E. We further give a reconstruction fine-tuning procedure for LorExperts, and BTExperts, a tree organization of dominants and corrections that enables inference-time amortization of shared computation.

## Metadata
- **Published**: 2026-08-07T23:23:40Z
- **Authors**: Inesh Chakrabarti, Sourjya Roy, Bowen Bao, Thiago Crepaldi, Spandan Tiwari, Ashish Sirasao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07814v1)