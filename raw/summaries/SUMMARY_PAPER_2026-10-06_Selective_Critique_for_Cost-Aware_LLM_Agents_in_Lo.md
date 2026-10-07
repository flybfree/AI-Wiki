---
title: Selective Critique for Cost-Aware LLM Agents in Long-Horizon Decision Making
url: http://arxiv.org/abs/2610.07335v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_20-09-48Z_SelectiveCritiqueforCost_AwareLLMAgentsinLong_Hori.md
generated_at: 2026-10-06 21:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SAG, a cost-aware framework for improving the reliability of large language model agents in long-horizon decision-making tasks. Instead of applying critique at every step, SAG selectively invokes critique only when its expected benefit justifies the additional token and latency cost. The method combines a lightweight gating mechanism with online self-improvement, yielding substantially better performance-cost trade-offs than no-critique or always-on critique agents.

## Key Takeaways
- SAG treats critique invocation as a step-wise decision problem during long-horizon interaction, using a lightweight, training-free gating mechanism to estimate when critique is likely to be useful. The mechanism relies on action-level ambiguity signals, specifically global entropy and local top-2 margin over admissible actions, and approximates the Value of Information of critique from a decision-theoretic perspective.
- The framework incorporates online bootstrapped self-improvement, allowing the actor model to internalize behaviors learned from critic-assisted feedback. This reduces the agent’s long-term dependence on expensive external critique, making the system more efficient as it interacts with the environment over time.
- Empirically, SAG improves the performance-cost trade-off across long-horizon interactive benchmarks. On ALFWorld, it increases task success from 24.6% to 78.4% while maintaining a token budget comparable to ReAct, achieving a 3.1x improvement in normalized token efficiency. A 7B actor paired with a lightweight 3B critic can match the performance of a 14B actor without critique, showing that selective critique can recover much of the reliability benefit of deliberation at lower inference cost.

## Context
Long-horizon LLM agents are vulnerable to early errors that propagate through multi-step trajectories, causing cascading failures in complex environments. Existing methods often improve reliability by adding external critique or deliberation, but applying these mechanisms at every step can be prohibitively expensive in tokens and latency. This paper matters because it addresses the practical tension between reliability and efficiency in autonomous agent deployment.

## Implications
For practitioners, SAG suggests that smaller models can be made substantially more reliable by selectively invoking critique only when uncertainty indicates high expected value. This is especially relevant for real-world agent systems where inference cost, latency, and token budgets constrain deployment. More broadly, the work points toward cost-aware deliberation as a practical design principle for LLM agents in robotics, tool use, planning, and other sequential decision-making settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07335v1)
