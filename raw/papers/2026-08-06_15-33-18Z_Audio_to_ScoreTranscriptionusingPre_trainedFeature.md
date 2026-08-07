---
title: Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset
published: 2026-08-06T15:33:18Z
authors: Eoin Cummins, Zhongyi Huang, Alexandre D'Hooge, Zhuoro Mo, Yaolong Ju
url: http://arxiv.org/abs/2608.06165v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset

## Abstract
Existing audio-to-score (A2S) systems primarily focus on classical music, and the application to popular music remains underexplored. This paper first presents the new SheetSage-A2S Dataset, which includes 61 hours of audio with \texttt{**kern} score encodings for 9,468 clips originating from 6,066 unique songs, the first of its kind to facilitate A2S research for popular music. Additionally, we improve on existing A2S approaches by using data augmentation and MuQ, a pretrained feature-extraction model for music audio, to enhance generalisation abilities and extract meaningful audio features. Results show that the proposed A2S model achieves 4.98\% symbol error rate (SER) on the Quartets collection for classical music, which significantly outperforms the 15.3\% SER from the existing state-of-the-art \cite{alfaro-contrerasTransformer2024}. Additionally, our model achieves 20.92\% SER on the SheetSage-A2S dataset for popular music, serving as a strong benchmark for future research. The dataset, model, and code are made publicly available at: https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model.

## Metadata
- **Published**: 2026-08-06T15:33:18Z
- **Authors**: Eoin Cummins, Zhongyi Huang, Alexandre D'Hooge, Zhuoro Mo, Yaolong Ju
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06165v1)