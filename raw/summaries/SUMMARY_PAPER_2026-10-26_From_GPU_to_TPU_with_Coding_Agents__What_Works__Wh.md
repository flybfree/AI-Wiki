---
title: From GPU to TPU with Coding Agents: What Works, What Fails, and What It Costs?
url: http://arxiv.org/abs/2610.34422v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_16-21-56Z_FromGPUtoTPUwithCodingAgents_WhatWorks_WhatFails_a.md
generated_at: 2026-10-26 23:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether AI coding agents (specifically Claude Code) can reliably migrate machine learning workloads from NVIDIA GPUs to Google Cloud TPUs, and at what cost. The authors build a dataset of 148 PyTorch ML research projects, migrate ten of them using an agent, and independently assess correctness, numerical fidelity, hardware targeting, goal preservation, and performance. The central finding is that agent-generated migrations are unreliable: 76% of execution attempts fail, nearly half of failures produce no error message, and silent numerical changes can degrade model accuracy without the agent reporting any problem.

## Key Takeaways
- Migrations require significant human oversight: on average 2.4 human interventions per migration are needed, and only 8 out of 10 projects meet the authors' project-goal criterion, indicating that fully autonomous agent-driven hardware migration is not yet viable for production use.
- Silent failures dominate: of 70 execution attempts, 53 fail (76%), and 26 of those failures (49%) raise no error at all. The most frequent failure cause is repeated compilation and execution inefficiencies, while interactions with third-party libraries can silently alter computation. In one four-chip TPU migration, the agent reported success despite a change in gradient clipping that reduced accuracy from 86.53% to 84.89%, demonstrating that numerical behavior preservation is not guaranteed.
- Performance and cost outcomes are highly workload-dependent: for one specific workload, the TorchTPU backend trained 1.86 times faster and 25% cheaper per run than the GPU baseline, but such gains are not generalizable across the broader dataset, underscoring the need for workload-specific evaluation rather than blanket hardware-switching assumptions.

## Context
As GPU supply constraints, rising compute costs, and vendor lock-in pressures push organizations toward alternative accelerators like Google Cloud TPUs, the question of whether automated coding agents can handle the software migration burden has become practically urgent. This paper is among the first to systematically evaluate agent-generated hardware migrations against rigorous correctness and numerical-fidelity criteria, rather than simply checking whether code runs. It contributes to the broader discourse on AI-assisted software engineering by exposing failure modes—silent numerical drift, library incompatibilities, compilation overhead—that are invisible to naive success metrics.

## Implications
For practitioners and engineering teams considering GPU-to-TPU migrations, the findings argue strongly for independent reference runs on the target hardware, verification under the exact intended hardware configuration, and workload-specific acceptance and stopping criteria that account for both computational and human costs. The paper also signals that current coding agents should not be trusted as sole migration agents without a human-in-the-loop verification pipeline, and that organizations should budget for the 2.4 average human interventions per migration rather than assuming a fully automated transition. For the AI research community, the work highlights the need for benchmark suites that test numerical equivalence and silent-failure detection, not just execution success, when evaluating agent-driven code transformations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34422v1)
