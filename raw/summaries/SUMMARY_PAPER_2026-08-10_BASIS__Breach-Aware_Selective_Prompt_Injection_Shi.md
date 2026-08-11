---
title: BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes
url: http://arxiv.org/abs/2608.08027v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_09-32-07Z_BASIS_Breach_AwareSelectivePromptInjectionShieldin.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BASIS, a defense mechanism that uses attention competition ratio features to train two sparse probes for detecting prompt injection and predicting breaches without additional LLM inference. Experiments show near‑perfect detection while cutting over‑refusal on safe attack samples across tasks and models.

## Key Takeaways
- BASIS employs the Attention Competition Ratio (ρ) as a feature to train two sparse linear probes, an existence probe and a breach probe, enabling defense decisions via cascaded gating without additional LLM inference.  
- The cascade refuses only when the model would actually be compromised, thereby avoiding unnecessary over‑refusal on instructions that are robust to injection attacks.  
- Experiments across four tasks and six open‑source LLMs demonstrate that BASIS maintains high detection rates while substantially reducing false refusals on safe attack samples.

## Context
Prompt injection remains a critical security challenge for large language models, prompting developers to balance safety with usability. Existing methods often sacrifice responsiveness by refusing all suspicious inputs, leading to user frustration and reduced adoption of LLM services in production systems.

## Implications
For industry practitioners, BASIS offers a practical way to deploy injection defenses that do not degrade model performance or increase latency. By reducing over‑refusal, the approach supports smoother user experiences while maintaining security, encouraging wider deployment of AI assistants in commercial applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08027v1)
