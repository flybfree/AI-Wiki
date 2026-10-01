---
title: AgBench: Agentic AI Benchmarks for Personal AI Devices
published: 2026-09-29T23:18:37Z
authors: Yizhou Han, Di Wu, Dhananjay Saikumar, Blesson Varghese
url: http://arxiv.org/abs/2609.38652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgBench: Agentic AI Benchmarks for Personal AI Devices

## Abstract
Agentic AI systems increasingly rely on cloud-hosted large language models for planning, tool use, and iterative execution, raising concerns about API cost and data exposure. Advances in personal AI devices enable agents to execute locally, but limited resources on device may affect task success and performance. Existing benchmarks are inadequate for systematically characterizing these trade-offs across devices, workloads, and deployment architectures. We present AgBench, a benchmark suite and open artifacts for reproducible evaluation of agentic AI on personal devices. Using AgBench, we evaluate local, hybrid, and cloud execution across agentic workloads, examining task success, latency, cloud API cost, and data exposure. Our results, drawn from over 162.07 million data points, show that personal AI devices can complete many agent tasks locally, but local-only execution generally has lower task success and longer completion times than cloud-only execution, especially as concurrency increases. Local-only execution eliminates cloud model API costs and sensitive-information exposure to cloud agents. Hybrid execution can improve task success, but its cloud cost and data exposure depend on how agents divide work and share information. No single architecture performs best across task success, goodput, cloud cost, and data exposure; deployment choices should reflect the intended workload and device capabilities. AgBench is available at https://anonymous.4open.science/r/AgBench-2777.

## Metadata
- **Published**: 2026-09-29T23:18:37Z
- **Authors**: Yizhou Han, Di Wu, Dhananjay Saikumar, Blesson Varghese
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38652v1)