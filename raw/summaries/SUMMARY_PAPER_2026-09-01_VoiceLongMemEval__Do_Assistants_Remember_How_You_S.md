---
title: VoiceLongMemEval: Do Assistants Remember How You Sounded?
url: http://arxiv.org/abs/2609.00570v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-06-10Z_VoiceLongMemEval_DoAssistantsRememberHowYouSounded.md
generated_at: 2026-09-01 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VoiceLongMemEval (VLME), a benchmark that evaluates AI assistants on how they remember the spoken aspects of conversation, such as emotion labels, prosody descriptors, and voice events. The study shows that when only the textual transcript is provided, leading language models perform poorly, but adding paralinguistic metadata improves accuracy by 0.09 to 0.38 (or up to 0.61 to 0.69 with hints). Audio‑native models can extract these cues directly from speech and achieve higher scores than blind baselines.

## Key Takeaways
- Strong language models fail when given only the transcript, highlighting a gap in handling human interaction dynamics.
- Providing text‑track paralinguistic metadata yields an accuracy boost of 0.09 to 0.38 (or 0.61 to 0.69 with evidence hints).
- Audio‑native models extract cues directly from speech, achieving performance of 0.354 to 0.412 versus a blind baseline of 0.325.

## Context
Current AI benchmarks focus on information retrieval over long dialogue histories or temporal reasoning but largely ignore the fundamental human‑agent interaction dynamics such as voice and emotion cues. Multi‑agent architectures increasingly rely on continuous conversation, yet these models are not equipped to remember how users sounded. This paper fills that gap by emphasizing paralinguistic metadata as a critical component of conversational memory.

## Implications
The findings suggest that industry practitioners must integrate audio and emotional metadata into AI assistants to improve responsiveness and personalization. Ignoring voice cues leads to suboptimal performance, so embedding these signals could enhance user experience across various applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00570v1)
