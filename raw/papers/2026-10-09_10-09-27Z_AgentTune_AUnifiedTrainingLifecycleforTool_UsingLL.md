---
title: AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents
published: 2026-10-09T10:09:27Z
authors: R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
url: http://arxiv.org/abs/2610.13335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents

## Abstract
Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent projections for training, evaluation, and auditing. Building on this substrate, the library provides a shared agent runtime, tool-calling reinforcement learning, agentic distillation, retrieval-augmented generation, decision workflows, evaluation utilities, and a designed path toward self-healing agents. These components are exposed through composable interfaces so that agent strategies, training methods, evaluation procedures, and recovery mechanisms can be combined without requiring separate representations or pipelines. We demonstrate the framework across agentic tasks including legal contract search and domain-specific applications, illustrating its use for trajectory-based optimization, tool-use evaluation, and cross-task agent development. AgentTune is released as a source-available library at https://github.com/Lexsi-Labs/AgentTune

## Metadata
- **Published**: 2026-10-09T10:09:27Z
- **Authors**: R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13335v1)