---
title: No One Architecture Fits All: A Cross-Environment Evaluation of Hierarchical Red Team Agents
url: http://arxiv.org/abs/2610.00557v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_18-32-50Z_NoOneArchitectureFitsAll_ACross_EnvironmentEvaluat.md
generated_at: 2026-10-01 21:26
model: qwen3.6-35b-a3b
---

## Summary
This study conducts a controlled cross-environment evaluation of hierarchical autonomous red team agents to determine whether architectural advantages generalize across different cyber simulation settings. By comparing an RL-based hierarchy against an LLM-based hierarchy in CybORG CAGE-4 and Cyberwheel networks at varying scales, the research reveals a pronounced performance inversion where each architecture excels in distinct environments due to specific bottlenecks in the kill chain. The findings demonstrate that no single architecture is universally superior, emphasizing the need for environment-specific design choices over generalized assumptions about planner-executor combinations.

## Key Takeaways
- Performance exhibits a sharp environment-dependent inversion: RL+RL architectures dominate compact and small-scale networks, achieving 78.5% disruption success in CAGE-4 compared to 18.0% for LLMs, and 81.0% versus 50.5% in the 100-host Cyberwheel network, while pretrained cybersecurity LLM agents achieve 55.0% success against a mere 0.0% for RL in the larger 1010-host escalation-gated network.
- Kill-chain analysis uncovers architecture-specific bottlenecks that explain these inversions; RL agents successfully discover and compromise hosts but stall at privilege escalation in large networks, whereas LLM agents obtain privileged access but rarely convert it into operational impact within compact environments like CAGE-4.
- Conclusions drawn from single-environment evaluations may not generalize, indicating that hybrid planner-executor

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00557v1)
