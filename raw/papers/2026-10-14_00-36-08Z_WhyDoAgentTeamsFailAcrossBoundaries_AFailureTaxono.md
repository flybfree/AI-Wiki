---
title: Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States
published: 2026-10-14T00:36:08Z
authors: Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke, Vaidehi Patil, Jiayu Wang, Srijan Bansal, Trong Huy Nguyen, Dingfeng Jiang, Dongqi Liu, Ruochen Zhao, Wei Lu, Giuseppe Carenini, Mohit Bansal, Shafiq Joty
url: http://arxiv.org/abs/2610.19342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States

## Abstract
Agents are increasingly interacting with other agents that act for different principals -- people or organizations on whose behalf they work -- e.g., a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-agent system failure studies assume only one orchestrator, shared workspace, or principal. We ask how A2A systems fail when these assumptions are removed. We study more than 2,500 recorded runs of A2A systems built from different agent harnesses and models, spanning 488 scenarios across eight families (legal, CRM, security, commerce, etc.). From these traces, we derive $A^2$-Failures, a taxonomy of 20 A2A failure modes in four categories: (i) discovery and delegation, (ii) grounding and record consistency, (iii) verification, and (iv) conduct and fidelity. Three observations hold across the harnesses, models, and scenarios studied: (1) Agents match tasks to peer names mentioned in the prompt rather than actively searching for available peers; (2) Agents never fact-check each other unprompted; (3) Scoring only the final output rewards the lead agent while hiding internal coordination, verification, and behavioral breakdowns. Our study makes a case for comprehensive evaluations where agents are scored individually against their own objectives in addition to task outcome. We release the run logs behind the taxonomy at https://huggingface.co/datasets/a2a-salesforce/a2-failures.

## Metadata
- **Published**: 2026-10-14T00:36:08Z
- **Authors**: Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke, Vaidehi Patil, Jiayu Wang, Srijan Bansal, Trong Huy Nguyen, Dingfeng Jiang, Dongqi Liu, Ruochen Zhao, Wei Lu, Giuseppe Carenini, Mohit Bansal, Shafiq Joty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19342v1)