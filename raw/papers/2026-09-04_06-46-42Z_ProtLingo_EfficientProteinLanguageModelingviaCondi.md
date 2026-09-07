---
title: ProtLingo: Efficient Protein Language Modeling via Conditional Memory and Expert Routing
published: 2026-09-04T06:46:42Z
authors: Mingrui Li, Sixian Shen, Minzhang Li, Ruiyi Zhang, Kexin Zhang, Jiakai Zhang, Jingyi Yu
url: http://arxiv.org/abs/2609.04793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProtLingo: Efficient Protein Language Modeling via Conditional Memory and Expert Routing

## Abstract
Proteins perform diverse cellular functions, and even single amino-acid substitutions can alter stability, activity, or molecular interactions. Protein language models (PLMs) provide a scalable approach for modeling such sequence--function relationships from unlabeled sequences, but increasing the size of dense Transformer backbones often brings substantial computational cost without consistently improving mutation-sensitive prediction. We introduce ProtLingo, an efficient PLM framework that augments a pretrained single-sequence backbone with conditional local memory and sparse expert routing. ProtLingo maps contextual residue representations into route-specific discrete codes, composes centered local windows into latent $N$-gram addresses, and retrieves reusable residual signals associated with recurring local sequence contexts. In parallel, selected feed-forward blocks are upcycled into sparse Mixture-of-Experts layers with shared and routed experts, enabling residue-dependent computation while activating only a subset of parameters. Experiments on protein fitness prediction, FLIP benchmarks, and supervised contact prediction show that ProtLingo achieves competitive performance with a 150M-scale backbone, including strong parameter efficiency on mutation-effect prediction and preserved long-range structural representations.

## Metadata
- **Published**: 2026-09-04T06:46:42Z
- **Authors**: Mingrui Li, Sixian Shen, Minzhang Li, Ruiyi Zhang, Kexin Zhang, Jiakai Zhang, Jingyi Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04793v1)