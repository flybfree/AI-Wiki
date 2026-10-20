---
title: WeAct: Dynamic Weight Switching as Agent Actions
url: http://arxiv.org/abs/2610.26847v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_17-59-19Z_WeAct_DynamicWeightSwitchingasAgentActions.md
generated_at: 2026-10-19 23:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
WeAct (Weight-level Internal Actions) introduces a novel approach for long-horizon agents to dynamically switch between capability-specific LoRA adapters during task execution, treating adapter selection as an agent action within the model's native tool-calling interface. The method trains independent adapters over a frozen backbone, enabling on-demand capability composition without catastrophic forgetting, and demonstrates significant accuracy improvements across eight deep-research benchmarks while using less compute than full fine-tuning.

## Key Takeaways
- WeAct addresses catastrophic forgetting in long-horizon agents by training independent capability-specific LoRA adapters over a frozen backbone rather than updating shared parameters. This prevents degradation of previously acquired capabilities when learning new ones, which is a fundamental limitation of conventional joint training and static adapter merging approaches that maintain a fixed parameter configuration throughout execution.
- The method integrates adapter selection directly into the agent's action space using the model's native tool-calling interface, enabling on-demand capability composition within a shared context. This means the agent can dynamically choose which capability adapter to activate at different stages of a trajectory, matching the heterogeneous capability requirements that emerge as complex tasks unfold.
- Empirical results show Qwen3-32B with WeAct achieves a 6.2% relative accuracy improvement over full fine-tuning counterparts while using less compute, and a 27.5% improvement over the strongest static LoRA-merging method across eight deep-research benchmarks. Additionally, WeAct supports modular continual adaptation, demonstrated by adding a new code computation adapter and updating an existing writing adapter without modifying the backbone or other adapters.

## Context
This paper sits at the intersection of continual learning, parameter-efficient fine-tuning, and agentic AI systems. Long-horizon agents that must handle diverse subtasks—research, coding, writing—face a fundamental tension between learning new capabilities and preserving old ones. Prior approaches like LoRA merging or full fine-tuning treat the model as a monolithic entity, ignoring the fact that different trajectory stages demand different skills. WeAct reframes model adaptation as an agentic decision problem, aligning with the broader trend of making AI systems more modular and composable.

## Implications
For practitioners building agentic systems, WeAct offers a practical path toward modular continual adaptation where new capabilities can be added or existing ones refined without retraining the entire model or risking degradation of unrelated skills. This has direct implications for production agent deployments where capabilities evolve over time and compute budgets are constrained. The approach also suggests a broader architectural principle: treating internal model configuration changes as first-class agent actions could unlock more flexible and maintainable AI systems across domains beyond research tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26847v1)
