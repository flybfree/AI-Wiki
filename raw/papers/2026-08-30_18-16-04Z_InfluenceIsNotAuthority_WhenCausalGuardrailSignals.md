---
title: Influence Is Not Authority: When Causal Guardrail Signals Make Legitimate Tool Use Look Like an Attack in Tool-Using LLM Agents
published: 2026-08-30T18:16:04Z
authors: Tanzim Ahad, Ismail Hossain, Md Jahangir Alam, Sai Puppala, Syed Bahauddin Alam, Sajedul Talukder
url: http://arxiv.org/abs/2608.29942v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Influence Is Not Authority: When Causal Guardrail Signals Make Legitimate Tool Use Look Like an Attack in Tool-Using LLM Agents

## Abstract
The key limitation of current state-of-the-art influence-based guardrails is that they do not reliably distinguish a legitimate, user-authorized action from a malicious, unauthorized action when both rely on external tool information. This ambiguity can cause benign actions to trigger unnecessary verification and intervention, reducing utility and adding latency. We expose this limitation through an authorization-equivalence audit of 96 conditions derived from 24 base cases. Within matched source comparisons, we hold authorization, the exact committed action, and its intended effect fixed, changing only whether a required value comes from the user or a legitimate tool result. Although the action remains unchanged, this harmless relocation shifts the causal signal toward the attack region in all 24 cases under both Llama and Gemma scorers. Matched unauthorized controls show that the signal remains attack-sensitive, yet the benign relocation produces a larger average score shift than the actual change in authorization. Architecture-level evaluation shows how this mismatch propagates through guardrail designs. With a semantic monitor, attack success is 0% and utility is 28%, compared with 16% and 60% without it. A shadow-based guardrail allows every tested harmless run, yet does not reject matched unauthorized actions more often overall: 57.5% of unauthorized runs pass automatically before reaching the later security check, compared with 29.2% of authorized runs. These results show that the studied causal signal reveals what shaped an action without reliably encoding whether the action was authorized, and that reference construction and routing are integral to the effective security decision.

## Metadata
- **Published**: 2026-08-30T18:16:04Z
- **Authors**: Tanzim Ahad, Ismail Hossain, Md Jahangir Alam, Sai Puppala, Syed Bahauddin Alam, Sajedul Talukder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29942v1)