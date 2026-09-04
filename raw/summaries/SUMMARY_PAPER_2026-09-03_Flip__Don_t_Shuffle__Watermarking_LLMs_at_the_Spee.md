---
title: Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference
url: http://arxiv.org/abs/2609.03844v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_13-38-49Z_Flip_Don_tShuffle_WatermarkingLLMsattheSpeedofInfe.md
generated_at: 2026-09-03 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Stateless Bernoulli Watermarking (SBW), a new statistical watermark for large language models that detects green‑list membership with constant‑time per token checks using independent Bernoulli trials. Experiments show SBW is faster than existing methods, adds minimal inference overhead, and maintains the same detection guarantees as traditional fixed‑size green lists.

## Key Takeaways
- SBW reduces membership complexity to O(1) by performing a single comparison per token against a counter‑based random number generator, enabling single‑kernel execution with no intermediate allocations.  
- The stateless design allows full‑vocabulary self‑salt watermarking that is over 6000 times faster than KGW’s self‑salt and twice as fast as SynthID while still biasing the entire vocabulary with candidate‑dependent seeding.  
- GPU‑native Jenkins hash improves null calibration by a factor of 1.8 and yields more diverse generated text, confirming that hash function design is an under‑explored axis for watermark quality.

## Context
Current watermarking techniques such as KGW and SynthID rely on complex permutations or multi‑layer tournaments that increase latency and memory usage. As LLMs become larger and inference must be served at scale, these limitations hinder real‑time detection and deployment. SBW addresses this by decoupling watermark generation from the model’s forward pass, making it compatible with distributed inference pipelines.

## Implications
For industry practitioners, SBW offers a practical way to embed detectable signatures without sacrificing performance or throughput. The low overhead and constant‑time checks make it suitable for real‑time applications where latency is critical. Moreover, its statistical equivalence across multiple configurations ensures robust detection even under adversarial seeding strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03844v1)
