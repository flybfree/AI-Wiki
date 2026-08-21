---
title: The Asymmetric Harms of LLM Compression
url: http://arxiv.org/abs/2608.19670v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_06-06-14Z_TheAsymmetricHarmsofLLMCompression.md
generated_at: 2026-08-20 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how compressing large language models affects their behavior beyond simple performance metrics. The authors find that compression harms head knowledge more than tail knowledge, leaves compressed models confidently wrong on lost facts, and hides divergent bias shifts across demographic groups despite stable aggregate scores.  

## Key Takeaways
- Compression disproportionately erodes the retention of head knowledge relative to tail knowledge, leading to noticeable loss in factual recall for commonly used patterns.  
- The resulting models maintain high confidence scores even when answering incorrectly on newly lost information, indicating a decoupling between confidence and accuracy.  
- Aggregate bias metrics can mask substantial, opposing shifts in stereotypical preferences among different demographic subgroups, revealing hidden asymmetries.  

## Context
Model compression is essential for reducing computational costs and enabling deployment on resource‑limited devices. However, existing evaluation practices rely heavily on aggregate perplexity or accuracy scores that do not reflect subtle behavioral degradations. This work adds a granular lens to assess how compression influences knowledge structure, confidence calibration, and social bias in LLMs.  

## Implications
Practitioners must move beyond single‑number benchmarks when deploying compressed models, as they may introduce hidden failures that affect both functionality and fairness. Granular evaluation protocols are needed to ensure that compression does not silently degrade model reliability or exacerbate societal harms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19670v1)
