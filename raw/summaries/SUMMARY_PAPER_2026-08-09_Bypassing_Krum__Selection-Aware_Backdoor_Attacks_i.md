---
title: Bypassing Krum: Selection-Aware Backdoor Attacks in Federated Learning
url: http://arxiv.org/abs/2608.06637v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_23-07-15Z_BypassingKrum_Selection_AwareBackdoorAttacksinFede.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Krum‑Proxy, a selection‑aware backdoor attack that defeats Byzantine‑robust aggregation methods like Krum and Multi‑Krum in federated learning. By optimizing malicious updates to lie within the dense core of benign data and using a two‑stage optimization with nearest‑neighbor proxy, stochastic reference modeling, and anchor‑guided alignment, the method consistently bypasses geometric constraints while preserving clean accuracy.

## Key Takeaways
- Krum‑Proxy exploits the assumption that benign updates form a compact cluster by generating attacks that are both similar to legitimate data and positioned in regions favored during distance‑based aggregation.  
- The attack uses a two‑stage optimization: first, it creates task‑specific malicious updates; second, it refines them with a nearest‑neighbor proxy and stochastic reference modeling to align with the aggregation geometry.  
- A projection mechanism limits adversarial updates to realistic norm and variance bounds, ensuring stealth while maintaining high attack success rates.

## Context
Federated learning relies on robust aggregation to handle malicious clients, yet distance‑based rules such as Krum are vulnerable because they assume benign data is geometrically compact. This paper demonstrates that adaptive selection strategies can be subverted without violating the geometric constraints assumed by these methods.

## Implications
For practitioners, this work underscores the need for selection‑aware defenses beyond simple scaling or constraint tightening in federated learning systems. It also raises concerns about trustworthiness of aggregation protocols and motivates research into more resilient client behavior detection mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06637v1)
