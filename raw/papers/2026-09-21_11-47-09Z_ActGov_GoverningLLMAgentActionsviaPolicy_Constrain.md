---
title: ActGov: Governing LLM Agent Actions via Policy-Constrained Validation
published: 2026-09-21T11:47:09Z
authors: Kaiyuan Zhang, Yuke Peng, Ke Jiang, Yinqian Zhang
url: http://arxiv.org/abs/2609.24446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ActGov: Governing LLM Agent Actions via Policy-Constrained Validation

## Abstract
Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM-proposed tool action before it causes external effects. Built on a unified semantic model of authorization, actions, runtime context, and security constraints, the ActGov-Policy component iteratively constructs a policy set from tool specifications, benign tasks, and observed failure traces, with each update verified through SMT-based counterexample checking. At runtime, ActGov-Runtime abstracts each tool call into finite policy records and permits it only if it remains within the task-scoped authorization boundary and satisfies all applicable policies. This per-action enforcement preserves authorization throughout long-horizon, dynamically branching workflows.   We evaluate ActGov on the AgentDojo and AgentDyn benchmarks across multiple models and attack configurations. It shows that ActGov consistently reduces the success rate of indirect prompt-injection attacks while preserving task utility, significantly outperforming existing defenses. These results demonstrate that ActGov can enforce fine-grained authorization over dynamic agent executions without relying on the underlying LLM to correctly identify malicious instructions.

## Metadata
- **Published**: 2026-09-21T11:47:09Z
- **Authors**: Kaiyuan Zhang, Yuke Peng, Ke Jiang, Yinqian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24446v1)