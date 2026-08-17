---
title: Leading-Silence Augmentation and Multi-Stage Synthetic Supervision for the Second MLC-SLM Challenge
published: 2026-08-14T10:00:42Z
authors: Kexin Shi, Renhe Sun, Yuge Huang, Ximeng Wang, Jiayi Zhou, Jian Liu, Malu Zhang
url: http://arxiv.org/abs/2608.14150v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leading-Silence Augmentation and Multi-Stage Synthetic Supervision for the Second MLC-SLM Challenge

## Abstract
The second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge evaluates two tasks over complete, unsegmented multilingual conversations: speaker diarization and recognition (Task 1) and conversational speech understanding (Task 2). Neither task provides oracle utterance boundaries or speaker labels at evaluation, and Task 2 provides no question-answer training set. For Task 1, we fine-tune VibeVoice-ASR-7B with random leading-silence cropping, consistent timestamp correction, and an exponential moving average (EMA) training strategy. For Task 2, we construct synthetic question-answer pairs through multimodal candidate generation, silent-audio filtering, and distribution-matched augmentation, and fine-tune Qwen3-Omni-30B-A3B-Instruct for tagged direct answering. On the Task 1 evaluation set, cropping reduces tcpMER from 18.30% to 17.27%, and EMA further reduces it to 16.73%. On the Task 2 evaluation set, jointly applying distribution-matched augmentation and tagged direct answering raises accuracy from 83.0% to 86.0%.

## Metadata
- **Published**: 2026-08-14T10:00:42Z
- **Authors**: Kexin Shi, Renhe Sun, Yuge Huang, Ximeng Wang, Jiayi Zhou, Jian Liu, Malu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14150v1)