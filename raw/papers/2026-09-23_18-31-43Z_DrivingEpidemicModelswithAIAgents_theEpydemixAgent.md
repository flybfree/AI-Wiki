---
title: Driving Epidemic Models with AI Agents: the Epydemix Agent Framework
published: 2026-09-23T18:31:43Z
authors: Nicolò Gozzi, Ciro Cattuto, Alessandro Vespignani
url: http://arxiv.org/abs/2609.28692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Driving Epidemic Models with AI Agents: the Epydemix Agent Framework

## Abstract
Artificial Intelligence agents based on large language models provide convenient natural language interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix Agent Framework, an additive layer over Epydemix, an open-source Python library for stochastic compartmental epidemic modeling. The framework extends the library with four capabilities to facilitate interaction with an AI agent: discovery of available models and parameters, preventive validation of a declarative scenario specification, execution through tested library code, and inspectability of results. These capabilities let an agent handle the entire modeling process, from the natural-language description of the scenario to quantitative results, figures, and interpretation of findings without writing custom code. Each step reads input files and saves results in a separate output bundle, making the process auditable and reproducible. First, we show the end-to-end workflow with a case study comparing vaccination strategies for a novel respiratory virus. Second, we assessed the framework across 50 agent sessions and five modeling tasks by comparing the agent use of the framework against the direct use of the Python interface. The framework reduced turns, output tokens, and cost on most tasks, unless it trades resources for per-point reproducibility.

## Metadata
- **Published**: 2026-09-23T18:31:43Z
- **Authors**: Nicolò Gozzi, Ciro Cattuto, Alessandro Vespignani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28692v1)