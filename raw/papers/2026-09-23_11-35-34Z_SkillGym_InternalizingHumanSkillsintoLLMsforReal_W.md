---
title: SkillGym: Internalizing Human Skills into LLMs for Real-World Problem Solving
published: 2026-09-23T11:35:34Z
authors: Zhilong Ge, Yuting Shao, Yutao Yang, Yuxuan Cai, Jie Zhou, Kai Chen, Bo Zhang, Qin Chen, Liang He
url: http://arxiv.org/abs/2609.27717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillGym: Internalizing Human Skills into LLMs for Real-World Problem Solving

## Abstract
Human-written agent skills encode rich workflows for real-world problem solving, but are typically used as external inference-time instructions rather than internalized as reusable model capabilities. We introduce \texttt{SkillGym}, a framework that transforms these skills into executable, verifiable training environments for large language model agents. Its skill-to-task pipeline instantiates concrete tasks, verifies outcomes with code-based checkers, and assesses empirical skill dependence through contrastive executions. We construct and release 2,756 environments across 12 categories and collect 8,364 successful trajectories from multiple models and harnesses, averaging 49 tool calls and over 60k logged text tokens. These resources support supervised fine-tuning on verified workflows and reinforcement learning with outcome-based rewards. Under Claude Code, supervised fine-tuning improves Qwen3.5-35B-A3B by 199 Elo on GDPval-AA v2, 19.10 percentage points on Terminal-Bench 2.1, and 28.13 and 12.38 points on SkillsBench v1.1 with and without skills, respectively. Our 35B \texttt{SkillGym-Agent} reaches 51.47\% on skill-assisted SkillsBench, exceeding reported scores for Claude Sonnet 4.6, GPT-5.4 Mini, and DeepSeek V4 Pro. Without skills, it also surpasses skill-assisted bases under Codex and Claude Code, suggesting reusable procedural competence.

## Metadata
- **Published**: 2026-09-23T11:35:34Z
- **Authors**: Zhilong Ge, Yuting Shao, Yutao Yang, Yuxuan Cai, Jie Zhou, Kai Chen, Bo Zhang, Qin Chen, Liang He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27717v1)