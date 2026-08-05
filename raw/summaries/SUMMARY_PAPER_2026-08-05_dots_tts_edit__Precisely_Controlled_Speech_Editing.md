---
title: dots.tts.edit: Precisely Controlled Speech Editing with a Continuous Autoregressive Model
url: http://arxiv.org/abs/2608.02673v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-02_15-03-37Z_dots_tts_edit_PreciselyControlledSpeechEditingwith.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces dots.tts.edit, a system that precisely controls speech editing using XML-style tags and a continuous autoregressive model. It achieves high instruction following and local preservation while maintaining audio quality comparable to existing TTS systems.

## Key Takeaways
- The system uses transcript-grounded structural edit instructions with XML-style tags to specify operations and target regions explicitly, avoiding ambiguous natural language.
- Four editing controls—lexical content, affective expression, pitch/speaking-rate, temporal phrasing—are demonstrated with a bilingual evaluation suite doteBench measuring instruction following, local preservation, and audio quality.
- Experiments show the model follows instructions and preserves surrounding context while keeping TTS recognition error rates and speaker similarity nearly unchanged from the base model.

## Context
Speech editing is crucial for content creation but often suffers from ambiguous natural language prompts. Continuous autoregressive models like dots.tts provide a foundation for high-quality synthesis, yet precise control over edits remains challenging. This work bridges that gap by offering an explicit interface that aligns with the transcript and preserves source context.

## Implications
For developers, this provides a reliable way to generate edited speech without sacrificing quality or speaker identity. In industry, it enables automated dubbing, voice modulation, and localized content adaptation at scale. Practitioners can integrate precise editing commands into existing TTS pipelines for better user control.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02673v1)
