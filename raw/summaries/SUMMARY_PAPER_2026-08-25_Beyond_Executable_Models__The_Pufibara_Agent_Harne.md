---
title: Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling
url: http://arxiv.org/abs/2608.23653v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_11-50-07Z_BeyondExecutableModels_ThePufibaraAgentHarnessandt.md
generated_at: 2026-08-25 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Pufibara, an agent harness designed to maintain persistent engineering state across revisions while associating execution and simulation evidence with the candidate model. Evaluated against Claude Code under two large language models, Pufibara achieves higher task success rates and significantly lower token consumption and runtime for Modelica workflows.

## Key Takeaways
- The harness preserves engineering state between revisions, preventing loss of requirements or reliance on outdated simulation evidence.  
- Submission is treated as an explicit agent action, ensuring clear separation of execution from evaluation.  
- Pufibara reduces logical-token totals by 76.4% to 82.5% and cuts sequential runtime by up to 58.4%, outperforming Claude Code.

## Context
AI agents are increasingly employed for simulation‑driven engineering tasks, yet physical system modeling in languages like Modelica demands correctness beyond mere syntax. This work addresses the challenge of maintaining model integrity across iterative revisions within an agent workflow.

## Implications
The results demonstrate that complete harnesses can vary markedly in task success and resource efficiency even when using matched LLM backends. Practitioners should consider harness design to optimize both accuracy and computational cost for physical system modeling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23653v1)
