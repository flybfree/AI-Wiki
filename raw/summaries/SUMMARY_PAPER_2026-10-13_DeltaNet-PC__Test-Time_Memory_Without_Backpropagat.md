---
title: DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time
url: http://arxiv.org/abs/2610.15185v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_21-17-00Z_DeltaNet_PC_Test_TimeMemoryWithoutBackpropagationT.md
generated_at: 2026-10-13 22:12
model: gpt-5.6-luna
---

## Summary
DeltaNet-PC introduces a predictive-coding approach to test-time memory for sequential data without requiring backpropagation through time (BPTT). The method treats each per-step memory update as a latent variable rather than a slow parameter update, producing a local, PC-native rule that supports verbatim sequence recall, contextual inference, and key-value associative memory.

## Key Takeaways
- The central contribution is a new way to integrate test-time memory into predictive coding. Instead of learning memory updates through slow weight optimization, DeltaNet-PC infers the update \(ΔS_t\) as a latent variable at each time step, enabling online storage and retrieval with local computations.
- The authors derive their update rule from the log probability of a standard predictive-coding probabilistic model. This connects the method to established linear-attention mechanisms, including DeltaNet, showing that some attention-style memory updates can be interpreted through a predictive-coding framework.
- Empirical tests examine scaling capacity, memory footprint, and contextual disambiguation. DeltaNet-PC reportedly achieves perfect recall for single sequences, multiple stored sequences, and key-value associative memory pairs, while also inferring context from evidence such as distinguishing “bank” in a river-related setting from “bank” in a financial setting.

## Context
Modern Transformers rely on attention and BPTT-based training to learn how to store and retrieve sequential information, but these approaches can impose substantial memory and computation costs. Predictive coding offers a potentially more efficient alternative because it uses local prediction-error updates, yet it has historically lacked an effective mechanism for rapidly memorizing sequence-specific information at inference time. DeltaNet-PC addresses this gap by combining predictive-coding principles with a dynamic memory state.

## Implications
The work suggests a path toward recurrent or attention-like systems that can adapt to new information during inference without modifying model weights or storing full backpropagation histories. If the reported recall and scaling properties hold beyond the tested settings, the approach could benefit memory-constrained language models, continual-learning systems, and edge applications requiring rapid context adaptation. It also provides a theoretical bridge between predictive coding and linear attention, potentially enabling new architectures that trade some Transformer complexity for local, online memory updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15185v1)
