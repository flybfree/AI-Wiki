---
title: Moose: Latent concept learning with reasoning-shortcut awareness in $\mathcal{EL}^{++}$
published: 2026-08-13T08:44:48Z
authors: Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho, Robert Hoehndorf
url: http://arxiv.org/abs/2608.12961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Moose: Latent concept learning with reasoning-shortcut awareness in $\mathcal{EL}^{++}$

## Abstract
The OWL 2 EL profile is used in some of the largest production ontologies, including the Gene Ontology and SNOMED CT. Existing neuro-symbolic (NeSy) learning methods accept propositional theories or Datalog, and reasoning-shortcut (RS) awareness has not been investigated in ontology settings. We present Moose, a method that compiles an $\mathcal{EL}^{++}$ TBox and finite ABox to a Sentential Decision Diagram (SDD). The SDD acts as a differentiable weighted-model-counting layer, and we add closure clauses outside the $\mathcal{EL}^{++}$ profile on declared exhaustive families to overcome the limited expressivity of $\mathcal{EL}^{++}$ under partial supervision. We show termination, soundness, completeness, and polynomial intermediate sizes, and validate the proofs in Lean. We then define the first formal partial-supervision latent-concept-learning task over an OWL EL ontology, i.e., learning per-individual classifiers for latent concepts from observed ABox literals, and evaluate Moose on MNIST-with-ontology and Pizzaïolo. Moose improves over propositional-NeSy, fuzzy-logic, and ontology embedding baselines, and presents the first reasoning-shortcut analysis in an OWL EL setting.

## Metadata
- **Published**: 2026-08-13T08:44:48Z
- **Authors**: Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho, Robert Hoehndorf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12961v1)