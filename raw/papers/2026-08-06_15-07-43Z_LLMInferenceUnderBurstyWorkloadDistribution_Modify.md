---
title: LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm
published: 2026-08-06T15:07:43Z
authors: Anjali Gangadhar Katageria, Shobha Rani, Raghu Nandan Sengupta
url: http://arxiv.org/abs/2608.06135v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm

## Abstract
Large Language Models (LLMs) such as ChatGPT and Claude are widely used for information retrieval and problem-solving. Recent work has focused on improving scheduling algorithms to boost throughput while maintaining low latency. However, these approaches often assume Poisson request arrivals with constant rates - an assumption that fails to reflect the inherently bursty and dynamic nature of real-world traffic. We propose a lightweight extension to the state-of-the-art WAIT algorithm [1], which adapts to time-varying arrival rates without prior traffic knowledge. The proposed algorithm performs online estimation of request intensity based on observed interarrival times. Using Markov Modulated Poisson Process (MMPP)-based synthetic workloads with diverse request types, we conduct a simulation-based evaluation demonstrating that the proposed method achieves higher throughput than Sarathi-Serve [2], ORCA [3], and vLLM [4] in the evaluated low arrival-rate shift scenarios while maintaining comparable latency.

## Metadata
- **Published**: 2026-08-06T15:07:43Z
- **Authors**: Anjali Gangadhar Katageria, Shobha Rani, Raghu Nandan Sengupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06135v1)