---
title: SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments
published: 2026-10-25T19:49:40Z
authors: Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed
url: http://arxiv.org/abs/2610.34535v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments

## Abstract
Large language model (LLM) agents are increasingly wired to consequential tools that send public alerts, dispatch responders, and query citizen records, where one erroneous tool call carries real-world cost. Existing agent-safety benchmarks measure generic harm or prompt-injection success and implicitly treat refusing as the safe default. In public-safety deployments that assumption breaks: an agent too cautious to dispatch help fails as surely as one that triggers a false alert. We present SentryBench, which scores agents on a two-sided, cost-sensitive frontier jointly measuring attack success, over-refusal (missing a real emergency), and over-reaction (unwarranted action) under adversarial tool use, with scenarios grounded in real emergency-call transcripts, disaster messages, and real injection/jailbreak payloads. We formalize deployment harm as an asymmetric cost functional, prove naive caution is harm-dominated whenever it refuses more genuine emergencies than the attack harm it averts, and prove a targeted trust gate adds zero over-refusal on clean input. Across 840 scored episodes over three frontier models and three defenses, refuse-more caution drives over-refusal to 100 percent on two of three models for at most a 3.7-point change in attack success and yields the worst harm everywhere, whereas our trust-gating wrapper dominates the frontier (lowest harm on every model, over-refusal at or below baseline, higher containment). Provider content filters also silently perform part of the defending and must be reported separately.

## Metadata
- **Published**: 2026-10-25T19:49:40Z
- **Authors**: Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34535v1)