---
title: I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents
published: 2026-11-06T00:06:13Z
authors: Parth Illendula, Garik Livingston, Zain Shamsi, Ravi Srinivasan, Alex Liu
url: http://arxiv.org/abs/2611.08811v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents

## Abstract
Large Reasoning Models (LRMs) are one of the key components of current agentic systems. LRMs augment their output with an explicit chain-of-thought reasoning stage, introducing a new attack surface for thought injection, in which untrusted text resembling the model's own deliberation is fed back to the model. We present a two-part study of this attack, performed against the prevailing large, production class open-weight models (e.g., GLM-5.3, MiniMax-M2.5, Qwen3.8-Flash-Next). We first evaluate the effectiveness of static thought-injection prompts under different styles as well as tagged and untagged conditions and find that the effects of thinking tags and payload styles are all properties of the specific target model. In the second study, we exploit this model-specificity in a containerized agentic cyber range, using indirect injection prompts styled in the form of the target model's own reasoning traces to achieve attack success rates (ASR) up to 50% on operational objectives such as reverse-shell exfiltration and repository backdooring. We also find that the same malicious objective in standard prompt injection user voice never succeeds, and thinking tags suppress the agent's tendency to disclose the injection. Our results show that imitating a reasoning model's own thought style is effective for this style of attack, and that tag stripping is an unreliable defense.

## Metadata
- **Published**: 2026-11-06T00:06:13Z
- **Authors**: Parth Illendula, Garik Livingston, Zain Shamsi, Ravi Srinivasan, Alex Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.08811v1)