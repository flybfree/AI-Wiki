---
title: CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model
published: 2026-07-28T09:24:17Z
authors: Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi, Donghwan Hwang, Donghun Ryu, Seokhyun Kim
url: http://arxiv.org/abs/2607.25487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model

## Abstract
Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. Three components target different axes of the problem: dual-view temporal input of 16 history frames per step with textual camera and time markers; hierarchical chain-of-thought (CoT) distillation from a 35B teacher into an episode-level Plan and a chunk-level Think span over task phase, gripper state and next subaction; and paraphrase augmentation expanding 40 base commands into 800 variants. On LIBERO-Plus, spanning 10,030 perturbed tasks across seven perturbation dimensions, CoTinyVLA reaches 90.8% on Spatial, 87.3% on Object, 86.6% on Goal and 80.7% on Long, leading the strongest 7B baseline on all four suites by 4.7, 2.8, 15.9 and 3.0 points, with every margin interval excluding zero. The gains concentrate on the hardest axes of the benchmark: across the eleven published baselines none exceeds 53.2% on Robot Initial States in any suite, whereas CoTinyVLA reaches 73.6% on Goal against 39.9% for the strongest baseline. Ablations show the three components to be separable by perturbation axis, and at a matched image budget how frames are divided between the two cameras and across time accounts for 8.6 points on its own. Closed-loop inference peaks at 2.25 GiB of allocated GPU memory, and paired interventions show the episode Plan to be load-bearing: replacing it with an empty or contradictory span costs 40 to 45 points of success. Structured supervision thus lets a 0.9B backbone exceed all of them. Code: https://github.com/BrainJellyPie/CoTinyVLA

## Metadata
- **Published**: 2026-07-28T09:24:17Z
- **Authors**: Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi, Donghwan Hwang, Donghun Ryu, Seokhyun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25487v1)