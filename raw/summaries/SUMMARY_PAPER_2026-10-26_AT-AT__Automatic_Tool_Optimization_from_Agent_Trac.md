---
title: AT-AT: Automatic Tool Optimization from Agent Traces
url: http://arxiv.org/abs/2610.34679v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_01-18-17Z_AT_AT_AutomaticToolOptimizationfromAgentTraces.md
generated_at: 2026-10-26 23:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AT-AT (Automatic Tool Optimization from Agent Traces) is a novel approach that improves LLM-based agent performance by modifying the shared tool environment rather than the agents themselves. A lightweight coding agent analyzes historical execution trajectories and evaluation results to selectively edit tool descriptions and implementations, achieving higher task completion rates on benchmarks like τ²-bench-verified and demonstrating practical improvements on production MCP servers at a large enterprise.

## Key Takeaways
- AT-AT operates on the environment side of agent-tool interaction, recognizing that a tool's description shapes how an agent calls it and its implementation determines the results and errors the agent receives. This is critical because many tools such as APIs and MCP servers are shared across many agents and maintained by providers who cannot modify those agents, making tool-side optimization the only viable improvement path for those providers.
- On τ²-bench-verified, AT-AT achieves the highest task completion rates in the Airline and Telecom domains at lower cost than strong prompt- and tool-optimizer baselines, with the Telecom gain confirmed as statistically significant under paired permutation tests. Additionally, optimizing tools within a coding agent harness improves held-out performance on TerminalBench-2 and TBLite, demonstrating generalization beyond the training traces.
- When deployed on three production MCP servers at a large enterprise, AT-AT lowered cost or tool error rates on every server and increased held-out task passes on one, providing real-world validation that offline optimization from accumulated execution traces can yield tangible operational improvements without requiring changes to the agents or their prompts.

## Context
The broader AI agent landscape has predominantly focused on improving agents through prompt engineering, fine-tuning, or architectural changes, while largely neglecting the tool environments through which agents interact with the world. This paper matters because it reframes agent improvement as an environment-side learning problem, which is especially relevant given the rapid proliferation of MCP servers and shared API toolsets that serve thousands of agents simultaneously and cannot be individually customized per agent.

## Implications
For industry practitioners and tool providers who maintain shared APIs and MCP servers, AT-AT offers a practical pathway to continual improvement by mining accumulated agent execution traces for actionable edits to tool descriptions and implementations without requiring any changes to downstream agents. This environment-side learning paradigm could reduce operational costs, lower tool error rates, and improve task success across enterprise deployments, effectively enabling a form of automated maintenance and optimization for the tool ecosystems that underpin modern agentic AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34679v1)
