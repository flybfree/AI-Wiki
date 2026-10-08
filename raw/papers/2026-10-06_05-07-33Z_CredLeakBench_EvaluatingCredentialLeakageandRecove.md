---
title: CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents
published: 2026-10-06T05:07:33Z
authors: Rafid Ahmed, Joseph Fioresi, Mubarak Shah, Yuzhang Shang
url: http://arxiv.org/abs/2610.08871v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents

## Abstract
Language model agents are increasingly deployed to automate everyday digital chores from managing emails and social media to handling banking and bills allowing users to step away from supervision. However, this capability also exposes sensitive information to phishing. Safe execution requires distinguishing malicious requests from genuine ones without simply refusing to act. Despite its practical importance, this problem remains underexplored and it is unclear whether current agents or existing defenses can achieve it. To study this problem, we first propose CredLeak-Bench, a comprehensive benchmark designed to evaluate how effectively and securely agents automate human workflows when confronted with phishing and identity verification. The benchmark covers both user-directed authentication and autonomous inbox monitoring, where agents are not explicitly instructed to log in. It systematically varies deceptive cues and pairs phishing scenarios with legitimate counterparts, enabling joint evaluation of information leakage and utility on genuine tasks. Within a sandboxed environment, leakage is measured through actual submissions of information rather than agents' self-reported behavior. Our evaluation reveals that all tested models are vulnerable to leakage. Agents also disclose sensitive information during autonomous inbox monitoring, demonstrating that phishing can induce disclosure without a user request to authenticate. Furthermore, most evaluated mitigations that reduce leakage also impair performance on genuine tasks, exposing a security utility trade off in existing defenses. These findings show why reducing leakage alone is insufficient: effective defenses must prevent unauthorized disclosure while preserving legitimate task completion. CredLeak-Bench provides a controlled framework for measuring both objectives and evaluating progress toward secure, useful agents.

## Metadata
- **Published**: 2026-10-06T05:07:33Z
- **Authors**: Rafid Ahmed, Joseph Fioresi, Mubarak Shah, Yuzhang Shang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08871v1)