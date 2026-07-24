---
title: On the Computational Complexity of Structural Generalization
published: 2026-07-21T21:00:32Z
authors: Zichao Wei
url: http://arxiv.org/abs/2607.19573v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Computational Complexity of Structural Generalization

## Abstract
Structural generalization has been measured repeatedly by several benchmarks, yet it has never been formally defined. We give a definition that translates the two premises (compositional structure and unbounded generalization) into mathematical language. The definition itself is neutral: a compiler that hard-codes the rules satisfies it just as well. But structural generalization becomes a scientific question only insofar as the capacity can autonomously emerge from finite data. This question pits the computational lower bound $\mathrm{NC}^1$ against the learnable ceiling $\mathrm{TC}^0$ of pure Transformers. Under a Montagovian instantiation, each compositional rule splits into two projections: a syntactic face ($F_γ$) and a semantic face ($G_γ$). Tree evaluation on the $G_γ$ side is an instantiation of BFVP, which is $\mathrm{NC}^1$-complete (Buss, 1987). A pure Transformer must learn both faces at once, but Kraus et al. (2026) prove that its learnable class $\subseteq \mathrm{TC}^0$. Under the standard assumption $\mathrm{TC}^0 \neq \mathrm{NC}^1$, a pure Transformer cannot learn structural generalization. Neuro-symbolic systems achieve the best benchmark scores precisely because they inject $G_γ$, sidestepping the genuinely hard half. Benchmark scores cannot distinguish "learned" from "given." This is what this paper sets out to make clear.

## Metadata
- **Published**: 2026-07-21T21:00:32Z
- **Authors**: Zichao Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19573v1)