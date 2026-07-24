---
title: Adversarial Frontiers: Minimum-Norm Attack Ensembles for Robustness Evaluation
published: 2026-07-22T07:43:38Z
authors: Luca Scionis, Luca Melis, Maura Pintor, Fabio Brau, Ambra Demontis, Giorgio Fumera, Fabio Roli, Battista Biggio
url: http://arxiv.org/abs/2607.19855v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Frontiers: Minimum-Norm Attack Ensembles for Robustness Evaluation

## Abstract
Adversarial robustness is commonly evaluated with predefined attack ensembles, such as AutoAttack, at a single perturbation budget $\varepsilon$ and on a selective choice of perturbation norms. We argue this formulation is fundamentally limited. First, robustness--perturbation curves may intersect or decay at different rates across models, making single-$\varepsilon$ rankings unstable. Second, current ensembles provide no evidence of optimality, leaving an unknown gap to worst-case performance. Third, fixed attack configurations provide no systematic control over the trade-off between attack strength and evaluation cost. To address these limitations, we introduce a unified evaluation framework based on a comprehensive pool of minimum-norm attacks and robustness--perturbation curves across $\ell_0$, $\ell_1$, $\ell_2$ and $\ell_\infty$ norms. We define the attack frontier as the worst-case robustness estimate the attack pool produces against a model. We then formalize evaluation as a frontier-approximation problem, constructing minimum-norm attack ensembles, optimized subsets of the comprehensive pool, that approach the frontier under a controllable query budget, with larger budgets monotonically tightening the estimate. Furthermore, we define the defense frontier as the maximum robustness across the model set at each perturbation size. We finally propose the Defense Optimality Index to rank defenses by their gap to the defense frontier, providing a ranking without selecting a reference $\varepsilon$. On CIFAR-10 and ImageNet, our ensembles match or exceed AutoAttack on most defenses at every budget tier, at fixed and controllable query cost, offering practitioners a query-controlled, curve-based alternative to fixed-$\varepsilon$ evaluation.

## Metadata
- **Published**: 2026-07-22T07:43:38Z
- **Authors**: Luca Scionis, Luca Melis, Maura Pintor, Fabio Brau, Ambra Demontis, Giorgio Fumera, Fabio Roli, Battista Biggio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19855v1)