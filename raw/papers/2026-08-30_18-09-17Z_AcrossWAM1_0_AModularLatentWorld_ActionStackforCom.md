---
title: AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies
published: 2026-08-30T18:09:17Z
authors: Yafei Zhang, Nan Wu
url: http://arxiv.org/abs/2608.29937v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies

## Abstract
Latent world-action models avoid rendering future pixels by predicting an action-relevant visual subgoal in feature space. LaWAM established this formulation, but its original presentation left the world model, multimodal backbone, and deployment checkpoint tightly coupled. We introduce AcrossWAM1.0, a modularization and scaling study of this latent world-action stack. Rather than presenting latent subgoals as a new algorithm, we make the module boundary explicit: a policy adapter produces latent-action and action-generation contexts; a retained latent world decoder grounds the predicted transition in the current scene;and a flow-matching expert generates continuous action chunks. We further separate training-only teachers from the inference graph and provide a verifiable deployment export. On 2,000 paired LIBERO episodes, replacing a Qwen3-VL-2B backbone with Qwen3.5-0.8B yields 97.45% success versus 98.00% for the 2B model (a-0.55percentage-point difference; exact McNemarp=0.266). This does not prove equivalence, but it meets a prespecified two-point retention criterion. The compact, inference-reachable checkpoint contains 1,472.6M unique parameters, 42.4% fewer than the original 2B policy, while all retained tensors are bitwise identical to the source checkpoint. Cross-family execution is additionally checked with a MiniCPM-V adapter smoke test; closed-loop cross-family transfer remains an open evaluation. AcrossWAM1.0 therefore contributes an auditable software and evaluation boundary for compact latent world-action policies, distinct from LaWAM's original latent-subgoal contribution.

## Metadata
- **Published**: 2026-08-30T18:09:17Z
- **Authors**: Yafei Zhang, Nan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29937v1)