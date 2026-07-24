---
title: A Better Start for Language Models: Domain-Conditional Position Offsets
url: http://arxiv.org/abs/2607.18302v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_02-12-09Z_ABetterStartforLanguageModels_Domain_ConditionalPo.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a domain‑conditional position offset that mitigates the cold‑start accuracy loss of autoregressive language models by adding a learned vector to embeddings at the first tokens while keeping all model weights frozen. Experiments across Mamba, GPT‑NeoX and Llama variants show up to 27 % reduction in in‑domain perplexity with minimal latency.

## Key Takeaways
- A single learned vector is added only to the activation of the first sequence positions, reducing cold‑start error without retraining model weights.  
- The offset can be switched between domains instantly and requires no additional state or latency overhead.  
- Compared with direct logit‑bias correction, the offset achieves higher perplexity gains while leaving later‑token loss unchanged.

## Context
Language models often struggle to generate coherent text at the start of a sequence because they rely on generic pretraining priors that lack domain knowledge. This cold‑start penalty is especially pronounced for specialized or short documents where early tokens carry most of the signal. Recent work has explored adapters and soft prompts, but many require extra parameters or active computation.

## Implications
The offset provides a lightweight, switchable tool for rapid in‑domain scoring and calibration without modifying model architecture. Practitioners can apply it to improve retrieval reranking or classification when early tokens are decisive, offering a practical alternative to heavier adapters like LoRA.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18302v1)
