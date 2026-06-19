---

title: A Non-Monotone Preconditioned Trust-Region Method for Neural Network Training
published: "2026-05-14T14:06:51Z"
authors: Andrea Angino, Bindi Çapriqi, Shega Likaj, Ken Trotti, Rolf Krause
url: http://arxiv.org/abs/2605.14860v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# A Non-Monotone Preconditioned Trust-Region Method for Neural Network Training



**Source**: [Original Paper](http://arxiv.org/abs/2605.14860v1)
## Abstract
Training deep neural networks at scale can benefit from domain decomposition, where the network is split into subdomains trained in parallel and coupled by a global trust-region mechanism. Building on the Additively Preconditioned Trust-Region Strategy (APTS), we propose a non-monotone variant with a nonlinear additive Schwarz preconditioner that combines parallel subdomain corrections with global coarse-space directions. A windowed acceptance criterion allows controlled objective increases, avoiding needless rejection of effective coarse steps. The resulting non-monotone APTS (NAPTS) preserves accuracy while reducing CPU time by 30\% and cutting rejected steps to one third of those in APTS.

## Metadata
- **Published**: 2026-05-14T14:06:51Z
- **Authors**: Andrea Angino, Bindi Çapriqi, Shega Likaj, Ken Trotti, Rolf Krause
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.14860v1)