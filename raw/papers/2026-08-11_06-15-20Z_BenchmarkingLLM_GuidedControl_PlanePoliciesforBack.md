---
title: Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy
published: 2026-08-11T06:15:20Z
authors: Aman Chauhan, Vishnu Pendyala
url: http://arxiv.org/abs/2608.10532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy

## Abstract
Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes. We ask whether a Large Language Model can replace the static routing policy itself, reading HAProxy and Prometheus telemetry every 10 seconds and isolating faulty servers through guardrailed calls to the HAProxy Data Plane API. On a reproducible benchmark with a persistent structural fault built into roughly one-third of a heterogeneous fleet, we sweep 15 open-weight models across five families (0.35B to 35B total parameters; dense, mixture-of-experts, and efficient-sparse architectures), reasoning modes, fleet scales of 3 to 9 backends, and two routing algorithms, totaling 240 runs. We find a capability threshold near 3B active parameters. Below it, LLM policies are typically unreliable and sometimes worse than no policy; above it, every model, regardless of architecture, saturates near an 88% reduction in client-perceived 5xx errors over the static baseline. The threshold is approximate: Gemma 4 E2B clears it with 2B active parameters, while the dense 3B Granite 4.0 Micro does not. The availability gain has costs. Draining concentrates load onto surviving servers, inflating tail latency 2.6 to 2.8 times, and enabling reasoning multiplies token spend roughly tenfold, overrunning the control interval and degrading effectiveness. The efficient operating point is a supra-threshold model in its cheapest non-reasoning mode, wrapped inside deterministic guardrails.

## Metadata
- **Published**: 2026-08-11T06:15:20Z
- **Authors**: Aman Chauhan, Vishnu Pendyala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10532v1)