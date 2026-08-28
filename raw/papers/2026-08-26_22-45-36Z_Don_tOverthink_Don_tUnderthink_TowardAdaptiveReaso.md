---
title: Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI
published: 2026-08-26T22:45:36Z
authors: Md Jueal Mia, M. Hadi Amini
url: http://arxiv.org/abs/2608.26442v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI

## Abstract
Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks. However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space interventions, and are often evaluated on standalone reasoning benchmarks rather than full agentic workflows. These assumptions may not hold in agentic AI systems, where reasoning requirements evolve dynamically through planning, tool use, memory retrieval, and agent-to-agent interactions. Consequently, reasoning can become either excessive or insufficient, resulting in unnecessary computation, increased latency, planning drift, excessive tool use, or incomplete solutions. We argue that a major challenge for next-generation agentic AI is not merely how much reasoning a language model should perform, but how it should allocate reasoning according to evolving task demands. We characterize over-reasoning and under-reasoning as recurring failure modes of misallocated reasoning and evaluate them on MATH-500 and the GAIA public validation benchmark. Using tool-decision latency, token consumption, token-limit exhaustion, and answer correctness, our results suggest that cases classified as over-reasoning are associated with higher computational cost without proportional accuracy gains, whereas cases classified as under-reasoning are consistently associated with incorrect or incomplete solutions. These findings motivate future research on adaptive reasoning mechanisms for agentic AI.

## Metadata
- **Published**: 2026-08-26T22:45:36Z
- **Authors**: Md Jueal Mia, M. Hadi Amini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26442v1)