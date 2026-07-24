---
title: Pushing the Frontier of Full-Song Generation: Hierarchical Autoregressive Planning Meets Flow-Matching Rendering
published: 2026-07-22T15:11:46Z
authors: Junyu Dai, Xinyue Fan, Weiqin Li, Xiangang Li, Yunjia Li, Bin Ma, Yukun Ma, Chongjia Ni, Yufei Shi, Biao Tian, Haoxu Wang, Menglin Wu, Jianwei Yu, Huaicheng Zhang, Han Zhao, Shengkui Zhao, Haina Zhu
url: http://arxiv.org/abs/2607.20253v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pushing the Frontier of Full-Song Generation: Hierarchical Autoregressive Planning Meets Flow-Matching Rendering

## Abstract
In this report, we present a unified song generation framework capable of producing high-quality full-length music from lyrics, text descriptions, and musical attributes. The proposed framework supports three tasks: Lyrics-to-Song Generation, which generates complete songs from text descriptions, lyrics, and musical attributes; Instrumental Music Generation, which creates music without vocals; and Cover Song Generation, which reinterprets existing songs with different styles while preserving their melodic content. Architecturally, our system consists of four main components: a semantic-aware tokenizer, hybird-LM, FullDiT, and a two-level melody module. The tokenizer encodes audio into 8-codebook RVQ tokens for efficient discrete music representation. Based on these tokens, hybird-LM performs hierarchical autoregressive audio-token modeling for full-song generation. To improve audio fidelity, FullDiT performs full-song flow matching in a continuous VAE latent space conditioned on codec tokens, lyrics, and text captions. For cover song generation, the melody module extracts and discretizes melody cues from reference audio to guide generation while preserving the original melodic content. Finally, we investigate DPO, GRPO, and OPD as reward-based post-training strategies for hybird-LM and apply flow-based GRPO to FullDiT to improve musicality and rendering quality. Experimental results on a multilingual automatic benchmark, complemented by the Artificial Analysis Music with Vocals leaderboard, show that the proposed framework achieves competitive performance in the evaluated settings.

## Metadata
- **Published**: 2026-07-22T15:11:46Z
- **Authors**: Junyu Dai, Xinyue Fan, Weiqin Li, Xiangang Li, Yunjia Li, Bin Ma, Yukun Ma, Chongjia Ni, Yufei Shi, Biao Tian, Haoxu Wang, Menglin Wu, Jianwei Yu, Huaicheng Zhang, Han Zhao, Shengkui Zhao, Haina Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20253v2)