---
title: API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary
published: 2026-09-27T08:55:16Z
authors: Patrick Kenney, Hadi Ahmadi, Denis Lusson, Donald Nguyen, Gurbinder Gill
url: http://arxiv.org/abs/2609.33371v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary

## Abstract
Tool-using large language model (LLM) agents turn credential hygiene from a storage problem into an execution-security problem. A key pasted into a prompt, or embedded in a system prompt or tool configuration, crosses from an authentication boundary into a data pipeline, where it may persist in conversation history, logs, memory stores, generated code, and error payloads. Prompt injection and excessive agency then convert passive disclosure into unauthorized action. This paper formalizes the credential-exposure threat chain for agentic systems; synthesizes evidence from a platform secret-store incident, vendor-reported secret-sprawl measurement, and OWASP and NIST guidance; and describes a vault-mediated execution architecture in which the model selects a connector identifier while a trusted request boundary supplies authentication. We evaluate a production implementation, Corvic Security Vault, in two controlled black-box experiments. Across 16 probes spanning seven control domains, every probe met its expected outcome: an authenticated GitHub API request succeeded while the credential stayed absent from process environment values, caller-visible request headers, tested filesystem locations, three third-party echo services, and two unrelated API origins; both cloud instance-metadata endpoints were unreachable. We also report a negative result, a connector whose stored header mapping did not satisfy its provider's authentication contract, showing that centralized custody does not by itself guarantee correct configuration. Vault mediation removes several disclosure paths but is necessary rather than sufficient: least privilege, deterministic action authorization, human approval, telemetry redaction, and rotation remain independently required. The study is purposive and small, a functional security evaluation rather than a certification.

## Metadata
- **Published**: 2026-09-27T08:55:16Z
- **Authors**: Patrick Kenney, Hadi Ahmadi, Denis Lusson, Donald Nguyen, Gurbinder Gill
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33371v1)