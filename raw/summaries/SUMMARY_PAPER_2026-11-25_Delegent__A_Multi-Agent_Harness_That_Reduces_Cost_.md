---
title: Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance
url: http://arxiv.org/abs/2611.33098v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_18-34-40Z_Delegent_AMulti_AgentHarnessThatReducesCostwithout.md
generated_at: 2026-11-25 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Delegent is a multi-agent harness built on Claude Code that reduces the operational cost of frontier language model agents by delegating routine subtasks—such as code investigation, test execution, and corpus searching—to a small language model (SLM) running on locally available hardware. The paper demonstrates that a 27B FP8 SLM can cut frontier-model costs for long-horizon coding by 67% and agentic search by 59% with no measurable loss in task performance, while even a 2B SLM fitting on a laptop achieves a 66% coding cost reduction.

## Key Takeaways
- Delegent fundamentally differs from existing model-routing and cascade approaches: rather than selecting a single model to handle an entire task, the frontier model retains full orchestration authority and only hands off narrowly scoped, low-difficulty subtasks to an SLM subagent. This preserves the frontier model's strategic reasoning while offloading mechanical "legwork" such as file inspection, running unit tests, or searching a document corpus.
- The system requires no trained router or fine-tuned model, meaning either the frontier model or the SLM can be swapped freely at deployment time. This plug-and-play design makes the approach immediately applicable without additional training infrastructure, and the savings scale proportionally with the volume of routine subtasks the frontier model would otherwise handle itself.
- A carefully crafted short instruction that explicitly reserves core coding decisions for the frontier model accounts for most of the cost savings and prevents the 2B SLM from degrading task outcomes, showing that prompt-level guidance is sufficient to maintain quality boundaries between the two model tiers.

## Context
This work sits at the intersection of agentic AI systems and efficient inference, addressing a practical bottleneck as frontier-model agents become standard tooling for software engineering and information retrieval. Prior efficiency strategies like model cascades or learned routers operate at the task-selection level, which can compromise coherence in multi-step workflows. Delegent instead proposes a subtask-level delegation architecture that keeps the high-capability model as the persistent orchestrator, a design choice that aligns with how real engineering workflows naturally separate high-level planning from repetitive execution steps.

## Implications
For practitioners and enterprises deploying coding agents or agentic search pipelines, Delegent offers a path to dramatically lower API costs without purchasing additional frontier-model capacity, since the SLM can run on hardware already available in most development environments. For the broader field, the paper validates that subtask-level delegation guided by simple instructions can match the performance of full frontier-model execution, suggesting that future agent frameworks should architect around heterogeneous model teams rather than monolithic single-model pipelines. The open-source code release further lowers the barrier for teams to adopt this pattern in production tooling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33098v1)
