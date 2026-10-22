---
title: Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing
url: http://arxiv.org/abs/2610.28815v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_18-36-33Z_ForgingMoreTasksintoBetterHarnesses_AgenticHarness.md
generated_at: 2026-10-21 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a paradoxical failure mode in agentic harness evolution: as the pool of tasks used to evolve an agent's instructions, tools, and control flow grows larger, existing methods actually degrade in performance due to suboptimal evidence selection during optimization. To solve this, the authors propose Successive Scale Racing (SSR), a framework that adaptively searches for optimal evidence combinations each evolution round by constructing diverse combinations based on task quality and coverage, then racing candidate harnesses under a small compute budget. SSR achieves state-of-the-art results across three benchmarks in all six configurations, improving pass rates from 64.3% to 68.3% as the task pool scales from 40 to 200 tasks, while baselines decline.

## Key Takeaways
- Existing agentic harness evolution methods suffer a counterintuitive degradation: expanding the task pool from 40 to 200 tasks causes baseline performance to drop, contradicting the intuitive expectation that more tasks should yield better optimization. The root cause is traced to suboptimal evidence selection, where different evidence combinations produce substantially different and often worse evolution outcomes.
- SSR addresses this by constructing diverse evidence combinations guided by task quality and coverage metrics, then efficiently racing multiple candidate harnesses under a constrained compute budget. This racing mechanism identifies near-optimal candidates while reducing validation executions by 60%, making the search process both effective and computationally practical.
- Empirically, SSR outperforms all baselines across three distinct benchmarks in six configurations. Critically, as the task pool grows from 40 to 200 tasks, SSR steadily improves pass rates from 64.3% to 68.3%, demonstrating that proper evidence selection is the key to scaling agentic harness evolution rather than simply adding more tasks.

## Context
Agentic harness evolution represents a growing paradigm in AI systems where agents iteratively refine their own instructions, tool-use strategies, and control flow based on accumulated task execution experience. This self-improving loop is central to building autonomous agents that adapt across diverse task distributions. However, the field has largely assumed that more diverse and numerous tasks automatically lead to better agent optimization. This paper challenges that assumption head-on, revealing that the selection and combination of evidence during evolution is a critical bottleneck that existing methods overlook. By formalizing the evidence selection problem and proposing a structured racing mechanism, the work bridges a gap between theoretical optimization frameworks and practical agent self-improvement pipelines.

## Implications
For practitioners building self-improving agent systems, this work signals that simply increasing the volume of training or evolution tasks is insufficient and can actively harm performance; instead, careful curation and combination of evidence is essential. The SSR framework's 60% reduction in validation executions makes it feasible for teams with limited compute budgets to deploy harness evolution at scale, lowering the barrier for industrial adoption. For the broader AI research community, the findings underscore that meta-optimization strategies—how evidence is selected and combined—deserve as much attention as the optimization algorithms themselves, potentially reshaping how future agentic systems are designed and evaluated.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28815v1)
