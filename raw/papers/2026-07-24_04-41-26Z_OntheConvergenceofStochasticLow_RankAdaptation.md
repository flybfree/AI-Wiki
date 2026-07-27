---
title: On the Convergence of Stochastic Low-Rank Adaptation
published: 2026-07-24T04:41:26Z
authors: Ru Wang, Chengchang Liu, John C. S. Lui
url: http://arxiv.org/abs/2607.21975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Convergence of Stochastic Low-Rank Adaptation

## Abstract
Low-rank adaptation (LoRA) optimizes $J(B,A)=\mathcal L(W_\mathrm{base}+sBA)$ over two adapters $B \in \mathbb{R}^{m \times r}$ and $A \in \mathbb{R}^{r \times n}$ that form a low-rank update to a frozen pretrained weight matrix $W_\mathrm{base} \in \mathbb{R}^{m \times n}$. The prior analysis shows LoRA-GD takes $\exp\{\mathcal{O}(ε^{-2})\}$ oracle calls to find an $ε$-stationary point such that $\|\nabla J(B,A)\|\leq ε$ in the deterministic setting. We sharpen the analysis and show that $\mathcal{O}(ε^{-4})$ full-gradient evaluations suffice for the same first-order criterion. We further study stochastic LoRA under unbiased gradient estimates and finite variance. We propose LoRA-NSGDM, which finds an $ε$-stationary point with $\mathcal{O}(ε^{-8})$ stochastic oracle complexity. Under the additional mean-square smoothness condition, we use variance reduction strategy and propose LoRA-STORM, which improves the stochastic oracle complexity to $\mathcal{O}(ε^{-6})$.

## Metadata
- **Published**: 2026-07-24T04:41:26Z
- **Authors**: Ru Wang, Chengchang Liu, John C. S. Lui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21975v1)