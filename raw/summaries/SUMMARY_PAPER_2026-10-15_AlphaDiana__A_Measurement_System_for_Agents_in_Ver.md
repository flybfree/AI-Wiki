---
title: AlphaDiana: A Measurement System for Agents in Verifiable Reasoning Tasks
url: http://arxiv.org/abs/2610.20675v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_14-04-48Z_AlphaDiana_AMeasurementSystemforAgentsinVerifiable.md
generated_at: 2026-10-15 22:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AlphaDiana is a modular measurement system designed to evaluate AI agents that combine reasoning models with execution harnesses, enabling researchers to link execution conditions to outcomes, behavior, and resource consumption. The paper's central finding is that harnesses do not consistently improve reasoning accuracy: gains on questions a model cannot solve alone are frequently offset by losses on questions the model already answers correctly without tools. The system supports both macro-level comparisons of complete agents and micro-level interventions on individual components such as tools, skills, and memory under matched experimental conditions.

## Key Takeaways
- Harnesses wrapping reasoning models do not reliably improve task accuracy. The paper demonstrates that while harnesses can help solve questions the base model fails on, they simultaneously degrade performance on questions the model handles correctly without any tool use. This means net accuracy gains are inconsistent and often negative, challenging the common assumption that adding scaffolding always helps.
- Component-level interventions such as skill guidance instructions and retained conversation history do not reliably improve accuracy either. The authors tested these interventions across three open-source models and three open-source harnesses on five answer-based benchmarks and two interactive benchmarks, finding that neither skills nor memory retention produced consistent improvements, suggesting that agent design choices are more nuanced than current practice assumes.
- Token usage and behavioral metrics must be evaluated jointly with correctness. The paper warns that low token entropy can accompany incorrect answers, and that reducing output tokens per execution can paradoxically increase output tokens per correct answer when overall accuracy drops. This means resource efficiency metrics are misleading without simultaneous correctness tracking, and AlphaDiana addresses this by linking answer correctness and execution status to full traces and resource records.

## Context
The rapid proliferation of agent frameworks—combining large language models with tool-calling harnesses, skill libraries, and memory systems—has outpaced the development of rigorous evaluation infrastructure. Most existing benchmarks measure final answers without controlling for how the agent's execution environment, file access policies, or memory retention strategies influence outcomes. AlphaDiana fills this gap by providing a standardized, modular measurement system that separates the evaluation of the reasoning model from the evaluation of the harness and its components, enabling controlled ablation studies. Published by researchers spanning multiple institutions, it represents a methodological contribution to the growing subfield of agent evaluation and reproducibility.

## Implications
For practitioners building agent pipelines, this work serves as a caution against blindly adding tool harnesses, skill instructions, or persistent memory to reasoning models, as these additions can degrade performance on tasks the model already handles well. For the research community, AlphaDiana offers a reproducible framework for diagnosing agent failures under shared task and resource policies, which could inform more principled agent design and help industry teams allocate compute budgets more effectively. The finding that token efficiency metrics are misleading without correctness tracking also has direct implications for cost optimization strategies in production agent deployments, where teams may inadvertently increase total cost per successful task while appearing to reduce per-execution token usage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20675v1)
