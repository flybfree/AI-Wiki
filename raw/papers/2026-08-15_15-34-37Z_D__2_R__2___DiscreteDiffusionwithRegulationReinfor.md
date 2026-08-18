---
title: $D^{2}R^{2}$: Discrete Diffusion with Regulation Reinforcement for Single-Cell Perturbation Prediction
published: 2026-08-15T15:34:37Z
authors: Ninghan Fan, Qi Liu, Xunuo Zhu, Yukai Sun, Luyuan Chen, Xuheng Zhou, Yuetian Du, Ming Kong, Xiaojun Zhu, Jie Liu, Zhan Zhou, Qiang Zhu
url: http://arxiv.org/abs/2608.15288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $D^{2}R^{2}$: Discrete Diffusion with Regulation Reinforcement for Single-Cell Perturbation Prediction

## Abstract
Predicting single-cell transcriptomic responses to genetic perturbations is central to functional genomics and virtual-cell modeling. Existing approaches, however, typically predict an entire expression profile as a whole, leaving the order in which individual gene responses are generated unmodeled. To address this problem, we introduce \textbf{$D^{2}R^{2}$} (\textbf{D}iscrete \textbf{D}iffusion with \textbf{R}egulation \textbf{R}einforcement), which reformulates perturbation prediction as regulation-guided gene-wise progressive generation. A Masked Discrete Diffusion Model represents expression as ordinal tokens and reconstructs a fully masked profile step by step, allowing generated gene responses to condition those that remain masked. A Regulatory Policy Module initializes the generation policy from a gene regulatory network inferred from control cells and adapts it to the perturbation and current partially generated state. Then, group-relative policy optimization refines only the ordering policy using final perturbation-effect agreement as reward. Across Norman19 and VCC-H1, $D^{2}R^{2}$ achieves the best performance on all five metrics on Norman19 and remains competitive on H1. Controlled ablations holding the generator and generation budget fixed show that biological-prior ordering improves over random ordering and is more reliable than uncertainty-based heuristics, whereas reversing the biological-prior ordering degrades every metric. Biological analyses further show that the refined policy prioritizes regulatory genes early while promoting perturbation-specific transcription factors and responsive genes. These results establish gene generation order as an effective, controllable, and biologically interpretable dimension of single-cell perturbation prediction.

## Metadata
- **Published**: 2026-08-15T15:34:37Z
- **Authors**: Ninghan Fan, Qi Liu, Xunuo Zhu, Yukai Sun, Luyuan Chen, Xuheng Zhou, Yuetian Du, Ming Kong, Xiaojun Zhu, Jie Liu, Zhan Zhou, Qiang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15288v1)