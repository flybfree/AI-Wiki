---
title: SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution
published: 2026-08-08T09:48:21Z
authors: Xinle Jiang, Remy Xie, Ming Tang
url: http://arxiv.org/abs/2608.08037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution

## Abstract
LLM-based agent frameworks now act as personal assistants for multi-step tasks. Existing agent frameworks such as OpenClaw commonly follow the Cloud Agent depolyment mode using closed-source cloud LLMs as backbone model, which may expose private user information and incur repeated LLM-calling costs. Local Agents address these deployment concerns by depolying frontier open-source SLMs on user-controlled devices, but their task effectiveness still lags far behind Cloud Agents. Through diagnostic analysis, we reveal that the limited effectiveness of Local Agents with frontier SLM backbones mainly comes from missing environment knowledge caused by limited backbone model scale including environment rules and operation procedures. To supply such knowledge non-parametrically, context-efficiently, and without expert authoring, we present SkillSmith, a Cloud--Local Agent collaboration framework that uses Skill as a context-efficient knowledge carrier, automatic constructs Skill from Cloud Agent task exploration and evolves Skill using Local Agent execution feedback to enhance a frozen Local Agent. Experiments on daily agent task datasets AppWorld and WorkBench show that the automatically generated Skill enables the Local Agent with Qwen3.6-27B(SLM) to achieve task effectiveness comparable to Cloud Agents with frontier LLMs, outperform the strongest non-parametric baselines, reduce average actions per task from 36.1 to 9.9 on AppWorld-Normal, and generalize to other SLM backbone models without rerunning Skill construction.

## Metadata
- **Published**: 2026-08-08T09:48:21Z
- **Authors**: Xinle Jiang, Remy Xie, Ming Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08037v1)