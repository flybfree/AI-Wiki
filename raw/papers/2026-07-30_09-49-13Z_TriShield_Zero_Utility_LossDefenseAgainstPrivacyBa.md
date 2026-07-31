---
title: TriShield: Zero-Utility-Loss Defense Against Privacy Backdoors in Federated Language Model Fine-Tuning via Orthogonal Gradient Projection and Optimizer State Entanglement
published: 2026-07-30T09:49:13Z
authors: Cheng Wei
url: http://arxiv.org/abs/2607.27940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TriShield: Zero-Utility-Loss Defense Against Privacy Backdoors in Federated Language Model Fine-Tuning via Orthogonal Gradient Projection and Optimizer State Entanglement

## Abstract
Federated fine-tuning of large language models (LLMs) enables collaborative training without exposing raw data. However, a recent attack, NeuroImprint [1] (arXiv:2606.20553), demonstrates that a malicious parameter server can corrupt a PEFT adapter into a privacy backdoor: by assigning a dedicated memorization neuron to each training sample and ensuring each neuron updates at most once, the server can analytically reconstruct 59\%--79\% of client training data with high semantic fidelity. Existing defenses---including local differential privacy (LDP) [8] and gradient clipping---either fail against this attack or impose unacceptable utility degradation. We present \textbf{TriShield}, a three-layer deterministic defense that completely prevents NeuroImprint-style reconstruction with \textbf{zero model utility loss} and \textbf{no additional communication rounds}. TriShield consists of: (1) a \textbf{Parameter Artifact Detector} that identifies memory-neuron signatures in distributed model parameters before local training begins; (2) a \textbf{Stateful Virtual Iteration} mechanism that forces Adam/AdamW's momentum state to irreversibly entangle gradients across virtual steps, invalidating NeuroImprint's closed-form inversion; and (3) a \textbf{Zero-Utility Orthogonal Projection} operator that projects all local gradient updates onto the main-task semantic subspace computed via SVD, physically eliminating any gradient components that carry private memorization. We prove theoretically that after Layers 2 and 3, the mutual information between the uploaded gradient and any individual training sample is zero. Experiments on GPT-2 (117M) and Llama-Guard-3-1B verify that TriShield reduces NeuroImprint reconstruction rate to \textbf{0\%} across all tested attack variants, while maintaining or improving training accuracy, with less than 5\% additional GPU computation overhead.

## Metadata
- **Published**: 2026-07-30T09:49:13Z
- **Authors**: Cheng Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27940v1)