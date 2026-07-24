---
title: Towards Agentic Agent-based Models: Feasibility, Performance, and Statistical Model Checking
published: 2026-07-20T13:49:51Z
authors: Stefano Blando, Emanuele Guerrazzi, Riccardo Porcedda, Giuseppe Squillace, Max Tschaikowski, Andrea Vandin
url: http://arxiv.org/abs/2607.17948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Agentic Agent-based Models: Feasibility, Performance, and Statistical Model Checking

## Abstract
Agent-based models (ABMs) rely on simple, explicit and reproducible rules for individual decision making, while complex collective behavior emerges from interactions among agents. Recent advances in large language models (LLMs) make it tempting to replace, enrich, or perturb these rules with LLM-based agentic capabilities. However, this raises a methodological question: how does introducing LLM-driven decisions affect the reliability, computational cost, and behavior of ABM simulations? We investigate this for Mesa ABM models, a popular Python library for ABMs, analyzed by statistical model checking. Building on Mesa's integration with the statistical model checker MultiVeStA, we extend the classical Schelling segregation model with a hybrid population: ordinary agents classify neighbors using the standard symbolic rule, while one agent delegates this task to an LLM through tool calls. The LLM-enabled agent receives natural-language descriptions of neighboring agents and invokes tools that increment counters of similar/different neighbors; these counters determine its happiness according to the original Schelling dynamics. This provides a minimal but controlled setting where the semantic, operational, and computational behavior of LLM-based decisions can be studied inside an otherwise standard ABM. We report preliminary experiments with locally served LLMs of different sizes, showing that smaller models may fail simple semantic classification experiments or become operationally unusable during repeated tool-call generation, while larger tested models pass these preliminary checks. We discuss how statistical model checking can estimate classical ABM observables and quantify the impact of introducing agentic LLM components into simulation models.

## Metadata
- **Published**: 2026-07-20T13:49:51Z
- **Authors**: Stefano Blando, Emanuele Guerrazzi, Riccardo Porcedda, Giuseppe Squillace, Max Tschaikowski, Andrea Vandin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17948v1)