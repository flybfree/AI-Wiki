---
title: When Does More Correct Data Hurt? Insertion-Stability and the Limits of Dimension-Based Theory
url: http://arxiv.org/abs/2608.14020v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_07-07-55Z_WhenDoesMoreCorrectDataHurt_Insertion_Stabilityand.md
generated_at: 2026-08-16 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when adding correctly labeled examples can increase a learner’s error and introduces the concept of insertion‑stability to describe learners that are immune to such attacks. It shows that high‑probability guarantees survive insertions for insertion‑stable learners but that classical VC‑dimension bounds cannot predict which classes suffer the penalty, especially under monotone adversarial insertion.

## Key Takeaways
- Insertion‑stable learners keep their error region non‑expanding when correct data are added, so risk after insertions never exceeds clean part risk.  
- Classical VC‑dimension theory fails to capture class‑specific performance; two classes with the same dimension can have different rates—one Theta(1/n) and another Theta(log(en)/n).  
- No finite monotone permutation‑invariant compression can achieve the clean rate on Mehrotra’s hard class, indicating a fundamental limitation beyond VC bounds.

## Context
The tension between data quality and model performance is central to active learning and online learning research. This work highlights that theoretical guarantees often ignore how specific data distributions interact with learners, which affects practical deployment of robust algorithms.

## Implications
For practitioners, insertion‑stability provides a clear criterion for selecting models that are resilient to noisy or adversarial additions. It also warns against relying solely on VC dimension when designing learning systems, urging empirical assessment of class behavior under realistic data perturbations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14020v1)
