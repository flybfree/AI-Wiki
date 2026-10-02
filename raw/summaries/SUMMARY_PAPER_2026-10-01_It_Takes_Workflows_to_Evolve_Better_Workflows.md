---
title: It Takes Workflows to Evolve Better Workflows
url: http://arxiv.org/abs/2610.01026v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_04-15-49Z_ItTakesWorkflowstoEvolveBetterWorkflows.md
generated_at: 2026-10-01 21:23
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces FloWright, a method to optimize multi-agent workflows by enabling both workflow generators and execution agents to co-evolve through a hierarchical, structure-aware reward paradigm. Unlike prior approaches that only train the generator while keeping other agents fixed, FloWright addresses the coupling challenge of sparse outcomes without requiring additional models or labels. Experiments show that small open models trained with this approach achieve significant performance gains across diverse domains, with co-evolving multiple roles yielding better results than optimizing a single role alone.

## Key Takeaways
- FloWright utilizes the workflow as a harness to optimize performance by introducing a hierarchical, structure-aware reward system that allows for self-evolution of individual roles and co-evolution of two or more roles simultaneously, eliminating the need for extra models, labels, or additional executions.
- To address the limitation where workflows are often trained on data too simple for single agents, the authors propose DataWright, an adaptive data hardening technique that transforms existing datasets into more challenging workflow-level tasks to improve robustness and generalization.
- Evaluations across document, slide, chart, code, math, and finance tasks demonstrate that small open models trained with FloWright improve performance by up to +7.41%, with co-evolving multiple roles providing a +5.03% gain compared to +2.83% when optimizing just one role, highlighting the benefit of joint optimization.

## Context
Multi-agent workflows are increasingly essential for complex real-world tasks that exceed the capabilities of single large language models, yet current training methods often fail to optimize all components involved in workflow execution. This research addresses a critical gap in agent coordination by tackling the coupled nature of agents and the difficulty of attributing sparse rewards, moving beyond generator-only optimization toward holistic workflow improvement.

## Implications
This work enables practitioners to significantly boost the performance of small open-source models in multi-agent settings without incurring the costs of additional model training or extensive labeling efforts. By demonstrating that co-evolution yields superior results and introducing adaptive data hardening, FloWright provides a scalable framework for developing robust workflow systems capable of handling increasingly difficult tasks across various industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01026v1)
