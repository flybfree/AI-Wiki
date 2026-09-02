---
title: FinLifeBench: Exhaustive Life-Event History and Financial-State Reconstruction from Longitudinal Banking Dialogue
published: 2026-09-01T13:06:27Z
authors: Hangyeul Lee, Juyoung Oh, Jaeyong Ko, Sunmin Kim, Jaeik Park, Hyunkyu Kim, Jungmin Son, Pilsung Kang
url: http://arxiv.org/abs/2609.01198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinLifeBench: Exhaustive Life-Event History and Financial-State Reconstruction from Longitudinal Banking Dialogue

## Abstract
Repeated banking interactions require assistants to maintain complete, current, and traceable customer records as life changes emerge incidentally in routine requests. Existing benchmarks emphasize question answering, bounded episodes, or targeted recall rather than exhaustive longitudinal reconstruction. We introduce FinLifeBench, which evaluates two tasks over the same cumulative dialogue: reconstructing every life-event instance with its first-establishing session and reconstructing a complete 34-path financial state at consecutive checkpoints. The benchmark contains 6,000 eight-turn Korean banking sessions from 20 independent synthetic trajectories, with deterministic, exhaustive gold for 24 event types and 34 state paths and consensus quality assurance. Across eleven LLMs under a full-context condition, event-anchor recall falls from 0.591 at 15 sessions to 0.445 at 300. Errors are driven primarily by omitted events rather than poor anchor localization, while financial-state reconstruction frequently treats superseded or potentially outdated information as current; the best GCA@15 reaches 0.470. Performance on the two reconstruction tasks is only weakly associated. These results show that models can localize evidence for recovered events while still failing to maintain complete and temporally valid longitudinal records.

## Metadata
- **Published**: 2026-09-01T13:06:27Z
- **Authors**: Hangyeul Lee, Juyoung Oh, Jaeyong Ko, Sunmin Kim, Jaeik Park, Hyunkyu Kim, Jungmin Son, Pilsung Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01198v1)