---
title: What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents
url: http://arxiv.org/abs/2610.06406v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_14-25-16Z_WhatDidtheAgentActuallyDo_Evidence_GroundedOversig.md
generated_at: 2026-10-05 22:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the challenge of human oversight over autonomous agents performing long-horizon tasks, where users must monitor vast amounts of agent activity without clear guidance on which decisions require verification. The authors introduce AgentMonBench, a software-engineering benchmark for evaluating monitors that identify consequential decisions and locate supporting evidence, alongside the Evidence-Grounded Behavior Graph (EBG), a training-free method that structures source-linked evidence into interpretable behavior graphs. Experiments across eight models demonstrate that EBG improves both decision identification and evidence localization compared to direct access to raw agent context, with gains persisting across varying input scales and hyperparameter configurations.

## Key Takeaways
- AgentMonBench is a novel software-engineering benchmark comprising three subsets that evaluate two complementary dimensions of oversight: alignment between stated requirements and actual agent behavior, and the ability to identify consequential autonomous decisions that warrant human verification. This benchmark fills a gap in evaluation infrastructure for monitoring systems that must operate over extended agent task horizons rather than single-step interactions.
- The Evidence-Grounded Behavior Graph (EBG) is a training-free structural method that groups source-linked evidence into coherent behavioral units and organizes their interrelationships into a graph structure. Task-oriented views of this graph help monitors interpret agent behavior in context, enabling evidence-grounded judgments without requiring model fine-tuning or additional training data.
- Experimental validation across eight different models shows that EBG consistently improves both decision identification and evidence localization in most settings compared to providing monitors with direct access to the original agent context. Additional experiments confirm that these evidence-localization gains remain robust across different input scales and hyperparameter settings, and real-world application case studies illustrate practical utility for human oversight workflows.

## Context
As large language model agents increasingly handle multi-step, long-horizon tasks in software engineering, research, and enterprise workflows, the human role shifts from making individual decisions to supervising autonomous execution chains. This transition creates a critical gap: existing monitoring and evaluation frameworks are designed for single-turn interactions and do not adequately support the fragmented, voluminous evidence trails produced by extended agent runs. This paper sits at the intersection of agent evaluation, human-in-the-loop safety, and interpretability research, addressing a bottleneck that limits the safe deployment of autonomous agents in production settings.

## Implications
For practitioners deploying long-horizon agents in software engineering pipelines, EBG offers a practical, training-free oversight mechanism that reduces the cognitive burden on human monitors by surfacing only consequential decisions and their supporting evidence rather than overwhelming them with raw activity logs. For the broader AI safety and alignment community, this work highlights that oversight tools must be designed around evidence structure and decision consequence rather than mere activity volume, suggesting that future agent monitoring systems should incorporate graph-based evidence organization as a foundational component. The benchmark also provides a reusable evaluation standard for the growing ecosystem of agent monitoring tools, enabling more rigorous comparison of oversight approaches across different model architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06406v1)
