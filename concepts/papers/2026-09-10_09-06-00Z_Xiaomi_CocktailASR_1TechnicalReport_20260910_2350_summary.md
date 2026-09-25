# Summary: 2026-09-10_09-06-00Z_Xiaomi_CocktailASR_1TechnicalReport.md
Saved: 2026-09-10 23:50
Source: 2026-09-10_09-06-00Z_Xiaomi_CocktailASR_1TechnicalReport.md
Model: None

---

## Summary
Xiaomi-CocktailASR-1 is an end-to-end target-speaker automatic speech recognition system for mixed-speaker audio. It uses reference speech as a voiceprint prompt to transcribe the target speaker without a separate speech-separation stage, while supporting rejection when the target speaker is absent.

## Findings
- The unified architecture targets the cocktail-party problem while retaining competitive single-speaker performance.
- Negative-sample rejection lets the system return empty output when the requested speaker is not present.
- The paper reports strong results across synthetic and real-world multispeaker benchmarks.

## Why It Matters
Specialist multimodal capability is moving into compact, end-to-end systems: speaker selection, transcription, and rejection are handled in one model rather than a brittle multi-stage pipeline. The reported benchmark results remain author claims until independently reproduced.

## Original Paper Reference
- **Source:** [Original Paper](https://arxiv.org/abs/2609.11274)
