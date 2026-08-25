---
title: Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion
url: http://arxiv.org/abs/2608.22140v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_23-51-33Z_LexicalPerturbationsDisruptLLMReasoning_AnEmpirica.md
generated_at: 2026-08-24 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This study investigates how small lexical errors such as keyboard noise, character swaps, and filler insertion affect the reasoning ability of large language models. Experiments on four open‑weight instruction‑tuned models and frontier models across multiple benchmarks reveal that character‑level perturbations cause large drops in accuracy, especially for multi‑step tasks, while filler insertion has minimal impact.

## Key Takeaways  
- Character‑level perturbations fragment subword tokens, causing a shift of attention mass toward middle and final transformer layers.  
- The degradation is driven by token fragmentation rather than prompt length, as confirmed with length‑matched controls.  
- Restoring only the attention distribution or only the token content does not fully recover performance; both must be restored together to close most of the gap.

## Context  
Understanding how robust LLMs are to realistic input noise is crucial for deploying models in noisy environments such as chatbots and automated feedback systems. This work highlights a previously unnoticed vulnerability that could undermine performance without obvious error signals, prompting broader research into attention mechanisms under corruption.

## Implications  
For practitioners, the findings suggest that inference‑time fixes like spell‑checking or chain‑of‑thought prompting are unlikely to fully mitigate lexical errors because they address only one of two coupled problems. Future work should explore joint repair strategies that restore both token content and attention allocation to achieve reliable reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22140v1)
