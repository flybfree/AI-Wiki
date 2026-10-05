---
title: Harness-Aware Distillation for Small Language Model Agents
url: http://arxiv.org/abs/2610.02858v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_05-53-26Z_Harness_AwareDistillationforSmallLanguageModelAgen.md
generated_at: 2026-10-04 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Harness-Aware Distillation (HAD), a method for distilling large language model agents into smaller ones while accounting for the software harness that manages context, tools, and feedback in agent deployments. Rather than imitating the teacher's full outputs as standard distillation does, HAD isolates and transfers only the teacher-specific reasoning abilities that the harness cannot supply, such as correctly interpreting harness-provided information. The method outperforms on-policy distillation baselines across multiple long-horizon agent benchmarks without requiring task rewards, success labels, or future information.

## Key Takeaways
- HAD introduces an action preference mechanism that contrasts the same teacher's actions generated with and without access to harness information, scored after the student's own reasoning. This contrast reveals what the teacher genuinely adds beyond what the harness already provides, giving the student information that simple imitation of teacher outputs cannot supply.
- A validity check component filters out preference pairs where the preferred action contradicts the harness records, ensuring that the student learns only from consistent and actionable supervision signals rather than from noisy or contradictory training pairs.
- The method requires no task rewards, success labels, or future information, making it a purely self-supervised distillation approach. Empirical analysis shows that HAD-trained students enter fewer unproductive loops and recover from errors more frequently than baselines, suggesting the student adaptively encodes learnable feedback in its weights while delegating state information to the harness.

## Context
Distilling large language model agents into smaller, deployable models is a critical challenge for making agentic AI systems practical and cost-effective. Existing distillation methods treat the entire agent output as the target, conflating the contributions of the model itself with those of the surrounding software infrastructure. This paper addresses a gap in the literature by formally separating the harness's role from the model's reasoning, which matters because real-world agent deployments always include tool-use frameworks, context managers, and feedback loops that are not part of the model weights.

## Implications
For practitioners deploying agent systems at scale, HAD offers a distillation recipe that preserves the reasoning capabilities a small model truly needs while avoiding the waste of learning behaviors already handled by the harness. This could reduce training costs and improve reliability of small agent models in production environments. For the broader field, the work signals that future distillation research for agentic systems must explicitly model the boundary between learned behavior and infrastructure-provided behavior, potentially reshaping how model compression pipelines are designed for tool-using AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02858v1)
