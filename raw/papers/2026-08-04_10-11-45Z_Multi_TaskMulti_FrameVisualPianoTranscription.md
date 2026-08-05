---
title: Multi-Task Multi-Frame Visual Piano Transcription
published: 2026-08-04T10:11:45Z
authors: Yonghyun Kim, Hoyeol Sohn, Juhan Nam, Alexander Lerch
url: http://arxiv.org/abs/2608.03419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Task Multi-Frame Visual Piano Transcription

## Abstract
Audio-based piano transcription performs well on onset, pitch, and velocity, but the sustain pedal lets sound persist long after key release, so audio systems predict pedal-extended offsets rather than physical key release. Yet existing Visual Piano Transcription (VPT) systems focus on onset detection from short video windows, offset accuracy lags onset by a wide margin, and note-level velocity has not been reported. To address these gaps, we present V2N (Video to Notes), the first complete VPT system: a shared temporal backbone feeds task-specific heads for onset, offset, key hold, and velocity, jointly trained with per-frame supervision rather than only at the window center. Ablations show that multi-task supervision enables offset and velocity prediction while improving onset accuracy; longer temporal context yields further improvements. V2N sets new state-of-the-art results on PianoVAM and R3.

## Metadata
- **Published**: 2026-08-04T10:11:45Z
- **Authors**: Yonghyun Kim, Hoyeol Sohn, Juhan Nam, Alexander Lerch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03419v1)