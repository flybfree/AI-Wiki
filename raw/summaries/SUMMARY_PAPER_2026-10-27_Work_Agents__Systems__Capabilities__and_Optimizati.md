---
title: Work Agents: Systems, Capabilities, and Optimization
url: http://arxiv.org/abs/2610.35845v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_17-56-21Z_WorkAgents_Systems_Capabilities_andOptimization.md
generated_at: 2026-10-27 00:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a unified, work-centric framework for understanding how AI agents reliably execute delegated digital tasks by combining foundation models with runtime harnesses operating in stateful workspaces. The authors introduce a two-dimensional characterization system (work persistence and work openness), classify digital work into five distinct forms, identify five core capability families necessary for reliable execution, and systematically examine optimization strategies spanning model-level, harness-level, and joint approaches. The work culminates in a reorientation of evaluation methods toward verifiable work outcomes rather than isolated task performance.

## Key Takeaways
- The paper reframes work agents as integrated systems comprising foundation models and runtime harnesses that operate within stateful workspaces to produce verifiable outcomes, moving beyond the common framing of agents as mere tool-calling pipelines. This system-level perspective is essential because reliability in real-world work execution depends on the interaction between the model's reasoning capabilities and the harness's orchestration, memory management, and environment interaction mechanisms.
- The authors introduce two complementary dimensions—work persistence (the temporal and stateful continuity of a task) and work openness (the degree to which a task interacts with unpredictable, external environments)—and use these to classify digital work into five forms based on task scope and organizational structure. This taxonomy provides a structured way to reason about which agent architectures and optimization strategies suit which categories of real-world work.
- The paper identifies five core capability families required for reliable work execution and maps them onto three optimization pathways: model optimization, harness optimization, and their joint optimization. It further critiques existing evaluation methods by arguing that benchmarks should be assessed from the perspective of actual work outcomes and practical verifiability, rather than abstract task completion rates. Future directions include sustained work delegation over long horizons, adaptation to open and evolving environments, and the feedback loop between executing work and improving underlying capabilities.

## Context
As foundation models transition from generating text and code to autonomously completing multi-step workflows across applications, the AI research community lacks a coherent, unified framework for analyzing what makes an agent reliably deliver finished work. Most existing literature treats agent capabilities, tool use, and evaluation as separate subtopics. This paper fills that gap by providing a single architectural and conceptual lens that connects model training, runtime orchestration, task classification, and outcome-based evaluation into one coherent research program, which is timely given the rapid commercial deployment of agentic systems in enterprise settings.

## Implications
For practitioners building agentic systems, the work persistence and work openness dimensions offer a practical diagnostic tool for selecting appropriate architectures, optimization strategies, and evaluation protocols for specific deployment scenarios. For the broader AI research community, the call to evaluate agents by verifiable work outcomes rather than synthetic benchmark scores could reshape how progress is measured and reported. Industry stakeholders deploying agents in production environments stand to benefit from the structured taxonomy of digital work forms, which can inform product design, risk assessment, and the development of safety and reliability guarantees for autonomous task execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35845v1)
