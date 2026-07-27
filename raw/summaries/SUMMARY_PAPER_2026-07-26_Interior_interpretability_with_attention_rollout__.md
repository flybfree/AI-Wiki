---
title: Interior interpretability with attention rollout: contraction and propagation profiles in Transformers
url: http://arxiv.org/abs/2607.22367v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_14-51-28Z_Interiorinterpretabilitywithattentionrollout_contr.md
generated_at: 2026-07-26 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces interior interpretability as a propagation‑based view of how attention mechanisms move information through Transformer layers, using attention rollout to model these interactions. It applies Doeblin–Dobrushin contraction theory to show that rollout operators with small Dobrushin coefficients behave like rank‑one stochastic matrices whose rows follow normalized column sums. Experiments on metabolomic age prediction reveal stronger rollout contraction at deeper layers and differences between trained and randomly initialized models, though the work does not prove causal impact of any variable.

## Key Takeaways
- A rollout operator with a small Dobrushin coefficient approximates a rank‑one stochastic matrix whose rows are proportional to normalized column sums. 
- The measured contraction strength increases as model depth grows, indicating more pronounced propagation effects in deeper layers. 
- Trained and randomly initialized models exhibit distinct propagation profiles, suggesting that initialization influences attention‑mediated information flow.

## Context
This work moves beyond feature attribution toward understanding the internal dynamics of Transformer architectures, offering a diagnostic tool for probing how attention weights compose across layers without relying on external optimization criteria. It highlights that interpretability methods can reveal structural patterns even when they do not directly explain predictions.

## Implications
For practitioners, interior interpretability provides a principled way to assess whether attention mechanisms are effectively aggregating information, which may guide model design and regularization strategies. The findings suggest that depth‑related propagation strength could be leveraged for more robust feature selection or risk mitigation in high‑dimensional data tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22367v1)
