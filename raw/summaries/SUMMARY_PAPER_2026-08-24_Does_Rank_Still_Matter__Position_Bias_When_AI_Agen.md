---
title: Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf
url: http://arxiv.org/abs/2608.22697v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_01-22-28Z_DoesRankStillMatter_PositionBiasWhenAIAgentsShopon.md
generated_at: 2026-08-24 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the position of search results influences AI agents' behavior when they purchase on behalf of users. By randomizing the order of hotel listings across many sessions and comparing four large language models to human data, the authors find that higher positions still attract more inspection but with weaker effects than expected.

## Key Takeaways
- Position predicts which listings are inspected even in AI‑driven searches, though the effect is not monotonic; middle items have lower inspection probability than bottom ones.
- The depth of search varies among models: some reach the choice stage while others stop earlier, a pattern that does not correspond to model provider or capability.
- All models converge on selecting the same undominated listing, suggesting that attributes displayed on the page matter more than placement.

## Context
This work highlights a shift from human‑centric search where ranking matters, to agentic search where agents can view entire result pages instantly. The findings challenge assumptions about monotonic importance of position and reveal model heterogeneity in decision making.

## Implications
For designers of AI shopping assistants, the paper suggests optimizing displayed attributes rather than relying on rank alone. It also warns that current ranking systems may need adjustment if they do not account for non‑monotonic attention patterns in automated agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22697v1)
