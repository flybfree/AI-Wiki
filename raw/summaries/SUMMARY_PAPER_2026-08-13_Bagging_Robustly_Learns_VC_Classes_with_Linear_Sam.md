---
title: Bagging Robustly Learns VC Classes with Linear Sample Complexity
url: http://arxiv.org/abs/2608.13514v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-36-49Z_BaggingRobustlyLearnsVCClasseswithLinearSampleComp.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper revisits adversarial robustness in learning VC classes and proves that sample complexity can be linear in the dual VC dimension, improving on prior bounds. It introduces a simple bagging algorithm that combines bootstrap aggregation with robust empirical risk minimization to achieve this bound. The authors also establish a matching lower bound showing that any oracle learner must make at least Ω(d*) calls to an RERM oracle.

## Key Takeaways  
- Sample complexity for adversarially robust VC learning is O(d*), where d* is the dual VC dimension, not the original d.  
- The algorithm uses only O(d*) independent bootstrap samples and outputs their majority vote, making it computationally efficient.  
- A lower bound proves that Ω(d*) calls to an RERM oracle are unavoidable in the general oracle model.

## Context  
VC theory provides a framework for understanding the capacity of statistical learners, but its application to adversarial robustness has been limited by high sample complexity requirements. This work bridges that gap by showing linear dependence on the dual dimension, which is often much smaller than the original VC dimension, thus offering practical scalability.

## Implications  
For practitioners developing robust machine learning models, this result suggests that simple bagging strategies can be theoretically justified with minimal data overhead. It also guides algorithm design toward oracle‑based RERM calls, influencing future research on sample‑efficient adversarial defenses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13514v1)
