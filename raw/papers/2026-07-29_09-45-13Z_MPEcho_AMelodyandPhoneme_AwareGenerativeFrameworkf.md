---
title: MPEcho: A Melody and Phoneme-Aware Generative Framework for Controllable Cover Song Generation
published: 2026-07-29T09:45:13Z
authors: Wei-Jaw Lee, Hsuan-Yu Yeh, Ting-Yi Hu, Chih-Pin Tan, Fang-Duo Tsai, Yi-Hsuan Yang
url: http://arxiv.org/abs/2607.26698v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MPEcho: A Melody and Phoneme-Aware Generative Framework for Controllable Cover Song Generation

## Abstract
Cover song generation (CSG) should preserve the melodic and linguistic content of a reference song while recreating the remaining musical components. The state-of-the-art model SongEcho utilizes $F_0$ sequences and voiced/unvoiced (V/UV) tags for conditioning; however, implicit linguistic information from V/UV tags cannot guarantee lyric accuracy, leading to a high phoneme error rate (PER). Inspired by singing voice synthesis (SVS), we propose MPEcho, which integrates a phoneme encoder and a length regulator (LR) into the SongEcho framework. By providing explicit phoneme-level conditioning and precise temporal boundaries, MPEcho significantly reduces PER. To enable this, we developed Phonsa, a Whisper-based automatic transcription model that provides high-precision phoneme-level annotations for singing voices, overcoming the scarcity of high-quality audio-phoneme pairs. Experimental results validate the effectiveness of Phonsa for alignment and MPEcho for end-to-end CSG. The audio samples, code and weights can be accessed from https://lonian6.github.io/MPEcho.github.io/.

## Metadata
- **Published**: 2026-07-29T09:45:13Z
- **Authors**: Wei-Jaw Lee, Hsuan-Yu Yeh, Ting-Yi Hu, Chih-Pin Tan, Fang-Duo Tsai, Yi-Hsuan Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26698v1)