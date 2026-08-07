---
title: Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks
published: 2026-08-05T18:57:24Z
authors: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
url: http://arxiv.org/abs/2608.05340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks

## Abstract
Time-Sensitive Networking (TSN) and Mobile Edge Computing (MEC) hold strong potential for enabling ultra-reliable low-latency communication for time-sensitive applications, such as eXtended Reality (XR). However, the widespread adoption of XR introduces significant challenges due to co-located services in MEC environments, leading to contention for shared network resources. Moreover, XR traffic types have distinct characteristics and criticality in terms of timing requirements, further increasing the complexity and dynamics of such environments. Although reinforcement learning has shown promise for TSN scheduling optimization in dynamic network scenarios, existing approaches rely on centralized or high-level multi-agent designs and are typically tailored to periodic and predictable industrial traffic, limiting their applicability to XR workloads. As a result, these approaches suffer from (i) limited ability to capture inter-queue dependencies due to coarse-grained control, and (ii) poor adaptability to highly dynamic and heterogeneous XR traffic. To address these gaps, we propose a multi-agent reinforcement learning approach for queue-level XR traffic scheduling. We adopt the multi-agent transformer (MAT) to model inter-queue dependencies via attention over agents' observations and actions, enabling implicit coordination across heterogeneous co-located XR applications. Our simulation results show that the proposed method outperforms baselines, achieving up to 71.42% latency reduction and up to 83.2% reduction in failure rate, while consistently achieving high reliability across all queues.

## Metadata
- **Published**: 2026-08-05T18:57:24Z
- **Authors**: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05340v1)