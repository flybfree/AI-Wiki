---
title: CIDER: A Dataset of Contextual Disclosure Boundaries for Privacy Preference Alignment
url: http://arxiv.org/abs/2608.09164v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_06-17-19Z_CIDER_ADatasetofContextualDisclosureBoundariesforP.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CIDER, a dataset of 14,850 human annotations that capture users' nuanced disclosure boundaries in interpersonal communication scenarios. The study demonstrates that inference‑time personalization can improve prediction accuracy by up to 11.41 percentage points using only six historical examples, highlighting both the potential and limitations of personalized privacy alignment.

## Key Takeaways
- Human participants provide detailed boundary decisions across nine sharing variants per scenario, revealing individual privacy preferences that differ from generic norms.  
- In‑context personalization boosts model performance significantly, yet it often creates imbalanced shifts in false‑positive and false‑negative rates, with only Claude Sonnet 4.6 achieving balanced improvements.  
- Larger models such as GPT‑5.4 and Claude Sonnet 4.6 better leverage semantic context to understand user‑specific disclosure patterns, while smaller models rely on structured heuristics tied to disclosure granularity.

## Context
The work addresses a critical gap in evaluating how large language models align with human privacy preferences beyond broad norms. By providing fine‑grained, contextual data, CIDER enables researchers to test personalization strategies that adapt predictions to individual communication contexts, which is essential for real‑world deployment of privacy‑aware AI.

## Implications
For practitioners, the findings suggest that personalized inference can enhance model accuracy but must be managed carefully to avoid bias in error rates. The dataset offers a valuable resource for advancing research on contextual disclosure boundaries and informing industry practices aimed at delivering truly user‑centric privacy solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09164v1)
