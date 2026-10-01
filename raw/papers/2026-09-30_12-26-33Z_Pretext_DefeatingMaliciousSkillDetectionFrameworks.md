---
title: Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents
published: 2026-09-30T12:26:33Z
authors: Tobias Kaisar, Aritra Dhar
url: http://arxiv.org/abs/2609.39607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents

## Abstract
Skills extend an agent's capabilities by injecting instructions and information into the context, and are widely used by agents such as OpenClaw and Claude Code. Prior work shows third-party marketplaces host malicious skills that give attackers direct influence over the victim's agent. The emerging defense scans skills before installation, pairing deterministic static checks with an LLM-based semantic judge, as in NVIDIA's SkillSpector. We show that such defenses fall to an attacker who knows the detector. Our white-box LLM attacker, Pretext, iteratively crafts skills that evade detection while still delivering the payload and performing the benign task: moving the payload from code into natural language leaves static analysis inert, while framing it as the skill's legitimate purpose and splitting instructions across files keeps the LLM stage below its blocking threshold. Across three open-source models, Pretext achieves up to 97\% and 77\% against a frozen detector and a co-adaptive one, respectively, revealing major gaps in current skill scanners.

## Metadata
- **Published**: 2026-09-30T12:26:33Z
- **Authors**: Tobias Kaisar, Aritra Dhar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39607v1)