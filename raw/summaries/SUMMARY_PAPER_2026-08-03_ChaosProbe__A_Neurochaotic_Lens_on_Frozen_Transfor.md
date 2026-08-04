---
title: ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces
url: http://arxiv.org/abs/2608.01968v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-35-11Z_ChaosProbe_ANeurochaoticLensonFrozenTransformerInp.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
ChaosProbe introduces a deterministic neurochaos‑inspired method that creates response‑based fingerprints for frozen transformer input‑embedding spaces by applying chaotic trajectory transformations to prompt‑level embeddings and summarizing firing‑rate and entropy channel responses. Experiments on 80 neutral prompts across GPT‑2, DistilGPT‑2, BERT‑base‑uncased, and RoBERTa‑base demonstrate that correlation measures recover all same‑family nearest‑neighbor assignments and both expected mutual family pairs.

## Key Takeaways
- Pearson and Spearman correlations recover all four same‑family nearest‑neighbor assignments, indicating strong structural similarity within each model’s embedding family.  
- Euclidean distance recovers three of the four assignments and one of the two mutual family pairs, showing moderate but useful recovery across distances.  
- Paired bootstrap resampling supports the stability of these pairings over the observed prompt set, confirming that the signatures are not random.

## Context
This research extends neurochaos concepts to frozen transformer embeddings, offering a probe that does not require downstream task adaptation. It reveals hidden regularities in embedding spaces that are often ignored when evaluating models solely on benchmark performance.

## Implications
Researchers can use ChaosProbe signatures for model clustering and interpretability without fine‑tuning, providing an alternative lens beyond traditional performance metrics. Practitioners may leverage these fingerprints to assess similarity across frozen representations or detect anomalies in pre‑trained models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01968v1)
