---
title: AOS-Bench: Can LLM Agents Manage Dynamic Workloads?
url: http://arxiv.org/abs/2610.33178v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_18-20-48Z_AOS_Bench_CanLLMAgentsManageDynamicWorkloads.md
generated_at: 2026-10-26 20:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AOS-Bench introduces a benchmark that evaluates LLM coding agents not as single-task solvers but as workload managers handling concurrent, time-arriving tasks under shared CPU and memory constraints. The paper demonstrates that isolated task success does not translate evenly to streaming success, with systems losing 13 to 23 points on heavy workloads and exhibiting up to 26-point performance gaps on medium workloads. The authors identify task intake policy as a critical bottleneck, showing that serial dispatch leaves 73% of heavy-workload tasks unclaimed, while simple fixed-concurrency policies can nearly match the best agent-managed strategies.

## Key Takeaways
- Isolated benchmark performance is a poor predictor of streaming performance: two systems separated by only 0.6 points in isolated success delivered 54% and 68% of the same tasks under workload conditions, revealing a 14-point divergence that existing benchmarks cannot detect. This gap spans 26 points on medium workloads across five model-harness pairs, indicating that workload management is a distinct capability not captured by current evaluation frameworks.
- Task intake policy is the primary failure mode: serial dispatch strategies leave 73% of heavy-workload tasks unclaimed, meaning agents fail not because they cannot solve tasks but because they never accept them. This reframes the problem from reasoning quality to scheduling and admission control, areas where agents lack explicit training or tooling.
- Elaborate agent-managed concurrency policies provide marginal gains over trivial baselines: a fixed concurrency of two comes within four points of the best agent-managed policy on both medium and heavy workloads, and median CPU utilization stays below 30% of provisioned cores under every tested policy while tasks wait. This suggests that current agent systems are not effectively utilizing available compute resources for parallel task execution.

## Context
The field of LLM agents has rapidly advanced single-task benchmarks such as SWE-bench and HumanEval, which evaluate agents on isolated coding problems. However, real-world deployments increasingly involve persistent assistants receiving streams of heterogeneous tasks—builds, data pipelines, bug fixes—arriving asynchronously on shared infrastructure. AOS-Bench addresses a fundamental evaluation gap: no existing benchmark measures an agent's ability to manage concurrent workloads, delegate tasks, and respect hardware constraints, leaving a critical deployment capability unmeasured and unoptimized.

## Implications
For practitioners deploying coding agents in production environments, this work signals that raw model capability is insufficient; scheduling, admission control, and resource-aware task dispatch are now first-class engineering concerns that determine whether agents deliver value under realistic load. For the research community, AOS-Bench establishes workload management as a distinct evaluation axis, suggesting that future agent training and tooling should incorporate explicit concurrency and resource-budget reasoning rather than assuming sequential task execution. Industry teams building agent platforms should treat fixed-concurrency baselines as strong starting points and invest in intake policies before pursuing more complex agent-managed orchestration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33178v1)
