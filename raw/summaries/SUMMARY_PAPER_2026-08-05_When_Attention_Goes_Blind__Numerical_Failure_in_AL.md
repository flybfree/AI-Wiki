---
title: When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings
url: http://arxiv.org/abs/2608.03994v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-54-01Z_WhenAttentionGoesBlind_NumericalFailureinALiBiPosi.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reveals a hidden flaw in ALiBi’s linear positional encoding that causes floating‑point underflow, wiping out many attention weights and making certain heads effectively blind. The authors analyze the failure mode, test mitigation strategies on large pretrained models, and show that log‑scaled distances improve retrieval while keeping baseline performance strong.

## Key Takeaways
- ALiBi’s linear bias scaling can underflow in floating‑point arithmetic, nullifying a large fraction of attention weights.
- The blind heads still function but retrieve tokens less accurately than expected, especially for needle‑in‑haystack tasks.
- Training with log‑scaled distances provides the most consistent boost to passkey retrieval compared to other mitigation approaches.

## Context
ALiBi is widely used in transformer models to replace sinusoidal positional encodings without learnable parameters. While it offers computational efficiency, this paper uncovers a numerical stability issue that could silently degrade model behavior on large‑scale pretraining.

## Implications
Practitioners should monitor attention weight magnitudes and consider log‑scaled distances when deploying ALiBi for retrieval‑oriented tasks. Ignoring the underflow risk may lead to unexpected performance drops in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03994v1)
