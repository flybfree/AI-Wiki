---
title: TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling
url: http://arxiv.org/abs/2608.19737v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-37-10Z_TempJail_TemporalJailbreakAttackagainstLargeVision.md
generated_at: 2026-08-20 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TempJail, a black‑box video jailbreak that exploits temporal vulnerabilities in large vision‑language models by manipulating subtitle sequences to satisfy harmful query intentions. Experiments on four LVLMs and two datasets show the attack achieves significantly higher success rates than existing methods, with gains of 53 % for GPT‑5 and 18 % for Gemini 3.5‑Flash.

## Key Takeaways
- TempJail demonstrates that jailbreak effectiveness depends not only on subtitle semantics but also on how those subtitles are scheduled over time, including duration and placement within the video timeline.  
- The framework constructs dialogue‑style subtitle sequences aligned with the query’s harmful intent, allowing precise temporal control without visual intrusion.  
- On all evaluated model–dataset combinations, TempJail outperforms the strongest baseline by a large margin in average success rate.

## Context
Video jailbreak research has traditionally focused on textual or image manipulation, ignoring the temporal dimension of video content. This work highlights that timing is as crucial as content for exploiting language‑vision models, opening new avenues for adversarial testing beyond static media.

## Implications
For practitioners, TempJail underscores the need to consider temporal dynamics in AI safety evaluations and prompts. Industry stakeholders should incorporate temporal constraints into model robustness assessments to prevent exploitation through subtly timed cues.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19737v1)
