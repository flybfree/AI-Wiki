---
title: Less is More: Modality-Decoupling for General AIGC Audio-Video Detection
published: 2026-07-28T10:23:36Z
authors: Jielun Peng, Yabin Wang, Yaqi Li, Jincheng Liu, Xiaopeng Hong, Athanasios V. Vasilakos
url: http://arxiv.org/abs/2607.25543v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Less is More: Modality-Decoupling for General AIGC Audio-Video Detection

## Abstract
Generative AI has rapidly expanded audio-visual forgery beyond human-centric deepfakes into general scenes. Existing AIGC detection methods assume audio-visual content correspondence, identifying forgeries by spotting cross-modal inconsistencies. However, we empirically find that this assumption does not consistently hold in general scenarios. We argue that, for general audio-visual AIGC detection, decision-level fusion is a more robust alternative to feature-level fusion. Therefore, we propose DAV-Det, a decoupled audio-visual AIGC detection system that independently models forensic evidence from each modality. The visual detector leverages multi-granularity representations at global, patch, and segment levels to capture spatial forgery cues, while the audio detector exploits both temporal and spectral irregularities via a gated temporal-spectral dual-branch architecture to model acoustic artifacts. Our method ranks 1st in the General AIGC Audio-Video Detection Challenge of the IJCAI-ECAI 2026 DDL 2.0 Workshop, with a final score of 0.8460. Code is available at https://github.com/tuffy-studio/DAV-Det.

## Metadata
- **Published**: 2026-07-28T10:23:36Z
- **Authors**: Jielun Peng, Yabin Wang, Yaqi Li, Jincheng Liu, Xiaopeng Hong, Athanasios V. Vasilakos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25543v1)