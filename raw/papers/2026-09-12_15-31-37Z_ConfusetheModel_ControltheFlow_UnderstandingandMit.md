---
title: Confuse the Model, Control the Flow: Understanding and Mitigating Privacy Leakage from LLM Agents with Information Flow Control
published: 2026-09-12T15:31:37Z
authors: Minsun Shim, Ramisha Raida Karim, Ruthwik Jakkula, Kaiwen Zhou, Xin Liu, Xin Eric Wang, Zhou Li
url: http://arxiv.org/abs/2609.14003v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Confuse the Model, Control the Flow: Understanding and Mitigating Privacy Leakage from LLM Agents with Information Flow Control

## Abstract
Personal AI agents built on large language models (LLMs) are increasingly given access to a user's private data and communications in order to provide personalized assistance. This access creates a persistent privacy risk: the agent must decide whether a given sensitive information should be disclosed to a particular party. Existing defenses address this by making the agent's backend LLM more privacy-preserving through stronger system prompts, training, or explicit consent-checking procedures, but this approach has a structural challenge: whenever enforcement is a judgment the LLM makes over the same conversational context an adversary controls, the enforcement mechanism and the attack surface coincide. We demonstrate this against existing defenses with three new attacks that require only ordinary agent interaction and no prompt injection: Collaborative Workspace Lure reframes an extraction attempt as collaborative work; Semantic Obfuscation Attack induces disclosure through omission rather than through anything the agent writes; and Channel Decoupling Attack splits the extraction request and the disclosure across independent channels. All three achieve substantially higher leak rates than the attacks these defenses were originally designed to withstand. Guided by this observation, we present FLOWSEAL, a defense that enforces confidentiality through a tool-level interceptor outside the LLM's context, grounded in data provenance and an information-flow-control lattice with controlled declassification. Evaluated across three benchmarks, five prompt-based baselines, and eight attacks, including a real agent executing live tool calls through MCP, FLOWSEAL reduces leak rates to near zero (e.g., 52.2% to 0.5% against Collaborative Workspace Lure) while preserving task utility, regardless of the underlying LLM backend.

## Metadata
- **Published**: 2026-09-12T15:31:37Z
- **Authors**: Minsun Shim, Ramisha Raida Karim, Ruthwik Jakkula, Kaiwen Zhou, Xin Liu, Xin Eric Wang, Zhou Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14003v1)