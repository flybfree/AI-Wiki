---
title: A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems
published: 2026-10-20T18:33:19Z
authors: Wendy Zheng, Liang Wu, Yinhan He, Mayank Darbari, Jundong Li, Liangjie Hong
url: http://arxiv.org/abs/2610.28811v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems

## Abstract
Agentic systems have demonstrated strong capabilities on complex tasks by enabling multiple interacting large language model (LLM)-based agents to collaborate and execute subtasks in parallel. However, this collaborative structure introduces new challenges for reliably evaluating and diagnosing system failures, particularly failure attribution: tracing a system's execution to identify the agent step responsible for an incorrect final outcome. Because manually performing this task is time- and labor-intensive, recent work has turned to LLMs as judges to automate the process, referred to as automated failure attribution (AFA). These approaches assume that a sufficiently capable model can infer the failing step directly from an interaction transcript. In practice, however, direct prompting often performs poorly, which motivates follow-up work that explores various ways to improve AFA performance, including alternative prompting strategies and inference-time interventions. In this paper, we examine a more fundamental question: whether this weak behavioral performance reflects a genuine capability limitation. Using linear probes applied to internal activations, we uncover a significant \emph{knows-but-won't-say gap:} models encode sufficient information to attribute a failure correctly but fail to explicitly output the responsible step. Building on this finding, we propose \emph{grafting}, a simple manual intervention that exploits knowledge already encoded in the model to improve AFA performance without requiring ground-truth labels at inference time. Extensive evaluations across multiple LLMs and benchmark settings demonstrate that grafting consistently outperforms direct-prompting approaches, underscoring the potential of leveraging latent model knowledge for more reliable failure attribution. Our code is available at https://github.com/wendyzheng22/mi4afa.

## Metadata
- **Published**: 2026-10-20T18:33:19Z
- **Authors**: Wendy Zheng, Liang Wu, Yinhan He, Mayank Darbari, Jundong Li, Liangjie Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28811v1)