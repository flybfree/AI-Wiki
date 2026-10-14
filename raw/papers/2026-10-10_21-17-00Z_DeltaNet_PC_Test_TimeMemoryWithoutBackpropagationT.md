---
title: DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time
published: 2026-10-10T21:17:00Z
authors: Todd Morrill, Richard Zemel
url: http://arxiv.org/abs/2610.15185v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time

## Abstract
Test-time memorization of sequential information is a foundational capability for any intelligent system that needs to rapidly store and retrieve data, as demonstrated by the attention mechanism in large language models. However, Transformers and linear attention variants are trained via backpropagation through time (BPTT), which has drawbacks such as its enormous memory requirements. Predictive coding (PC), an algorithm that optimizes a prediction-error energy function with local updates, offers a compelling solution but still lacks test-time memory for sequential data. We develop a solution to this problem by treating the per-step memory update $ΔS_t$ as a latent variable, as opposed to a slow weight to be learned. By taking the log probability of a standard PC-based probabilistic model, we derive a PC-native solution for verbatim sequence memory, and relate our update rule to common choices in the linear attention literature (e.g., DeltaNet). We present an extensive set of empirical tests to probe our system's properties, including its scaling capacity, memory footprint, and ability to infer a context from evidence (e.g., bank (river) vs. bank (money)). We show how DeltaNet-PC can be used for storing single sequences of data, multiple sequences of data, and key-value associative memory pairs with perfect recall accuracy.

## Metadata
- **Published**: 2026-10-10T21:17:00Z
- **Authors**: Todd Morrill, Richard Zemel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15185v1)