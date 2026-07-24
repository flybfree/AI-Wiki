---
title: What the Waveform Knows: Transparent-first Speech and Audio Intelligence with Caption Studio
published: 2026-07-21T04:56:00Z
authors: Cheng Siong Chin, Jianhua Zhang, Mohan Venkateshkumar
url: http://arxiv.org/abs/2607.18704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What the Waveform Knows: Transparent-first Speech and Audio Intelligence with Caption Studio

## Abstract
Caption Studio is a transparency-first speech and audio intelligence platform that transforms spoken audio and video into structured, searchable content through automated transcription, speaker diarization, speech analytics, signal-level audio analysis, and subtitle generation. The system is built on a FastAPI backend with a real-time dashboard and adopts a three-layer architecture comprising (i) a transcription and diarization core based on Whisper-class automatic speech recognition and pyannote speaker diarization, (ii) an audio intelligence layer that extracts acoustic and linguistic features, including waveforms, spectrograms, pitch, speaking rate, silence, filler-word frequency, and sentiment, directly from the audio signal, and (iii) an integration layer that supports data export and downstream workflow integration. A principal contribution of this work is the transparency-first framework, in which every reported metric is explicitly identified as measured, derived, or unavailable, thereby improving the traceability, interpretability, and reliability of speech analytics. The paper presents the system architecture, benchmarking methodology, explainability and uncertainty framework, and key considerations for enterprise-scale deployment.

## Metadata
- **Published**: 2026-07-21T04:56:00Z
- **Authors**: Cheng Siong Chin, Jianhua Zhang, Mohan Venkateshkumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18704v1)