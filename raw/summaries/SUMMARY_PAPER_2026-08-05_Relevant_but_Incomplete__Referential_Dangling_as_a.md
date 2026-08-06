---
title: Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure Mode in Hard Prompt Compression
url: http://arxiv.org/abs/2608.04569v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_07-58-53Z_RelevantbutIncomplete_ReferentialDanglingasaParadi.md
generated_at: 2026-08-05 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates a structural flaw in hard prompt compression where independent token selection can leave essential supporting information absent, causing referential dangling that breaks answer coherence. Experiments on multiple multi‑hop QA datasets show dangling rates up to 60% and reinserting missing support restores accuracy by 29–34 points without increasing the compression ratio.

## Key Takeaways
- Independent scoring can split dependent evidence pairs, leaving an answer but deleting the entity that defines it, which the authors label referential dangling.  
- At a 0.30 compression ratio, Beaver leaves incomplete answer paths in 34–54% of bridge examples across three datasets, and all six hard compressors exhibit dangling rates up to 60%.  
- Reinserting omitted sentences improves accuracy by 4.7 points on HotpotQA while only raising the compression ratio from 0.30 to 0.31.

## Context
Hard prompt compression aims to lower inference cost by discarding low‑relevance content, but it often sacrifices referential completeness that is crucial for multi‑step reasoning tasks. This paper highlights a gap between efficiency gains and loss of logical coherence in compressed prompts.

## Implications
For practitioners building efficient language models, compressing prompts must consider both relevance and the preservation of necessary references to maintain answer quality. Ignoring dangling can degrade performance even with stronger models, prompting a shift toward methods that jointly optimize compression and referential completeness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04569v1)
