---
title: COPEX: Benchmarking LLM Robustness to Adversarial Context Across Model Context Protocol Layers
published: 2026-10-03T08:44:20Z
authors: Nahom Birhan, Mehrdad Rostamzadeh, Sidhant Narula, Mahmoud Nazzal, Mohammad Ghasemigol, Daniel Takabi
url: http://arxiv.org/abs/2610.04378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# COPEX: Benchmarking LLM Robustness to Adversarial Context Across Model Context Protocol Layers

## Abstract
Large language models increasingly mediate tool use in Model Context Protocol (MCP) systems, where adversarial influence may enter through user instructions, tool schemas, tool outputs, or protocol messages. Existing benchmarks often evaluate deployed agents, conflating model susceptibility with guardrails, orchestration, and general task capability. We introduce COPEX (COntext Provider EXploitation), a controlled benchmark that isolates the model as an MCP client by fixing the surrounding agent stack and varying only the tool-selecting model. COPEX covers 25 attack types instantiated as 125 scenarios across four entry surfaces: model/agent, client, server/tool, and transport. Across nine models and 3,375 trials, the mean attack success rate is 64.4%, with surface-level means ranging from 58.3% to 71.4%. Some client- and transport-level attacks succeed partly outside the model's observation or control, separating system exposure from model susceptibility. Combined input and context scanning reduces mean attack success by 49.6% on an eight-attack defense subset relative to the undefended setting. The benchmark is available at https://github.com/inspire-center/copex.

## Metadata
- **Published**: 2026-10-03T08:44:20Z
- **Authors**: Nahom Birhan, Mehrdad Rostamzadeh, Sidhant Narula, Mahmoud Nazzal, Mohammad Ghasemigol, Daniel Takabi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04378v1)