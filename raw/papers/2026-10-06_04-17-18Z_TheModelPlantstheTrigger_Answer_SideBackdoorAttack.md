---
title: The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models
published: 2026-10-06T04:17:18Z
authors: Yibo Zhang, Tianrong Guan, Liang Lin, Puze Wang, Jin Wang, Qingsong Wen
url: http://arxiv.org/abs/2610.07723v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models

## Abstract
Safety alignment in Large Language Models (LLMs) remains vulnerable to backdoor attacks. Existing LLM backdoors are almost all input-centric: activation depends on explicit trigger patterns in the user input, so modern guardrails are built to sanitize the input space. We challenge this assumption with a novel answer-side backdoor for multi-turn dialogue. Instead of inserting the trigger into the input, the adversary uses a benign first-turn prompt to naturally induce the model to generate a specific, seemingly innocuous word. Once merged into the dialogue history, this self-generated word becomes the trigger. When a later harmful query arrives, the model detects its own trigger and bypasses its safety refusal, while the user input stays perfectly clean. Across four LLMs, our attack reaches near-perfect Attack Success Rates, approaching 100\% at only a 5\% poisoning rate, while preserving general utility and clean-input safety, and it evades mainstream input-centric defenses. Representation-level analysis shows that the self-generated trigger consistently suppresses the model's refusal signal, exposing a critical blind spot in current LLM defenses.

## Metadata
- **Published**: 2026-10-06T04:17:18Z
- **Authors**: Yibo Zhang, Tianrong Guan, Liang Lin, Puze Wang, Jin Wang, Qingsong Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07723v1)