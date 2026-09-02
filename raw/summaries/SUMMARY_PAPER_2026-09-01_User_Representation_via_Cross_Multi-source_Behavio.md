---
title: User Representation via Cross Multi-source Behavior Pre-training for Mobile Games
url: http://arxiv.org/abs/2609.01057v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_10-53-47Z_UserRepresentationviaCrossMulti_sourceBehaviorPre_.md
generated_at: 2026-09-01 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CM-PTM, a cross‑multi‑source behavior pre‑training model designed to learn user representations from heterogeneous mobile device logs. The authors show that the model outperforms previous app‑centric approaches on large real‑world datasets and improves downstream game recommendation tasks.

## Key Takeaways
- CM-PTM uses hierarchical cascaded mask‑then‑predict proxy tasks to infer behavior sources before refining predictions at the app‑action level, enabling unified modeling of cross‑source dependencies.  
- The model captures users’ endogenous interests by leveraging multi‑granular behavioral logs that are typically ignored in single‑app studies.  
- Extensive experiments on large mobile datasets demonstrate consistent performance gains across multiple recommendation benchmarks.

## Context
User representation learning remains a core challenge in personalization, especially when data is sparse and sources are diverse. Existing methods often treat each app or source in isolation, missing the rich interplay of user actions across devices and applications.

## Implications
The findings suggest that device‑level pre‑training can unlock deeper insights into user behavior, benefiting both research on scalable personalization and industry practitioners seeking more accurate game recommendations with limited data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01057v1)
