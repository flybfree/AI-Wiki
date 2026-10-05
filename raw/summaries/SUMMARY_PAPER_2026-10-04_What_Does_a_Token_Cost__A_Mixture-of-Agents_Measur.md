---
title: What Does a Token Cost? A Mixture-of-Agents Measurement of Sufficient Per-Token Compute
url: http://arxiv.org/abs/2610.02491v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_21-11-41Z_WhatDoesaTokenCost_AMixture_of_AgentsMeasurementof.md
generated_at: 2026-10-04 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a Mixture-of-Agents (MoA) framework to empirically measure the minimum computation a language model actually needs to generate each individual token, challenging the assumption that uniform per-token compute is necessary. By deploying a panel of fifteen models across three families (Qwen, OLMo, and R1-distilled) and identifying the smallest agent that can reproduce each reference token, the authors establish a "sufficient compute" upper bound per token. The key finding is that the vast majority of tokens require only trivial computation, while a small fraction of tokens dominate total FLOP expenditure, creating substantial headroom for adaptive inference strategies.

## Key Takeaways
- A 0.5B-parameter agent can successfully reproduce 92–95% of reference tokens across three core benchmarks, demonstrating that the overwhelming majority of tokens in a sequence require negligible compute and that uniform allocation across model sizes is grossly inefficient.
- The most expensive 10% of tokens account for 64–80% of estimated FLOPs across all tested model panels, revealing a highly skewed compute distribution that existing inference systems fail to exploit and that adaptive routing or drafting strategies could target directly.
- Using the MoA-derived sufficient-compute map, model routing reduces projected latency from 7.59 to 5.12 seconds on all 500 MATH-500 problems while slightly improving accuracy over the best confidence-routing baseline, and speculative drafting uses 32.6% fewer draft tokens with approximately 20% lower projected latency compared to fixed-window drafting at comparable accuracy.

## Context
Current LLM inference pipelines treat every token as equally expensive, allocating full model capacity uniformly regardless of token difficulty. Techniques like speculative decoding, model routing, and early-exit strategies implicitly assume that some tokens are "easy," but no prior work has quantified the actual per-token compute floor. This paper fills that gap by constructing a ground-truth measurement infrastructure, providing the empirical foundation that adaptive inference controllers have long needed to move from heuristic confidence signals to principled compute allocation.

## Implications
For practitioners deploying LLMs at scale, this work provides a concrete blueprint for building inference controllers that dynamically allocate model capacity per token, potentially cutting serving costs by large margins without sacrificing output quality. For the research community, the MoA measurement methodology offers a reproducible benchmark for evaluating routing, drafting, and early-exit systems against a known per-token compute budget rather than against opaque confidence heuristics. Industry deployments in high-throughput settings—chatbots, code generation, and agentic pipelines—stand to gain directly from sufficient-compute-aware scheduling that eliminates wasted FLOPs on trivial tokens while preserving capacity for genuinely difficult ones.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02491v1)
