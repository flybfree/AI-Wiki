---
title: Compression-Based Behavioral Similarity for Open-World Sybil Discovery on Ethereum
url: http://arxiv.org/abs/2607.27370v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_18-23-58Z_Compression_BasedBehavioralSimilarityforOpen_World.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a compression-based similarity method to detect Sybil actors on Ethereum without requiring direct financial links between wallets. It builds a symbolic transaction grammar from EVM traces and uses Gzip‑based non‑circularity distance to form behavioral graphs that differentiate bots, organic users, and arbitrage bots. Experiments show the approach can discover suspicious seed wallets during a temporal split and survive synthetic camouflage attacks.

## Key Takeaways
- The method relies on symbolic Transaction Grammar derived from EVM traces to capture rhythm, execution structure, and intent without supervised training.
- Gzip‑based NCD creates a behavioral graph that enables leakage‑aware Sybil discovery independent of token transfers or funding links.
- Experiments demonstrate robustness against temporal drift and adversarial camouflage, showing the framework can expand suspicious seed wallets during open‑world audits.

## Context
This work advances AI research in blockchain security by applying compression techniques to model user behavior as a symbolic grammar. It moves beyond graph construction that depends on financial activity toward a training‑free detection primitive suitable for large‑scale audit pipelines.

## Implications
Practitioners can integrate this leakage‑aware primitive into existing audit tools, reducing reliance on supervised models and enabling continuous monitoring of open‑world blockchains without retraining. The approach offers a scalable, low‑resource alternative for Sybil candidate identification across diverse blockchain ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27370v1)
