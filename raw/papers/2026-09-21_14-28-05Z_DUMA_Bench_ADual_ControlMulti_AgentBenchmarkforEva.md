---
title: DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security
published: 2026-09-21T14:28:05Z
authors: Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, Yaroslav Rogoza
url: http://arxiv.org/abs/2609.24662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security

## Abstract
LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~\cite{barres2025tau} with adversarial environments covering eight vulnerability classes, including RAG poisoning, cross-agent manipulation, and unsafe output handling. We evaluate \textbf{14 models from five model families} (OpenAI, Anthropic, DeepSeek, Qwen, and Z.ai) across eight domains and multiple user-behavior regimes. Across our experiments, introducing dual-control interaction increases the attack success rate from \textbf{26.9\%} to \textbf{41.1\%}. These results show that agent security is not solely a property of the model but emerges from the interaction between the model, the user, and the environment. DUMA-Bench provides a missing evaluation layer for studying security in realistic agent deployments.

## Metadata
- **Published**: 2026-09-21T14:28:05Z
- **Authors**: Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, Yaroslav Rogoza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24662v1)