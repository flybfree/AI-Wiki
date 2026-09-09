---
title: Quantization Amplifies Determinism, Not Bias: Scale-Dependent Behavioral Effects of Serving-Time Weight Compression
url: http://arxiv.org/abs/2609.07901v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_19-06-31Z_QuantizationAmplifiesDeterminism_NotBias_Scale_Dep.md
generated_at: 2026-09-08 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how serving-time weight quantization influences both determinism and bias in open-weight LLMs, finding that 4‑bit quantization narrows output diversity at the smallest model size while larger models exhibit stylistic drift rather than increased stereotype amplification.  

## Key Takeaways
- At 8B, int4 reduces output diversity: the probability two samples for the same scenario recommend the same brand rises by 5.1 percentage points (Holm p = .023) and lexical diversity drops (TTR -0.011).  
- At 14B and 32B no content‑concentration measure is significant; instead stylistic drift appears, with em‑dash rates increasing to +0.46/1k at 14B and +0.61/1k at 32B (both Holm p ≤ .0024).  
- Token‑level distribution becomes flatter (entropy +0.091 bits, p = .015) while semantic distribution concentrates (collision +2.6pp, p = .023), indicating less predictable tokens but more repetitive meanings.  

## Context
This work challenges the common view that quantization merely cuts cost, revealing scale‑dependent behavioral shifts in model outputs that affect diversity and style across different model sizes.  

## Implications
Practitioners must assess concentration metrics alongside bias when deploying quantized models, as small models may produce less varied responses that could impact user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07901v1)
