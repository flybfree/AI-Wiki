---
title: Building AI That Works: ESnet's Pragmatic Approach to AI-Driven Operational Excellence
published: 2026-07-24T23:20:59Z
authors: Bin Dong, Sukhada Gholba, Brooklin Gore, Shawn Kwang, David Mitchell, Samuel Oehlert, Garrett Stewart, Brendan White, Luke Baker, Ed Balas, Britt Gathright, Chin Guok, Jon-Paul Heron, John MacAuley, Scott Richmond, Chris Robb, Chris Tracy, Kesheng Wu
url: http://arxiv.org/abs/2607.22948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Building AI That Works: ESnet's Pragmatic Approach to AI-Driven Operational Excellence

## Abstract
The ORBIT (Operations Responses and Business Intelligence Toolkit) project was initiated to assess agentic AI for the upcoming ESnet 7 initiative and to address persistent operational pain points in the Network Operations Center (NOC) workflow. ESnet operators experience slow retrieval from siloed data sources, incidents described in lengthy and difficult-to-parse tickets, and context loss across shift handoffs. These challenges increase cognitive load and prolong incident resolution times. ORBIT therefore targets routine automation, cross-source synthesis, and actionable insights delivered directly within operators' existing tooling.   ORBIT is an agentic AI system integrated into ServiceNow, ESnet's primary incident management platform. The design uses a modular, layered architecture comprising a centralized reasoning hub, tool access via MCPs for ESnet data sources, a semantic search layer, and an operator-facing chat interface. To manage the complexity and stochasticity of the AI toolchain, ORBIT follows industry best practices by structuring task logic as versioned, tested "skills" that guide the system in performing bounded responsibilities. This improves reliability and predictability compared to fully unconstrained agent behavior.   Key results show that ORBIT successfully delivered all six initial tasks, and the architecture enabled rapid development of two additional tasks proposed by NOC engineers. We observed strong organic adoption of general-purpose infrastructure components, especially the chat interface and LiteLLM model gateway, including high request volumes from outside the project. Experiments with skills indicate that this approach can reduce task completion steps while eliminating observed error modes.

## Metadata
- **Published**: 2026-07-24T23:20:59Z
- **Authors**: Bin Dong, Sukhada Gholba, Brooklin Gore, Shawn Kwang, David Mitchell, Samuel Oehlert, Garrett Stewart, Brendan White, Luke Baker, Ed Balas, Britt Gathright, Chin Guok, Jon-Paul Heron, John MacAuley, Scott Richmond, Chris Robb, Chris Tracy, Kesheng Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22948v1)