---
title: Conditional Neural Optimal Transport for Predicting Cellular Phenotypes from Molecular Structure
url: http://arxiv.org/abs/2608.14293v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_13-25-04Z_ConditionalNeuralOptimalTransportforPredictingCell.md
generated_at: 2026-08-16 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a conditional neural optimal transport model to predict cellular phenotypes from molecular structures using high‑content microscopy images. The authors demonstrate that static optimal transport fails on large datasets and replace it with a molecule‑conditioned Neural Optimal Transport (NOT) framework that learns a Monge‑Gap regularized transport mapping. On unseen molecules, NOT outperforms baselines, showing promise for chemical phenotype prediction.

## Key Takeaways
- The model treats phenotype prediction as an inductive conditional optimal transport problem where the molecular structure conditions the transport from a negative‑control image to the perturbed one.
- Incorporating a Monge‑Gap regularization improves molecule‑specific recovery of phenotypic effects while suppressing microscopy technical variation across experimental batches.
- Generalization is limited by the molecular encoder; compressing representations and improving the encoder are identified as key directions for better out‑of‑distribution performance.

## Context
The work addresses the challenge of mapping vast chemical spaces to cellular responses, a problem that classical optimal transport cannot handle due to static couplings. By conditioning neural transport on molecular descriptors, the authors illustrate how generative AI can bridge experimental and computational domains in systems biology.

## Implications
This framework offers a scalable tool for drug discovery pipelines where rapid phenotype prediction is essential. Practitioners can leverage NOT to prioritize compounds with favorable cellular outcomes without exhaustive wet‑lab testing, accelerating research cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14293v1)
