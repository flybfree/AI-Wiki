---
title: DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck
url: http://arxiv.org/abs/2610.17184v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_17-54-30Z_DuoDiscover_ScalingAutonomousDiscoveryBeyondtheEva.md
generated_at: 2026-10-14 01:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DuoDiscover is a search system designed to overcome the evaluation bottleneck that limits autonomous discovery in real-world engineering tasks where a single true evaluation can take hours. The system jointly discovers what to optimize and how to evaluate progress efficiently by having coding agents co-discover tailored proxy evaluators called "yardsticks," continuously validating them against true objectives, and operating as a decentralized fleet without central problem decomposition. It demonstrates state-of-the-art results across software optimization benchmarks and hardware design tasks, surpassing both human experts and prior autonomous systems.

## Key Takeaways
- Each worker in a fleet of coding agents independently co-discovers an optimization target and a fast, tailored proxy evaluator (a "yardstick"), then hill-climbs the yardstick rather than the expensive true evaluation, enabling many more search iterations within a fixed evaluation budget.
- Fidelity tests continually recheck each yardstick's ranking against the true objective and invalidate any yardstick that drifts, preventing the search from exploiting gaps between the proxy and the actual goal and ensuring the optimization remains grounded in real performance.
- The fleet operates bottom-up with no central decomposition: a lightweight orchestrator spawns, terminates, and briefs agents, seeding new agents with confirmed work from others, enabling scalable parallel discovery across domains from software kernels to CPU microarchitecture design.
- On SWE-fficiency, DuoDiscover doubles the average speedup achieved by human experts; on SOL-Exec it ranks first on 121 of 235 kernels; on heavily optimized vLLM and SQLite engines it achieves 1.92x and 1.38x gains; and on a CPU microarchitecture task with evaluations up to 28 hours, it surpasses AlphaEvolve-based ArchAgent v2 with 1.65x its gain in 16.7 days versus over 40 days.

## Context
Autonomous discovery systems have advanced rapidly through methods like AlphaEvolve and evolutionary search, but they remain constrained by the cost of evaluating candidate solutions in real engineering settings. This paper addresses a fundamental scaling problem: when a single benchmark run or hardware simulation takes hours, a search process can afford only a handful of true evaluations, severely limiting exploration. DuoDiscover reframes the problem by treating evaluation design as a co-discovery task alongside optimization, which is a novel departure from prior systems that assume a fixed, expensive evaluation oracle.

## Implications
For practitioners in software engineering, compiler optimization, and hardware design, DuoDiscover offers a practical path to autonomous optimization that can operate within realistic evaluation budgets, potentially accelerating kernel tuning, engine optimization, and chip architecture exploration far beyond what human teams or prior autonomous agents achieve. For the broader AI research community, the co-discovery of proxy evaluators and the bottom-up fleet architecture suggest a generalizable paradigm for scaling any autonomous discovery pipeline where evaluation is the dominant cost, opening new directions for agentic systems in scientific and engineering domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17184v1)
