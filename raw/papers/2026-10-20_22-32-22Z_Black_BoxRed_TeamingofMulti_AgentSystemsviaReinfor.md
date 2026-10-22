---
title: Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning
published: 2026-10-20T22:32:22Z
authors: Yuqi Jia, Hangsheng Zhang, Chenxi Liu, Junjie Liang, Xun Chen
url: http://arxiv.org/abs/2610.28966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning

## Abstract
Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not directly interact with the user. Therefore, we introduce ReMAS, the first reinforcement learning-based red-teaming framework tailored to MASs, which fine-tunes attacker LLMs to generate effective adversarial prompts for system prompt extraction. The framework follows a two-step process: first, a rewrite stage refines base attack prompts to increase extraction success, and second, a template generation stage constructs attack templates that improve the likelihood of invoking specific sub-agents and thus revealing their system prompts. Extensive experiments show that our method substantially improves attack success rates compared to existing black-box attacks, with transferability across different backend LLMs and MAS structures. These results underscore the vulnerabilities of multi-agent systems and the importance of developing stronger defenses against adaptive black-box adversaries.

## Metadata
- **Published**: 2026-10-20T22:32:22Z
- **Authors**: Yuqi Jia, Hangsheng Zhang, Chenxi Liu, Junjie Liang, Xun Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28966v1)