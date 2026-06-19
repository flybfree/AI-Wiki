---

title: "IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning"
url: http://arxiv.org/abs/2606.02563v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-01_17-54-10Z_IntraShuffler_APrivacyPreservingFrameworkforHetero.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces IntraShuffler, a privacy‑preserving middleware for heterogeneous differential privacy federated learning that mitigates server inference attacks. Experiments show it reduces gradient recoverability by over 60% and lowers surrogate inference accuracy from 0.78 to 0.33 while keeping model utility stable.

## Key Takeaways
- IntraShuffler groups clients into privacy‑compatible buckets and shuffles parameters within each bucket, breaking persistent gradient patterns that enable server attacks.
- The framework works with ε‑aware aggregation by preserving declared privacy budgets without compromising the shuffling mechanism.
- Experimental results across four datasets demonstrate a 60% drop in recoverability and a sharp decline in surrogate inference accuracy from 0.78 to 0.33.

## Context
Federated learning systems increasingly rely on heterogeneous differential privacy where clients choose varying ε budgets, yet server‑side inference attacks exploit non‑IID gradient structures. Existing defenses like Shuffle-Model are incompatible with this setting, highlighting a gap in privacy‑aware model protection.

## Implications
This work provides a practical solution for organizations deploying HDP‑FL that must balance utility and privacy against curious administrators. Practitioners can adopt IntraShuffler to strengthen security without sacrificing performance across diverse data environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.02563v1)
