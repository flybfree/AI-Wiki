---
title: Distilling Agentic Systems: A Roadmap across Models, Artifacts, and Harnesses
url: http://arxiv.org/abs/2609.36630v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-29_03-38-17Z_DistillingAgenticSystems_ARoadmapacrossModels_Arti.md
generated_at: 2026-09-29 20:46
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces "Agent Distillation," a comprehensive framework for transferring task-solving knowledge from teacher to student agents that transcends traditional parameter-based distillation by accounting for competence distributed across memories, tools, and execution logic. The authors categorize knowledge retention into four distinct substrates—model weights, artifacts, harnesses, and cross-substrate transfers—and propose an evaluation framework that links these mechanisms to causal contribution and deployed utility. Together, these contributions establish a structured foundation for the reliable, maintainable, and safe development of increasingly complex agentic systems.

## Key Takeaways
- Conventional knowledge distillation is limited because it assumes student models merely imitate teacher parameters, whereas Agent Distillation addresses the persistent transfer of task-solving knowledge that resides in non-parameter elements like external memories, tool usage patterns, and execution logic essential for modern agent competence.
- The study organizes the field by identifying where transferred knowledge is retained across four dimensions: within the model, as artifacts, through the execution harness, or across substrates, which clarifies how knowledge moves between components and effectively separates transfer evidence from its ultimate outcome.
- An evaluation framework is developed to relate retention mechanisms to their causal contribution and deployed utility, providing a rigorous methodology to assess distillation

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36630v1)
