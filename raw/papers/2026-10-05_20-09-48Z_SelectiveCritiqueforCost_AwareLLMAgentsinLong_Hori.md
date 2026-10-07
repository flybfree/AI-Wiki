---
title: Selective Critique for Cost-Aware LLM Agents in Long-Horizon Decision Making
published: 2026-10-05T20:09:48Z
authors: Heewon Park, Somin Im, Minhae Kwon
url: http://arxiv.org/abs/2610.07335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Selective Critique for Cost-Aware LLM Agents in Long-Horizon Decision Making

## Abstract
Improving the reliability of large language model (LLM) agents in long-horizon decision-making remains a key challenge. When deployed as autonomous agents interacting with complex environments, early mistakes can propagate through trajectories and cause cascading failures. Recent approaches improve reliability by incorporating external critique or deliberation, but invoking these mechanisms at every step substantially increases token consumption and latency, limiting practical deployment. We propose SAG (Self-improving Agent with Gated critique), a cost-aware framework that formulates critique invocation as a step-wise decision problem during long-horizon interaction. SAG introduces a lightweight, training-free gating mechanism that estimates the utility of critique using action-level ambiguity signals--global entropy and local top-2 margin--computed over admissible actions. From a decision-theoretic perspective, this mechanism approximates the Value of Information (VoI) of critique, enabling the agent to selectively allocate expensive feedback only when its expected benefit justifies the cost. SAG further incorporates online bootstrapped self-improvement, allowing the actor to internalize critic-assisted behaviors and progressively reduce reliance on critique. Across three long-horizon interactive benchmarks and multiple backbone models, SAG substantially improves the performance-cost trade-off compared with both no-critique and always-on critique agents. On ALFWorld, SAG increases task success from 24.6% to 78.4% while maintaining a token budget comparable to ReAct, yielding a $3.1\times$ improvement in normalized token efficiency. Moreover, a 7B actor with a lightweight 3B critic achieves performance comparable to a 14B actor without critique, showing that selective critique can recover most of the reliability benefits of deliberation while dramatically reducing inference cost.

## Metadata
- **Published**: 2026-10-05T20:09:48Z
- **Authors**: Heewon Park, Somin Im, Minhae Kwon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07335v1)