---
title: RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue
published: 2026-09-15T04:19:53Z
authors: Yuqi Wang, Fengyuan Liu, Haochen Luo, Zhiqi Yu, Qi Liu
url: http://arxiv.org/abs/2609.16614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue

## Abstract
Speech-to-speech dialogue models increasingly support persona control, yet existing spoken role-playing benchmarks remain largely character-centric and short-horizon. This leaves open whether spoken dialogue models can sustain diverse roles over extended interactions, especially beyond predefined fictional characters. We introduce RoleBreak, an open benchmark for long-horizon role-playing robustness in spoken dialogue. RoleBreak contains 310 character-based and user-centered roles, 6,688 human-verified dialogue turns, and 11,743 fine-grained evaluation criteria, with 1,856 turns carrying expressive emotion targets for evaluating vocal emotion. Its scenarios are designed to stress role consistency, interaction quality, safety, and affect over extended conversations. We evaluate nine configurations spanning full-duplex, omni-modal, and cascaded ASR--LLM--TTS paradigms. We find four key patterns. First, current systems are substantially stronger at semantic role adherence than at vocal emotion. Second, semantic robustness remains brittle over long interactions: even the strongest evaluated system encounters its first persona and safety failures after only 10.4 and 11.6 turns on average. Third, scaling the LLM substantially improves semantic robustness and delays failure, but yields little improvement in vocal emotion. Finally, user vocal emotion affects role-playing behavior even when linguistic content is fixed. These findings highlight persistent gaps in both long-horizon robustness and vocal expressiveness in spoken role-playing systems.

## Metadata
- **Published**: 2026-09-15T04:19:53Z
- **Authors**: Yuqi Wang, Fengyuan Liu, Haochen Luo, Zhiqi Yu, Qi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16614v1)