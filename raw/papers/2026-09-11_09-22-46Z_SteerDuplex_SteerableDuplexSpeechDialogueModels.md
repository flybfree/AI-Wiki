---
title: SteerDuplex: Steerable Duplex Speech Dialogue Models
published: 2026-09-11T09:22:46Z
authors: Utkarsh Tyagi, Ramaneswaran Selvakumar, Advait Gosai, Sonal Kumar, Nikhil Barhate, Isabell Sagar, Steven Li, Miheer Bavare, Daniel Quigley, Fabiola Tapia Carrillo, Jose M Patron E, Diego Macías Gutiérrez, Paul Song, Ramani Duraiswami, Dinesh Manocha, Yunzhong He
url: http://arxiv.org/abs/2609.12623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SteerDuplex: Steerable Duplex Speech Dialogue Models

## Abstract
Full-duplex spoken dialogue models support low-latency turn taking, interruption handling, and backchanneling, yet a key capability remains underexplored: steerability, the ability to reliably shift conversational behavior along attributes such as tone, persona, speaking rate, and voice style in response to user instructions. We introduce a taxonomy of text- and audio-based steerability that identifies substantial gaps in current full-duplex models. To address this gap, we introduce SteerDuplex, a Moshi-based full-duplex speech model fine-tuned on natural conversations and synthetic dialogues targeting instruction following, vocal delivery, reasoning, and duplex interaction. We further apply two-stage reinforcement learning (RL) with hybrid rewards, combining verifiable interaction checks and judge-based semantic feedback to improve timing and response continuity. To evaluate full-duplex spoken steerability, we introduce SteerBench, a benchmark with 390 spoken prompts and 1,067 human-authored binary audio and text rubrics spanning tone, persona, style/accent, and speed/length. On SteerBench, supervised training improves audio-steering average pass rate by 44.5 percentage points over the strongest evaluated open baseline. On Audio MultiChallenge, task average pass rate improves by 7 points over its strongest evaluated open baseline. RL further raises source-clean interruption response from 72.5% to 82.5% and reduces synthetic pause barge-in from 26.5% to 9%. Steering and aggregate task scores remain comparable or higher, while reward probes reveal reward hacking through incomplete responses. Our model and benchmark support systematic research on spoken steerability, with reward analysis showing why timing gains must be evaluated alongside response completeness.

## Metadata
- **Published**: 2026-09-11T09:22:46Z
- **Authors**: Utkarsh Tyagi, Ramaneswaran Selvakumar, Advait Gosai, Sonal Kumar, Nikhil Barhate, Isabell Sagar, Steven Li, Miheer Bavare, Daniel Quigley, Fabiola Tapia Carrillo, Jose M Patron E, Diego Macías Gutiérrez, Paul Song, Ramani Duraiswami, Dinesh Manocha, Yunzhong He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12623v1)