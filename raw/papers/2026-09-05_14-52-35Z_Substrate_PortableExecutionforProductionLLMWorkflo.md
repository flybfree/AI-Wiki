---
title: Substrate-Portable Execution for Production LLM Workflows
published: 2026-09-05T14:52:35Z
authors: Tarun Gopinath, Atul Kulkarni, Vijay Rajakumar, Shrikar Katti, Parthasarathy Govindarajen
url: http://arxiv.org/abs/2609.06128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Substrate-Portable Execution for Production LLM Workflows

## Abstract
Production LLM agents execute tool-calling loops, retrieval chains, and compositional workflows in multiple modes, yet execution semantics are often coupled to one runtime. We encountered this portability problem in Rufus, a conversational AI assistant with a large tool catalog that serves millions of Amazon customers. Rufus supports real-time serving, asynchronous background tasks, and high-volume batch workloads such as evaluation and content pregeneration. Each mode has distinct service-level objectives and typically uses a separate runtime. Reusing streaming orchestration makes asynchronous and batch workloads blocking and prevents use of batch inference APIs, which offer a 50 percent discount at published prices. We present a binding-adaptive agent execution platform that separates workflow definition from execution substrate. Developers define a workflow once as a typed dataflow graph. The platform compiles the graph to in-process streaming for real-time serving, durable AWS SWF orchestration for asynchronous execution, or distributed Apache Flink stream processing for batch inference. No workflow code changes are required. LLM inference is represented as a suspendable graph node whose behavior depends on the substrate: streaming delivery online, durable retry asynchronously, and batched submission offline. We validated dozens of production agent configurations across five orchestration patterns: single-inference RAG, iterative ReAct, compositional PreAct, conditional routing, and multi-agent deep research. Across all three bindings, we found no detectable difference in output quality. Batch execution reduced per-query inference cost in line with published batch API pricing while operating alongside the streaming path at production scale.

## Metadata
- **Published**: 2026-09-05T14:52:35Z
- **Authors**: Tarun Gopinath, Atul Kulkarni, Vijay Rajakumar, Shrikar Katti, Parthasarathy Govindarajen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06128v1)