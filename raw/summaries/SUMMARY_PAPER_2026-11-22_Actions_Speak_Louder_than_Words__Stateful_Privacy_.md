---
title: Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions
url: http://arxiv.org/abs/2611.27046v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_03-17-51Z_ActionsSpeakLouderthanWords_StatefulPrivacySniffin.md
generated_at: 2026-11-22 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SNOOP, a stateful hierarchical probing framework that exploits behavioral covert channels in LLM agents' web interactions to recover fine-grained private user context without any explicit transmission of sensitive content. The authors demonstrate that an agent's browsing decisions—what it searches, which links it follows, and in what order it reads pages—encode user prompts, dialogue history, and profiles, achieving average F1 scores of 0.89 for query concept recovery and 0.80 for user profile reconstruction across multiple agents and LLM backbones. They further propose Selection-Obfuscated Retrieval (SOR) as a defense mechanism that reduces SNOOP's recovery performance to 0.39 F1 without requiring additional LLM inference.

## Key Takeaways
- Behavioral covert channels represent a fundamentally new privacy attack surface for LLM agents: unlike prior passive network traffic analysis (which yields only coarse correlations) or indirect prompt injection attacks (which require placing sensitive content in outgoing fields and are blocked by content-level defenses), SNOOP actively reconstructs private context purely from the observable pattern of an agent's web navigation decisions, meaning no sensitive content is ever transmitted and content-level inspection cannot detect the leakage.
- SNOOP operates as a stateful hierarchical probing framework that narrows a coarse-to-fine hypothesis tree per task, leveraging the agent's benign web decisions as a signal channel. Evaluated across four agents and three LLM backbones on 500 StackExchange queries and 378 multi-turn iKAT dialogues, it achieves strong recovery performance, and four representative agent defenses alter its recovery by less than 0.03 F1, indicating that current defensive strategies are largely ineffective against this class of attack.
- Selection-Obfuscated Retrieval (SOR) offers a practical mitigation by acquiring resources under a fixed budget independent of private context and confining the agent's selection to a local snapshot, cutting SNOOP's F1 to 0.39 without additional LLM inference overhead, suggesting that architectural changes to how agents retrieve information can meaningfully reduce behavioral leakage.

## Context
As LLM agents increasingly perform complex tasks through web interaction—issuing searches, following links, and reading pages—their actions become driven by private user context including prompts, dialogue history, memory, and connected data sources. This paper addresses a gap in the privacy literature: prior work either passively analyzed network traffic or relied on prompt injection techniques that are detectable by content-level defenses. By identifying that the mere pattern of an agent's navigation choices constitutes a covert information channel, this work expands the threat model for agent privacy and challenges the assumption that agents are safe as long as no sensitive text is explicitly transmitted.

## Implications
For practitioners deploying LLM agents in sensitive domains such as healthcare, finance, or legal research, this work demonstrates that existing content-filtering and prompt-injection defenses are insufficient to protect user privacy, since the agent's behavioral choices alone leak fine-grained context. Industry teams building agentic systems should consider architectural mitigations like SOR—fixed-budget retrieval and local snapshot confinement—as part of their privacy-by-design strategy, and researchers should treat agent action patterns as a first-class privacy concern rather than focusing solely on transmitted content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27046v1)
