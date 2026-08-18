---
title: PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies
published: 2026-08-15T15:32:08Z
authors: Yufei Guo, Yinan Wu, Haoran Duan, Guiguang Ding, Jungong Han
url: http://arxiv.org/abs/2608.15285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies

## Abstract
Parameter-efficient fine-tuning (PEFT) is a natural way to adapt pretrained vision-language-action (VLA) policies, but most adapter designs apply temporally static updates throughout a control rollout, overlooking the phase-dependent nature of continuous-action manipulation. Such policies traverse distinct regimes, including approach, contact transition, grasping, transport, and placement, each requiring different adaptation behaviors. We propose \textbf{PhaseLoRA}, a lightweight LoRA parameterization that conditions adaptation at each action-chunk prediction step using two weakly supervised descriptors: fine-control tendency and event/boundary intensity. PhaseLoRA modulates the LoRA left factor in the action expert, allowing the effective low-rank update direction to vary over time while keeping the backbone largely frozen. On LIBERO, PhaseLoRA improves average success rate by 12.2 points over a matched-parameter high-rank LoRA baseline and outperforms stronger LoRA variants. Ablations show that random temporal modulation and scalar gating do not reproduce the performance of the full model, while update-direction analyses reveal structured temporal variation associated with the predicted control descriptors. These results establish within-trajectory conditioning as an effective lightweight PEFT axis for continuous-action VLA policies.

## Metadata
- **Published**: 2026-08-15T15:32:08Z
- **Authors**: Yufei Guo, Yinan Wu, Haoran Duan, Guiguang Ding, Jungong Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15285v1)