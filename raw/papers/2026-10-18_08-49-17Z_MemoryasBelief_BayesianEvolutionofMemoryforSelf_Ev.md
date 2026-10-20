---
title: Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents
published: 2026-10-18T08:49:17Z
authors: Yiming Xu, Qian Yang, Zihan Chen, Yuefei Wu, Wenhan Zeng, Bin Shi, Bo Dong
url: http://arxiv.org/abs/2610.25119v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents

## Abstract
Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation. However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task contexts. Despite its importance, memory valuation remains largely underexplored, with existing methods relying on historical retrieval success rates that overlook the context dependency of memory usefulness and the varying reliability of estimates under different amounts of evidence. Inspired by the Bayesian brain hypothesis, we propose BEAM (Bayesian-style Evolutionary Agentic Memory), a framework that reformulates memory value evaluation as a parameterized cognitive inference process, where memory value is represented as a context-conditioned dynamic belief rather than a passive historical statistic. Specifically, BEAM infers memory value beliefs from current task contexts and continuously calibrates them using execution feedback as empirical evidence, transforming memory from passive storage into an adaptive cognitive mechanism for continual self-evolution. Extensive experiments across reasoning and code generation benchmarks demonstrate that BEAM consistently improves memory utilization and enables continual self-evolution of LLM agents.

## Metadata
- **Published**: 2026-10-18T08:49:17Z
- **Authors**: Yiming Xu, Qian Yang, Zihan Chen, Yuefei Wu, Wenhan Zeng, Bin Shi, Bo Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25119v1)