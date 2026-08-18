---
title: VTInstructor: Visual Trajectory Prompting for Navigation Instruction Generation in Continuous Environments
published: 2026-08-15T15:31:27Z
authors: Haolin Yang, Yuxing Long, Zihan Yang, Hao Dong
url: http://arxiv.org/abs/2608.15284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VTInstructor: Visual Trajectory Prompting for Navigation Instruction Generation in Continuous Environments

## Abstract
Navigation instruction generation from ego-centric RGB video in continuous environments is an important yet challenging task for human-robot interaction and scalable dataset construction. Prior instruction generators assume discrete viewpoint graphs with panoramic observations, where trajectory structure is explicit; in continuous environments, however, the agent receives only a dense RGB stream, making trajectory cues difficult to recover. We propose VTInstructor, the first VLN instruction generation framework for continuous environments. Our key idea is to convert implicit trajectory geometry into explicit visual trajectory prompts: EDTC condenses long RGB trajectories into navigation-critical keyframes, VTP overlays path, turn, and goal cues onto these anchors, VTMod injects the resulting trajectory signals into the visual encoder, and VT-GRPO further calibrates this spatial injection during training, all without requiring a navigation graph, pre-built map, or scene reconstruction. On the challenging R2R-CE and RxR-CE Val Unseen benchmarks, VTInstructor sets a new state of the art across all standard NLG metrics, surpassing the strongest baseline by +0.357 CIDEr and +0.109 CIDEr, respectively. Beyond automatic metrics, VTInstructor-generated instructions raise a frozen follower's success rate to 63.3%, a +14.7 percentage-point gain over the best competing instruction source, and provide consistent data augmentation gains of +3 SR points on downstream navigation tasks.

## Metadata
- **Published**: 2026-08-15T15:31:27Z
- **Authors**: Haolin Yang, Yuxing Long, Zihan Yang, Hao Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15284v1)