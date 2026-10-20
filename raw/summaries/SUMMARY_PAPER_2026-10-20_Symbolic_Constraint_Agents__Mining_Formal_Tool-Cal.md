---
title: Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors
url: http://arxiv.org/abs/2610.25552v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-18_21-49-20Z_SymbolicConstraintAgents_MiningFormalTool_CallCons.md
generated_at: 2026-10-20 00:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Symbolic Constraint Agents (SCA), a framework that automatically mines formal, programmatic constraints from API documentation and execution traces to verify LLM agents' tool calls at runtime using an SMT solver. Rather than relying on predefined safety policies, SCA discovers tool-dependency constraints from the environment itself, enabling deterministic error detection and, in cases where a valid replacement is uniquely determined, automatic repair of erroneous tool calls. The framework demonstrates substantial improvements in error-detection F1 scores and end-to-end task success across multiple models and benchmarks.

## Key Takeaways
- Symbolic constraints mined from API documentation and refined against execution traces significantly outperform predefined safety policies: error-detection F1 improves from 37.0 to 58.3 on GPT-5.5 traces and from 39.3 to 61.9 on Qwen3.5-27B traces on the AppWorld benchmark, showing that environment-derived constraints capture tool dependencies that hand-written policies miss.
- At runtime, the automatic repair mechanism raises GPT-5.4-mini's task success by 5.4 points under a 40-call budget and by 9.8 points when environment errors are hidden, while eliminating 59–87% of failed calls across models. This demonstrates that deterministic SMT-based checking can catch errors that the LLM itself cannot self-correct, particularly when failures are costly or difficult to diagnose.
- The approach transfers beyond its training environment, achieving gains of up to 5.6 points on the τ²-bench, indicating that mined symbolic constraints generalize across different tool-calling environments and are not overfit to a single API configuration.

## Context
LLM agents increasingly rely on multi-step tool-calling pipelines where errors in one call cascade into downstream failures, making reliability a critical bottleneck for deploying agents in production. Prior work on agent safety has focused on predefined guardrails or heuristic policies, which fail to capture the intricate dependency graphs among tools in complex software environments. SCA addresses this gap by treating constraint discovery as a mining problem over documentation and traces, bridging formal methods (SMT solving) with the empirical reality of agent execution logs.

## Implications
For practitioners building agentic systems, SCA offers a path toward deterministic safety guarantees without hand-authoring dozens of policy rules per tool environment, reducing maintenance burden as APIs evolve. For the broader field, the results suggest that formal verification techniques can be integrated into agent runtimes as a complementary layer to model-level reasoning, particularly in high-stakes domains such as software engineering automation or financial transaction processing where silent tool-call errors are expensive to diagnose and costly to recover from.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25552v1)
