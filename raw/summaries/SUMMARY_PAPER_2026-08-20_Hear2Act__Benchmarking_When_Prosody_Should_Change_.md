---
title: Hear2Act: Benchmarking When Prosody Should Change What an Assistant Does
url: http://arxiv.org/abs/2608.19515v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_00-16-36Z_Hear2Act_BenchmarkingWhenProsodyShouldChangeWhatan.md
generated_at: 2026-08-20 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Hear2Act, a unified benchmark that tests whether prosodic cues influence task‑oriented assistant behavior when lexical information is limited or absent. The study compares audio‑capable large language models across scenarios where the same user concern is conveyed either through words alone, via prosody only, or through an explicit textual representation of the concern. Results show modest gains in optimal‑solution rates with audio input (14.6% → 15.3%) when only prosody is used, but substantial improvements (up to 39.6%) when models translate audio into a representable state for action selection.

## Key Takeaways
- Adding audio to the transcript raises the optimal‑solution rate modestly from 14.6% to 15.3%, indicating that raw prosody alone has limited impact on downstream decisions.
- Models that infer and represent concern status from audio, then use it for next‑action selection achieve a higher success rate (39.6%) close to the ground‑truth performance of 40.7%.
- The advantage disappears under explicit lexical feedback where the concern is verbally mentioned in the utterance.

## Context
The paper addresses a gap in existing dialogue evaluation protocols that treat prosody perception, response appropriateness, and task execution as separate dimensions. By integrating these factors into a single benchmark with hidden user concerns, it provides a more realistic test of multimodal reasoning for assistants that process both text and speech.

## Implications
For developers building audio‑capable assistants, the findings suggest that merely adding audio to transcripts is insufficient; models must explicitly encode prosodic information into internal representations. Practitioners should design evaluation frameworks that capture multimodal interactions to guide more effective system design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19515v1)
