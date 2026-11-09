---
title: Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?
url: http://arxiv.org/abs/2611.07166v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-04_21-49-40Z_Multi_stepSWE_CanCodingAgentsKeepBuildingonTheirOw.md
generated_at: 2026-11-08 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Multi-step SWE, a benchmark of 69 software engineering tasks designed to evaluate coding agents on long-horizon, multi-step development workflows where each step builds upon code the agent previously generated. The benchmark reveals that even the strongest frontier models achieve only an 18.5% solve rate, and 38 out of 69 tasks remain unsolved by any model tested, highlighting a significant gap between current agent capabilities and realistic multi-step software engineering demands.

## Key Takeaways
- Multi-step SWE consists of 69 tasks, each structured as a chain of 5 to 15 dependent steps on a single codebase, where every step is a complete multi-hour engineering request that begins from the code the agent produced in prior steps. This design ensures that early design decisions and errors propagate forward, mimicking how real developers iteratively build, extend, upgrade, and optimize their own code over time.
- The benchmark spans four families of engineering work and nine programming languages, covering both from-scratch builds and modifications to existing open-source codebases. Every step is grounded in an existing source of truth that defines both the instruction and its verifier, ensuring tasks are realistic and objectively evaluable rather than synthetic or trivial.
- Across nine frontier models evaluated on the benchmark, the best-performing model achieved a solve rate of only 18.5%, while 38 of the 69 tasks were not solved by any model at all. This demonstrates that current coding agents struggle severely with sustained, dependent multi-step reasoning and the compounding of errors across a long development horizon.

## Context
Most existing coding-agent benchmarks, such as SWE-bench, evaluate models on isolated single-task problems, which fails to capture the iterative, cumulative nature of real software development. Multi-step SWE addresses this gap by constructing tasks that mirror how developers actually work: building a component, then extending, upgrading, and optimizing it across many dependent steps. This shift from single-shot evaluation to long-horizon chained evaluation represents a critical methodological advance in how the AI research community measures agent capability, pushing the field toward more ecologically valid assessments of autonomous coding systems.

## Implications
For practitioners and industry teams deploying coding agents in production, these results signal that current models cannot yet reliably handle the kind of sustained, multi-step engineering workflows that define real software projects, meaning human oversight and iterative correction remain essential in the near term. For the AI research community, the benchmark provides a concrete, publicly available evaluation suite that exposes specific failure modes in long-horizon reasoning and error propagation, offering a clear target for future model and agent-architecture improvements. The fact that over half the tasks remain unsolved by any frontier model underscores that significant algorithmic and architectural progress is still needed before coding agents can operate autonomously over extended development cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07166v1)
