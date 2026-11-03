---
title: Learning to Interact and Direct: Co-Evolving Video Director Agents
published: 2026-10-30T15:18:07Z
authors: Yingzhao Jian, Zhongan Wang, Yuxuan Hou, Hehe Fan
url: http://arxiv.org/abs/2610.41865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Interact and Direct: Co-Evolving Video Director Agents

## Abstract
Video director agents orchestrate multistage production to realize users' creative visions. Emerging research on their self-evolution advances screenplay planning effectively. However, the mutual reinforcement between directing and user interaction remains largely overlooked. Improved interaction clarifies user intent and informs workflow refinement, while more reliable execution shifts collaboration from troubleshooting to creative decisions. To this end, we introduce LIT (Learning to Interact and DirecT), a framework comprises a director agent, a simulated user, and a meta engineer. Simulated user assigns creative tasks to probe the director's weaknesses, while the meta engineer uses the task traces to revise the director's interaction and production strategy. Although this approach can address discovered interaction and production issues, it still relies on passive attribution by the meta agent. This limits its ability to adapt to broader user interaction patterns and production techniques. To solve this problem, we equip LIT with a co-evolution paradigm. The meta agent proactively learns external knowledge, thereby improving its ability to discover problems and propose solutions. The meta agent, simulated user, and director together form an evolutionary closed loop, collaboratively enhances the system's directing and interaction capabilities. Across the Test and OOD Test splits, LIT improves production and Interaction scores by 19.1% and 32.0%, respectively, relative to the initial pipeline. Controlled ablations reveal the correlation between improvements in production and interaction, where the co-evolution mechanism further encourage directing skill and interaction mode exploration.

## Metadata
- **Published**: 2026-10-30T15:18:07Z
- **Authors**: Yingzhao Jian, Zhongan Wang, Yuxuan Hou, Hehe Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.41865v1)