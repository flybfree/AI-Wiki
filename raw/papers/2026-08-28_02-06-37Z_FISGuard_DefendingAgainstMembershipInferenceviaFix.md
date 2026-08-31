---
title: FISGuard: Defending Against Membership Inference via Fixed Input Subspaces
published: 2026-08-28T02:06:37Z
authors: Haocheng Jiang, Hua Shen
url: http://arxiv.org/abs/2608.27836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FISGuard: Defending Against Membership Inference via Fixed Input Subspaces

## Abstract
As large language models are increasingly adopted in federated learning, protecting user privacy while performing parameter-efficient fine-tuning on distributed private data has become an important challenge. Although clients only share gradients instead of directly uploading raw data, the shared gradients may still leak membership information about training samples. ProjRes (S&P, 2026) further increases this risk: with less information and without accessing model outputs, an attacker can effectively distinguish members from non-members solely based on the projection residual between a candidate representation and the subspace induced by server-observable gradients. Existing defenses against membership inference mostly rely on gradient perturbation or regularization, which can not only degrade model utility but also fail to effectively defend against the membership inference attack introduced by ProjRes, which exploits the geometric structure of gradients.   To address this issue, we propose FISGuard, a lightweight defense. Its key idea is to construct and fix a low-dimensional representation subspace using independent public data, thereby restricting the space through which private representations are exposed via gradients while preserving the primary information required for downstream tasks. This substantially reduces the projection-residual discrepancy between members and non-members.   We evaluate FISGuard against five representative defense methods across three NLP datasets, two LLMs, and two fine-tuning strategies, Adapter and LoRA. The results show that FISGuard reduces the ProjRes attack AUC to near the random-guessing level of 0.5 in most settings, while maintaining downstream task performance close to that of the undefended model and introducing only limited computational overhead, thereby achieving a favorable privacy--utility trade-off.

## Metadata
- **Published**: 2026-08-28T02:06:37Z
- **Authors**: Haocheng Jiang, Hua Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27836v1)