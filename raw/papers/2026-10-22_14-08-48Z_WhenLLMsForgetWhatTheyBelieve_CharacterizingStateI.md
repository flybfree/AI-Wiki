---
title: When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues
published: 2026-10-22T14:08:48Z
authors: Yancheng Zhu, Yifan Yuan
url: http://arxiv.org/abs/2610.31314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues

## Abstract
Large language models can repeat an instruction while failing to keep obeying it. We study this recall-compliance dissociation in long-horizon dialogue and define State Integrity Collapse: a model preserves a stated constraint in memory but stops applying it to later turns. We introduce StateTrack-Bench, a controlled suite of conversations covering numerical, format, role/persona, factual-memory, and logical-rule constraints. Across seven provider-pinned model snapshots and five dialogue-depth probes, strict joint retention ranges from 62.4% to 100.0%, with degradation concentrated in symbolic constraints and in one especially brittle model. A forked recall audit shows that 88.6% of observed failures are behavioral-drift failures rather than ordinary forgetting; excluding the brittle outlier preserves this diagnosis (84.4% of failures). Extended evaluations at depths up to 50 turns confirm that the dissociation persists beyond the core benchmark, while Structured State Anchoring recovers up to 24.4 points on immutable constraints. The results show that reliability cannot be inferred from single-turn instruction following alone; evaluation must track whether remembered constraints remain operational as dialogue state grows. Code and artifacts are available at: https://github.com/xzzvsxd/StateTrack.

## Metadata
- **Published**: 2026-10-22T14:08:48Z
- **Authors**: Yancheng Zhu, Yifan Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31314v1)