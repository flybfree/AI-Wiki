---
title: Learning-to-Transition for Large-scale and High-Order MIMO Detection
url: http://arxiv.org/abs/2608.14511v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_17-29-07Z_Learning_to_TransitionforLarge_scaleandHigh_OrderM.md
generated_at: 2026-08-16 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a learning-to-transition framework that treats MIMO detection as a sequence of vector transitions, using a channel‑coupled Transformer and blockwise autoregressive factorization to handle high‑order MIMO while keeping complexity moderate. Hard‑output detection employs recursive transition networks trained via residual‑to‑BER curriculum, whereas soft‑output detection clones the hard policy into an IDD receiver with tied‑to‑untied transfer.

## Key Takeaways
- The framework models detection as a stochastic sequence of complete‑vector transitions where each step updates both embedding and sampling policy using a Transformer.  
- Hard‑output training first learns MIMO search geometry from exact residual metric then aligns policy with bit accuracy via residual‑to‑BER curriculum.  
- Soft‑output uses tied‑to‑untied transfer to preserve zero‑prior dynamics while allowing layer‑specific specialization during decoder feedback.

## Context
High‑order MIMO detection remains a bottleneck due to exponential search space and computational cost. Recent AI approaches aim to replace exhaustive optimization with differentiable policies, yet few integrate end‑to‑end training of both encoder and decoder components.

## Implications
This work enables scalable detection that can be deployed in real‑time systems such as 5G/6G networks. Practitioners can leverage the learned transition dynamics for faster inference and improved link reliability without sacrificing decoding performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14511v1)
