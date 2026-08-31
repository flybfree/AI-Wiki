---
title: AI Writers Have a Consistent Stylometric Footprint, but AI Editors Do Not
url: http://arxiv.org/abs/2608.27855v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_02-58-58Z_AIWritersHaveaConsistentStylometricFootprint_butAI.md
generated_at: 2026-08-30 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether AI-generated and AI-edited texts leave similar stylometric footprints. It finds that generation creates a distinct pattern of high lexical diversity and low entropy, while editing only modestly changes these features and introduces lexical density as the main signal.

## Key Takeaways
- Generation leaves a consistent stylometric footprint dominated by entropy and lexical diversity across multiple LLMs and domains.
- Editing shows only small increases in lexical diversity and decreases in entropy, unlike generation’s joint increase.
- Lexical density becomes the primary editing‑associated feature and is less effective at distinguishing edited text from human writing.

## Context
Large language models are increasingly used for both content creation and post‑editing tasks, yet their stylometric signatures remain poorly understood. This study clarifies that AI generation and AI editing produce qualitatively different traces, which has been overlooked in prior research.

## Implications
Researchers must treat generation and editing as separate phenomena when developing detection methods. Practitioners should design tools that account for these distinct stylistic patterns to improve authenticity assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27855v1)
