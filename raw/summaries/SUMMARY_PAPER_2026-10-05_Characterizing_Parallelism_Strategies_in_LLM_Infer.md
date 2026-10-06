---
title: Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs
url: http://arxiv.org/abs/2610.05305v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_15-28-50Z_CharacterizingParallelismStrategiesinLLMInference_.md
generated_at: 2026-10-05 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a unified analytical framework for modeling distributed LLM inference under tensor parallelism (TP), pipeline parallelism (PP), and hybrid parallelism (HB), decomposing end-to-end latency into computation, inter-GPU communication, and pipeline bubble overhead. The authors derive closed-form models that capture how hardware, model architecture, and workload characteristics interact across the distinct prefill and decoding phases, revealing fundamental compute-communication trade-offs that explain why PP favors compute-intensive prefill while TP reduces decoding latency by eliminating pipeline bubbles. Experimental validation on modern LLMs across multi-GPU platforms confirms the analytical predictions and provides actionable guidance for parallelism selection and capacity planning.

## Key Takeaways
- The framework decomposes end-to-end inference latency into three distinct components—computation time, inter-GPU communication overhead, and pipeline bubble overhead—enabling practitioners to analytically predict the performance of TP, PP, and hybrid strategies rather than relying solely on empirical benchmarking. This decomposition captures TP collective communication patterns, PP point-to-point communication costs, and pipeline utilization as explicit functions of hardware topology, model dimensions, and workload parameters such as sequence length and batch size.
- The paper reveals a critical asymmetry between the prefill and decoding phases: PP-oriented configurations are advantageous for compute-intensive prefill workloads because pipeline bubbles are amortized over large computation blocks, whereas TP-oriented configurations dominate during decoding by eliminating pipeline bubbles entirely, since decoding involves small, sequential token generation where communication overhead is minimal relative to computation. This insight explains why a single parallelism strategy cannot optimally serve both phases.
- Existing approaches to parallelism selection rely heavily on empirical evaluation and trial-and-error tuning, providing limited analytical insight into the interactions among computation, communication, pipeline utilization, sequence length, batch size, and model architecture. This work fills that gap by providing closed-form models that predict optimal strategy selection given specific hardware and workload constraints, validated against modern LLMs on multi-GPU platforms.

## Context
As state-of-the-art LLMs routinely exceed the compute and memory capacity of a single GPU, distributed inference across multiple GPUs has become the standard deployment paradigm for production AI serving systems. The choice among tensor parallelism, pipeline parallelism, and hybrid strategies profoundly affects throughput, latency, and cost, yet the field has lacked a rigorous analytical foundation for understanding the trade-offs, particularly given the fundamentally different computational characteristics of the prefill and decoding phases. This paper addresses a gap that directly impacts the design of serving infrastructures for the dominant AI workload of the current era.

## Implications
For practitioners building and operating LLM serving systems, this framework provides practical, model-driven guidance for parallelism selection, capacity planning, and infrastructure optimization, reducing reliance on costly empirical search over configuration spaces. For the broader field, the analytical characterization of compute-communication trade-offs across parallelism strategies establishes a foundation for designing next-generation serving architectures, informing hardware-software co-design decisions and enabling automated parallelism planners that can adapt strategies dynamically to workload phase and resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05305v1)
