---
title: Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding
url: http://arxiv.org/abs/2607.27269v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_10-54-46Z_BeyondKVReconstruction_FunctionalReconstructionfor.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses a key limitation of multi‑head latent attention (MLA) conversion for open LLM checkpoints. By treating draft construction as functional reconstruction rather than simple cache compression, the authors improve token acceptance in speculative decoding. Their end‑to‑end method restores the original attention behavior on calibration hidden states without requiring verifier supervision.

## Key Takeaways
- Direct MHA/GQA to MLA conversion introduces errors from low‑rank factorization and RoPE handling that hurt draft‑token acceptance.  
- Functional reconstruction optimizes each converted module to match the post‑output projection of its original attention on hidden states, preserving cache efficiency.  
- The method works without verifier logits or supervision, making it converter‑agnostic for various backends.

## Context
LLM inference faces growing memory demands as context length increases, prompting interest in compact latent caches like MLA. Speculative decoding aims to accelerate generation by generating draft tokens ahead of verification, but its speed depends on how well drafts match the true output. This work bridges these two techniques by ensuring functional fidelity after conversion.

## Implications
Practitioners can deploy MLA‑based inference with higher acceptance rates and lower latency without retraining large models. The approach lowers development effort for companies using open checkpoints, encouraging wider adoption of efficient decoding strategies in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27269v1)
