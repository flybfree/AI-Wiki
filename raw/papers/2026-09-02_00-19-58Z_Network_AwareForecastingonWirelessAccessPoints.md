---
title: Network-Aware Forecasting on Wireless Access Points
published: 2026-09-02T00:19:58Z
authors: Niloo Bahadori, Swadhin Pradhan, Peiman Amini
url: http://arxiv.org/abs/2609.01957v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Network-Aware Forecasting on Wireless Access Points

## Abstract
Enterprise wireless access points (APs) are promising platforms for predictive machine learning (ML), but their primary responsibility remains providing wireless connectivity and network services. Predictive inference must therefore share an AP's CPU and memory with packet processing, Wi-Fi and IoT radio operations, and client management. This resource contention creates two risks: a model that performs well on proxy hardware may be too slow on the target AP, while a model that fits in isolation may still degrade network services under load. We define \textit{network-aware deployability} using two gates: qualification of the model and its execution path on the target AP, followed by validation of its execution profile under packet-service and forecasting constraints. Our benchmarks show that edge testbeds do not reliably capture target behavior. Across matched artifacts and serving settings, five model implementations run 6.1--19.1$\times$ slower on an AP than on a Raspberry Pi~5, while peak memory usage differs by up to 22\%. Moreover, two forecasting foundation models of similar size differ in AP latency by 19$\times$. When serving a smaller model across 13 parallel streams at a 30~s cadence under network saturation, default execution increases p99 round-trip time (RTT) by 76\% and reduces throughput by 7.06\%. Understanding these trade-offs is essential for live deployment if we aim to use APs for both networking and ML workloads.

## Metadata
- **Published**: 2026-09-02T00:19:58Z
- **Authors**: Niloo Bahadori, Swadhin Pradhan, Peiman Amini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01957v1)