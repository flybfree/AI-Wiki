---
title: Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking
url: http://arxiv.org/abs/2608.21230v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_15-37-35Z_UtilityUnderAttack_AgentMemoryPoisoningandtheLimit.md
generated_at: 2026-08-23 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how persistent memory can be poisoned by inserting false statements into a long‑term evaluation corpus, showing that even minimal contamination drops retrieval accuracy dramatically. It also evaluates provenance‑weighted retrieval and concludes that adding provenance scores does not reliably improve performance because it either blocks legitimate untrusted evidence or fails to stop query‑shaped attacks.

## Key Takeaways
- Poisoning 1.2% of a LongMemEval corpus reduces accuracy from 0.850 to 0.300, demonstrating that persistent memory amplifies small errors into severe failures.
- A write‑time screening pipeline achieves high recall on indirect prompt injection but fails to reject poisoned memories because they are indistinguishable from benign text containing trigger words.
- Provenance weighting is ineffective: a weight strong enough to block attacks also suppresses valid untrusted evidence, leading to accuracy drops when answer‑bearing evidence is itself untrusted.

## Context
The study highlights a fundamental limitation of content‑only defenses in AI systems that rely on long‑term memory, where false information can persist across sessions. It underscores the difficulty of distinguishing malicious from benign statements without external grounding and suggests that current provenance mechanisms may be too blunt for real‑world use.

## Implications
For practitioners, this research calls for bounded occupancy constraints at retrieval rather than additive provenance penalties to avoid over‑blocking. The findings have broader implications for AI safety, emphasizing that robust defenses must balance accuracy preservation with the protection of legitimate untrusted content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21230v1)
