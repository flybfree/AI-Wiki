---
title: X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment
published: 2026-07-23T17:35:20Z
authors: Dongjie Fu, Di Cao, Xize Cheng, Zihan Zhang, Wenxu Jia, Yifu Chen, Shengpeng Ji, Yu Zhang, Tao Jin
url: http://arxiv.org/abs/2607.21550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment

## Abstract
While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language student. During training, the student generates reasoning trajectories conditioned on its own acoustic perception, while the teacher provides token-level guidance using matched textual inputs and verified answers. We further construct a three-tier symmetric corpus covering textual reasoning rendered into speech, audio-event reasoning grounded in complex acoustic scenes, and spoken-dialogue reasoning involving paralinguistic cues. This design extends cross-modal distillation beyond textually recoverable content to reasoning grounded in non-linguistic events, prosody, and conversational context. Experiments on MMSU, MMAU, BIG Bench Audio, and MMAR demonstrate that X$^3$-OPD substantially improves audio-grounded reasoning and chain-of-thought quality while largely preserving the model's existing capabilities under domain shift.

## Metadata
- **Published**: 2026-07-23T17:35:20Z
- **Authors**: Dongjie Fu, Di Cao, Xize Cheng, Zihan Zhang, Wenxu Jia, Yifu Chen, Shengpeng Ji, Yu Zhang, Tao Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21550v1)