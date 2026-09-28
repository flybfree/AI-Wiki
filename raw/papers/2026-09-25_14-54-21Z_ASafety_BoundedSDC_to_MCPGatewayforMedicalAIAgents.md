---
title: A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents
published: 2026-09-25T14:54:21Z
authors: Bennet Gerlach, Stefan Fischer
url: http://arxiv.org/abs/2609.31358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents

## Abstract
The Model Context Protocol (MCP) provides a common interface through which AI applications discover and use external resources and tools. It allows language-model agents to ground their reasoning in current system state and interact with heterogeneous services. In medical environments, however, exposing device state and action affordances requires deterministic constraints on possible effects. We present an IEEE 11073 Service-Oriented Device Connectivity (SDC)-to-MCP gateway that exposes metrics, alarms, context references, and semantic metadata as read-only resources, while representing selected action affordances as policy-validated dry-run tools. The term safety-bounded denotes a narrow no-execution property: agent-facing requests dispatch no SDC device operation. A Python prototype supports simulated fault and lifecycle experiments, a software-reference protocol path spanning independent Java and Python implementations, deterministic baselines, representation ablations, and multi-model agent evaluation. The results show semantically explicit resource exposure, visible rejection of invalid or outdated state, and preservation of the no-execution boundary across resource, proposal, and authorization paths. Explicit semantic metadata improved conformity to required metric identifiers in structured alarm outputs relative to a generic representation, while retained structured-output failures reveal a distinction between plausible narrative answers and task-compliant machine-readable results.

## Metadata
- **Published**: 2026-09-25T14:54:21Z
- **Authors**: Bennet Gerlach, Stefan Fischer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31358v1)