---
title: APPSim-Bench: Bridging Real-world Apps and Reproducible Evaluation for Mobile GUI Agents
url: http://arxiv.org/abs/2609.07712v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_16-25-13Z_APPSim_Bench_BridgingReal_worldAppsandReproducible.md
generated_at: 2026-09-08 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AppSim-Bench to provide a controllable simulated environment for evaluating mobile GUI agents, balancing realism and reproducibility. It contains 557 tasks across 17 popular Chinese and English apps, enabling deterministic evaluation of 19 different agents. The best model succeeds in only about half the tasks.

## Key Takeaways
- AppSim-Bench creates a coding‑agent‑assisted workflow that generates reproducible simulated apps preserving task‑relevant interaction logic while eliminating uncontrolled real‑world variations such as ads or account changes.
- Evaluation shows autonomous mobile execution remains far from solved, with 50.27% of tasks completed by the best model and 28.55% unsolved across all agents.
- Failures are concentrated in longer workflows, numerical reasoning tasks, and trajectories that consume excessive actions or exhaust budget limits.

## Context
Mobile GUI agents aim to perform tasks from natural‑language instructions without human intervention, but existing benchmarks either simplify apps too much or expose them to unpredictable real‑world changes. This gap hampers reliable comparison of model performance across diverse environments.

## Implications
The study demonstrates that reproducibility can be achieved through controlled simulation, offering a valuable benchmark for future research and industry practitioners developing autonomous mobile agents. It also highlights the need for better handling of long‑range reasoning and action efficiency to improve real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07712v1)
