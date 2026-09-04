---
title: Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments
url: http://arxiv.org/abs/2609.04148v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-41-05Z_Terminal_Universe_TurningAgentTrajectoriesintoScal.md
generated_at: 2026-09-03 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Terminal‑Universe, a framework that converts existing terminal agent trajectories into reusable executable environments without generating new ones from scratch. By replaying recorded file operations and using completion agents to supply missing files, the system reconstructs original tasks and synthesizes novel ones. Applied to public data, it creates 37 300 task‑sufficient environments, boosting Qwen3.5‑27B performance on Terminal‑Bench 2.1 by 11.9 points and EvoCode‑Bench v2 MT@4 by 13.8 points.

## Key Takeaways
- The framework reconstructs each environment from the file‑operation history recorded in a trajectory, producing a partial workspace that can be completed by a dedicated agent.
- It scales tasks along two axes: breadth through cross‑workspace queries linking multiple codebases and depth via multi‑round sessions that capture iterative user feedback.
- Supervised fine‑tuning on this corpus significantly improves both single‑turn and multi‑turn performance across benchmark suites.

## Context
The rapid rise of terminal‑based AI agents has generated massive amounts of execution data, yet the lack of reusable environments hampers progress. This work bridges that gap by turning raw trajectories into verifiable, executable worlds, enabling more realistic testing and task synthesis. The approach aligns with broader efforts to make agent training more efficient and grounded in actual codebases.

## Implications
For developers, Terminal‑Universe provides a scalable way to generate diverse test scenarios directly from existing agent logs, reducing the need for manual environment creation. For researchers, it offers a large, labeled dataset that can be leveraged to fine‑tune large language models, accelerating progress in AI‑assisted coding and interactive development workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04148v1)
