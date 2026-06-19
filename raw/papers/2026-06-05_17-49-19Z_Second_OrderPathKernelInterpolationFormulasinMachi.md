---

title: Second-Order Path Kernel Interpolation Formulas in Machine Learning
published: "2026-06-05T17:49:19Z"
authors: Jin Guo, Roy Y. He, Jean-Michel Morel
url: http://arxiv.org/abs/2606.07495v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Second-Order Path Kernel Interpolation Formulas in Machine Learning



**Source**: [Original Paper](http://arxiv.org/abs/2606.07495v1)
## Abstract
Understanding how training data shape neural network predictions is a central problem in modern learning theory. In 2020, Pedro Domingos proposed an interpolation formula valid for every model learned by deterministic gradient descent. It expresses the model's prediction as an integral, along the optimization path, of a data-dependent kernel that aligns the model's gradients at the test and training data. Such a first-order characterization remains valid for models trained with batch-based stochastic optimization. In this paper, we develop second-order forms of these interpolation formulas. We show that the leading path-kernel interpolation is supplemented by a curvature-weighted interpolation term. For stochastic gradient descent, an additional sampling-induced component appears, coupling the curvature of the prediction with the covariance of mini-batch gradient noise. We also extend the representation to stochastic gradient descent with momentum, where the interpolation structure is preserved but with the weights modified by a memory-related factor. Moreover, we establish a concentration estimate for the terminal prediction, identifying the fluctuation scale around the expected second-order representation. Together, these results provide a refinement of the path-kernel interpretation of neural network prediction.

## Metadata
- **Published**: 2026-06-05T17:49:19Z
- **Authors**: Jin Guo, Roy Y. He, Jean-Michel Morel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.07495v1)