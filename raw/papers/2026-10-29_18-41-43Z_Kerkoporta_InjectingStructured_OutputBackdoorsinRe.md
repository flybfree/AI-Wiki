---
title: Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents
published: 2026-10-29T18:41:43Z
authors: Georgios Syros, Blake Bullwinkel, Alina Oprea, Cristina Nita-Rotaru, Amanda Minnich, Xiaodong Liu, Giorgio Severi
url: http://arxiv.org/abs/2611.00138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents

## Abstract
Existing large language model (LLM) backdoor attacks operate primarily in chat settings, where the risk is bounded by free-form text outputs. AI agents remove that bound by performing actions and executing commands on the user's machine. We introduce structured-output backdoor attacks against reasoning models in agentic coding settings. A trigger placed anywhere in the agent's context causes the model to emit an attacker-chosen tool call, which the harness executes, directly compromising the system's confidentiality, integrity, or availability. We present Kerkoporta, a methodology that constructs high-quality poison samples, injects the backdoor via supervised fine-tuning, and recovers utility loss with lightweight reinforcement learning. We evaluate on modern, heavily post-trained open-weight models across proprietary and open-source harnesses, focusing on coding for its wide adoption and long-horizon task structure. The attack reaches success rates of up to 96.2% and can be configured to generalize across harnesses or bind to a single target. The resulting models can outperform the clean baseline on standard utility benchmarks, giving victims a direct incentive to adopt them. Overall, we demonstrate that LLM backdoors can have critical security impacts in the context of modern coding agents, and we characterize the poisoning methodology required to insert backdoors that are both effective and stealthy in this setting.

## Metadata
- **Published**: 2026-10-29T18:41:43Z
- **Authors**: Georgios Syros, Blake Bullwinkel, Alina Oprea, Cristina Nita-Rotaru, Amanda Minnich, Xiaodong Liu, Giorgio Severi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.00138v1)