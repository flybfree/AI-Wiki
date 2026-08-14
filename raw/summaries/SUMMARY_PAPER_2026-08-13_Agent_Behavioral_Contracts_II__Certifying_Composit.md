---
title: Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence
url: http://arxiv.org/abs/2608.12895v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_07-25-05Z_AgentBehavioralContractsII_CertifyingCompositional.md
generated_at: 2026-08-13 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper examines the validity of assuming independence between component failures in multi‑agent systems and provides a reliability bound that does not rely on this assumption. Experiments show joint co‑failure exceeds the product of individual reliabilities by 90 %, indicating strong positive dependence, especially when components share a model. A finite‑sample certificate is derived as a linear program over measured moments.

## Key Takeaways
- Joint co‑failure occurs in 90 % of missions where either component fails, revealing a high level of positive dependence that inflates joint failure above the independence product.  
- Substituting one model for another changes the association only six times out of six contrasts, while changing vendors does not affect it, supporting the null hypothesis of no vendor‑specific dependence.  
- The bootstrap bound on fitted models has an O(1) identification gap versus an O(n^{-1/2}) haircut, and its coverage worsens with more data without visible symptom.

## Context
In AI reliability research, independence between components is routinely assumed to certify system safety and performance. This assumption often underestimates real‑world risk because shared models or vendor choices can create hidden dependencies that amplify failure probabilities.

## Implications
Practitioners must move beyond independence‑based certificates and test actual co‑failure patterns across diverse configurations. Certification methods should incorporate robust, dependency‑aware bounds to provide trustworthy reliability estimates for complex multi‑agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12895v1)
