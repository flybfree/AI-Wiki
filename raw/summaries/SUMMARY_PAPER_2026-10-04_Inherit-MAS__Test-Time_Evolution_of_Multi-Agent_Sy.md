---
title: Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance
url: http://arxiv.org/abs/2610.02396v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_19-23-32Z_Inherit_MAS_Test_TimeEvolutionofMulti_AgentSystems.md
generated_at: 2026-10-04 21:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Inherit-MAS introduces a test-time evolution framework for multi-agent systems that explicitly models inheritance at both the workflow and execution levels, inspired by biological evolution's interplay of inheritance and selection. The system uses a meta-model to synthesize agent workflows and a judge to diagnose deficiencies, then applies targeted refinements while preserving useful components and avoiding redundant computation through execution inheritance. It outperforms existing evolving-MAS baselines on WorkBench and HotpotQA benchmarks while significantly reducing token usage.

## Key Takeaways
- Workflow inheritance operates by starting from the latest completed candidate workflow, selectively discarding nodes judged unhelpful by a separately prompted judge, and applying only validated edits that address diagnosed deficiencies. This prevents the broad, disruptive revisions that plague earlier test-time evolution methods, preserving useful agent roles, communication inputs, and tool permissions while making targeted improvements.
- Execution inheritance ensures that when a new candidate workflow is executed, previously stored results are reused only when the complete resolved request and full execution context match exactly. This mechanism reduces worker-token usage by 29.1% on WorkBench and 34.6% on HotpotQA, and total token usage by 5.3% and 18.1% respectively, eliminating redundant model and tool calls across refinement rounds.
- Inherit-MAS achieves 55.4% completion on WorkBench and 49.7% joint F1 on HotpotQA FullWiki using GPT-4o-mini workers, surpassing EvoAgent, EvoMAS, and TacoMAS. With Qwen3-32B workers, it also exceeds these evolving-MAS baselines on both benchmarks, demonstrating that the inheritance mechanism generalizes across different model scales.

## Context
Multi-agent systems built from large language models have become a dominant paradigm for tackling complex, multi-step tasks that require coordination among specialized agents. However, designing effective workflows in advance remains a significant challenge, and existing test-time evolution approaches either make overly broad revisions that disturb useful components or re-execute unchanged requests, incurring substantial redundant computation. Inherit-MAS addresses these limitations by drawing on biological evolution principles, making inheritance a first-class mechanism rather than an implicit side effect of iterative refinement.

## Implications
For practitioners deploying multi-agent systems in production, Inherit-MAS offers a practical path toward reducing operational costs through execution inheritance while maintaining or improving task completion quality. The explicit separation of workflow inheritance and execution inheritance provides a modular design that can be adapted to various agent orchestration frameworks, potentially enabling more efficient and reliable autonomous systems in enterprise settings where token budgets and latency constraints are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02396v1)
