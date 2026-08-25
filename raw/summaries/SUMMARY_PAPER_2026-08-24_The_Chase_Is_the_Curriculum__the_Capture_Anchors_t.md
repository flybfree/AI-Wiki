---
title: The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning
url: http://arxiv.org/abs/2608.21871v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_09-30-29Z_TheChaseIstheCurriculum_theCaptureAnchorstheCredit.md
generated_at: 2026-08-24 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LURE, a pursuit‑evasion framework that enables large language models to improve reasoning through zero‑data self‑play without relying on human‑curated task collections. By treating the evader’s task placement as a game against a pursuer, LURE learns a positioning strategy and dense process credit, leading to stronger performance than existing baselines across multiple environments.

## Key Takeaways
- The evader uses a capture‑frontier reward that peaks when the solver captures it on exactly half of its rollouts, turning barely catchable tasks into a learned difficulty axis.  
- The pursuer receives dense process credit via monotone verifier progress group‑normalized with terminal capture under a round‑anchored KL divergence to keep co‑evolution stable.  
- A unified model outperforms specialist baselines and achieves the strongest aggregate OOD zero‑shot accuracy across nine held‑out benchmarks.

## Context
Zero‑data self‑play is increasingly used to train LLMs, yet it depends on large human‑curated datasets. This work reframes that process as a pursuit‑evasion game, offering a principled way to position tasks and distribute credit without manual tuning. The approach aligns with the broader trend of RL‑based reasoning enhancement while introducing stable credit mechanisms.

## Implications
The method enables scalable training pipelines that do not require extensive labeled data, which is valuable for industry practitioners seeking rapid model improvement. By improving OOD zero‑shot accuracy, LURE can be applied to diverse applications where generalization beyond training tasks matters most.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21871v1)
