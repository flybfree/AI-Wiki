---
title: CoSynFlow: Conformal Symplectic Neural Flows for Cross-System Prediction of Dissipative Hamiltonian Dynamics
published: 2026-08-01T10:12:58Z
authors: Baige Xu, Takaharu Yaguchi
url: http://arxiv.org/abs/2608.00571v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoSynFlow: Conformal Symplectic Neural Flows for Cross-System Prediction of Dissipative Hamiltonian Dynamics

## Abstract
Learning solution operators for differential equations is a central problem in scientific machine learning. However, many neural operator methods optimize prediction accuracy without explicitly enforcing the geometric structure of the dynamics. Structure-preserving models such as SympNets and Symplectic Neural Flows address this issue for conservative Hamiltonian systems by preserving the symplectic form. In dissipative Hamiltonian systems with conformal symplectic structure, however, the symplectic form evolves according to a conformal factor determined by the dissipation. We propose CoSynFlow, a conformal symplectic neural flow for learning continuous-time solution maps of dissipative Hamiltonian dynamics. CoSynFlow composes symplectic shear maps with explicit conformal scaling, preserving the conformal symplectic structure by construction. By conditioning it on a finite-dimensional Hamiltonian descriptor and the dissipation parameter, a single trained model predicts solution maps for unseen systems without retraining. CoSynFlow keeps the structure error at machine precision, attains the lowest long-horizon error, and admits physics-informed training.

## Metadata
- **Published**: 2026-08-01T10:12:58Z
- **Authors**: Baige Xu, Takaharu Yaguchi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00571v1)