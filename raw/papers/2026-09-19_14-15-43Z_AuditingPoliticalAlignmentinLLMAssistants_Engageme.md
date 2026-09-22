---
title: Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity
published: 2026-09-19T14:15:43Z
authors: Joan C. Timoneda
url: http://arxiv.org/abs/2609.23039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity

## Abstract
LLM-based AI systems answer political questions for hundreds of millions of people. Current audits measure what they say to an average user, but their behavior is dynamic. I argue that their political behavior is a set of policies over whom to answer, what to say, and whether to engage at all, conditional on the topic and what the system knows about the user. I call these policies the system's speech regime, which is how a developer settles the tradeoff between answering, accommodating the user, and refusing, each of which carries a cost that varies by topic. I derive a typology of five regimes from two dimensions, engagement and stance. I test six AI systems (OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek) in a preregistered experiment of 7,500 multi-turn conversations that randomly assign the user's political identity across five topics: abortion, Catalan independence, climate change, Nazism, and a zero-stakes control (pineapple on pizza). Two LLM judges from different developers score every answer, validated against human coding, and refusal is treated as an outcome rather than missing data. Every system accommodates the user on the control topic, showing that political restraint is a policy. On contested topics the systems fall into different regimes: on abortion, GPT engages and mirrors every user, Gemma refuses everyone, Claude answers strongly conservative users 35 percent of the time and almost no one else, and Grok accommodates conservatives only. On settled topics such as climate change and Nazism, five systems hold firm for every user. The systems also infer the user's overall ideology, so accommodation can spill over to topics not yet discussed. A comparison of two Grok releases shows the regime changing between versions in a way current audits miss. Speech regimes matter for alignment research and for polarization, political knowledge, and the quality of democracy.

## Metadata
- **Published**: 2026-09-19T14:15:43Z
- **Authors**: Joan C. Timoneda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23039v1)