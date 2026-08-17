---
title: A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents
published: 2026-08-14T09:12:14Z
authors: Ismail El Hamraoui, Sagar Jose, Nicolas Bureau, Robert Plana
url: http://arxiv.org/abs/2608.14109v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents

## Abstract
Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on every deployment, this work targets a plug-and-play recovery module instead. It introduces a graph-based framework in which a single small language model is trained via reinforcement learning to specialize at each node of a recovery graph, external to the main agent. Each node has a precise role\,: drift classification, operation detection, risk evaluation, or final decision and the model learns to produce structured XML-formatted reasoning adapted to that role. Training combines rule-based structural rewards with an LLM-as-judge semantic-quality signal, so that the model is graded both on how it answers (schema and length) and on what it says. Experiments on the public AppWorld benchmark show that the method generally exploits information about the suspected drift onset to issue correct recovery decisions using a small language model. In addition, the trained small language model reliably respects the prescribed output schema and produces semantically appropriate content in each field according to its assigned node role.

## Metadata
- **Published**: 2026-08-14T09:12:14Z
- **Authors**: Ismail El Hamraoui, Sagar Jose, Nicolas Bureau, Robert Plana
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14109v1)