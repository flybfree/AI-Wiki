---
title: FOCUS: Training-Free Decision-Preserving Context Compression for LLM Agents
published: 2026-09-29T13:45:34Z
authors: Shantanu Dixit, Anson Bastos, Xuchao Zhang, Chetan Bansal, Saravan Rajmohan
url: http://arxiv.org/abs/2609.37590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FOCUS: Training-Free Decision-Preserving Context Compression for LLM Agents

## Abstract
LLM agents accumulate interaction histories that grow linearly with task length, causing quadratic inference cost scaling and performance degradation from attention dilution. Existing context-compression methods learn what to discard offline: by contrastively optimizing guidelines, distilling compressors, or training compression policies. This incurs a substantial cost. Further, the compression policy is learned a priori and is not dynamically conditioned on the evolving test-time trajectories. In this paper we ask a complementary question: Which past interactions causally shape the agent's future decisions? We recast context compression as a causal decision preservation problem over discrete interaction units and introduce FOCUS, a training-free context compression framework that operates entirely at test time. Our method requires no offline data collection or fine-tuning, and is architecture-agnostic, attaching to any closed-API frontier model as a modular compression layer. We evaluate FOCUS on diverse agentic benchmarks including API and tool-calling, QA, web domain and multi-turn dialogue. Our method establishes new state of the art performance, cutting peak context by up to 48% and dependency by 73% while improving task success by up to 8.9 percentage points over uncompressed execution.

## Metadata
- **Published**: 2026-09-29T13:45:34Z
- **Authors**: Shantanu Dixit, Anson Bastos, Xuchao Zhang, Chetan Bansal, Saravan Rajmohan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37590v1)