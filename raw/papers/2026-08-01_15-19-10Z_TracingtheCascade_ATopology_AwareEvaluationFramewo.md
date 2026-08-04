---
title: Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations
published: 2026-08-01T15:19:10Z
authors: Xinshun Feng, Ziqi Miao, Lijun Li, Jing Shao
url: http://arxiv.org/abs/2608.00711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations

## Abstract
Large language model (LLM) agents are increasingly deployed in scientific research, where reliability is critical and the underlying knowledge is densely interconnected. In such settings, hallucinations are particularly damaging: a single erroneous claim on a foundational concept can propagate through multi-step reasoning and corrupt entire trajectories. Existing hallucination benchmarks largely operate at the surface level, treating facts in isolation and relying on uniform accuracy metrics that ignore this topological structure. We address this gap with SCHEMA, the first evidence-grounded, topology-aware evaluation framework for hallucinations in scientific agents. SCHEMA automatically constructs scientific concept graphs from benchmark seeds and literature evidence, synthesizes graph-grounded tasks spanning claim verification, multi-hop reasoning, open-ended explanation, and experimental code generation, and evaluates agents with two complementary diagnostics. A trajectory hallucination pipeline audits intermediate reasoning at scale via a topology-weighted severity score, while a multi-agent counterfactual attribution module pinpoints the causal mechanism behind selected failures. SCHEMA reveals that hallucinations concentrate at a small set of highly connected knowledge hubs, and that final-answer accuracy decouples from trajectory honesty; models often reach correct conclusions through structurally flawed reasoning. These results indicate that for high-stakes scientific applications, terminal accuracy alone is an insufficient signal of agent reliability, motivating mechanism-level evaluation grounded in knowledge topology. Code is available at https://github.com/circles-post/SCHEMA.

## Metadata
- **Published**: 2026-08-01T15:19:10Z
- **Authors**: Xinshun Feng, Ziqi Miao, Lijun Li, Jing Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00711v1)