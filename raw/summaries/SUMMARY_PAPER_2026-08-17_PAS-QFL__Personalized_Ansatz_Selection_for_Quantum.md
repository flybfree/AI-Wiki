---
title: PAS-QFL: Personalized Ansatz Selection for Quantum Federated Learning under Client Data Heterogeneity
url: http://arxiv.org/abs/2608.14995v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_02-52-39Z_PAS_QFL_PersonalizedAnsatzSelectionforQuantumFeder.md
generated_at: 2026-08-17 21:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PAS-QFL, a framework that selects quantum neural network ansätze personalized to client data heterogeneity in federated learning. It separates a globally shared ansatz from a per-client private ansatz and uses Macro-F1 to personalize the latter while stabilizing the former for aggregation. Experiments show improved average Macro-F1 over fixed-ansatz baselines.

## Key Takeaways
- PAS-QFL decomposes each client QNN into a shared global ansatz and a client-specific private ansatz, allowing structure personalization beyond parameter tuning.
- The shared ansatz is chosen via a stability‑aware cross‑client criterion to ensure reliable aggregation while the private ansatz adapts locally using Macro-F1.
- Only the shared parameters are uploaded, preserving federated privacy and keeping the aggregation process well‑defined.

## Context
Quantum federated learning aims to train quantum neural networks across many clients without exchanging raw data, a challenge compounded by non‑identically distributed datasets. Existing methods treat ansatzes as uniform, which can degrade performance when client data distributions differ significantly.

## Implications
This work demonstrates that personalizing the structure of quantum models can boost federated learning outcomes in real‑world settings with class imbalance. Practitioners can adopt PAS-QFL to design more robust and equitable quantum training pipelines, fostering trustworthy AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14995v1)
