---
title: Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks
url: http://arxiv.org/abs/2607.25227v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_02-59-32Z_Decision_LevelHijacking_InjectingCognitiveBiasinto.md
generated_at: 2026-07-28 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces decision‑level hijacking, a threat where attackers manipulate an LLM’s internal cognitive stance to sway downstream decisions without altering model outputs or violating content policies. The authors demonstrate that Bit‑Flip Attacks (BFAs) can achieve this by flipping only a few weight bits after deployment, using the CogBias framework and BitScout tool. Experiments on Llama‑3.2‑3B, Mistral‑7B, Qwen2.5‑14B show that sparse bit flips reliably shift model stances on target topics while leaving other tasks largely unaffected.

## Key Takeaways
- BFAs can inject cognitive bias by altering a minimal number of weight bits after the model is deployed, enabling stealthy manipulation without real‑time control or training interference.  
- The CogBias framework converts subjective preferences into optimization signals via a differentiable sentiment evaluator and a multi‑objective loss to steer the attack toward specific dimensions.  
- BitScout locates critical bits with an ultra‑sparse flip budget, producing targeted stance shifts on target topics while preserving overall output distribution.

## Context
The integration of open‑source LLMs into corporate strategy and recommendation systems amplifies their utility but also creates new security vulnerabilities. This work highlights that even subtle changes to model weights can alter high‑level decision processes, a concern not addressed by conventional content filters or robustness defenses. The findings underscore the need for bias‑aware evaluation in AI systems operating in critical domains.

## Implications
For practitioners, this research calls for safeguards against weight‑level attacks when deploying LLMs in high‑stakes environments. It also prompts regulators and developers to consider cognitive alignment beyond surface‑level output safety, ensuring that subtle internal manipulations do not compromise decision integrity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25227v1)
