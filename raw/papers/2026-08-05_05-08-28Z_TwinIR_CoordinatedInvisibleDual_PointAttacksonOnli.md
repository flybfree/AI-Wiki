---
title: TwinIR: Coordinated Invisible Dual-Point Attacks on Online HD Map Construction
published: 2026-08-05T05:08:28Z
authors: Haibo Hu, Jianghuai Deng, Chen Tang, Yang Lou, Qian Xu, Jianping Wang
url: http://arxiv.org/abs/2608.04453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TwinIR: Coordinated Invisible Dual-Point Attacks on Online HD Map Construction

## Abstract
Online HD map construction is critical to prediction and planning in autonomous driving. We find that existing physical attacks against online map construction are limited by a cross-boundary compensation effect: after the target boundary is perturbed, another visible boundary may retain sufficient geometric cues for the model to recover the original road geometry. Based on this observation, we propose TwinIR, a new mechanism-guided physical attack methodology for online map construction. TwinIR jointly optimizes attack effectiveness and point sparsity, seeking the minimum number of attack points needed to suppress compensating geometric cues from surrounding boundaries. To reduce the perceptibility of multi-point attacks, TwinIR models camera responses to near-infrared illumination and maps optimized attack points to feasible physical placements, producing camera-visible interference with minimal visible-spectrum changes. Experiments on nuScenes across state-of-the-art online map construction models show that TwinIR reduces mAP by 8.18-8.96 percentage points under RSA and 2.84-5.62 points under ETA, while increasing the unreachable-goal rate by 25-28 points and the unsafe-planned-trajectory rate by 19-20 points over clean inputs. These attacks are also validated on a real-world testbed AV, where TwinIR successfully induces both road straightening and early-turn deformations while remaining inconspicuous in full-color views.

## Metadata
- **Published**: 2026-08-05T05:08:28Z
- **Authors**: Haibo Hu, Jianghuai Deng, Chen Tang, Yang Lou, Qian Xu, Jianping Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04453v1)