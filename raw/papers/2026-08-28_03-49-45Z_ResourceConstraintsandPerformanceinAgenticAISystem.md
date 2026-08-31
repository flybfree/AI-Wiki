---
title: Resource Constraints and Performance in Agentic AI Systems
published: 2026-08-28T03:49:45Z
authors: Amaz Salman, Malka Halgamuge, Teo Susnjak
url: http://arxiv.org/abs/2608.27886v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resource Constraints and Performance in Agentic AI Systems

## Abstract
Progress toward more autonomous AI increasingly depends on agentic systems that combine a language model with tools, memory, state management, and multi-step execution. These mechanisms shape both task capability and operational burden. We compare OpenClaw and NanoBot as complete agentic systems using a paired primary benchmark and a more detailed instrumented subset of paired prompts. In the primary benchmark, the rate of full task completion was 31% for OpenClaw and 25% for NanoBot, a six-percentage-point difference with a 95% task-bootstrap interval from -3 to 15 percentage points, providing no statistically established full-completion advantage for either system. In the instrumented layer, both systems achieved 26% full completion, while NanoBot reached at least partial completion on 43% of prompts compared with 26% for OpenClaw. OpenClaw took longer on 83% of prompts and had a higher recorded peak-memory value on every prompt, with geometric mean ratios of 2.98 for wall time and 19.44 for peak memory. Among the ten detailed-layer prompts on which at least one system achieved partial or full completion, NanoBot weakly dominated on eight; across all 23 prompts, however, ten of its eighteen dominance cases were cheaper joint failures. Outcome labels differ across the two evidence layers, showing why agent-system evaluation should connect capability and resource measurements to attempt-level execution and scoring provenance. These findings show that progress toward more autonomous AI should be evaluated through verified task completion, observed resource use and records linking each result to the execution that produced it.

## Metadata
- **Published**: 2026-08-28T03:49:45Z
- **Authors**: Amaz Salman, Malka Halgamuge, Teo Susnjak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27886v1)