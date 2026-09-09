---
title: Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses
published: 2026-09-04T21:35:00Z
authors:  Cen,  Zhao, Haibo Ruan, Wenjie Chen, Pei-fen Tu, Usman Abbasi, Joel Hesch
url: http://arxiv.org/abs/2609.05736v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses

## Abstract
LLM tool agents can be improved without retraining by modifying the runtime harness around a fixed model: prompts, tool interfaces, middleware, state handling, and recovery logic. We study this setting as resource-bounded harness selection for fixed-model multi-turn tool agents, with the search surface scoped to prompts and tool-boundary middleware: edits are guarded intercepts at the tool boundary, not arbitrary rewriting of agent execution logic. Our optimizer-agnostic protocol reports mean held-out lift, worst-condition lift, repeatability, logged cost diagnostics, and RelLift95(B), a conservative estimate of the held-out gain of the harness selected under budget B. We instantiate the protocol with prompt-only and prompt-plus-middleware optimizers, including PRISM, which clusters failures and routes repairs to prompt, tool-boundary middleware, or joint edit surfaces within a Pareto search. On BFCL multi-round, tau2-Retail, and tau2-Telecom, PRISM obtains mean held-out lifts of 14.2, 14.9, and 10.1 percentage points and positive empirical RelLift95 on all three benchmarks, and a component ablation attributes the margin chiefly to failure-surface routing and the edit-pattern constraint. Across optimizers, the results show that some search procedures can occasionally find large gains but still choose brittle updates, so the reliability of the chosen harness should be reported alongside average held-out lift.

## Metadata
- **Published**: 2026-09-04T21:35:00Z
- **Authors**:  Cen,  Zhao, Haibo Ruan, Wenjie Chen, Pei-fen Tu, Usman Abbasi, Joel Hesch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05736v1)