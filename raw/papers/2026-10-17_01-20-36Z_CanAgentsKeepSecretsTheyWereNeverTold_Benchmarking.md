---
title: Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin
published: 2026-10-17T01:20:36Z
authors: Qishun Yang, Shu Yang, Difei Xu, Di Wang, Meng Ding
url: http://arxiv.org/abs/2610.24359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin

## Abstract
To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions. Reusing such memories can lead an agent to state a sensitive relation while completing an ordinary task that does not require it. The relation to protect and the combination of clues that reveal it may remain hidden at memory write time, when later records and tasks are still unknown. In this paper, we introduce MemJoin, a privacy benchmark of 288 synthetic analysis cases in which the complete history entails a sensitive relation, but every individual session is insufficient. We evaluate six memory systems with the same answer-generating model, alongside full-history and no-history controls. Each system writes and updates memories in session order and later retrieves context for an ordinary task, while target annotations remain with the evaluator. We separately check which target attribute values appear in stored records and retrieved context, and whether the final answer states the complete, person-linked relation. In a separate paired test on a prespecified subset, removing shared identifiers and other connecting clues can change complete-relation output while all checked target attribute values remain visible. These findings show why checking attribute visibility alone is insufficient to evaluate what records from different sessions reveal together.

## Metadata
- **Published**: 2026-10-17T01:20:36Z
- **Authors**: Qishun Yang, Shu Yang, Difei Xu, Di Wang, Meng Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24359v1)