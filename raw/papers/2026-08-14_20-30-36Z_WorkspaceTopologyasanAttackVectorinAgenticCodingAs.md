---
title: Workspace Topology as an Attack Vector in Agentic Coding Assistants
published: 2026-08-14T20:30:36Z
authors: Alexandre G. R. Day, Pradeep Yadlapalli, Sriram Venkatapathy, Thomas Paniagua, Nick Raines, Sahil Wadhwa, Himanshu Kumar, Andy Luo, Sudeep Panyam, Rikhiya Ghosh, Pranab Mohanty, Giri Iyengar
url: http://arxiv.org/abs/2608.14876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Workspace Topology as an Attack Vector in Agentic Coding Assistants

## Abstract
Agentic coding assistants are finding widespread use, not just in new code development but in quickly ingesting and leveraging third-party code. This opens up a risk of malicious code being ingested as these coding tools operate with broad filesystem access inside developer workspaces. In this paper, we extensively study the impact of different dimensions of a novel attack surface we term workspace topology -- defined via directory depth, codebase modularity, in-file injection position and context framing -- on the attack success rate of adversarial prompt injection attempts.   We perform an empirical study of indirect prompt injection (IPI) across a diverse set of open-source repositories spanning 10 languages and 6 engineering domains, evaluating three IPI entry points against open-weight models operating open source code harnesses.   We find that workspace topology measurably affects IPI success. Specifically, changes in codebase modularity can significantly alter the Attack Success Rate (ASR), with highly modular environments demonstrating significantly lower attack success rates. Furthermore, context framing and introduction of security-cues in the workspace can also alter the ASR. Our findings offer practical value for the evaluation and security testing of coding agents across diverse settings, while underscoring the importance of an uncontaminated testing environment to obtain reliable results and conclusions.

## Metadata
- **Published**: 2026-08-14T20:30:36Z
- **Authors**: Alexandre G. R. Day, Pradeep Yadlapalli, Sriram Venkatapathy, Thomas Paniagua, Nick Raines, Sahil Wadhwa, Himanshu Kumar, Andy Luo, Sudeep Panyam, Rikhiya Ghosh, Pranab Mohanty, Giri Iyengar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14876v1)