---
title: Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits
published: 2026-08-18T13:04:51Z
authors: Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho, Robert Hoehndorf
url: http://arxiv.org/abs/2608.17741v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits

## Abstract
OWL 2 DL ontologies, grounded in the description logic $\mathcal{SROIQ}$, express large knowledge bases in biomedicine and the Semantic Web. Neuro-symbolic (NeSy) learners over description logics either embed the ontology in a continuous space, abandoning classical entailment, or restrict to the Horn fragment $\mathcal{EL}^{++}$, which has a single canonical model. We present Baobab, which compiles a $\mathcal{SROIQ}$ ontology with a finite ABox into a Sentential Decision Diagram (SDD): it saturates a propositional core under a consequence-based calculus and instantiates the remaining $\mathcal{SROIQ}$ features (nominals, number restrictions, and the role axioms) over the active domain. The SDD's evidence-conditioned weighted model count then trains a perception network to recognize real images under partial ABox supervision: on an ontology that exercises every distinctive $\mathcal{SROIQ}$ feature, a CNN learns to read MNIST digits coupled by a successor relation and recovers latent ontology concepts that an independent perception leaves at chance. When the supervision admits several ontology-consistent completions, an independent perception collapses onto one, a reasoning shortcut: we show that a mixture indexed by the query's justifications can represent the calibrated posterior no independent perception can, and that seeding it from the circuit's enumerated completions attains the Bayes-optimal posterior on a real-image MNIST task where single-WMC and learned mixtures (the BEARS-ensemble hypothesis class) do not: to our knowledge the first to characterize and mitigate reasoning shortcuts in a non-Horn description logic. Soundness of the compiler and the representation result are machine-checked in Lean 4. Code is available at https://github.com/bio-ontology-research-group/baobab.

## Metadata
- **Published**: 2026-08-18T13:04:51Z
- **Authors**: Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho, Robert Hoehndorf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17741v1)