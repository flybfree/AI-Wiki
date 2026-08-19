---
title: Dynamic Entanglement-Weighted Pruning for Quantum Federated Unlearning in Supply-Chain Risk Prediction
url: http://arxiv.org/abs/2608.17069v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_19-17-30Z_DynamicEntanglement_WeightedPruningforQuantumFeder.md
generated_at: 2026-08-18 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Entanglement‑Weighted Pruning (EWP) as an unlearning procedure for quantum federated learning that scores each trainable circuit parameter by the product of a client‑specific quantum Fisher information entry and a structural entanglement weight, then prunes low‑scoring parameters followed by fine‑tuning. Benchmarks on a four‑qubit ansatz trained with FedAvg across five simulated supply‑chain clients show EWP matches full retraining accuracy while achieving a lower forgetting score and requiring roughly 16 times less wall‑clock time.

## Key Takeaways
- The method combines quantum Fisher information estimates per client with gate‑level entanglement to identify which parameters actually carry a given client's influence for unlearning.  
- Pruning based solely on QFI or entanglement alone degrades accuracy, demonstrating that the combined signal is necessary for effective unlearning.  
- EWP reduces computational cost by about 16 times while maintaining post‑unlearning performance comparable to full retraining.

## Context
Federated quantum learning enables privacy‑preserving risk prediction across supply chains without sharing raw data, yet GDPR mandates that clients can request removal of their contribution after the fact. Retraining from scratch is correct but wasteful, and there is no clear way to know which circuit parameters reflect a client’s influence.

## Implications
Practitioners can use EWP to quickly honor deletion requests while preserving model utility, cutting both time and resource expenditure. The approach also offers a principled framework for evaluating quantum parameter importance in federated settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17069v1)
