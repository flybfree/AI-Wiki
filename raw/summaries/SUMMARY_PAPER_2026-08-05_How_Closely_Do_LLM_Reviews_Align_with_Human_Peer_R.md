---
title: How Closely Do LLM Reviews Align with Human Peer Review?
url: http://arxiv.org/abs/2608.03659v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-39-36Z_HowCloselyDoLLMReviewsAlignwithHumanPeerReview.md
generated_at: 2026-08-05 01:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates how three large language model reviewers align with human peer review decisions for 300 ICLR 2026 submissions. The models—OpenAI GPT‑5.4, Google Gemini 3.1 Pro Preview, and Anthropic Claude Opus 4.6—were given identical instructions after the final decision was removed, producing scores on a common scale. While all three distinguished accepted from rejected papers, none reproduced the oral versus poster distinction that humans used.

## Key Takeaways
- Gemini assigned systematically higher ratings across all categories, indicating a bias toward leniency rather than matching human preferences.  
- OpenAI and Claude performed closer to human judgments for rejected and poster papers but were more critical of oral submissions, revealing provider‑specific scoring patterns.  
- Human reviewers emphasized computational‑efficiency concerns, whereas LLMs frequently highlighted missing baseline comparisons as weaknesses.

## Context
The rapid adoption of AI‑generated reviews raises questions about their reliability in scientific evaluation. Existing work often compares models in isolation, but this study examines alignment across multiple providers and finer human judgments within a controlled setting, providing a more nuanced view of LLM performance.

## Implications
For researchers relying on automated review systems, the findings suggest that broad decision matching does not guarantee agreement with detailed human priorities. Practitioners should treat AI‑generated scores as probabilistic rather than definitive and consider additional validation steps to ensure alignment with specific conference criteria.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03659v1)
