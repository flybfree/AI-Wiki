---
title: Twin Agent: Context Residual Compression for Privilege Separated Agents
published: 2026-07-21T21:47:52Z
authors: Zhanhao Hu, Dennis Jacob, Xiao Huang, Zhaorun Chen, Bo Li, David Wagner
url: http://arxiv.org/abs/2607.19595v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Twin Agent: Context Residual Compression for Privilege Separated Agents

## Abstract
Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use. Existing secure-by-design approaches mitigate this risk by separating untrusted observations from privileged execution and careful control of information flow, but often degrade utility and require extensive task-specific engineering. We thus propose Twin Agent, a general privilege separation design pattern inspired by residual coding in the agent context. Twin Agent consists of two nearly symmetric agents: an Explore Agent that inspects untrusted information and a Safe Agent that executes privileged actions. The Explore Agent is conditioned on the Safe Agent's current context and communicates only compact hints to the Safe Agent about the next action to take. This design reduces the information needed to preserve task utility and thus achieves a better security--utility tradeoff, which we empirically verify by measuring how utility and attack success change as the length of hints varies. We evaluate Twin Agent on long-horizon software engineering tasks with SWE-bench Lite and on heterogeneous multi-tool interaction tasks with AgentDojo and DecodingTrust-Agent. Across both benchmarks, Twin Agent preserves high task utility while preventing prompt injection attacks, outperforming both undefended agents and privilege separation baselines.

## Metadata
- **Published**: 2026-07-21T21:47:52Z
- **Authors**: Zhanhao Hu, Dennis Jacob, Xiao Huang, Zhaorun Chen, Bo Li, David Wagner
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19595v1)