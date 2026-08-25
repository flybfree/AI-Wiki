---
title: What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels
published: 2026-08-24T08:27:33Z
authors: Jiawei He, Mengyu Shi, Jie jia, Xikai Yang, Dong Sun
url: http://arxiv.org/abs/2608.22960v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels

## Abstract
Coding agents are increasingly evaluated not only by whether they solve a task, but also by how they execute it. However, existing process-level evaluations often treat action prediction, task uncertainty, and step attribution as if they were the same problem, which makes it unclear what such evaluations actually measure. In this paper, we introduce a measurement framework for process evaluation in coding agents and instantiate step-level causal attribution with SCAE, a replay-based estimator derived from a structural causal model of agent execution. Our framework combines prefix-conditioned identification, replay/intervention-based estimation, and controlled judge-information manipulation to study process evaluation at the action, task, and step levels. Experiments on 499 file-localization episodes from 12 repositories show that next actions are driven primarily by execution provenance rather than code-graph transitions, execution uncertainty is structured at the task rather than step level, and full-trace judges exhibit systematic collider bias, suggesting that current process evaluation often measures semantic relevance rather than certified causal contribution.

## Metadata
- **Published**: 2026-08-24T08:27:33Z
- **Authors**: Jiawei He, Mengyu Shi, Jie jia, Xikai Yang, Dong Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22960v1)