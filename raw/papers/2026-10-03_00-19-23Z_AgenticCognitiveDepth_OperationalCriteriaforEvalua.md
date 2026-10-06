---
title: Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents
published: 2026-10-03T00:19:23Z
authors: Nijesh Upreti, Chris Sypherd, Vaishak Belle
url: http://arxiv.org/abs/2610.04168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents

## Abstract
Agentic large language model (LLM) systems are commonly implemented as an LLM in a loop with Planning, Memory, Tools, and Control Flow. This application-focused view connects agentic LLM research with deployable systems and leaves open how such systems should be evaluated beyond end-to-end task success. Building on this view, we define agentic cognitive depth as a trajectory-level profile across five operational criteria. The profile contains context sensitivity ($C$), temporal continuity ($T$), multimodal coordination ($M$), adaptive interaction ($A$), and metacognitive monitoring ($Mc$). The first four criteria measure how well Control Flow, Memory, Tools, and Planning are used across a trajectory. The fifth measures whether the system monitors and regulates the full run. For each criterion, we give operational proxies and a perturbation procedure, then connect the profile to the agent's world model. We provide the structure needed to extend benchmarks such as GAIA, SWE-bench, WebArena, and TRIP-Bench with per-criterion diagnostics. Symbolic verifiers, structured memory, planner coupling, and tool constraints provide practical ways to build and test these capacities.

## Metadata
- **Published**: 2026-10-03T00:19:23Z
- **Authors**: Nijesh Upreti, Chris Sypherd, Vaishak Belle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04168v1)