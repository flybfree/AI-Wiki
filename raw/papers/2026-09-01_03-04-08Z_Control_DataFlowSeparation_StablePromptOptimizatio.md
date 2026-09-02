---
title: Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs
published: 2026-09-01T03:04:08Z
authors: Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie, Eugene Wen, Yuntian Deng
url: http://arxiv.org/abs/2609.00621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs

## Abstract
Prompt optimization can improve multi-agent LLM systems, but the prompts being optimized often serve two entangled roles: generating task-relevant content and specifying execution-critical protocols, such as message routing, output formatting, and termination signals, on which the underlying code relies. As a result, a prompt edit intended to improve content generation can inadvertently corrupt the protocol and cause the entire agent pipeline to fail. Our key observation is that these two roles have different representations: execution protocols are typically structured, while task-relevant content is usually expressed in unstructured language. Based on this, we propose control-data flow separation, where execution-critical control is represented as typed, validated program objects, while task-relevant language remains the optimizable data flow for agent communication. This design allows optimizers to improve multi-agent behavior without exposing the routing or formatting interface to prompt drift. Across synthetic reasoning, collaborative review generation, and insurance rating workflows, our framework empirically achieves 100% eventual protocol validity while consistently improving task performance.

## Metadata
- **Published**: 2026-09-01T03:04:08Z
- **Authors**: Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie, Eugene Wen, Yuntian Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00621v1)