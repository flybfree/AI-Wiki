---
title: Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents
published: 2026-08-18T08:46:26Z
authors: Ram Rachum, Yotam Amitai, Bálint Gyevnár, Reuth Mirsky, Cameron Allen
url: http://arxiv.org/abs/2608.17524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents

## Abstract
This preliminary paper outlines a planned evaluation benchmark for Explainable Reinforcement Learning (XRL) methods. Current evaluations rely on functionally-grounded metrics like faithfulness and compactness, and on human-grounded proxies like subjective ratings or prediction accuracy. We suggest evaluating XRL methods by how effectively their generated explanations help to diagnose and fix malfunctioning reinforcement learning (RL) agents. We propose EvalXRL, a benchmark in which a Large Language Model (LLM) coding agent uses different XRL methods to diagnose a held-out malfunction in an RL agent, and then repair it.   Our proposed benchmark iterates across (environment $\times$ malfunction $\times$ XRL method) tuples and uses the reward signal of the RL agents to form a final score for each XRL method. The coding agent may use the method interactively: invoke the XRL method, process its output, form new hypotheses on what is broken, and invoke the method again with parameters adjusted for testing these hypotheses. This closed-loop structure may be described as a simplified version of the scientific method. Some XRL methods provide self-evaluations that follow this pattern; we propose the first head-to-head comparison of multiple XRL methods in closed-loop usage.

## Metadata
- **Published**: 2026-08-18T08:46:26Z
- **Authors**: Ram Rachum, Yotam Amitai, Bálint Gyevnár, Reuth Mirsky, Cameron Allen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17524v1)