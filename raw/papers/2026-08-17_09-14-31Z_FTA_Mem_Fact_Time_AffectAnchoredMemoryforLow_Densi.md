---
title: FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue
published: 2026-08-17T09:14:31Z
authors: Chang Liu, Shuyi Zhang, Changsheng Ma, Yongfeng Tao, Minqiang Yang, Bin Hu
url: http://arxiv.org/abs/2608.16303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue

## Abstract
Long-term emotional-support agents require memory mechanisms for personalized understanding across sessions. However, emotional-support dialogue is often low-density: turns are incomplete, evidence is scattered, and user states evolve over time. Existing memory methods usually rely on fixed units, such as turn-level notes or session summaries, which may lose details or introduce redundant noise. We propose FTA-Mem, a structured memory framework for low-density long-term dialogue. FTA-Mem uses Boundary-preserving Window Segmentation (BWS) to form coherent situation fragments, and constructs Fact-Time-Affect Memory Units (FTA Units) that jointly encode factual content, temporal grounding, and affective context. Retrieved units are then synthesized into structured context for answer generation. Experiments on ES-MemEval and LoCoMo show that FTA-Mem improves overall long-term memory question answering across benchmarks with different information-density characteristics. On ES-MemEval, FTA-Mem achieves 0.3871 F1 and 0.6668 BERTScore. Further analysis shows that situation-level FTA construction better balances evidence preservation and construction cost than coarse session-level or overly fine-grained turn-pair construction, providing an effective granularity trade-off for long-term dialogue memory.

## Metadata
- **Published**: 2026-08-17T09:14:31Z
- **Authors**: Chang Liu, Shuyi Zhang, Changsheng Ma, Yongfeng Tao, Minqiang Yang, Bin Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16303v1)