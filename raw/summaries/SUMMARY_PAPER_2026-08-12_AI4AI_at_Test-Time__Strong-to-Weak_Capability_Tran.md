---
title: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
url: http://arxiv.org/abs/2608.12307v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-53-18Z_AI4AIatTest_Time_Strong_to_WeakCapabilityTransferv.md
generated_at: 2026-08-12 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large model capabilities can be transferred to smaller models at test time using inference‑time harnesses rather than training updates. On four Theory‑of‑Mind benchmarks, a stronger builder model creates a harness that boosts the weaker target’s performance from 0.49 to 0.91, nearly doubling its accuracy.

## Key Takeaways
- Gains come primarily from offloading unstable reasoning into deterministic code, benchmark‑specific routing, and strict answer‑format enforcement rather than encouraging more extensive or broader sampling.
- Builder‑model reasoning effort improves harness quality monotonically across the refinement process.
- Weaker target models receive the largest gains; platform effects are modest compared with the builder model’s own capability.

## Context
Traditional distillation relies on training‑time parameter updates to transfer knowledge. This work explores a complementary test‑time approach where harnesses act as scaffolding, allowing strong models to scaffold weaker ones without any retraining or additional data.

## Implications
Inference‑time harness design offers a scalable way for industry and researchers to leverage the strengths of large models while deploying smaller, cost‑effective agents. By offloading reasoning into deterministic code, practitioners can achieve higher performance with minimal computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12307v1)
