# Summary: 2026-08-05_08-50-36Z_EASy_TowardsEfficientLLM_BasedAgenticSystem.md
Saved: 2026-08-05 20:32
Source: 2026-08-05_08-50-36Z_EASy_TowardsEfficientLLM_BasedAgenticSystem.md
Model: None

---

## Summary  
The paper introduces EASy, a trainable orchestrator that coordinates heterogeneous LLM agents to solve complex tasks while minimizing computational cost and respecting executor capabilities. It moves beyond traditional router‑based systems by jointly optimizing task success and execution efficiency through reinforcement learning. The framework employs a milestone‑plan‑act workflow that creates dependency‑aware execution graphs and parallelizes independent steps. By training the orchestrator with tree‑structured rollouts and multi‑component rewards, EASy achieves strong performance‑efficiency trade‑offs on diverse benchmarks.  

## Key Contributions  
- [Finding 1] The milestone‑plan‑act workflow decomposes complex tasks into sequential milestones, builds dependency graphs, and assigns executors based on capability and cost profiles.  
- [Finding 2] A tree‑structured rollout method systematically explores alternative task decompositions and execution plans to discover efficient strategies.  
- [Finding 3] Multi‑component rewards simultaneously reward task correctness, computational efficiency, and trajectory completeness.  

## Methodology  
The authors designed EASy as a reinforcement learning system where the orchestrator’s policy is trained to maximize a composite reward. First, tasks are broken into milestones using a milestone‑plan‑act decomposition; each milestone defines an action that can be executed by any executor whose capability and cost profile match. The orchestrator then constructs an execution graph linking dependent actions. During training, the system performs tree‑structured rollouts: it recursively explores different milestone orders and parallelization choices, generating diverse trajectories. Each completed trajectory is scored with three reward components—task accuracy, total compute cost, and whether all milestones were reached in order.  

## Results  
Experiments on mathematical reasoning (e.g., solving equations), embodied decision‑making simulations, and deep research benchmarks show that EASy consistently outperforms strong agentic baselines. The performance‑efficiency trade‑off is quantified by higher task success rates at lower compute budgets, with average speed‑up of 1.8× compared to baseline agents while maintaining comparable accuracy.  

## Significance  
EASy addresses a critical gap in current LLM agentic systems: they prioritize correctness over practical constraints like executor capability and cost. By integrating explicit knowledge of heterogeneous executors and a structured reward function, EASy enables scalable, resource‑aware coordination, paving the way for real‑world deployment where efficiency is as important as accuracy.  

## Related Concepts  
- LLM‑based agents  
- Orchestration / routing  
- Reinforcement learning with composite rewards  
- Milestone decomposition  
- Execution graph construction  
- Tree‑structured rollout
