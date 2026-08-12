---
title: Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models
url: http://arxiv.org/abs/2608.10214v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_20-35-43Z_DecodableButNotDetachable_TrainingDataGranularityD.md
generated_at: 2026-08-11 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language models contain domain‑specific parametric shells—neuron populations that are crucial for a particular domain yet can be removed without harming other domains. Experiments across multiple model sizes, domains, and granularities reveal that such selective neuron groups exist only at the token level when training data is modular, not at higher abstraction levels.

## Key Takeaways
- Zero neurons exceed 60 % domain selectivity in the academic subject level despite linear decoding above 85 % accuracy.  
- At language and modality granularity, about 0.65–1.14 % of neurons reach 60 % selectivity with damage matrices that are nearly diagonal, indicating strong shell formation.  
- Masking code‑selective neurons reduces mathematical reasoning by 16–24 percentage points, whereas masking language or script‑specific neurons has little effect.

## Context
Understanding the internal organization of neural networks helps explain model behavior and limits their adaptability to new tasks. This study contributes a systematic view of how training data granularity shapes the emergence of domain‑selective neuron groups in LLMs.

## Implications
For practitioners, recognizing that shell neurons are tied to token‑level modularity suggests that fine‑grained data augmentation could improve task transfer. For researchers, it highlights the need for probing methods at appropriate abstraction levels to uncover true parametric specialization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10214v1)
