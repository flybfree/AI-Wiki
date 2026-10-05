---
title: Open-Endedness Bench: Measuring Epistemic Process from Agent Records
published: 2026-10-01T23:34:37Z
authors: Chengyang Shi, Xianglin Ji, Jintao Huang, Jicheng Wang, Yifeng He, Jiachen Liu
url: http://arxiv.org/abs/2610.02588v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Open-Endedness Bench: Measuring Epistemic Process from Agent Records

## Abstract
Agents are increasingly given open-ended research tasks: discovering an empirical law from self-designed experiments, improving a heuristic whose optimum nobody knows, or beating a standing record. Their execution logs record every step of this research, yet the runs are still judged by their outcome score. That score alone does not establish whether an agent's claims follow from executed experiments, and a reference answer may be unavailable. We evaluate the agent's epistemic process: how it forms hypotheses, tests them, and revises them in response to evidence. We introduce OEB (Open-Endedness Bench), a benchmark-agnostic methodology that reads only the agent's execution record and never a reference answer or an outcome score. OEB compiles the record into a unified epistemic event graph whose edges connect the propositions the agent states to the executed actions that test them; each node carries an exact excerpt that code verifies against the record. One principle governs scoring: prose can state a proposition, but only evidence returned by an executed action can support or refute it, so OEB checks what the agent writes against what it actually ran. From the graph, OEB scores four competence axes (evidence, experiment, revision, and no reward hacking), mostly as the share of opportunities for sound research that the agent took, and profiles six subjective persona traits that describe the agent's research habits. We score 119 existing runs over 12 tasks from three benchmarks: LLM post-training, chip design, and a training-speed record. Against logged results, only 16-29% of the improvements agents claim are real. On 9 of 10 tasks, the best run tries more new ideas in its second half than the worst run. The persona readings follow the model: for every trait, the model that ran explains more of its variance across runs than the task (a median of 43% against 7%).

## Metadata
- **Published**: 2026-10-01T23:34:37Z
- **Authors**: Chengyang Shi, Xianglin Ji, Jintao Huang, Jicheng Wang, Yifeng He, Jiachen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02588v1)