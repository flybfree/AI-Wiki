---
title: NeuroAbs: A Neuro-Symbolic RTL Abstraction Framework for Property Checking Acceleration
published: 2026-08-18T02:58:05Z
authors: Zhiyuan Yan, Xiaofeng Zhou, Ziyue Zheng, Ziyi Yang, Wenbin Che, Wei Zhang, Yangdi Lyu, Hongce Zhang
url: http://arxiv.org/abs/2608.17304v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuroAbs: A Neuro-Symbolic RTL Abstraction Framework for Property Checking Acceleration

## Abstract
Formal verification is a crucial technique for ensuring the functional correctness of hardware designs. In the context of property checking, a key challenge is how to efficiently prove a user-specified property in the face of increasingly complex RTL designs. To address this challenge, abstraction techniques are often employed to reduce system complexity and accelerate the verification process. However, prior RTL abstraction methods either require significant manual effort or rely on rule-based techniques that lack flexibility. This paper introduces NeuroAbs, a neuro-symbolic framework for RTL abstraction. NeuroAbs first uses LLM-assisted RTL analysis to identify signals suitable for abstraction. It then combines LLM-based abstraction with an AST-based symbolic RTL representation to better align the generated abstraction with the intended transformation. The soundness of each abstraction is checked using satisfiability modulo theories (SMT) solving. If the abstraction is too coarse for a successful proof, NeuroAbs applies counterexample-guided abstraction refinement (CEGAR) to iteratively refine the model. Experimental results show that NeuroAbs significantly improves the efficiency of hardware property checking across a range of verification tasks.

## Metadata
- **Published**: 2026-08-18T02:58:05Z
- **Authors**: Zhiyuan Yan, Xiaofeng Zhou, Ziyue Zheng, Ziyi Yang, Wenbin Che, Wei Zhang, Yangdi Lyu, Hongce Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17304v1)