---
title: LongSocialBench: Do Long-Context LLMs Understand Online Discussion Threads?
published: 2026-10-02T22:47:29Z
authors: Xinyi Liu, Rinat Khaziev, Dilek Hakkani-Tür, Tarek F. Abdelzaher
url: http://arxiv.org/abs/2610.04118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongSocialBench: Do Long-Context LLMs Understand Online Discussion Threads?

## Abstract
Long-context LLMs can now ingest entire online discussion threads, but understanding their social discourse requires more than reading a long document: models must track parent-reply relations, turning points, scoped subtrees, cross-branch contrasts, and participant trajectories. To test this structure-aware social reasoning, we introduce LongSocialBench, a benchmark of 1,462 verified human-authored multiple-choice items drawn from 94 complete Hacker News, Stack Exchange, and Reddit r/ChangeMyView episodes, with a median length of approximately 73K tokens. Each item pairs a complete serialized discussion and reply structure with a four-option question, requiring models to recover structured social evidence. Released items are verified for answerability, option uniqueness, and evidence grounding. Across 18 models and 29 evaluation settings, current long-context workflows remain far below human performance. The best individual result comes from Claude-Opus-4.7, which reaches 63.0% when prompted to eliminate incorrect options before answering, compared with 72.4% for independent human readers. Averaged across all 18 models, the full-context Baseline scores 43.9%. Supplying the gold evidence scope raises this to 55.0%, showing that substantial errors remain even after the relevant thread region is identified. LongSocialBench shows that the missing capability is not context access or prompting alone, but social understanding over structured reply trees.

## Metadata
- **Published**: 2026-10-02T22:47:29Z
- **Authors**: Xinyi Liu, Rinat Khaziev, Dilek Hakkani-Tür, Tarek F. Abdelzaher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04118v1)