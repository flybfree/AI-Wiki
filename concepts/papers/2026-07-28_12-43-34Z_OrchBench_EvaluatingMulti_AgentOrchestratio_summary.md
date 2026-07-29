# Summary: 2026-07-28_12-43-34Z_OrchBench_EvaluatingMulti_AgentOrchestrationPlansi.md
Saved: 2026-07-28 20:29
Source: 2026-07-28_12-43-34Z_OrchBench_EvaluatingMulti_AgentOrchestrationPlansi.md
Model: None

---

## Summary  
The paper introduces OrchBench, a deterministic simulation‑based benchmark designed to evaluate multi‑agent orchestration plans without invoking real workers or external tools. By constructing directed acyclic graphs (DAGs) that encode task dependencies and controlling agent budgets and context limits, OrchBench isolates the quality of the plan itself from worker capabilities, tool reliability, and environmental noise. The authors demonstrate that simulated scores correlate strongly with actual execution outcomes, offering a lightweight alternative to costly end‑to‑end evaluations. Their work thus provides an efficient, interpretable framework for comparing and diagnosing orchestration strategies.

## Key Contributions  
- [Finding 1] OrchBench creates a deterministic simulation environment that evaluates multi‑agent orchestration plans in isolation, separating plan quality from worker‑related factors such as tool reliability or environmental noise.  
- [Finding 2] The simulated metrics—result quality, makespan, and token cost—correlate with real‑world execution scores (Claude Code) at a Pearson coefficient of r = 0.816 while using only 1.3 % of the tokens and 10.3 % of wall‑clock time.  
- [Finding 3] Preserving task‑critical information is more important than simply increasing the number of agents; as coordination failures accumulate, the benefits of parallelism diminish.

## Methodology  
OrchBench begins with real‑world tasks that are decomposed into subtasks forming a directed acyclic graph (DAG). The DAG’s size and degree of parallelism are controlled to simulate various workflow scales. Given a DAG, a per‑agent context limit, and an agent budget, the planner assigns subtasks to agents and defines cross‑agent information transfers along with retention ratios. A deterministic simulator then executes the resulting plan without invoking actual workers, computing interpretable measures of quality, makespan, and token consumption. This simulation isolates the orchestration logic from external variability.

## Results  
Across a suite of diverse planners and workflow scales, OrchBench’s simulated scores align closely with human‑evaluated quality metrics (r = 0.816). The evaluation consumes merely 1.3 % of total tokens and 10.3 % of wall‑clock time compared to full end‑to‑end runs. Experiments reveal that maintaining task‑critical information yields the greatest gains, whereas adding more agents provides diminishing returns as coordination errors increase.

## Significance  
OrchBench establishes an efficient, interpretable benchmark for comparing and diagnosing multi‑agent orchestration plans, dramatically reducing computational cost while preserving analytical rigor. By isolating plan quality from worker‑related noise, it enables systematic research into how information retention, agent budgeting, and parallelism interact to affect system performance.

## Related Concepts  
multi‑agent systems, orchestration plans, directed acyclic graphs (DAGs), deterministic simulation, token cost, makespan, coordination failures, information retention ratios, agent budget, parallelism, task‑critical information.
