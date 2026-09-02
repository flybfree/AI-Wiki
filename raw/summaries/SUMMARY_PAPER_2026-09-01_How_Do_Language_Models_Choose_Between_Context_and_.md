---
title: How Do Language Models Choose Between Context and Memory?
url: http://arxiv.org/abs/2609.00753v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_05-35-36Z_HowDoLanguageModelsChooseBetweenContextandMemory.md
generated_at: 2026-09-01 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how language models decide whether to rely on the information present in a prompt versus knowledge encoded within their parameters. By manipulating activation directions that indicate which source should dominate, the authors reveal that steering does not guarantee causal use or cross‑task applicability. Experiments show that authority‑induced shifts are partially reproduced by context manipulation (30–68% effect) and that only local task‑specific direction learning yields strong reuse (57%), while cross‑task transfer is limited to 9%.

## Key Takeaways
- Authority directions can be altered by swapping context and parametric knowledge, producing a 30–68% shift in source choice across Qwen, Llama, and OLMo models.  
- Matched control prompts that do not alter the underlying authority produce almost no change, indicating the effect is specific to the intervention.  
- Cross‑task reuse of learned authority directions closes only about 9% of the authority gap, whereas direction learning within a single task achieves 57%, suggesting authority computations are largely task‑dependent.

## Context
Understanding how models prioritize context versus internal knowledge is crucial for building reliable AI systems that can adapt to diverse tasks without overfitting. This work bridges theory and practice by providing empirical evidence of the separability between representation and causal deployment, informing future research on modularity and transferability in large language models.

## Implications
For practitioners, the findings suggest that interventions affecting model behavior should be evaluated for both immediate task impact and long‑term cross‑task utility. Industries relying on consistent performance across multiple applications must design training pipelines that respect task‑specific authority mechanisms to avoid unintended degradation when reusing knowledge.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00753v1)
