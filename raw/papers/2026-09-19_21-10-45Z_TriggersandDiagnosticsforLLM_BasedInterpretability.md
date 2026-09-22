---
title: Triggers and Diagnostics for LLM-Based Interpretability Failures in Active Inference Agents
published: 2026-09-19T21:10:45Z
authors: Param Raval, Rohit Shenoy, Archana Vaidheeswaran
url: http://arxiv.org/abs/2609.23215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Triggers and Diagnostics for LLM-Based Interpretability Failures in Active Inference Agents

## Abstract
LLM explainers are increasingly attached to autonomous agents as runtime oversight, with operators reading a generated account of the agent's beliefs and actions rather than its internal state. We audit the account itself, pairing an Active Inference (AIF) agent that tracks German grid demand and adjusts generation with an LLM explainer on three backends (GPT-4o, Claude-3-Opus, Gemini), and probing the pair with three black-box triggers. Corrupting the observation stream by 600 MW per step moves the agent's posterior by 490 MW, roughly 0.9% of grid capacity. None of the 30 explanations produced during the injection flag anything under a stated rubric, and each narrates the corrupted belief fluently. On timesteps where the agent takes an objectively wrong action, all three explainers produce a sycophantic rationalization 80-95% of the time (n = 20 per backend). Attacker-controlled text in the observation metadata field steers the explainer, with susceptibility differing by provider and data exfiltration succeeding on all three. We propose mitigations for each failure but do not evaluate them. In every failure we observed, the explanation was fluent and wrong. Moreover, nothing in the explainer architecture checks whether an explanation is true before an operator acts on it. Testing the explainer therefore belongs in any audit of an agentic deployment.

## Metadata
- **Published**: 2026-09-19T21:10:45Z
- **Authors**: Param Raval, Rohit Shenoy, Archana Vaidheeswaran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23215v1)