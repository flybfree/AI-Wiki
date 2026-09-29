---
title: Org-Agent: Beyond Personal Assistants Towards Organizational Agents
published: 2026-09-28T06:07:00Z
authors: Luyao Zhuang, Yujing Zhang, Zijin Hong, Yilin Xiao, Xiao Huang
url: http://arxiv.org/abs/2609.34392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Org-Agent: Beyond Personal Assistants Towards Organizational Agents

## Abstract
Language model agents serving organizations must coordinate requests from multiple users while using knowledge distributed across their interactions. We identify two complementary capabilities for this setting, namely cross-user interaction and decision-making, as well as cross-user memory and knowledge use. Both capabilities are governed by organizational constraints across three aspects: user identity, authority, and access permissions; the attribution and temporal validity of information; and rules for resolving conflicting requirements across users and completion requirements for joint decisions. These constraints shape what information or decisions must be obtained before an action can proceed and what conditions must be satisfied during its execution. Motivated by this, we introduce Org-Agent, a unified constraint-centric reasoning framework that organizes task execution in three stages. Specifically, Org-Agent decomposes a task into atomic subtasks and constructs a task dependency graph whose edges encode the dependencies among them. Building on this graph, it schedules the subtasks in dependency order through topological sorting. It then executes each subtask while accounting for the task's constraints, supported by evidence-acquisition and memory-management tools. Experiments on MUSES-Bench and GroupMemBench demonstrate the effectiveness of Org-Agent on both capabilities, and ablations further support the contributions of dependency modeling and tool use.

## Metadata
- **Published**: 2026-09-28T06:07:00Z
- **Authors**: Luyao Zhuang, Yujing Zhang, Zijin Hong, Yilin Xiao, Xiao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34392v1)