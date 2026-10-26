---
title: When Agents Fail: Model or Harness--Who's to Blame?
published: 2026-10-23T10:57:54Z
authors: Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, Jingping Wang, Chunjiang Mu, Chen Zhang, Yang Chen, Bo Zhang, Shuyue Hu
url: http://arxiv.org/abs/2610.32483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Agents Fail: Model or Harness--Who's to Blame?

## Abstract
LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measures: (i) Valid Completion Rate (VCR), how reliably agents finish normally and deliver evaluable results, irrespective of task correctness; (ii) Model-Harness Fit, how well a harness supports task achievement through valid completion for a given model; (iii) Cross-Model Fit, a harness's overall suitability across evaluated models; (iv) Interaction Residuals, pairing-specific execution strengths and weaknesses hidden by component-level summaries; and (v) Token Load, the token demands of agent execution, including failed attempts. We evaluate four general-purpose harnesses (OpenCode, Codex CLI, Pi CLI, and DeepAgents) with four core models, plus two fixed native model-harness systems, on six benchmarks covering context management, tool use, long-context planning, multimodal interaction, and artifact handoff. Including native references and stress conditions, 111 evaluation settings yield 52,168 trajectories. Harness rankings vary across models and benchmarks; task performance and valid completion can favor different pairings, and similar task scores can accompany distinct execution profiles. OpenCode ranks first in cross-model performance, while DeepSeek V4 Flash Preview maintains consistently high Mean VCR across harnesses on the shared four-benchmark panel. These findings support evaluating model-harness interactions, training transferable harness-use capabilities in models, and harness designs adapted to the model and task.

## Metadata
- **Published**: 2026-10-23T10:57:54Z
- **Authors**: Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, Jingping Wang, Chunjiang Mu, Chen Zhang, Yang Chen, Bo Zhang, Shuyue Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32483v1)