---
title: Cross-Model Memory Transfer via Target-Side Reader Adaptation
url: http://arxiv.org/abs/2608.17050v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_18-54-42Z_Cross_ModelMemoryTransferviaTarget_SideReaderAdapt.md
generated_at: 2026-08-18 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how to transfer frozen memory from one large language model to another using a lightweight reader. It finds that both the stored content and correct addressing are needed, but the transferred table only works when paired with a target‑aligned reader. The best performance is achieved with a dual‑layer four‑branch reader, matching same‑model scores.

## Key Takeaways
- Learned memory content must be correctly addressed to retrieve useful information.
- The external addressable table alone is ineffective without a reader that matches the target model’s interface.
- Adding target‑side adaptation improves performance and can recover utility when direct reader reuse is insufficient.

## Context
Large language models often embed knowledge in either external tables or within weights, each with trade‑offs. This work shows that an intermediate “engram” approach can be portable across models if the reader side adapts, offering a reusable artifact without retraining the whole model.

## Implications
Researchers can reuse pre‑trained memory artifacts across different architectures by providing compatible readers, reducing development time and cost. Practitioners may adopt this to fine‑tune knowledge transfer with minimal overhead, especially in domain adaptation scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17050v1)
