---
title: AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report
published: 2026-07-20T17:15:41Z
authors:  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge, Yuanyang Yin, Jiaming Tan, Kang He, Liaoyuan Fan, Mingliang Zhai, Ruicong Liu, Xiaojie Xu, Xuangeng Chu, Zhen Li, Zhengyuan Lin, Zhixiang Wang, Zian Meng, Zihui Gao
url: http://arxiv.org/abs/2607.18367v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report

## Abstract
Unlike conventional video game development, which relies on labor-intensive pipelines for asset production, animation, physics, and programming, video world models generate interactive environments from user inputs instantly. It enable us to create customized, explorable, and continuously evolving virtual world from text, an image, or video. Realizing this vision requires four tightly coupled capabilities: interaction, persistent spatiotemporal consistency, stable long-horizon generation, and efficient response. We present AlayaWorld, an interactive long-horizon video world model that generates 24-fps video at 540p and 720p. Built on a 15B video diffusion transformer, AlayaWorld generates short latent chunks autoregressively under camera trajectories and switchable text prompts. Its bounded visual context combines a persistent sink frame, compressed temporal history, geometry-aligned spatial memory, and recent-frame conditioning. To reduce long-term drift, the model is trained with corrupted histories and prediction residuals collected from its own roll-outs. We further introduce a discrete autoregressive distillation formulation that combines distribution-matching distillation, self-forcing++, and consistency distillation, reducing inference from approximately 30 sampling steps to four steps per chunk. On iWorld-Bench, AlayaWorld achieves the best performance over long-horizon generation. Conceived as a full-stack, open-source, and long-term project, AlayaWorld is intended to provide an extensible foundation for future research on interactive video world models.

## Metadata
- **Published**: 2026-07-20T17:15:41Z
- **Authors**:  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge, Yuanyang Yin, Jiaming Tan, Kang He, Liaoyuan Fan, Mingliang Zhai, Ruicong Liu, Xiaojie Xu, Xuangeng Chu, Zhen Li, Zhengyuan Lin, Zhixiang Wang, Zian Meng, Zihui Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18367v1)