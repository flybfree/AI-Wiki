---
title: Full-bandwidth transformer
url: http://arxiv.org/abs/2608.08888v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
generated_at: 2026-08-10 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a full-bandwidth transformer that adds latent feedback to the standard autoregressive transformer architecture, allowing non‑verbalized computation to re-enter the stack without discarding top‑layer hidden states. Experiments show that this simple modification improves validation loss and performance on multiple downstream tasks while keeping the original parallel teacher forcing and KV cache.

## Key Takeaways
- Latent feedback fuses the previous top‑layer hidden state with the sampled token embedding via a gated linear unit, feeding it back as input for the next decoding step.  
- The method preserves the standard transformer structure, including the KV cache and language‑modeling objective, so training remains parallelizable.  
- Training schedules introduce latent feedback late in pretraining and mix a small fraction of deeper feedback passes to maintain stability.

## Context
Autoregressive transformers rely on dense attention for horizontal token access but discard vertical feedback between steps, limiting the model’s ability to reuse computation across layers. This paper demonstrates that a lightweight addition can restore this feedback, offering a path toward more efficient and effective language models without sacrificing parallel training.

## Implications
For industry practitioners, full‑bandwidth transformers could reduce inference latency by shortening reasoning traces while maintaining accuracy, lowering computational cost for large‑scale deployment. Researchers may explore similar feedback mechanisms in other sequence modeling tasks to improve efficiency and performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08888v1)
