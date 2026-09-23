---
title: Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction
published: 2026-09-21T14:20:47Z
authors: Lujia Bao, Qian Chen, Luyao Cheng, Chong Deng, Yuxiang Kong, Xiangang Li, Xu Li, Jiaqing Liu, Chao-Hong Tan, Haoyu Wang, Wen Wang, Xilou Wang, Junhao Xu, Liang Yi, Binbin Zhang, Qinglin Zhang, Qiquan Zhang
url: http://arxiv.org/abs/2609.25176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction

## Abstract
Real-time voice assistants must reason over evolving requests, execute actions, and follow conversational rules. Qwen-Audio-3.1-Realtime brings these requirements together through Think, Act, and Speak and Coordinate. Think combines Core-Cocktail supervised fine-tuning with Multimodality and Multi-Teacher On-Policy Distillation (M$^{2}$-OPD) to transfer language capabilities and develop native audio skills. Act uses self-evolving executable environments and multi-granularity rollouts for Group Relative Policy Optimization (GRPO), teaching the model to use tools, interpret feedback, and complete tasks. Speak and Coordinate aligns how, when, and whether the assistant speaks or acts. We evaluate audio reasoning, multilingual understanding, tool use, conversational behavior, full-duplex interaction, and safety. Compared with Qwen-Audio-3.0-Realtime, 3.1 raises overall task success from 78.4% to 82.0% on our half-duplex speech-to-text adaptation of $τ$-Voice. On speech-to-speech Full-Duplex-Bench v1.5, the response rate to background speech falls from 73.0% to 13.0%. We also present a separate Voice Harness prototype, using Qwen-Audio-3.0-Realtime as its foreground, that extends spoken interaction to persistent tasks through foreground--background coordination and memory.

## Metadata
- **Published**: 2026-09-21T14:20:47Z
- **Authors**: Lujia Bao, Qian Chen, Luyao Cheng, Chong Deng, Yuxiang Kong, Xiangang Li, Xu Li, Jiaqing Liu, Chao-Hong Tan, Haoyu Wang, Wen Wang, Xilou Wang, Junhao Xu, Liang Yi, Binbin Zhang, Qinglin Zhang, Qiquan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25176v1)