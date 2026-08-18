---
title: Architecture-Dependent Causal Transfer of Activation States Across Large Language Models
url: http://arxiv.org/abs/2608.16347v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-53-27Z_Architecture_DependentCausalTransferofActivationSt.md
generated_at: 2026-08-17 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether activation states from one large language model can be transferred causally to another using a learned projection, assessing representational similarity, retrieval accuracy, and end‑to‑end causal injection. Across four diverse models it finds strong alignment in trained representations but only partial success when activations are injected, indicating architecture‑dependent transfer rather than universal meaning.

## Key Takeaways
- Representational alignment exceeds random baseline and is best measured by rank‑based mutual k‑nearest‑neighbour metrics, which handle activation magnitude outliers better than centered kernel alignment.  
- A learned projection network retrieves target model states with 45‑50% top‑1 accuracy versus 5% chance for decoder‑only pairs but performs at chance level for the encoder‑based FLAN‑T5 pair.  
- Injecting projected activations into a generator yields a statistically significant increase in retrieval output similarity only for the Qwen2‑0.5B to Phi‑3‑mini transfer, while similar alignment fails to produce effects for Mistral‑7B pairs.

## Context
This work addresses a bottleneck in AI system integration: reliance on natural language introduces latency and token costs. By exploring direct activation communication, researchers aim to reduce these overheads, though prior attempts have been limited by lack of causal validation across architectures.

## Implications
The findings suggest that while representational similarity can be engineered, true end‑to‑end activation transfer remains sensitive to model design, limiting practical deployment of cross‑model activations. Practitioners should therefore consider architecture compatibility when planning such integrations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16347v1)
