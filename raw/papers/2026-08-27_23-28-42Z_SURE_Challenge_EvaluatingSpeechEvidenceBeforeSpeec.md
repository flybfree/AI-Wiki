---
title: SURE-Challenge: Evaluating Speech Evidence Before Speech-LLM Generation
published: 2026-08-27T23:28:42Z
authors: Mengzhe Geng
url: http://arxiv.org/abs/2608.27783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SURE-Challenge: Evaluating Speech Evidence Before Speech-LLM Generation

## Abstract
Speech LLMs are usually graded after they answer, although an operating system first has to decide whether a waveform should be sent to the model. We define the Speech-Unsupported Rejection Evaluation Challenge (SURE-Challenge) for this admission step. The benchmark pairs LibriSpeech-derived transcription and first-word question answering with unsupported silence, colored noise, synthetic tones, and source-ambiguous babble under disjoint source splits. Front-end ablations use Qwen2-Audio; the selected energy-plus-Whisper-score rule is then replayed before six speech/audio LLMs. On the 474-row leakage-screened SURE-Extended test set, raw Qwen2-Audio rejects 15/204 unsupported inputs, whereas the fixed rule rejects 196/204 and leaves supported accuracy unchanged. External checks delimit this number: Common Voice retention drops as the Whisper-score threshold is tightened, and no-speed babble gives 18 to 24 rejected clips out of 54 across regenerated seeds. The result identifies a pre-generation error mode missed by answer-only scoring.

## Metadata
- **Published**: 2026-08-27T23:28:42Z
- **Authors**: Mengzhe Geng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27783v1)