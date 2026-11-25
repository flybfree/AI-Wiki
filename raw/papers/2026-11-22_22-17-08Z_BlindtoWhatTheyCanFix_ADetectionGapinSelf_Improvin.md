---
title: Blind to What They Can Fix: A Detection Gap in Self-Improving Agents
published: 2026-11-22T22:17:08Z
authors: Teng Cao, Yu Deng, Kristian Kersting
url: http://arxiv.org/abs/2611.29807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Blind to What They Can Fix: A Detection Gap in Self-Improving Agents

## Abstract
AI agents can write programs that carry out a task without calling a model at every step, so the task runs fast and its logic stays open to inspection. Agents improve these programs by running them, studying their failures, and revising the code, a form of recursive self-improvement (RSI). We ask whether this process also yields runtime checks that can be trusted. In five task domains, with up to seven author models, agents bring their programs to high scores. Yet when the environment changes, the checks they were told to write stay silent on half or more of the resulting failures in four domains. These failures can be detected and repaired: a monitor built from records of normal runs catches most of them in three domains, and the same agents usually repair them once called. The checks do not examine the recorded relations that reveal the failures, and the strongest agent writes checks that catch most of them once told that its checks are the only thing that calls it back. An unreported failure stays unrepaired, which limits what self-improvement is worth in autonomous operation. Evaluations of self-improvement should measure not only scores but also whether a system notices its own failures.

## Metadata
- **Published**: 2026-11-22T22:17:08Z
- **Authors**: Teng Cao, Yu Deng, Kristian Kersting
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.29807v1)