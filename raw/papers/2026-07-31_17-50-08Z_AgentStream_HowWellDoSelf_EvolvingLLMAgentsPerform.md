---
title: AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?
published: 2026-07-31T17:50:08Z
authors: Dong Yan, Jian Liang, Dapeng Hu, Ran He, Nicholas Jing Yuan, Qi Zhang, Tieniu Tan
url: http://arxiv.org/abs/2608.00155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?

## Abstract
Large language model (LLM) agents can self-evolve by continually improving from their own accumulated experience. However, existing studies predominantly adopt independent evaluation. Consequently, the behavior of self-evolving agents in realistic streaming settings, where agents adapt to diverse and complex task streams, remains poorly understood. To address this gap, we introduce AgentStream, a unified framework that evaluates self-evolving agents spanning diverse evolution components by organizing agentic benchmarks into a configurable task stream and instantiating the \texttt{Isolated}, \texttt{Sequential}, and \texttt{Interleaved} streaming scenarios at test time, which progressively vary the scope and domain composition of the stream. Over these scenarios, we combinatorially evaluate five representative self-evolving methods across three frontier foundation models, disentangling how model capability, method architecture, and streaming scenario jointly shape self-evolution. Our results show that self-evolution reliability varies across streaming scenarios, the benefit of self-evolution is gated by model capability and non-monotonic in model strength, and no single method dominates across models and scenarios. These findings offer concrete guidance for selecting self-evolving methods across models and streaming scenarios. Overall, we advocate that self-evolving agents should be evaluated under realistic task streams rather than isolated single-task settings.

## Metadata
- **Published**: 2026-07-31T17:50:08Z
- **Authors**: Dong Yan, Jian Liang, Dapeng Hu, Ran He, Nicholas Jing Yuan, Qi Zhang, Tieniu Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00155v1)