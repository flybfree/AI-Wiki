---
title: openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents
url: http://arxiv.org/abs/2608.27969v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_06-31-38Z_openJiuwen_BeyondStaticHarnessesforLong_HorizonCod.md
generated_at: 2026-08-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces openJiuwen, an open-source harness for long-horizon coding agents that addresses structural composability and runtime adaptivity. It enables developers to compose heterogeneous capabilities across single agents, delegated sub‑agents, and Swarm Flow using a shared execution substrate. On benchmark suites it outperforms top official leaderboard points by 3.4% on SWE-bench Verified and 3.39% on Terminal-Bench 2.1.

## Key Takeaways
- openJiuwen provides a unified execution platform that allows seamless composition of capabilities without rebuilding orchestration, directly tackling the structural composability challenge.
- The harness dynamically adjusts runtime decisions based on evolving evidence such as diagnostics and task progress, fulfilling the runtime adaptivity requirement.
- Benchmark results show significant performance gains over existing solutions, confirming both composable design and adaptive effectiveness.

## Context
Long‑horizon coding agents must handle changing repository states and heterogeneous agent interactions, which current frameworks struggle to support. This work contributes a practical harness that bridges these needs, offering a template for future research on scalable AI agents.

## Implications
Developers can now build more flexible and responsive coding assistants without reinventing orchestration logic. The adaptive framework may reduce iteration time and improve success rates in real‑world code generation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27969v1)
