---
title: Ajar: Measuring Open Privilege in Agent Defenses
url: http://arxiv.org/abs/2609.26900v1
type: paper-summary
date: 2026-09-24
source_paper: 2026-09-22_18-01-41Z_Ajar_MeasuringOpenPrivilegeinAgentDefenses.md
generated_at: 2026-09-24 01:18
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces Ajar, a framework designed to measure "open privilege"—the degree to which an agent can perform unnecessary actions—within existing security defenses. It argues that current evaluation methods for agent safety are insufficient because they only focus on attack success and task utility, failing to quantify the actual permissions granted to the model during execution.

## Key Takeaways
- Current benchmarks evaluate defense mechanisms based on a trade-off between preventing successful attacks and maintaining agent utility, but they do not explicitly measure how much "extra" privilege an agent retains that isn't required for the task.
- Ajar addresses this by creating candidate tool calls that are irrelevant to specific tasks and observing whether these actions are permitted at various points in the agent's execution flow across existing benchmarks like AgentDojo.
- The researchers found that open privilege is a distinct metric; two defenses might appear similar in terms of attack prevention and utility but can differ significantly in how much unnecessary access they allow, highlighting a critical gap in current security audits.

## Context
As AI agents are increasingly granted access to private data and external tools, the industry needs more nuanced ways to verify that these systems adhere to the principle of least privilege. This research provides a necessary step toward objective safety standards by moving beyond "pass/fail" attack metrics toward a continuous measurement of permission overhead.

## Implications
For practitioners, Ajar offers a way to audit and refine security layers to ensure they are not just blocking attacks but are also minimizing the agent's ability to perform unnecessary actions. This allows for more precise safety engineering where developers can verify that an agent is granted only the permissions it needs to complete a specific goal, reducing the risk of "over-permissioned" systems in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.26900v1)
