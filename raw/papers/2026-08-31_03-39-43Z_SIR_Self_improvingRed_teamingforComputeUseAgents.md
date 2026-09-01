---
title: SIR: Self-improving Red-teaming for Compute Use Agents
published: 2026-08-31T03:39:43Z
authors: Chen Xiong, Zhiyuan He, Pin-Yu Chen, Stjepan Picek, Tsung-Yi Ho
url: http://arxiv.org/abs/2608.30207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SIR: Self-improving Red-teaming for Compute Use Agents

## Abstract
Computer use agents (CUAs) are vision-language models that perceive a screen and act on a real operating system through mouse, keyboard, and terminal, and they are increasingly deployed to automate everyday digital tasks. Because they can be exposed to untrusted content while operating, they are vulnerable to indirect prompt injection (IPI), in which an adversary plants instructions in content the agent will read and redirects it toward actions that violate the user's intent. Existing CUA safety benchmarks evaluate fixed injections written by hand, which may underestimate the risk posed by an adaptive adversary. We present SIR, a black box IPI attack that (i) composes stealthy injections from a small library of reusable principles stated in plain language and (ii) wraps composition in an iterative feedback loop that diagnoses the victim's failed trajectories and distills the bypasses into new, named strategies that are reapplied across tasks. Unlike prior red teaming of web agents, we target CUAs at the operating system level and score attacks with a fully deterministic oracle, using checks on filesystem, service, and permission state rather than an LLM judge. On experiment, we evaluate three frontier CUAs. Composing principles with feedback raises the attack success rate over a baseline written by hand, for example from 4% to 24% on Claude Opus 4.8 and from 0% to 28% on Gemini 3.5 Flash, while the benign task still completes. Principles discovered against one model further transfer to a different architecture with no additional feedback.

## Metadata
- **Published**: 2026-08-31T03:39:43Z
- **Authors**: Chen Xiong, Zhiyuan He, Pin-Yu Chen, Stjepan Picek, Tsung-Yi Ho
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30207v1)