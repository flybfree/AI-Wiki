---
title: Self-Evolving Agents via Likelihood-Guided Tool-Space Optimization
url: http://arxiv.org/abs/2609.34151v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_02-32-05Z_Self_EvolvingAgentsviaLikelihood_GuidedTool_SpaceO.md
generated_at: 2026-09-28 23:05
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces LOTS (Likelihood-Only Tool Scoring), a framework for self-evolving agents that optimizes tool usage by maintaining persistent, task-specific spaces derived from accumulated output experience without altering model parameters. By quantifying each tool's contribution through likelihood changes upon output ablation, LOTS ranks tools to continuously refine agent behavior, resulting in improved performance, reduced context overhead, and the ability to transfer learned configurations across different models.

## Key Takeaways
- Existing methods suffer from output-unaware selection, statelessness across requests, and high inference costs by relying on tool descriptions rather than actual outputs, failing to consolidate prior experience into persistent states, and repeatedly searching for tools instead of amortizing the selection effort over recurring tasks.
- LOTS implements an output-aware scoring mechanism where it estimates a tool's value by measuring how much the generated answer's likelihood drops when that tool's observed output is removed, enabling the system to rank tools and update persistent spaces after each request while keeping model weights fixed.
- Experiments across three benchmarks demonstrate that LOTS enhances task performance while substantially reducing tool context size; additionally, sequential tests show that task-specific spaces persist and improve over time, and cross-model evaluations confirm that optimized configurations transfer effectively between different foundation models.

## Context
As Large Language Models increasingly integrate external tools to execute complex actions, managing the explosion of available functions has become a significant challenge in agent development. Current approaches often overwhelm context windows with irrelevant tool descriptions and struggle to adapt efficiently to recurring tasks, limiting scalability and reliability in dynamic environments where agents must make rapid, informed decisions based on past interactions.

## Implications
This research provides a scalable solution for deploying efficient autonomous agents by enabling lightweight, evolving tool spaces that reduce latency and computational burden without requiring retraining of the base model. The demonstrated transferability of learned configurations suggests a new standard for agent interoperability, allowing practitioners to reuse optimized interaction patterns across diverse models and accelerating the deployment of robust, self-improving systems in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34151v1)
