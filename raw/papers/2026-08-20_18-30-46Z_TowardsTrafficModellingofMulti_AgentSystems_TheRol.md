---
title: Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology
published: 2026-08-20T18:30:46Z
authors: Davide Lamagna, Albert Cabellos, Alberto Rodriguez-Natal, Gábor Rétvári, Berta Serracanta
url: http://arxiv.org/abs/2608.20494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology

## Abstract
Multi-agent LLM systems are an emerging networked workload whose rapid deployment raises questions about the traffic patterns they generate. Compared to conventional applications, these systems generate requests internally: a single user task can induce a structured sequence of model calls whose timing is governed by coordination logic rather than by user arrival rate. It is not clear whether classical traffic models, designed for human-driven workloads, apply to this setting.   We present an empirical characterisation of LLM-call interarrival time distributions across sequential, star, and full-mesh agentic coordination topologies, using a multi-layer measurement framework over 500 repeated runs per topology. We find that topology fundamentally shapes the arrival process of requests to the LLM backend: fan-out coordination introduces a structural bimodality absent in sequential execution, and the reasoningphase component is best described by a log-normal distribution, with the Poisson exponential null model decisively rejected across all topologies. These differences propagate to inference and network level metrics. The framework and analysis pipeline are released openly at https://github.com/dlamagna/agentraffic.

## Metadata
- **Published**: 2026-08-20T18:30:46Z
- **Authors**: Davide Lamagna, Albert Cabellos, Alberto Rodriguez-Natal, Gábor Rétvári, Berta Serracanta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20494v1)