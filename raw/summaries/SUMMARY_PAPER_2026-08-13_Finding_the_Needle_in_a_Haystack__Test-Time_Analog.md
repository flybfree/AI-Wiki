---
title: Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization
url: http://arxiv.org/abs/2608.12687v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_01-09-58Z_FindingtheNeedleinaHaystack_Test_TimeAnalogCircuit.md
generated_at: 2026-08-13 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Test-Time Analog Representation Adaptation for Bayesian Optimization (TTARO), an online deep‑kernel method that continuously updates circuit embeddings and Gaussian‑process surrogates as new FoM labels are observed. By aligning the representation with the optimization objective throughout the search, TTARO reduces regret compared to fixed‑embedding approaches. Experiments show average AUC improvements of 15.2% over standard BO and 20.7% over Deep Kernel Learning across diverse settings.

## Key Takeaways
- TTARO jointly learns a nonlinear feature transformation and a Gaussian‑process surrogate using FoM labels from each evaluation, enabling real‑time adaptation of circuit representations.
- The framework continuously incorporates newly observed FoM information into both the representation encoder and the acquisition function, unlike methods that keep embeddings fixed after initial training.
- Compared to conventional Gaussian‑process BO and DKL, TTARO achieves up to a 46.7% reduction in regret AUC, demonstrating significant performance gains across multiple encoder/kernel/acquisition configurations.

## Context
The work addresses a longstanding challenge in Bayesian optimization where static representations hinder sample efficiency for high‑dimensional analog circuit search. As circuits become more complex and simulation costs rise, methods that adapt their feature spaces on the fly are essential to maintain convergence and reduce regret.

## Implications
For AI practitioners developing automated design tools, TTARO offers a practical path to improve robustness and efficiency without retraining encoders from scratch. Industry adoption could lower development timelines for analog hardware by enabling smarter acquisition strategies that align with evolving optimization landscapes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12687v1)
