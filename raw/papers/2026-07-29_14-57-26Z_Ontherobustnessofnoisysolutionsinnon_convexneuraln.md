---
title: On the robustness of noisy solutions in non-convex neural networks
published: 2026-07-29T14:57:26Z
authors: Enrico M. Malatesta, Alessandra Passalacqua, Riccardo Zecchina
url: http://arxiv.org/abs/2607.27000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the robustness of noisy solutions in non-convex neural networks

## Abstract
Optimization in non-convex neural network models is strongly influenced by the geometry of the solution space: sparse, isolated, point-like clusters are typically algorithmically inaccessible, whereas wide and flat regions can be found efficiently despite being relatively rare. At zero temperature this picture has been formalized in binary perceptrons through the overlap gap property (OGP), which limits algorithmic access to configurations with zero training error above a critical constraint density $α_{\rm OGP}$. Here we extend this description to finite temperature, where a positive training error is allowed and statistically penalized. We first show that the frozen one-step replica-symmetry-breaking solution, dominating the zero temperature equilibrium measure, survives at any finite temperature. We furthermore derive a general criterion, based on the smoothness of the single-pattern Gibbs weight near the decision boundary, that determines when a finite-temperature relaxation of the loss removes freezing. We then extend the OGP construction to finite temperature and show that dense, algorithmically accessible regions of finite-energy configurations persist beyond $α_{\rm OGP}$, up to a threshold $α_{\rm OGP}(ε)$ that grows with the allowed training error $ε$. Finally, in the teacher-student setting, we show that these wide, finite-energy regions still retain good generalization. Using a finite energy message-passing algorithm, we demonstrate numerically that thermal noise enables effective generalization in the regime of constraint densities where both recovering the teacher and finding a zero temperature solution are computationally hard.

## Metadata
- **Published**: 2026-07-29T14:57:26Z
- **Authors**: Enrico M. Malatesta, Alessandra Passalacqua, Riccardo Zecchina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27000v1)