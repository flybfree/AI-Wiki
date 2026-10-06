---
title: Nexus: An Execution Fabric for AI Agents Across Cloud, Edge, and Devices
published: 2026-10-05T02:47:01Z
authors: Cary Chang, Jialin Zhou
url: http://arxiv.org/abs/2610.05709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nexus: An Execution Fabric for AI Agents Across Cloud, Edge, and Devices

## Abstract
Language-model agents are evolving into long-running services that interact with models, tools, computers, mobile devices, and distributed environments. Existing agent frameworks simplify reasoning and tool invocation. However, cloud-centric designs face three limitations: centralized execution increases failure impact, scaling pressure, and compute cost; extending agents across computers, mobile devices, and edge environments requires a unified execution abstraction with permission control; and long-running executions require consistent lifecycle management across failures, recovery, results, usage, and settlement. We present Nexus, a cloud-edge platform that treats each invocation as a persistent task. Nexus uses an OpenWrt-based runtime for distributed serving, run-scoped delegation for authorized access to Computer and Mobile environments, and persistent records to track execution, outputs, failures, recovery, usage, and charging across cloud and edge components. We evaluate Nexus on controlled, cross-device, and model-driven workloads. All ten Computer-Android workflows succeed, and all six revocation tests block subsequent writes while preserving prior authorized reads. Under worker loss, journaling eliminates duplicate appends (six to zero per task), adding 0.933 s mean normal-path overhead. Across 24 matched task pairs, Nexus completes 24 tasks versus Dify's 22 and is a median 3.88 s faster on jointly successful pairs. In a separate workload, Nexus operates under a smaller tested incremental-runtime memory ceiling than Dapr (16 versus 64 MiB), although Dapr achieves lower successful-call latency. These results demonstrate how locality, operation-scoped authority, and persistent result identity support cloud-edge agent services with workload-dependent costs.

## Metadata
- **Published**: 2026-10-05T02:47:01Z
- **Authors**: Cary Chang, Jialin Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05709v1)