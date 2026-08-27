---
title: ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives
published: 2026-08-26T08:39:09Z
authors: Jihao Zhu, Zhiwei Yang, Wenxiao Zhang, Junqian Zhao, Qi You, Fangqi Wang, Zheyuan Deng, Hanzhe Yang, Yu Liu, Jin B. Hong
url: http://arxiv.org/abs/2608.25531v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives

## Abstract
Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but directly feeding them an entire long context remains costly, hard to inspect, and prone to missing sparse evidence. We present ClueWeaver, an evidence-aware dual-agent framework for long-narrative question answering with compact local models. A Finder identifies passages containing answer-critical clues through retrieval-guided segmentation, while an Interpreter derives the answer from the selected evidence, produces rationales with paragraph-ID citations, and applies an internal self-calibration pass for high-risk questions. Both agents are optimized with reward-guided reinforcement learning: Finder rewards emphasize evidence retention and faithful paragraph-ID references, and Interpreter rewards emphasize correctness, grounding, and concise explanations. This decomposition makes evidence selection and reasoning more inspectable than end-to-end prompting. Experiments across multiple long-context narrative question answering and claim verification settings show that ClueWeaver substantially improves local end-to-end language models while providing evidence coverage and paragraph-referenced reasoning traces. Code is available at https://github.com/Ameame1/ClueWeaver.

## Metadata
- **Published**: 2026-08-26T08:39:09Z
- **Authors**: Jihao Zhu, Zhiwei Yang, Wenxiao Zhang, Junqian Zhao, Qi You, Fangqi Wang, Zheyuan Deng, Hanzhe Yang, Yu Liu, Jin B. Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25531v1)