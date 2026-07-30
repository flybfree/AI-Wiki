---
title: MPEcho: A Melody and Phoneme-Aware Generative Framework for Controllable Cover Song Generation
url: http://arxiv.org/abs/2607.26698v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_09-45-13Z_MPEcho_AMelodyandPhoneme_AwareGenerativeFrameworkf.md
generated_at: 2026-07-29 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MPEcho, a melody and phoneme-aware generative framework for controllable cover song generation that reduces phoneme error rate (PER). By integrating an explicit phoneme encoder and a length regulator into the existing SongEcho model, MPEcho achieves higher lyric accuracy compared to prior approaches.

## Key Takeaways
- The paper proposes adding a phoneme encoder and a length regulator to the SongEcho framework to provide precise phoneme-level conditioning and temporal boundaries.
- It introduces Phonsa, a Whisper-based automatic transcription model that supplies high‑precision phoneme annotations for singing voices, addressing scarcity of audio‑phoneme pairs.
- Experimental results show MPEcho significantly reduces PER while preserving melodic content.

## Context
Cover song generation remains challenging because existing models rely on coarse F0 and V/UV tags that do not guarantee accurate lyrics. The integration of fine-grained phonemic information aligns with trends in speech synthesis where precise transcription improves model performance.

## Implications
This work advances controllable music generation by enabling reliable lyric reproduction, which is crucial for applications like karaoke services and personalized cover platforms. Practitioners can leverage Phonsa to obtain accurate phoneme annotations, improving downstream generative models across audio‑text tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26698v1)
