---
title: Architectural Implications of Agentic AI Workflows
published: 2026-08-05T05:31:33Z
authors: Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
url: http://arxiv.org/abs/2608.04458v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Architectural Implications of Agentic AI Workflows

## Abstract
Agentic AI is emerging in datacenters, but its architectural implications remain unexplored. We organize agentic workflows in a taxonomy and present its first architectural characterization with a production study at Microsoft Azure and a controlled study of open-source frameworks. We show that agentic execution is fragmented and heterogeneous. Requests expand into a workflow of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. Our taxonomy explains how this fragmentation turns into resource demand. As orchestration and tools run on the host, the CPU sits on the critical path. Execution structure sets the load over time, which stays low with sudden spikes. Model composition sets how evenly the workflow uses the GPUs. Diversity in tasks and tools widens this range even further. These characteristics expose architectural mismatches of conventional uniform servers. Fragmented execution strands CPU and GPU capacity despite bursty demand. Different software roles make homogeneous CPU provisioning inefficient. Finally, multiplexing many agents onto shared cores degrades microarchitectural locality. Guided by our findings, we derive implications for agentic servers and examine them through Agora, our prototype for commodity servers. Agora dynamically harvests idle CPU cores for co-located throughput work, while protecting agentic tail latency against tool spikes. It oversubscribes GPU memory by placing more agents on each GPU, prefetching the next agent's state to hide swap latency. To match the machine to the heterogeneous roles, Agora pools cores by role and applies affinity-aware scheduling to restore locality. It automatically tunes mechanisms to the workload. Agora improves utilization and server throughput while preserving agent tail latency. Our insights also identify key directions for future server architectures for agentic AI.

## Metadata
- **Published**: 2026-08-05T05:31:33Z
- **Authors**: Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04458v1)