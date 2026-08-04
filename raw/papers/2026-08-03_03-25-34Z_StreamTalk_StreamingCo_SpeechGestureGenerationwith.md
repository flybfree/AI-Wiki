---
title: StreamTalk: Streaming Co-Speech Gesture Generation with Key-Pose Anchoring
published: 2026-08-03T03:25:34Z
authors: Xiangyue Zhang, Jianfang Li, Jiaxu Zhang, Kaixing Yang, Steven Hoi
url: http://arxiv.org/abs/2608.01643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StreamTalk: Streaming Co-Speech Gesture Generation with Key-Pose Anchoring

## Abstract
Real-time co-speech gesture generation must produce 3D motion clip by clip as speech arrives. Existing streaming methods are open-loop: each clip depends on past context, but the model cannot check or correct its trajectory. Small errors therefore accumulate and cause drift over long sequences. We observe that this failure is mainly caused by the lack of a forward constraint rather than poor short-clip quality. A plausible key pose at the end of each clip provides a destination anchor that limits drift. Based on this observation, we propose StreamTalk, a closed-loop framework with a periodic generate-retrieve-refine cycle. Streaming Pose-Guided Generation first predicts a coarse clip, retrieves a plausible tail pose from a speaker-specific motion database, and refines the clip using this pose before continuing to the next window. During training, Stochastic Anchor Masking randomly masks pose and translation frames, teaching the model to recover complete motion from sparse boundary conditions. A part-aware DiT separates hand, body, and translation streams to reduce interference between global displacement and local articulation. On BEAT2, StreamTalk achieves state-of-the-art FGD, reduces long-horizon drift relative to open-loop baselines, and runs in real time at 76 FPS. Project page: https://xiangyue-zhang.github.io/StreamTalk/.

## Metadata
- **Published**: 2026-08-03T03:25:34Z
- **Authors**: Xiangyue Zhang, Jianfang Li, Jiaxu Zhang, Kaixing Yang, Steven Hoi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01643v1)