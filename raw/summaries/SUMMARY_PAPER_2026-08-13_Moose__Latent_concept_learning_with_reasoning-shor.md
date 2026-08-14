---
title: Moose: Latent concept learning with reasoning-shortcut awareness in $\mathcal{EL}^{++}$
url: http://arxiv.org/abs/2608.12961v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-44-48Z_Moose_Latentconceptlearningwithreasoning_shortcuta.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Moose, a method for latent concept learning in the OWL EL profile using reasoning-shortcut awareness. It compiles an EL++ TBox and finite ABox into a Sentential Decision Diagram that serves as a differentiable layer for model counting. The approach achieves termination, soundness, completeness, and polynomial intermediate sizes while handling partial supervision.

## Key Takeaways  
- Moose translates OWL EL ontologies into SDDs enabling a differentiable weighted-model-counting layer for latent concept learning.  
- It extends EL++ with closure clauses on exhaustive families to handle partial supervision beyond the profile's expressivity limits.  
- Evaluation shows Moose outperforms propositional NeSy, fuzzy logic, and ontology embedding baselines on MNIST-with-ontology and Pizzaïolo datasets.

## Context  
Neuro-symbolic learning methods have traditionally focused on propositional theories or Datalog, leaving reasoning-shortcut awareness unexplored in large-scale ontologies. This work bridges that gap by applying SDDs to OWL EL, demonstrating a novel integration of symbolic reasoning with differentiable computation.

## Implications  
For practitioners, Moose provides a framework to learn interpretable classifiers from limited ontology annotations, reducing reliance on full supervision. In industry, this could enable faster development of knowledge graphs and explainable AI models that respect existing semantic standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12961v1)
