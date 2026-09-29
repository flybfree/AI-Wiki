---
title: AgentPerfBench: A Benchmarking and Evaluation Suite for Inference Performance of Agentic LLMs
published: 2026-09-28T09:09:42Z
authors: Cheuk Hang Lau, Zeyu Cao, Kevin Wong Cheuk Yin, Yao Lai, Haoran Wu, Nicholas D. Lane, Robert D. Mullins, Ilia Shumailov, Yiren Zhao
url: http://arxiv.org/abs/2609.34683v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentPerfBench: A Benchmarking and Evaluation Suite for Inference Performance of Agentic LLMs

## Abstract
The optimization of LLM serving engines, such as vLLM and SGLang, is largely benchmark-driven: optimizations, scheduling policies, hardware and system designs are all selected based on representative workloads. However, a significant mismatch has emerged in the agentic era. Existing benchmarks primarily focus on simple single-turn chatbot workloads. LLM applications are increasingly agentic: coding agents, terminal execution systems, and tool-use agents issue multi-turn requests with growing context lengths. We introduce AgentPerfBench, a benchmark suite for agentic inference. It uses real traces from agentic benchmarks, such as SWE-Bench and TerminalBench, alongside standard chat baselines. This enables benchmarking of models on multi-turn tasks involving tool calling, skill utilization, and increasing context lengths. AgentPerfBench also samples from empirical distributions of input length, output length, and turn count derived from the real traces, generating representative synthetic profiles for cheap and accurate measurements on new hardware. In addition, we further find that several existing benchmarks fail to accurately reflect real hardware performance for two key reasons: 1) they do not account for realistic context-length growth, and 2) they measure inference performance without operating at hardware saturation. We discuss these issues in detail and provide rich kernel-level Nsight Compute (NCU) traces to construct a new multi-dimensional roofline model that captures hardware-system limitations in both memory bandwidth and memory capacity footprint. The benchmarking suite then includes automated scripts to identify potential bottleneck conditions on emerging hardware when evaluated with diverse agentic traces. Together, these contributions quantify the chat-to-agentic gap in current inference benchmarks and characterise per-kernel GPU resource utilisation via roofline analysis.

## Metadata
- **Published**: 2026-09-28T09:09:42Z
- **Authors**: Cheuk Hang Lau, Zeyu Cao, Kevin Wong Cheuk Yin, Yao Lai, Haoran Wu, Nicholas D. Lane, Robert D. Mullins, Ilia Shumailov, Yiren Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34683v1)