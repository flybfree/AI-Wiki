---

title: Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling
published: "2026-05-20T17:54:27Z"
authors: Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini, Christos Kozyrakis
url: http://arxiv.org/abs/2605.21470v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling



**Source**: [Original Paper](http://arxiv.org/abs/2605.21470v1)
## Abstract
Computer-use agents (CUA) automate tasks specified with natural language such as "order the cheapest item from Taco Bell" by generating sequences of calls to tools such as click, type, and scroll on a browser. Current implementations follow a sequential fetch-screenshot-execute loop where each iteration requires an LLM call, resulting in high latency and frequent errors from incorrect tool use. We present agent just-in-time (JIT) compilation, an alternative that compiles task descriptions directly into executable code that is free to include LLM calls, tool calls, and parallelization. Our approach comprises three components: (1) JIT-Planner, which generates multiple code plans, validates each against tool specifications, and selects the minimum-cost candidate; (2) JIT-Scheduler, which explores parallelization strategies via Monte Carlo cost estimation from learned latency distributions; and (3) an invariant-enforcing tool protocol specifying precondition and postcondition state requirements that reduce the rate of generating plans with incorrect tool use. Across 5 web applications, JIT-Planner achieves $10.4\times$ speedup and $+28\%$ accuracy over Browser-Use, while JIT-Scheduler achieves $2.4\times$ speedup and $+9\%$ accuracy over OpenAI CUA.

## Metadata
- **Published**: 2026-05-20T17:54:27Z
- **Authors**: Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini, Christos Kozyrakis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.21470v1)