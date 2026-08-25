---
title: Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents
published: 2026-08-21T18:34:48Z
authors: Baicheng Chen, Zheyuan Liu, Jingyu Zhang, Kaize Ding, Ningshan Ma, Yue Huang, Meng Jiang
url: http://arxiv.org/abs/2608.21544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents

## Abstract
Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

## Metadata
- **Published**: 2026-08-21T18:34:48Z
- **Authors**: Baicheng Chen, Zheyuan Liu, Jingyu Zhang, Kaize Ding, Ningshan Ma, Yue Huang, Meng Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21544v1)