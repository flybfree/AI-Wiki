---
title: Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair
url: http://arxiv.org/abs/2608.23144v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_11-49-37Z_Activation_WeightedSeededResidualCodingforLow_BitL.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Activation‑Weighted Seeded Residual Coding (AWSRC) as a lightweight repair codec that augments low‑bit quantized LLMs with deterministic seed‑based residual encoding. On Qwen2.5‑3B‑Instruct, it recovers 88.2 % of the PPL gap and improves accuracy metrics while adding only ~0.8 % to model size.

## Key Takeaways
- AWSRC encodes the weight error using deterministic seed‑generated bases and stores only low‑bit coefficients, scales, and sidecar selectors rather than a full codebook.
- The repair targets activation‑weighted errors that most influence layer outputs, prioritizing correction where it matters most.
- A 49.25 MB sidecar (≈0.8 % of BF16 payload) yields the best perplexity and task accuracy among sparse, low‑rank, and vector‑quantized codecs.

## Context
Low‑bit quantization is essential for efficient deployment but often introduces errors that degrade model performance. Existing repair methods either require large sidecars or are too complex to integrate with existing backbones. AWSRC offers a compact, deterministic solution compatible with INT4 RTN models.

## Implications
This approach can be applied to any quantized LLM without retraining, reducing storage and latency while preserving quality. Practitioners can adopt it to improve inference efficiency on edge devices or cloud services where bandwidth is limited.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23144v1)
