---
title: Orca: Neural Operators for Causal Reasoning in Continuous Time
published: 2026-07-30T08:41:39Z
authors: Gerrit Großmann, David A. Selby, Sebastian J. Vollmer
url: http://arxiv.org/abs/2607.27867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Orca: Neural Operators for Causal Reasoning in Continuous Time

## Abstract
Structural causal models are the standard language for reasoning about interventions and counterfactuals, but they describe static variables, typically measured once, and usually forbid cyclic dependencies. Many systems we care about, such as patients, climates, and economies, instead evolve continuously in time, are observed at irregular time points, and contain feedback loops. We argue that neural operator learning provides a natural foundation for causal reasoning in this setting, and propose Orca, a framework in which each node of the causal graph is a function of time and each mechanism is a learned map between function spaces. We extend existing neural operator architectures to express causal mechanisms: a mechanism computes the function value of a node from its parent nodes by taking several parent functions as input, respects the arrow of time, and treats latent exogenous noise as a function that can be inferred and reused for counterfactuals. We formalize the model class and demonstrate counterfactual reasoning on synthetic continuous-time examples. Code is available at https://github.com/gerritgr/orca

## Metadata
- **Published**: 2026-07-30T08:41:39Z
- **Authors**: Gerrit Großmann, David A. Selby, Sebastian J. Vollmer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27867v1)