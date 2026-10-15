---
title: Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off
url: http://arxiv.org/abs/2610.19405v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-53-24Z_ScalingLLMInferenceviaParallelism_Throughput_Laten.md
generated_at: 2026-10-14 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper develops a systematic framework for understanding how tensor parallelism (TP), pipeline parallelism (PP), and hybrid configurations affect the throughput-latency trade-offs in large language model serving systems. The authors introduce the concept of "parallelism operating regions" by constructing feasible sets and Pareto frontiers across TTFT and ITL dimensions, revealing that optimal parallelism configurations shift from TP-dominant to PP-dominant as workloads become increasingly prefill-heavy and context lengths grow.

## Key Takeaways
- The paper formalizes the distinction between prefill (governing time-to-first-token) and decode (governing inter-token latency) phases, showing that tensor parallelism and pipeline parallelism expose fundamentally different trade-offs across these two latency dimensions. By constructing TTFT-ITL feasible sets and Pareto frontiers, the authors demonstrate a systematic transition from TP-dominant to PP-dominant configurations as workloads shift toward prefill-heavy compositions, providing practitioners with a principled method for selecting parallelism strategies based on workload characteristics.
- The authors formulate SLO-aware parallelism selection using the concept of "goodput," showing that stringent TTFT requirements favor PP-dominated configurations, while relaxed latency constraints progressively shift optimality toward TP-dominated configurations that offer higher serving capacity. This provides a quantitative decision framework for operators who must meet specific service-level objectives under varying traffic patterns.
- Increasing context length fundamentally alters the relative advantages of parallelism configurations: PP-dominant setups exhibit more favorable scalability and SLO attainment in the long-context regime, while TP-dominant configurations degrade. This finding is critical for the growing deployment of long-context models where prefill costs dominate inference time.

## Context
As LLM serving systems scale to meet production demands across cloud providers and enterprise deployments, the selection of distributed inference parallelism strategies has become a critical operational decision. Despite widespread adoption of TP, PP, and hybrid approaches in frameworks like vLLM, TensorRT-LLM, and DeepSpeed, the field lacks a unified analytical framework connecting parallelism choices to workload-specific latency and throughput outcomes. This paper addresses that gap by providing a rigorous characterization grounded in Pareto frontier analysis and goodput optimization, bridging the gap between theoretical parallelism design and practical SLO-driven serving.

## Implications
For practitioners deploying LLM inference at scale, this work provides actionable guidance for configuring parallelism strategies based on workload composition, latency targets, and context length requirements rather than relying on heuristic or one-size-fits-all settings. For the broader field, it establishes a formal vocabulary and analytical framework—parallelism operating regions, TTFT-ITL feasible sets, and goodput-based selection—that future serving systems, scheduling algorithms, and auto-scaling infrastructure can build upon to automate optimal resource allocation under diverse and evolving service-level objectives.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19405v1)
