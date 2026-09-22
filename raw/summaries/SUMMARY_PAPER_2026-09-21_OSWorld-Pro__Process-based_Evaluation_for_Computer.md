---
title: OSWorld-Pro: Process-based Evaluation for Computer Use Agents
url: http://arxiv.org/abs/2609.24890v1
type: paper-summary
date: 2026-09-21
source_paper: 2026-09-21_16-55-24Z_OSWorld_Pro_Process_basedEvaluationforComputerUseA.md
generated_at: 2026-09-21 22:25
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces OSWorld-Pro, a framework designed to evaluate Computer Use Agents (CUAs) by focusing on the intermediate steps of a task rather than just the final output. By utilizing over 300 tasks and 67,000 human annotations, the authors provide a granular view of agent progress through a series of subgoals. Their findings show that OSWorld-Pro is significantly more challenging for state-of-the-art models like Claude Opus 5 than previous benchmarks, highlighting specific failure modes in complex UI interactions.

## Key Takeaways
- Current evaluation methods for Computer Use Agents are often limited to final deliverables, which obscures the specific reasons why an agent failed during a long sequence of actions.
- OSWorld-Pro introduces over 300 tasks containing more than 2800 subgoals, allowing for "procedural evaluation" that tracks progress through sequentially dependent steps.
- The framework utilizes robust human-aligned LLM-Judges to assess subgoal fulfillment, providing a much higher resolution of data regarding model performance and intermediate reasoning.
- Empirical results indicate that OSWorld-Pro is harder than the original OSWorld benchmark, and it helps identify specific issues such as subgoal-irrelevant actions or precise click-based mistakes in graphical user interfaces.

## Context
As AI agents move toward performing complex, real-world tasks on computers, the research community needs more sophisticated metrics to measure reliability beyond simple success rates. This paper addresses a critical gap by providing a way to diagnose "why" an agent fails, which is essential for moving from experimental prototypes to dependable production tools in fields like software automation and administrative assistance.

## Implications
For researchers and practitioners, OSWorld-Pro provides a roadmap for more targeted model improvements by identifying specific failure modes, such as keyboard input errors versus UI interaction mistakes. This shift toward process-based evaluation will likely lead to the development of more robust, interpretable AI agents that can be debugged and refined with much higher precision than current methods allow.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.24890v1)
