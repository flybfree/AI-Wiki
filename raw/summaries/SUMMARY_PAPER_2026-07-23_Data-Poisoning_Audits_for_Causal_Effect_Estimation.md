---
title: Data-Poisoning Audits for Causal Effect Estimation
url: http://arxiv.org/abs/2607.19692v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_02-46-57Z_Data_PoisoningAuditsforCausalEffectEstimation.md
generated_at: 2026-07-23 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a data‑poisoning audit for augmented inverse‑probability‑weighted causal estimation, aiming to quantify how adversarial addition of plausible records can shift the reported treatment effect. By fixing preprocessing and nuisance fits, it computes an exact finite‑sample worst‑case movement at each append budget using a greedy scan and derives a conservative total‑influence score that captures both direct and indirect contributions. Extensive simulations confirm the method’s accuracy and reveal material sensitivity when small budgets are used.

## Key Takeaways
- The audit defines a finite catalog of feasible records, an append budget, and nested source capacities, allowing the adversary to select a subset that maximizes movement in a specified direction, which is computed exactly via a greedy scan.  
- A total‑influence score combines each record’s direct contribution with its effect through the propensity and outcome models, providing a comprehensive measure of influence on the final estimate.  
- The framework yields a conservative finite‑budget bound for fully refitted estimates and shows that small append budgets can cause substantial shifts in causal results, validated by simulation.

## Context
In observational causal analysis, researchers often combine data from multiple sites, vendors, or collection systems to improve efficiency and power. This pooling creates opportunities for manipulation, as new records can be inserted without altering the underlying model assumptions, thereby biasing estimated treatment effects. The paper addresses this vulnerability by formalizing a risk assessment that translates adversarial composition into measurable movement.

## Implications
For practitioners in AI and causal inference, the audit offers a quantitative tool to evaluate how appending data might degrade reliability of reported effects, enabling proactive monitoring and safeguards at the source level. By making movement curves and critical budgets explicit, it supports more trustworthy causal reporting across heterogeneous datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19692v1)
