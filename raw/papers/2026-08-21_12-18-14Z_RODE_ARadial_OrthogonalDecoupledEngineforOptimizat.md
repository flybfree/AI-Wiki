---
title: RODE: A Radial-Orthogonal Decoupled Engine for Optimization
published: 2026-08-21T12:18:14Z
authors: Guoxiang Xu, Bince Qu, Qi Sun, Cheng Zhuo
url: http://arxiv.org/abs/2608.21024v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RODE: A Radial-Orthogonal Decoupled Engine for Optimization

## Abstract
Modern neural network training increasingly uses matrix-aware optimizers, yet their conditioned matrix step is typically added directly to the weight, jointly changing its norm and direction. This interaction matters because the current norm determines angular motion, while directional learning can drive norm growth and thereby alter later steps. We introduce RODE, which gives the radial and directional components separate update rules and step sizes. RODE explicitly updates the matrix Frobenius norm through a scalar radial rule, while its directional channel performs Newton--Schulz-conditioned updates in the tangent space. Controlled GPT-2 interventions show gains from both direct norm control and RODE's directional update. Across two language-modeling and two image-classification tasks, RODE outperforms both Muon variants in every direct comparison and ends with lower full-model norms. At 1.5B scale, using the learning rate transferred directly from the Qwen2-style LM sweep, RODE lowers loss from 4.145 to 3.346 and final global norm from 11964 to 2183 relative to Muon RMS, with fixed-radius RODE improving further. For Qwen3.5-9B full-parameter fine-tuning, all six optimizers use the same tuning budget and the same formal-training and evaluation settings; RODE outperforms both Muon variants on all four evaluation tasks and attains the highest mean on GSM8K and MATH-500. Thus, decoupling radial and directional dynamics offers a more effective and controllable approach to matrix optimization.

## Metadata
- **Published**: 2026-08-21T12:18:14Z
- **Authors**: Guoxiang Xu, Bince Qu, Qi Sun, Cheng Zhuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21024v1)