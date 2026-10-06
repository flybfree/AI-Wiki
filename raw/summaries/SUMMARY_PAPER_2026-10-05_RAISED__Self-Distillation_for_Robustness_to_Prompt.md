---
title: RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents
url: http://arxiv.org/abs/2610.06401v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_14-21-30Z_RAISED_Self_DistillationforRobustnesstoPromptInjec.md
generated_at: 2026-10-05 22:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RAISED (Robust Attack Invariance through Self-Distillation), a training framework designed to make tool-using language-model agents robust against indirect prompt injection attacks without sacrificing general capabilities. The authors demonstrate that existing training-time defenses cause substantial drift in model output distributions, leading to utility degradation, and propose a self-generation and self-distillation approach that preserves both robustness and performance on agentic and general-purpose benchmarks.

## Key Takeaways
- Training-based defenses against prompt injection induce substantial drift in the model's output distribution, altering behavior even in benign settings. This drift provides a mechanistic explanation for why prior defenses degrade general capabilities, revealing that the problem is not merely about attack resistance but about preserving the model's natural behavioral distribution across all contexts.
- A critical failure mode of existing defenses is identified: on benign tool-use tasks, the model refrains from completing a necessary step when that step is indicated by a tool output. This means the very mechanism that makes agents useful—acting on external tool guidance—becomes a vulnerability that defenses inadvertently suppress, undermining legitimate task completion.
- RAISED addresses these limitations through a two-stage process: first, the model self-generates tool-use scenarios emphasizing cases where task completion requires acting on legitimate guidance from tool outputs; second, through self-distillation, a student model is trained to match the teacher's clean-context behavior on both clean and injected variants of the same trajectory, thereby learning attack invariance without distorting benign behavior.

## Context
Indirect prompt injection remains one of the most pressing security challenges for deployed LLM agents that interact with external tools, APIs, and user-generated content. As agentic systems become increasingly integrated into production workflows, the tension between security hardening and functional utility has become a central concern in AI safety and reliability research. This paper contributes to the growing body of work on training-time defenses by diagnosing why prior approaches fail mechanistically and proposing a principled alternative grounded in distribution preservation rather than behavioral suppression.

## Implications
For practitioners deploying tool-using agents in production environments, RAISED offers a path toward robustness that does not require accepting degraded agent performance, which is critical for applications in coding assistants, data retrieval pipelines, and autonomous workflows where both security and task completion are non-negotiable. For the broader research community, the identification of output-distribution drift as the root cause of utility loss in training-based defenses provides a diagnostic framework that could inform the design of future robustness methods across diverse model architectures and deployment scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06401v1)
