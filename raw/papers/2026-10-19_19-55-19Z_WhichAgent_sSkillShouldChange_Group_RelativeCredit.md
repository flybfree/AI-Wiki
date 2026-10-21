---
title: Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams
published: 2026-10-19T19:55:19Z
authors: Yanan Ma, Yang Wang, David Le, Chenhan Yuan, Yizheng Sun, Guangwei Zhang, Chenghao Xiao, Chenghua Lin, Imon Banerjee
url: http://arxiv.org/abs/2610.27227v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams

## Abstract
Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present \textbf{GRSE}, \textbf{G}roup-\textbf{R}elative \textbf{S}kill \textbf{E}volution, which assigns behavioral credit by comparison: inspired by GRPO, it executes each question several times under the same skill libraries and contrasts the executions to credit agent--skill pairs, with structured diagnosis of failures. On HotpotQA and LoCoMo with two open-weight actors, GRSE outperforms MASkills, the closest prior method, on HotpotQA and every LoCoMo category except open-domain, with the largest gains on multi-hop questions ($+6.7$ and $+3.2$ F1). Its gains rest on better-grounded retrieval rather than answers given without evidence, and its learned skills transfer between the multi-hop tasks. GRSE is robust to corrupted libraries: starting from planted harmful skills, it credits every planted skill with the correct sign and recovers the score of a clean library ($+6.3$ points), whereas MASkills misattributes two and falls below its starting point.

## Metadata
- **Published**: 2026-10-19T19:55:19Z
- **Authors**: Yanan Ma, Yang Wang, David Le, Chenhan Yuan, Yizheng Sun, Guangwei Zhang, Chenghao Xiao, Chenghua Lin, Imon Banerjee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27227v1)