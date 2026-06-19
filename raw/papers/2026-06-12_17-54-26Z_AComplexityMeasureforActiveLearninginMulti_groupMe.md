---

title: A Complexity Measure for Active Learning in Multi-group Mean Estimation
published: "2026-06-12T17:54:26Z"
authors: Abdellah Aznag, Rachel Cummings, Adam N. Elmachtoub
url: http://arxiv.org/abs/2606.14690v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# A Complexity Measure for Active Learning in Multi-group Mean Estimation



**Source**: [Original Paper](http://arxiv.org/abs/2606.14690v1)
## Abstract
We study a \emph{max-risk} objective for active learning in a multi-group mean estimation $d$-armed bandits: a learner adaptively allocates a budget of $T$ samples across $d$ groups to minimize the worst-case uncertainty index $\max_{k\in[d]}σ_k^2/n_k$, where $σ_k$ is the standard deviation of the distribution of arm $d$, and $n_k$ is the number of times arm $d$ is sampled. We develop a local minimax framework and prove the first general lower bound for this objective, valid for any finite-variance hypothesis class. The bound separates difficulty into three orthogonal factors: a \emph{budget} term, a \emph{heteroscedasticity} index measuring how unevenly the uncertainty is spread across arms, and a model-dependent complexity measure, the \emph{Variance Local Curvature} ($\mathrm{VLC}$), which captures how much information a local change of variance creates inside the hypothesis class. For smooth classes, the $\mathrm{VLC}$ is a reparametrization of a variance--Fisher information, with closed-form values for common families. Benchmarking against the strongest available upper bound shows near-optimality up to logarithmic factors in broad regimes, and pinpoints a systematic gap in highly heterogeneous instances. Our proof introduces two key ingredients: a loss-induced $\ell_1$ geometry on the decision space, and a representation-based instance generator that reduces hard-instance construction to an explicit random matrix calculation.

## Metadata
- **Published**: 2026-06-12T17:54:26Z
- **Authors**: Abdellah Aznag, Rachel Cummings, Adam N. Elmachtoub
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.14690v1)