---
title: myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR
published: 2026-08-11T15:12:42Z
authors: Ye Kyaw Thu, Ye Bhone Lin, Thura Aung, Htet Arkar, Myat Oo Swe, Thet Htet San, Min Thiha Tun, Thazin Myint Oo, Thepchai Supnithi
url: http://arxiv.org/abs/2608.11036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR

## Abstract
Although Whisper models benefit from large-scale multilingual pre-training, their performance on Burmese medical speech remains limited. This work presents a Burmese medical speech recognition framework built on a high-quality 28-hour corpus recorded and validated by native speakers. We fine-tune Whisper models using full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) with LoRA. To evaluate robustness, we apply waveform- and spectrogram-level data augmentation under controlled noise and simulated room acoustics. While augmentation reduces performance on clean speech, it significantly improves robustness in noisy and reverberant environments across FFT and PEFT settings. Our best-performing system, fully fine-tuned myMediWhisper-Medium without augmentation, achieves a state-of-the-art Word Error Rate (WER) of 23.44%, outperforming much larger general-domain fine-tuned models. Dataset and other resources can be found at the Huggingface repository: https://huggingface.co/datasets/LULab/mediTalk-mm-rdy.

## Metadata
- **Published**: 2026-08-11T15:12:42Z
- **Authors**: Ye Kyaw Thu, Ye Bhone Lin, Thura Aung, Htet Arkar, Myat Oo Swe, Thet Htet San, Min Thiha Tun, Thazin Myint Oo, Thepchai Supnithi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11036v1)