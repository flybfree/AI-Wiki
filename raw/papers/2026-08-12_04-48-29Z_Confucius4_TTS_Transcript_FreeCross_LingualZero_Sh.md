---
title: Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder
published: 2026-08-12T04:48:29Z
authors: Huaxuan Wang, Huimin Wang, Ruiyu Zhang, Yingjie Li, Yitao Duan
url: http://arxiv.org/abs/2608.11650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder

## Abstract
Recent advances in zero-shot text-to-speech (TTS) have substantially improved speech quality and voice cloning fidelity. However, many zero-shot TTS systems still depend on audio prompt transcripts at inference time. This dependency limits cross-lingual voice cloning, since in-the-wild reference audio is often untranscribed. In this technical report, we present Confucius4-TTS, a multilingual zero-shot TTS system that supports 14 languages and performs both intra-lingual and cross-lingual reference cloning without requiring transcripts of audio prompts. Confucius4-TTS follows a two-stage architecture, consisting of text-to-semantic (T2S) and semantic-to-acoustic (S2A) modules. The LLM-based T2S module uses a learnable speaker encoder to extract timbre features from self-supervised speech representations, and the conditional flow-matching S2A module converts the predicted semantic tokens into mel-spectrograms. The same model also supports continuation cloning when a reference transcript is available. Confucius4-TTS is trained on large-scale multilingual speech data. It achieves high intelligibility and speaker similarity on public benchmarks. On the CV3-Eval cross-lingual benchmark, Confucius4-TTS obtains an average WER of 3.73% across six directions. On our internal cross-lingual set, it achieves the best average overall rank in human evaluation among recent open-source and commercial systems. We release code, model checkpoints, and demos at https://github.com/netease-youdao/Confucius4-TTS.

## Metadata
- **Published**: 2026-08-12T04:48:29Z
- **Authors**: Huaxuan Wang, Huimin Wang, Ruiyu Zhang, Yingjie Li, Yitao Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11650v1)