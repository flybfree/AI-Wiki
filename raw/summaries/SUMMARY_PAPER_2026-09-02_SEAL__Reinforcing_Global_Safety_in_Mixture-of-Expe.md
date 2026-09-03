---
title: SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment
url: http://arxiv.org/abs/2609.02293v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-40-19Z_SEAL_ReinforcingGlobalSafetyinMixture_of_Expertsth.md
generated_at: 2026-09-02 20:49
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SEAL, a lightweight training-time defense for Mixture-of-Experts models that mitigates adversarial attacks by adding an adapter to shared experts. Experiments show SEAL cuts attack success rates by up to 60% while keeping capability loss under 1.4% across five benchmarks.

## Key Takeaways
- Shared experts provide a constant anchor of safety-critical neurons, eliminating dependence on the stochastic routing path and thus stabilizing global alignment.
- The proposed adapter is trained only in parallel with the main model, making it parameter-efficient and plug‑and‑play without retraining the entire MoE.
- SEAL reduces attack success rates by up to 60% across six combined attack scenarios that include harmful prompting, jailbreak, malicious fine‑tuning, and neuron pruning.

## Context
Mixture-of-Experts architectures are central to scaling large language models, yet their routing mechanisms create exploitable vulnerabilities. Existing defenses focus on the router but often fail when adversaries can manipulate activation decisions or bypass them through nondeterministic processes.

## Implications
SEAL offers a practical solution that can be integrated into existing MoE pipelines with minimal overhead, encouraging safer deployment in commercial and open‑source models. Practitioners should adopt such alignment techniques to protect model integrity against evolving adversarial strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02293v1)
