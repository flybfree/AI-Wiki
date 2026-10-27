---
title: Adaptive Memory Index Evolution for Agents
published: 2026-10-26T07:50:16Z
authors: Yuntong Hu, Tongli Su, Yuanfu Sun, Shuo Ma, Qiaoyu Tan, Liang Zhao
url: http://arxiv.org/abs/2610.34977v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Memory Index Evolution for Agents

## Abstract
Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate this target as Memory Index Evolution and instantiate it with Adaptive Memory Index Evolution (AMIE), a lightweight plug-in layer that evolves per-memory access state from deployment retrievals without modifying stored content or retraining the host memory system. AMIE distils a semantic teacher's keep/suppress judgments into a retrieval-conditioned policy and accumulates its selective actions into bounded state that reweights subsequent host retrievals. Surprisingly, even a zero-call policy that simply accumulates retrieval frequency can match or outperform semantic policies in several settings, revealing retrieval traffic itself as a strong signal for access adaptation, while learned selectivity improves robustness when frequently retrieved memories remain useful. Across five retrieval-based hosts and three benchmarks, trained AMIE improves downstream F1 or accuracy in all 15 comparisons, by 0.70--3.37 percentage points (up to 25% relative), and improves retrieval in all 10 comparisons. Controlled analyses show that persistent competitor suppression can expose previously unseen evidence, while suppressing repeatedly useful memories creates the complementary failure mode. Together, these results establish persistent memory access as a practical adaptation layer, distinct from the content it serves, in retrieval-based agent memory systems.

## Metadata
- **Published**: 2026-10-26T07:50:16Z
- **Authors**: Yuntong Hu, Tongli Su, Yuanfu Sun, Shuo Ma, Qiaoyu Tan, Liang Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34977v1)