---
title: SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes
published: 2026-09-17T04:59:08Z
authors: Mengxiao Wang, Nitesh Saxena
url: http://arxiv.org/abs/2609.19705v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes

## Abstract
Autonomous large language model (LLM) agents are moving rapidly into high-stakes domains, yet existing agentic-AI security studies remain largely domain-agnostic and overlook the distinctive, high-consequence attack surface such settings create. We examine this gap through financial trading agents, a representative case of high-stakes agentic security, where a single compromised agent has direct execution authority over real capital in an adversarial, reflexive market. To this end, we present FARSIGHT (Financial Agent Robustness and Security Investigation and Global Holistic Testing), a framework that performs scheme-level evaluation of financial LLM agents on two axes: robustness under market turbulence (including flash-crash-like scenarios), and security against three attack types: attacks on information sources, attacks on agents, and agent-as-attacker behaviors. Applying FARSIGHT to 15 representative academic schemes, we find that most overlook robustness and realistic adversarial threats: 80% fail at least one core robustness metric and 100% exhibit security vulnerabilities. These two failure modes are inseparable: a small misjudgment can cascade into a market-wide crash on its own, while an adversary can deliberately trigger the same collapse at minimal cost.

## Metadata
- **Published**: 2026-09-17T04:59:08Z
- **Authors**: Mengxiao Wang, Nitesh Saxena
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19705v1)