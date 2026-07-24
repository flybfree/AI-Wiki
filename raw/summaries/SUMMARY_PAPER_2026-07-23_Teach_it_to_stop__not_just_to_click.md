---
title: Teach it to stop, not just to click
url: http://arxiv.org/abs/2607.17136v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_08-46-06Z_Teachittostop_notjusttoclick.md
generated_at: 2026-07-23 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the reliability of agentic computer‑use reinforcement learning agents that can perform tasks in a single run, arguing that reported success rates are misleading due to high variance. By applying verifier‑guided repair across five oracle‑graded environments and analyzing variance components, the authors find that evaluation variance is negligible while training‑seed effects are small; most uncertainty stems from data draws and run‑to‑run nondeterminism, especially on the hardest cell where a single run has only about 30 % chance of failure. They also show that repairs can be either reliable fixed tokens or partial open‑ended actions, and that frame‑level repair only transfers to task success when it removes the last blocker.

## Key Takeaways
- The evaluation variance is negligible (σ_eval ≈ 0) and training‑seed effects are ≤10 %, indicating that single‑run numbers reflect upstream data draw and nondeterministic run behavior rather than stable performance.  
- On the hardest cell, data draws dominate the variance at ~48 % of total uncertainty, with run‑to‑run distribution showing a bimodal Hartigan dip (p=0.07) that makes mean±std an inadequate summary.  
- Repairability is two‑tiered: fixed token corrections work reliably (detection 0.97 ± 0.06), whereas spatial‑coordinate clicks and generative field fills are only partially effective, and frame‑level repair only succeeds when it eliminates the final blocker.

## Context
The paper addresses a growing trend in AI research where single‑run agentic agents claim high success rates without accounting for stochastic variability. This work highlights that such claims often overlook variance components, leading to inflated performance metrics. By introducing a systematic k‑seed reporting framework and multimodal self‑distillation, the authors aim to provide more honest assessments of complex, real‑world AI systems.

## Implications
For researchers, this study calls for rigorous replication across seeds before publishing single‑run results, preventing overstated claims in the field. Practitioners should adopt the released cua_reliability library to evaluate and report agentic agents with appropriate confidence intervals, ensuring that improvements are meaningful rather than artifact of randomness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17136v1)
