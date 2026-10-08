---
title: Agent Plasticity: Measuring Self-Improvement Through Experience
url: http://arxiv.org/abs/2610.08902v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_17-58-57Z_AgentPlasticity_MeasuringSelf_ImprovementThroughEx.md
generated_at: 2026-10-07 21:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "agent plasticity," a metric that quantifies how efficiently an AI agent converts accumulated experience into measurable gains in future held-out performance, moving beyond static capability evaluations. The authors study self-improvement in a controlled setting where agents amortize past interactions into reusable artifacts inherited by subsequent instances, revealing that frontier models exhibit sharply divergent improvement trajectories despite comparable learning opportunities.

## Key Takeaways
- Agent plasticity is defined as the efficiency with which an agent transforms experience into gains on held-out tasks, and the paper measures this at each checkpoint by accounting for learning cost alongside performance on both training and out-of-distribution interactions. This reframes evaluation from "what can the agent do now?" to "how effectively does the agent become better through experience?"
- Across multiple environments, some frontier models achieve substantial and persistent gains while others remain near or below their initial performance, and gains within the training regime often transfer only partially to out-of-distribution conditions. Critically, the agent that ultimately performs best need not be the one that improves most efficiently, meaning endpoint capability and acquisition efficiency are distinct axes of evaluation.
- Tracing failures through the improvement loop reveals distinct bottleneck categories: low-plasticity agents often fail to reuse relevant artifacts, while more plastic agents may still fail despite reusing them, pointing to limitations in artifact quality, generalization, or application. This suggests that self-improvement is a multi-stage process where any single stage can become the limiting factor.

## Context
As AI agents increasingly deploy in dynamic, interactive environments where they can diagnose failures and adapt over time, the field lacks evaluation frameworks that capture learning dynamics rather than snapshot performance. This paper addresses a fundamental gap in agent evaluation by formalizing self-improvement as a measurable, multi-dimensional property, providing a controlled experimental setting that isolates the learning loop from confounding factors. It matters because the next generation of autonomous agents will be judged not just on their initial competence but on their capacity to compound knowledge across episodes.

## Implications
For practitioners building self-improving agent systems, this work provides a diagnostic framework to identify where the improvement pipeline breaks down—whether at artifact generation, artifact reuse, or artifact application—enabling targeted engineering interventions rather than blanket model upgrades. For the broader AI community, the divergence between endpoint capability and acquisition efficiency suggests that model selection for agentic deployments should account for learning trajectory, not just benchmark scores, reshaping how we benchmark and deploy autonomous systems in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08902v1)
