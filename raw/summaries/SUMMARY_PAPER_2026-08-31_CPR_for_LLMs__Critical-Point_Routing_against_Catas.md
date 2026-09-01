---
title: CPR for LLMs: Critical-Point Routing against Catastrophic Forgetting in Domain Adaptation
url: http://arxiv.org/abs/2608.30158v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_02-19-10Z_CPRforLLMs_Critical_PointRoutingagainstCatastrophi.md
generated_at: 2026-08-31 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces CPR, a critical‑point routing method that mitigates catastrophic forgetting when adapting large language models to new domains. By keeping the original base model intact and only invoking its expert derivative on specific tokens where the former fails, CPR decouples general capability from domain adaptation, achieving state‑of‑the‑art performance while limiting the overall capacity loss.

## Key Takeaways  
- CPR trains a lightweight hierarchical router that estimates an expert‑call probability for each token based on critical points where the base model errs but the expert succeeds.  
- The routing framework uses momentum smoothing and threshold gating to combine the base model’s output with expert responses, preserving general knowledge while applying domain expertise only when needed.  
- Experiments show CPR improves domain performance by 1.4‑5.5% compared with pure SFT expert adaptation and reduces the general‑capability drop from 3.4‑14.5% to at most 0.5%, invoking the expert on roughly one‑third of tokens.

## Context  
Catastrophic forgetting remains a major challenge in continual learning, where fine‑tuning often erodes a model’s prior knowledge. Existing loss‑based methods force a trade‑off between adaptation and preservation, limiting their practicality for large models with high compute budgets. CPR’s token‑level routing offers a more efficient alternative that aligns well with the growing demand for scalable, continual AI systems.

## Implications  
This work demonstrates that decoupling general and domain capabilities can be achieved without sacrificing overall model utility, encouraging researchers to explore modular adaptation strategies. For industry practitioners, CPR provides a practical pathway to deploy specialized models while maintaining broad applicability, reducing training costs and preserving user trust in the system’s reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30158v1)
