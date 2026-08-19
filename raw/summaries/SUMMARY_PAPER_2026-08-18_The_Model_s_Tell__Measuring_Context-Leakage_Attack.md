---
title: The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges
url: http://arxiv.org/abs/2608.17829v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_14-28-51Z_TheModel_sTell_MeasuringContext_LeakageAttackSigna.md
generated_at: 2026-08-18 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LeakGauge, a lightweight probe that measures context‑leakage attack signals by appending a suffix to queries and mapping prefill token probabilities to an attack‑risk score. Experiments across eleven large language models show AUROC values between 0.944 and 0.996 on unseen attacks, demonstrating the method’s effectiveness in detecting both verbatim and semantic disclosures while remaining stable under language or content changes.

## Key Takeaways
- LeakGauge extracts an internal “tell” from model responses using token‑probability gauges rather than relying solely on explicit initial tokens.  
- The risk score is robust to variations in input language or attack type, indicating a reliable signal across diverse scenarios.  
- Activation‑steering interventions reveal that the observable gauge aligns with the direction of leakage within the model’s hidden representation.

## Context
Large language models increasingly incorporate external contexts such as system prompts and retrieved documents, creating vulnerabilities where adversarial inputs can cause unwanted disclosure. Detecting these leaks early is crucial for safeguarding proprietary information without significantly impacting latency or parameter count.

## Implications
LeakGauge offers practitioners a practical tool to monitor model behavior in production environments, enabling rapid response to potential leakage incidents. Its minimal overhead and low latency make it suitable for real‑time monitoring across enterprise AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17829v1)
