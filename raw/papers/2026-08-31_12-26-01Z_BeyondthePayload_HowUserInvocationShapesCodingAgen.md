---
title: Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning
published: 2026-08-31T12:26:01Z
authors: Fukang Zhu, Binbin Zhao, Ruixiao Lin, Ping He, Tianyu Du, Shouling Ji
url: http://arxiv.org/abs/2608.30686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning

## Abstract
Coding agents are increasingly used for software engineering tasks, including bootstrapping projects from third-party repositories whose integrity cannot be assumed. Prior work on repository poisoning largely focuses on attacker-controlled injection and disguise, but developers also shape risk through everyday invocation choices: what task to delegate, how to phrase the request, and which skills or rules to supply. We term these user-side choices Prompt-Level Configurations (PLCs) and introduce CIPR (Coding In Poisoned Repos), the first benchmark that systematically varies PLCs in poisoned real-world repositories. CIPR comprises 1,920 instances across 20 repositories, four task types, three social-media-grounded prompt styles, and three skill/rule conditions, and measures attack success rate (ASR) and agent alert rate (AR) using automated runtime and trace-based oracles. Our evaluation reveals two key insights: (1) Vulnerability is highly context-dependent, with task type creating up to a 4.5-fold difference in ASR, with test-execution task forming a silent attack surface (high ASR, low AR). (2) Prompt expression shifts risk indirectly: underspecified prompts reduce ASR by truncating execution depth; noisy prompts exhibit a directional trend toward suppressing alerts by making malicious content less conspicuous. These findings highlight that coding agent vulnerability is not a static property, but a dynamic outcome shaped by everyday user configurations.

## Metadata
- **Published**: 2026-08-31T12:26:01Z
- **Authors**: Fukang Zhu, Binbin Zhao, Ruixiao Lin, Ping He, Tianyu Du, Shouling Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30686v1)