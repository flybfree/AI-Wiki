---
title: MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel
published: 2026-07-21T15:50:28Z
authors: Lenore Mulin, Gaetan Hains
url: http://arxiv.org/abs/2607.19456v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel

## Abstract
We derive four memory-optimal inference artifacts for transformer attention using the Mathematics of Arrays (MoA), each following directly from the forward-pass Denotational Normal Form (DNF) of with the query-row index fixed to the current decode step. The artifacts are: (1)~a single-query decode DNF in which the $ψ$-reduction eliminates the $K^\top$ buffer algebraically, achieving $(d_k + nd_k+ nd_v+ d_v)\times4\,{B}$ Dynamic Random Access Memory (DRAM) traffic result numerically verified to $\|{err}\|_\leq2\times10^{-7}$; (2)~a C/OpenACC Graphics Processing Unit (GPU) kernel with Operational Normal Form (ONF) stride arithmetic and hardware-coalesced memory access, verified to $\|\mathrm{err}\|_\infty=0$ (exact IEEE-754 floating-point arithmetic); (3)~a multi-step KV-cache with $O(d_k+d_v)$ per-step append via MoA concatenation $\#$; and (4)~Grouped-Query Attention (GQA) and Multi-Query Attention (MQA) derived via $ψ$-selection, achieving a proven $\frac {h_q} { h_{kv} }$ reduction in KV traffic. All programs are verified against PyTorch scaled_dot_product_attention.

## Metadata
- **Published**: 2026-07-21T15:50:28Z
- **Authors**: Lenore Mulin, Gaetan Hains
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19456v1)