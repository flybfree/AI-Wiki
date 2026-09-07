---
title: What Attention Recalls and Recurrence Controls in Hybrid Language Models
published: 2026-09-03T19:56:26Z
authors: Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Anton Korznikov
url: http://arxiv.org/abs/2609.04434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Attention Recalls and Recurrence Controls in Hybrid Language Models

## Abstract
Hybrid language models combine attention with a fixed-size recurrent state, but the role of each channel remains unclear. We introduce two cache-level interventions. Split-prefill keeps only the KV cache or only the recurrent state from a prefilled context, then generates an answer. State-swap pairs the KV cache from one context with the recurrent state from another in a single forward pass. On Qwen3.5 and Falcon-H1, the two channels split sharply by function. Exact retrieval survives only through attention (64-98% of full accuracy) and collapses to zero through recurrence. Output language and persona reverse the pattern: both survive recurrence (70-80% and 3-5x) while KV-only drops to ~1% language accuracy. State-swap confirms this causally: the answer takes its value from the KV side and its language from the recurrent side. Recurrent-only generation also accepts words that were never in the context but share meaning or parts with seen items. Attention provides a lookup over what was said; the recurrent state shapes how the model says it next.

## Metadata
- **Published**: 2026-09-03T19:56:26Z
- **Authors**: Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Anton Korznikov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04434v1)