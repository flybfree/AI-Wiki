# Summary: 2026-10-12_22-35-08Z_ScalingInference_TimeComputewithTeamsofCodingAgent.md
Saved: 2026-10-14 02:11
Source: 2026-10-12_22-35-08Z_ScalingInference_TimeComputewithTeamsofCodingAgent.md
Model: None

---

## Summary
This paper investigates the optimization of multi-agent systems for coding tasks by framing team design as a compute allocation problem. The authors explore how to scale inference-time compute effectively by distributing tasks across multiple agents rather than relying on a single agent’s extended reasoning. By systematically varying delegation strategies, model heterogeneity, and team size, the study identifies specific configurations that maximize reward while minimizing cost. The core contribution is a practical guide for allocating inference budgets, demonstrating that strategic delegation of planning tasks to cheaper models can achieve near-optimal performance at significantly lower costs compared to homogeneous, high-cost teams.

## Key Contributions
- **Planning is the most valuable delegation target:** The study finds that delegating only the planning phase to workers, while the lead agent handles implementation and verification, yields the same performance as full delegation but at half the cost. This suggests that the cognitive load of structuring a solution is the primary bottleneck where multi-agent collaboration provides the highest utility.
- **Heterogeneous teams offer superior cost-efficiency:** The authors demonstrate that using cheap models as planners and strong models as implementers is highly effective. A strong lead agent utilizing cheap planners recovers 47.5% of the performance gains of an all-strong team for only 13.9% of the additional cost, whereas using cheap models for implementation actively degrades performance.
- **Diminishing returns in implementation and verification:** The research establishes that while adding more planner agents continues to improve reward, increasing the number of implementer or verifier agents plateaus beyond four workers. This indicates that parallelism is beneficial for ideation and structuring but less so for execution and checking, where coordination overhead likely outweighs benefits.

## Methodology
The authors constructed a minimal multi-agent harness from the ground up to rigorously test the reward-cost Pareto frontier. They began with a baseline solo agent and systematically introduced multi-agent capabilities by varying three specific parameters independently: the workflow stage where delegation occurs (planning, implementation, or verification), the composition of the team (homogeneous strong models vs. heterogeneous strong/weak models), and the number of worker agents. These configurations were evaluated on the ProgramBench dataset, allowing the authors to isolate the impact of each variable on both task success (reward) and computational expense (cost).

## Results
Experimental results on ProgramBench show that while multi-agent teams generally outperform solo agents, they typically incur three to seven times the cost. However, optimized heterogeneous teams can achieve near-parity with expensive homogeneous teams at a fraction of the cost. Specifically, a 17-agent heterogeneous team came within 1.4 points of a strong 5-agent homogeneous team while costing 70% less. The data confirms that "planning-heavy" delegation strategies dominate the Pareto frontier, while "implementation-heavy" strategies suffer from diminishing returns and higher costs without proportional performance gains.

## Significance
This work provides a critical framework for deploying large language models in production environments where cost and latency are constrained. By identifying exactly where additional compute yields diminishing returns, the paper offers actionable guidelines for engineering efficient multi-agent systems. It challenges the assumption that more agents or stronger models in every role are necessary for high performance, instead advocating for a nuanced allocation of resources that prioritizes high-quality planning and leverages cheaper models for less critical tasks.

## Related Concepts
- Inference-Time Compute Scaling
- Multi-Agent Systems (MAS)
- Reward-Cost Pareto Frontier
- Heterogeneous Model Teams
- Workflow Delegation Strategies
- ProgramBench
- Compute Allocation Optimization
