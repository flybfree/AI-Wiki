---
title: CG4AI: A Column Generation Framework for Training AI Models Under Constraints
published: 2026-08-26T20:00:32Z
authors: Youcef Magnouche, Abderrahmane Driouch, Sébastien Martin, Pierre Bauguion
url: http://arxiv.org/abs/2608.26375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CG4AI: A Column Generation Framework for Training AI Models Under Constraints

## Abstract
Standard machine-learning training minimizes a loss function over a dataset, but does not guarantee that the resulting model will satisfy predefined rules or constraints on its outputs. In many real-world applications, ranging from autonomous systems to network routing, such guarantees are essential. We propose CG4AI, a framework that builds a convex combination of AI models while enforcing linear constraints on the combined output. A master linear program (LP) determines the optimal mixture weights, while a pricing subproblem generates new models guided by LP dual variables, focusing attention on the most violated constraints. A cutting-plane procedure extends feasibility guarantees beyond the training set. We apply CG4AI to two problems: (i) digit classification on MNIST, where we demonstrate four distinct uses of constraints, learning from constraints alone, improving adversarial robustness, correcting misclassified examples, and enforcing output relabeling; and (ii) the multi-commodity flow problem, where link capacity constraints are enforced on neural-network routing predictors. Experiments on MNIST and standard SNDLIB benchmark networks show that CG4AI reliably produces feasible predictors while achieving better accuracy than single-model baselines.

## Metadata
- **Published**: 2026-08-26T20:00:32Z
- **Authors**: Youcef Magnouche, Abderrahmane Driouch, Sébastien Martin, Pierre Bauguion
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26375v1)