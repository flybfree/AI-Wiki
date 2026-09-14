---
title: Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents
published: 2026-09-10T00:10:51Z
authors: Hazel Mak, Susheel Suresh, Sahil Bhatnagar, Barry Wang, Chhaya Methani, Alejandro Gutierrez Munoz
url: http://arxiv.org/abs/2609.11999v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents

## Abstract
In this study, we examine whether a general shell can outperform specialized tools on enterprise tasks. Shell-based agents have shown strong results in coding, but enterprise work also involves moving between applications and services, coordinating with coworkers, and performing professional analysis. We compare five tool interfaces on TheAgentCompany and APEX-Agents using Opus-4.8 and GPT-5.5: typed tools, typed tools plus bash, bash alone, bash with persistent agent-synthesized tools, and programmatic tool calling (PTC), which runs programs whose actions are restricted to a typed tool catalog. Bash alone outperforms typed tools on both benchmarks, improving score by 21.8-24.5 pp on TheAgentCompany and 4.8-7.4 pp on APEX-Agents while using 19-72% fewer total tokens. Adding typed tools or persistent tool synthesis to bash produces no detectable pooled score gain. PTC uses fewer tokens than direct typed calls with broadly similar task performance, but generally underperforms bash alone in both quality and cost efficiency. For enterprise practitioners, these results favor bash alone when arbitrary execution can be isolated and PTC when security or compliance policies require a fixed tool catalog.

## Metadata
- **Published**: 2026-09-10T00:10:51Z
- **Authors**: Hazel Mak, Susheel Suresh, Sahil Bhatnagar, Barry Wang, Chhaya Methani, Alejandro Gutierrez Munoz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11999v1)