---
title: Audio-Anchored Fusion of Multi-Ratio DiT Reconstruction Residuals for Cross-Domain Audio Deepfake Detection
published: 2026-07-29T04:55:14Z
authors: Haotian Mo, Jie Liu, Siqi Shen, Songzhu Mei, Xinhai Chen, Xiangyang Wang, Yigui Feng, Shuai Li, Gencheng Liu, Keqi Yang, Qinglin Wang
url: http://arxiv.org/abs/2607.26472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Audio-Anchored Fusion of Multi-Ratio DiT Reconstruction Residuals for Cross-Domain Audio Deepfake Detection

## Abstract
Audio deepfake detectors often degrade when generators, corpora, or recording conditions change. We use a Diffusion Transformer (DiT), trained only on bona fide speech, as a frozen reconstruction probe. Reconstructions at masking ratios 0.5, 0.75, and 0.9 yield explicit multi-ratio residual maps. Because these residuals are domain sensitive, our audio-anchored detector passes the projected frozen-WavLM auditory representation into the fusion sum without gate-based attenuation and uses residuals only as a scalar-gated additive correction. The pre-specified seed-42 run obtains 6.5442% EER / 0.18456 min-DCF on ASVspoof 5 Eval and 13.8372% / 0.36921 on ITW Full; three-seed means are 6.8885 (0.3308)% and 15.3328 (2.0719)%. The latter is below a separately optimized WavLM-ResNet18 reference under both supervision settings. Auxiliary supervision raises dynamic competitive fusion from 18.4007% to 25.2968% mean ITW EER, worsening all three seeds. The results support reconstruction residuals as complementary evidence and motivate a non-competitive auditory path for ASVspoof 5-to-ITW transfer, without claiming a componentwise causal ablation of anchoring alone.

## Metadata
- **Published**: 2026-07-29T04:55:14Z
- **Authors**: Haotian Mo, Jie Liu, Siqi Shen, Songzhu Mei, Xinhai Chen, Xiangyang Wang, Yigui Feng, Shuai Li, Gencheng Liu, Keqi Yang, Qinglin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26472v1)