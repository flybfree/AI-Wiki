---
title: Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf
published: 2026-09-11T05:10:00Z
authors: Yu-Yu Yang, Ti-Rong Wu, Hung Guei, Hsing-Yu Chen, I-Chen Wu
url: http://arxiv.org/abs/2609.12446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf

## Abstract
Social-deduction games such as Werewolf are increasingly used to evaluate LLM agents, but existing evaluations often rely on final game outcomes. We propose a belief-shift evaluation benchmark in Werewolf for analyzing communication skills through belief updating. Using LLM-played games, we annotate suspicion and accusation messages and measure how an observing village-side model's beliefs change after each message. We evaluate 40 open-weight LLM configurations on 1,224 annotated messages. Our results show that larger models better distinguish true wolves from villagers based on game history, but accusations still strongly influence their beliefs. Models become more suspicious of the accused target and less suspicious of the accuser, especially when the accuser is trusted, even if the accuser is wolf-aligned. Larger models better resist accusations from accusers they already distrust. Overall, our findings suggest that current open-weight LLMs up to 120B parameters still struggle to integrate accusation content with source trust in strategic communication. Our benchmark and code are available at https://rlg.iis.sinica.edu.tw/papers/werewolf-accusation-benchmark.

## Metadata
- **Published**: 2026-09-11T05:10:00Z
- **Authors**: Yu-Yu Yang, Ti-Rong Wu, Hung Guei, Hsing-Yu Chen, I-Chen Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12446v1)