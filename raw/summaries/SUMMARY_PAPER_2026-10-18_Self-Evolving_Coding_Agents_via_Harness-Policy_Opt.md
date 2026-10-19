---
title: Self-Evolving Coding Agents via Harness-Policy Optimization
url: http://arxiv.org/abs/2610.22791v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_01-07-52Z_Self_EvolvingCodingAgentsviaHarness_PolicyOptimiza.md
generated_at: 2026-10-18 20:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Self-HPO, a recursive self-improving framework for LLM-based coding agents that jointly optimizes both the harness (the environment interface mediating agent-environment interaction) and the policy model through alternating optimization rounds. The framework uses the evolving policy itself as a harness proposer, enabling targeted improvement of failure modes across iterations. Across three coding benchmarks, Self-HPO improves Qwen3.5-35B-A3B's average resolve rate from 57.8% to 64.8%, with gains generalizing to out-of-distribution settings and exceeding the sum of individually optimized components.

## Key Takeaways
- The core insight is that harness and policy are mutually reinforcing: a harness tuned for one policy checkpoint may fail to target the failure modes of an updated policy, while policy learning is limited to trajectories elicited by a fixed harness. Self-HPO addresses this by alternating an H-step (where the current policy analyzes its own failures and proposes new harness candidates) with a P-step (where the policy is updated through reinforcement learning under the selected harness), creating a closed-loop self-improvement cycle.
- Hard tasks identified during RL training form the next harness search set, ensuring that harness optimization remains targeted to the policy's evolving failure modes rather than static or generic. This recursive targeting mechanism prevents the harness from becoming stale as the policy improves, which is a critical limitation of prior approaches that optimize only one component.
- The joint gain of optimizing both components exceeds the sum of their individual gains, demonstrating a superadditive effect. Additionally, each optimized component retains its gains even when paired with the other's base version, confirming independent value. The framework also improves reliability (Pass@1) and expands the capability frontier (Pass@k), and substituting a stronger external model like Opus 4.8 as the harness proposer yields further performance boosts, suggesting the framework is model-agnostic in its proposer role.

## Context
This work sits at the intersection of agentic AI, reinforcement learning, and automated tool-use optimization. Prior research on coding agents has typically treated the harness (scaffolding, tool interfaces, execution environments) and the policy (the LLM generating actions) as separately tunable components, optimizing one while freezing the other. Self-HPO challenges this decoupling by formalizing their mutual dependence and proposing a principled alternating optimization loop. This is significant because as coding agents scale to more complex software engineering tasks, the interaction between what the agent can do and how the environment presents problems becomes the dominant bottleneck, not raw model capability alone.

## Implications
For practitioners building coding agents, Self-HPO provides a concrete recipe for continuous improvement without requiring manual harness redesign after every model update, reducing engineering overhead in agent deployment pipelines. For the broader field, the finding that joint harness-policy optimization yields superadditive gains suggests that future agent systems should be designed as co-evolving systems rather than fixed pipelines, and that using the agent itself as a meta-optimizer for its own environment is a viable and scalable strategy. The framework's compatibility with stronger external proposers also opens a path toward hierarchical agent systems where specialized models handle meta-level optimization while deployment models handle task execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22791v1)
