---
title: Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model
published: 2026-07-27T17:59:53Z
authors: Senqiao Yang, Kaichen Zhang, Zhaoyang Jia, Jinghao Guo, Yifei Shen, Xinjie Zhang, Xiaoyi Zhang, Haoqing Wang, Xiao Li, Peng Zhang, Xiang An, Yin Xie, Zhening Liu, Xun Guo, Jiahao Li, Shicheng Zheng, Jinglu Wang, Zongyu Guo, Wenxuan Xie, Zihan Zheng, Yuxuan Luo, Bin Li, Yan Lu
url: http://arxiv.org/abs/2607.24904v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model

## Abstract
Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

## Metadata
- **Published**: 2026-07-27T17:59:53Z
- **Authors**: Senqiao Yang, Kaichen Zhang, Zhaoyang Jia, Jinghao Guo, Yifei Shen, Xinjie Zhang, Xiaoyi Zhang, Haoqing Wang, Xiao Li, Peng Zhang, Xiang An, Yin Xie, Zhening Liu, Xun Guo, Jiahao Li, Shicheng Zheng, Jinglu Wang, Zongyu Guo, Wenxuan Xie, Zihan Zheng, Yuxuan Luo, Bin Li, Yan Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24904v1)