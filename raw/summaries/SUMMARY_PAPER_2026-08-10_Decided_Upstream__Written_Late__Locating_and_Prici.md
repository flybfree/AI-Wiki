---
title: Decided Upstream, Written Late: Locating and Pricing the Cross-Lingual Refusal Circuit of a Multilingual MoE
url: http://arxiv.org/abs/2608.08032v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_09-39-41Z_DecidedUpstream_WrittenLate_LocatingandPricingtheC.md
generated_at: 2026-08-10 22:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why multilingual models exhibit inconsistent safety refusals across languages and identifies a specific neural circuit that governs the refusal. It shows that harmful intent is encoded early in a language‑invariant direction, but the actual generation of the refusal occurs later through a mixture‑of‑experts writer.

## Key Takeaways
- Harmful intent is represented as an internal direction with near‑identical cosine similarity between English and Indic embeddings at layer 11.  
- The refusal is not generated in a single forward pass but assembled over the generation process, indicating a late‑stage circuit.  
- Intervening on this writer is cheap (damping the opposer) or costly (amplifying it), while editing individual heads has no effect.

## Context
This work highlights a persistent safety alignment problem across multilingual AI systems where models perform differently in high‑ and low‑resource languages, prompting researchers to seek language‑agnostic solutions. The findings contribute to understanding how internal representations influence downstream behavior.

## Implications
For practitioners, the cost‑measured map suggests that improving refusal reliability can be achieved with minimal architectural changes, offering a practical path for safe deployment of multilingual models without extensive retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08032v1)
