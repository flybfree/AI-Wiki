---
title: Stateful CARS: Exact Cross-History Reuse for Policy-Constrained LLM Agents
published: 2026-08-08T18:26:25Z
authors: Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan
url: http://arxiv.org/abs/2608.08282v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stateful CARS: Exact Cross-History Reuse for Policy-Constrained LLM Agents

## Abstract
Tool-using language-model agents face constraints whose meaning changes with observations and prior actions. We study exact sampling from the model distribution conditioned on a hard stateful validator while reusing invalidity certificates across histories. Stateful CARS freezes a bank of sound state--continuation schemas within each attempt and removes every trajectory containing a certified continuation at a matching abstract state. An exact residual Doob transform samples from the resulting proposal. We give a checkable future-validity bisimulation condition, prove schema soundness, adaptive exactness, i.i.d.\ outputs, almost-sure termination, monotone acceptance, and compression invariance, and characterize computation by the number of reachable full-history product states. This number can be exponential for a history-dependent language model; the evaluated method therefore makes no generic finite-trie scalability claim. On enumerable workflows, its analytic law matches the valid conditional to $10^{-16}$ at validity probability $6\times10^{-8}$, whereas state-aware local decoding can be $0.97$ away. A matched comparison is negative: observation-keyed official CARS is cheaper in sampler steps (root/Stateful ratio $0.942$ $[0.934,0.951]$), and the Qwen comparison is null ($0.99$ $[0.90,1.08]$). Cross-history transfer helps only in an internal matched-key ablation ($1.27\times$). Thus the evidence supports exact schema-induced conditioning, not a systems advantage over CARS.

## Metadata
- **Published**: 2026-08-08T18:26:25Z
- **Authors**: Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08282v1)