---
title: OrchestraBench: Evaluating Multi-Agent Orchestration Failure Modes, Recovery, and Decomposition Quality
url: http://arxiv.org/abs/2608.05263v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_17-27-15Z_OrchestraBench_EvaluatingMulti_AgentOrchestrationF.md
generated_at: 2026-08-06 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
OrchestraBench evaluates failure, recovery, and decomposition in multi‑agent orchestration pipelines by injecting reproducible failures into templated enterprise workflows. The study finds that an intent‑reasoning router achieves 100 % diagnostic accuracy on adversarial cases, whereas a keyword/flag router scores 0 %, highlighting the importance of deeper reasoning over surface cues.

## Key Takeaways
- A keyword/flag router scored 0 % on adversarial cases with misleading or missing surface flags.  
- An intent‑reasoning model router scored 100 %, matching the oracle.  
- Controlled mechanism probes revealed three failure‑handling tiers across five MAST modes: tool faults recovered fully (recovery rate = 1.0), ambiguous delegation recovered partially (recovery rate = 0.30), and latent or semantic modes never recovered (recovery rate = 0.0).  
- Cascade radius increased with pipeline depth, ranging from a mean of 0.9 to 4.7 across depths 3‑7.

## Context
Multi‑agent orchestration frameworks are essential for coordinating complex AI workflows, yet existing benchmarks often report only task accuracy without diagnosing why pipelines fail or where cascades begin. OrchestraBench addresses this gap by providing a controlled diagnostic harness that measures both failure propagation and recovery quality.

## Implications
Robust routing policies must prioritize accurate fault attribution to prevent cascade escalation. In industry, reliance on autonomous agents hinges on transparent detection mechanisms rather than blind retries; practitioners should focus on building trustworthy diagnostic layers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05263v1)
