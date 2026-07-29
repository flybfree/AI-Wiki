---
title: A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain
published: 2026-07-28T08:10:25Z
authors: Debjyoti Paul
url: http://arxiv.org/abs/2607.25415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain

## Abstract
Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy. Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API. We take a narrower, more constrained position: treat the harness as a small, fixed, human-legible action space and learn a policy over it online with classic sample-efficient reinforcement learning (an $ε$-greedy contextual bandit and REINFORCE), scored against a multi-objective reward (task success, verifier score, policy compliance, cost, latency, and an unsupported-claim penalty). We instantiate this control system with DSPy (Khattab et al., 2024) as both the context assembler and the source of the strongest non-adaptive baseline (a DSPy BootstrapFewShot static prompt), and evaluate it across three verifiable task domains -- tool-use workflows, code generation (HumanEval), and multi-hop retrieval QA (HotpotQA) -- and two model providers (a local Ollama model and AWS Bedrock). We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup.

## Metadata
- **Published**: 2026-07-28T08:10:25Z
- **Authors**: Debjyoti Paul
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25415v1)