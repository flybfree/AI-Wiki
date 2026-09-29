---
title: AgentPerfBench: A Benchmarking and Evaluation Suite for Inference Performance of Agentic LLMs
url: http://arxiv.org/abs/2609.34683v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_09-09-42Z_AgentPerfBench_ABenchmarkingandEvaluationSuiteforI.md
generated_at: 2026-09-28 22:49
model: qwen3.6-35b-a3b
---

## Summary
AgentPerfBench addresses the critical mismatch between existing LLM inference benchmarks and the demands of agentic workloads by introducing a comprehensive evaluation suite tailored for multi-turn, tool-using scenarios that involve dynamic context growth. The authors demonstrate that current benchmarks fail to accurately reflect real hardware performance due to unrealistic assumptions about context length and insufficient hardware saturation, proposing synthetic profiles derived from real traces like SWE-Bench and TerminalBench to enable cost-effective yet precise measurements on emerging hardware.

## Key Takeaways
- AgentPerfBench bridges the gap between traditional chatbot benchmarks and modern agentic applications by leveraging real-world traces from tools like SWE-Bench and TerminalBench, enabling accurate evaluation of multi-turn tasks involving tool calling, skill utilization, and dynamic context expansion that standard single-turn workloads fail to represent.
- The suite generates representative synthetic profiles by sampling empirical distributions of input length, output length, and turn counts derived from actual agentic traces, allowing researchers to perform cheap yet precise performance measurements on emerging hardware without requiring extensive

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34683v1)
