---
title: "AI Model Release Coverage Watchlist"
type: reference
status: active
updated: "2026-09-22"
tags: [ai-intelligence, model-releases, frontier-models, open-weights, quality-control]
---

# AI Model Release Coverage Watchlist

This is a quality-control list for daily AI Intelligence briefings. Each high-signal release should be explicitly classified as **covered**, **deferred**, or **excluded with a reason**. A release should not disappear merely because a newer model in the same family arrives.

## Active watchlist

- [Grok 4.7](https://x.ai/news/grok-4-7) — frontier general model; released September 21, 2026. Check capabilities, agentic coding, context, pricing, and independent evaluation.
- [MiMo-V2.5](https://mimo.mi.com/docs/en-US/news/latest/v2.5-open-sourced) — open multimodal/reasoning family. Track separately from the later MiMo-V2.6 training and telemetry story.
- [Jev / System One Models](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — typed probabilistic decision model; not a conventional chat-model release.
- [YuE2](https://map-yue2.github.io/) — open music-generation model using an editable symbolic plan before rendering a song.
- [IFM K2 Horizon](https://ifm.ai/blog/k2) — fully open foundation-model fleet from 0.9B to 375B parameters.

## Coverage rules

1. **Model releases are first-class intelligence signals.** They must appear in the executive summary or a named model-release section when material.
2. **Track model families, not only the newest version.** MiMo-V2.5 remains a distinct release even when MiMo-V2.6 becomes the current focus.
3. **Cover diverse modalities.** General language, reasoning, agentic, decision, vision, audio, music, robotics, and multimodal releases all qualify when they materially change capability or access.
4. **Use first-party sources first.** Add benchmark, system-card, pricing, weights, license, and runtime links when available.
5. **State evidence quality.** Separate vendor claims, independent evaluations, community adoption, and verified deployment evidence.
6. **Record omissions explicitly.** If a release is not covered, the briefing must say whether it was missed, deferred for verification, or excluded as low-signal.

## Briefing QA command

From the wiki root:

```bash
python3 scripts/check_model_release_coverage.py --days 10
```

The check is intentionally a gate, not a replacement for judgment. A missing match requires review before publication; it does not automatically mean the model belongs in the final narrative.
