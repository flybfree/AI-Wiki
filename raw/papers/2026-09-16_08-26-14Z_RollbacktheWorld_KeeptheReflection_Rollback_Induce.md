---
title: Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents
published: 2026-09-16T08:26:14Z
authors: Yi Yu, Liuyi Yao, Yaliang Li, Enshu Wang, Libing Wu
url: http://arxiv.org/abs/2609.18304v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents

## Abstract
Large language model (LLM) agents increasingly tackle long-horizon tasks through multi-step environment interaction, yet a single erroneous action can alter subsequent states and observations, causing errors to compound over time. Existing methods either correct the context without repairing altered environment states or restore earlier states while discarding useful experience, making it difficult to both eliminate failure conditions and avoid repeating past mistakes. We argue that reliable recovery should instead be treated as a rollback-boundary control problem that jointly determines when to intervene, where to resume, and what information should survive recovery. Based on this view, we propose Rollback-Induced Reflection (RIR), a unified recovery framework that restores execution to a selected prior state while carrying forward reusable knowledge distilled from the abandoned trajectory to guide subsequent decisions. We further characterize recovery through a unified operator over rollback depth and retained memory, providing a general view of state restoration and knowledge retention. Experiments on three long-horizon benchmarks demonstrate that RIR consistently improves task performance across multiple LLM backbones, with structured reflection memory preserving useful experience and selective rollback enabling efficient recovery.

## Metadata
- **Published**: 2026-09-16T08:26:14Z
- **Authors**: Yi Yu, Liuyi Yao, Yaliang Li, Enshu Wang, Libing Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18304v1)