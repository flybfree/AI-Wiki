---

title: "ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents"
url: http://arxiv.org/abs/2605.12481v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-12_17-57-04Z_ToolCUA_TowardsOptimalGUI_ToolPathOrchestrationfor.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---


## Summary
ToolCUA is an end-to-end framework that learns optimal GUI-Tool path selection for computer use agents. Experiments on OSWorld-MCP show it reaches 46.85% accuracy, a 66% improvement over baselines and a further 3.9% gain over pure GUI settings.

## Key Takeaways
- The paper addresses the uncertainty in hybrid action spaces by proposing an interleaved training pipeline that synthesizes tool trajectories from static GUI data.
- Tool-Bootstrapped GUI RFT combines warmup SFT with single-turn RL to improve decisions at critical switching points between GUI actions and tool calls.
- Online Agentic RL optimizes execution using a path reward that favors efficient tool use, yielding state-of-the-art performance.

## Context
The field of computer use agents faces challenges in integrating low-level GUI operations with high-level tool capabilities. Existing models often rely on manual engineering or scarce real-world trajectories, limiting scalability and robustness. This work demonstrates that synthetic data generation can bridge this gap effectively.

## Implications
For practitioners developing digital assistants, ToolCUA provides a scalable method to train agents that seamlessly switch between UI interactions and backend tools without extensive labeling. The approach could accelerate the deployment of complex automation systems across industries where precise tool orchestration is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.12481v1)
