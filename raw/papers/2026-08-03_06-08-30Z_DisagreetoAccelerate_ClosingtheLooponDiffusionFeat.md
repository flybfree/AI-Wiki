---
title: Disagree to Accelerate: Closing the Loop on Diffusion Feature Forecasts
published: 2026-08-03T06:08:30Z
authors: Yanchao Li, Jiaqing Xie, Ben Gao, Wanhao Liu, Yanbo Wang, T. Y. Tsui, Jinfei Liu, Yuqiang Li, Tianfan Fu
url: http://arxiv.org/abs/2608.01740v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disagree to Accelerate: Closing the Loop on Diffusion Feature Forecasts

## Abstract
Training-free feature forecasting accelerates diffusion sampling by predicting features at skipped denoising steps. Recent work has mainly focused on designing stronger forecasters. Yet forecast error varies sharply across steps, and open-loop caches trust the forecast in full at every skipped step. This fixed trust is what breaks as acceleration turns aggressive. The missing question is not only how to forecast better, but when and how much to trust a forecast. We show that reliability can be observed from the cache itself. Two forecasts agree where the feature trajectory is smooth, and they diverge where prediction turns hard. Their disagreement is a cheap runtime signal, and it costs no extra denoiser evaluation. Based on this signal, we introduce RACER, a training-free closed-loop controller with two responses. It continuously shrinks uncertain forecasts toward the last computed feature. At the riskiest steps, RACER refreshes the feature and repays the added evaluation by skipping a later scheduled one. We derive a deterministic error bound for the shrinkage and empirically evaluate its validity and tightness across acceleration regimes. At the same number of denoiser evaluations, RACER improves the strongest open-loop baseline across SD3.5-Large, FLUX.1-dev, Wan2.1-14B, and HunyuanVideo on DrawBench, VBench, and COCO. On SD3.5, we further show that RACER samples faster at equal quality. RACER generalizes across forecasting designs as well. For example, it recovers much of the quality lost on a Taylor base. These results show that reliable diffusion acceleration also depends on how forecasts are used. Code is available at https://github.com/LiZaiyuan0619/RACER

## Metadata
- **Published**: 2026-08-03T06:08:30Z
- **Authors**: Yanchao Li, Jiaqing Xie, Ben Gao, Wanhao Liu, Yanbo Wang, T. Y. Tsui, Jinfei Liu, Yuqiang Li, Tianfan Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01740v1)