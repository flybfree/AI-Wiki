---
title: Sentry: Learning to Recover from LLM Agent Failures at Test Time
url: http://arxiv.org/abs/2610.02994v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_08-26-47Z_Sentry_LearningtoRecoverfromLLMAgentFailuresatTest.md
generated_at: 2026-10-04 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Sentry, a failure-management layer that runs alongside LLM agents to help them recover from mid-task failures such as invalid tool calls, repeated actions, or poorly grounded reasoning. The authors demonstrate that the delivery mechanism of failure knowledge—how and when it reaches the agent—is as critical as the content itself, and that conditionally exposing failure lessons only when a matching failure is detected yields substantially better performance than either keeping lessons in the agent's context or applying runtime interventions that do not learn from their repairs.

## Key Takeaways
- Failure knowledge is conditional knowledge: when failure lessons are kept in the agent's context, they misfire when the corresponding failure is absent, and removing them from an evolving playbook actually improves performance. This finding challenges the common assumption that more accumulated context always helps an agent.
- Sentry operates as a sidecar layer that detects failures, retrieves matching lessons from an external playbook to guide recovery, verifies recovery without access to task rewards, and stores a new lesson only if the agent successfully recovered. The full playbook never enters the agent's context, preventing the misfire problem.
- Across multiple agentic benchmarks, Sentry outperforms the strongest runtime-intervention baseline by 37% on average and the strongest context-evolution baseline by 39% on benchmarks where both are evaluated. Combining Sentry with context evolution yields further gains, and learned lessons transfer to held-out tasks, demonstrating generalization beyond the tasks on which they were acquired.

## Context
LLM agents deployed in tool-use, coding, and multi-step reasoning tasks frequently encounter mid-task failures that current systems handle poorly. Existing approaches either inject accumulated failure knowledge into the agent's prompt context or apply runtime patches that fix errors without retaining any learning signal. This paper sits at the intersection of agent reliability research, retrieval-augmented systems, and test-time adaptation, addressing a gap in how failure knowledge is structured and delivered rather than merely what it contains.

## Implications
For practitioners building agentic systems in production, Sentry offers a modular, reward-free recovery mechanism that can be layered onto existing agent architectures without modifying the core model or its prompt, making it broadly deployable. The finding that full-context exposure of failure lessons degrades performance even when relevant lessons remain available on demand has direct design implications for any system that accumulates experience or memory for agents, suggesting that selective, condition-triggered retrieval should replace ever-growing context windows. For the broader field, the work establishes a principled framework for treating failure knowledge as conditional and argues that test-time learning systems must respect the conditions under which their knowledge is useful.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02994v1)
