---
title: GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs
published: 2026-09-27T00:21:26Z
authors: Guang Yang, Fengchen Liu
url: http://arxiv.org/abs/2609.35882v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs

## Abstract
Genome foundation models are most useful where sequences are generated, yet the largest models need datacenter accelerators and a place to send private DNA. We ask whether a 15-billion-parameter genome mixture-of-experts (MoE) model can instead run on volunteers' web browsers, with the experts spread across many untrusted devices, without changing its predictions and without revealing the sequence to any single device. We build a system in which a trusted coordinator runs attention and routing while browser workers run every expert feed-forward network through hand-written WebGPU kernels, and we protect the expert inputs with real-valued Lagrange coded computing: each worker receives only a Gaussian-padded share, computes the expert's linear maps, and the coordinator decodes from any two of three workers. On GenomeOcean-MoE (8 experts, top-2 routing, 24 layers), the browser path matches native llama.cpp at every quantization level, the distributed path stays at the BF16 numerical noise floor (KL 0.0036 nats per token), and an unfitted latency model predicts decode time within 0.74% (median) under emulated wide-area links. We first show that plaintext expert inputs are not private: a probe recovers the token from a single vector at every depth, and one worker can identify the source genome from 300 unordered tokens with 92% accuracy. With coded experts, an adaptive attacker trained on shares falls to the most-frequent-token baseline, one worker's information about each token is bounded below one bit per forward pass, and the fidelity cost stays below the BF16 noise floor; in Chrome, coded decoding runs at 220 to 376 ms per token, depending on how much of the routing is hidden, and continues without replicas when a worker fails.

## Metadata
- **Published**: 2026-09-27T00:21:26Z
- **Authors**: Guang Yang, Fengchen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35882v1)