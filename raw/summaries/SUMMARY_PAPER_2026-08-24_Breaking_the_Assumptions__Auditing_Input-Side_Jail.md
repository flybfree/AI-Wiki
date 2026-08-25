---
title: Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks
url: http://arxiv.org/abs/2608.21895v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_10-14-23Z_BreakingtheAssumptions_AuditingInput_SideJailbreak.md
generated_at: 2026-08-24 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits defense mechanisms used in locally deployed LLMs against semantic jailbreak attacks, showing that many defenses rely on specific assumptions whose violations produce observable patterns. By testing six open-weight models across a large dataset of 13,800 records, the authors demonstrate that failures are not random but traceable to underlying assumptions such as smoothness or perplexity thresholds.

## Key Takeaways
- The study identifies that defenses like SmoothLLM and Erase-and-Check provide formal guarantees while others depend on empirical detection of smoothness, which can be bypassed when the assumption is violated.  
- Empirical patterns predicted by each defense’s condition are consistently observed in jailbreak prompts, revealing a systematic failure mode rather than isolated bugs.  
- The audit shows that local deployment removes API‑level moderation, making these assumptions critical for safety without external oversight.

## Context
Large language models increasingly influence content generation and decision making, yet their safety is often assumed to be inherent or enforced by cloud services. This paper highlights a gap: locally run models lack those safeguards, exposing the fragility of current defenses built on unproven assumptions.

## Implications
For developers deploying open‑weight LLMs offline, understanding which assumptions are violated can guide more robust design and testing. The findings urge industry to move beyond empirical fixes toward mathematically grounded safety mechanisms that hold across diverse model sizes and environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21895v1)
