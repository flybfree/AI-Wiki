---
title: Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents
url: http://arxiv.org/abs/2609.36130v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_19-04-21Z_MemoryIsaDerivation_TheDistributed_EvidenceParadox.md
generated_at: 2026-09-29 20:38
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the derivation problem in long-term LLM agents, where persistent memories may not logically follow from interaction history due to scattered evidence or compression artifacts that introduce unsupported relations. The authors present DerivAudit, a framework evaluating whether memories are supported by write-time history across three dimensions: evidence scope, compositional validity, and admission reliability. Their results indicate that while expanding historical context recovers support for nearly 60% of seemingly unsupported memories, significant gaps persist, and broader evidence alone fails to prevent the admission of invalid memories across verification models.

## Key Takeaways
- The study highlights a distributed-evidence paradox where valid memories may appear unsupported because citations omit relevant evidence scattered across earlier interactions, while individually supported facts can be composed into stronger statements that the history never established, leading to false confidence in derived information.
- DerivAudit decomposes memory auditing into three coupled requirements: verifying if

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36130v1)
