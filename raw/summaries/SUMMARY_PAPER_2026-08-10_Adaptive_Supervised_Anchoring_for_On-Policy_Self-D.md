---
title: Adaptive Supervised Anchoring for On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.07935v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_05-46-32Z_AdaptiveSupervisedAnchoringforOn_PolicySelf_Distil.md
generated_at: 2026-08-10 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates on-policy self-distillation (OPSD) and shows that its performance is limited by the quality of rollout trajectories, which can drift from target tasks. It identifies a failure mode called rollout-conditioned signal degradation where conditioning the teacher on off-target prefixes degrades supervision. The authors propose a unified framework with two supervision pathways to improve task acquisition while preserving general capabilities.

## Key Takeaways
- Rollout-conditioned signal degradation occurs when teacher guidance is based on prefixes that do not match the student’s actual visited states, weakening task relevance.
- A dual‑supervision approach separates rollout‑conditioned distribution matching from canonical ground‑truth cross‑entropy to avoid incompatibility.
- Token‑level alignment adapts anchor strength, strengthening it during cold start and relaxing as rollouts improve.

## Context
On-policy self-distillation aims to make language models more task‑specific while retaining general reasoning abilities. This work highlights a subtle but critical issue: the mismatch between generated rollout prefixes and teacher conditioning can degrade learning efficiency across model scales.

## Implications
For practitioners, this framework offers a practical way to maintain stability during early training phases of OPSD. In industry, it could improve fine‑tuning pipelines where task‑specific adaptation is required without sacrificing broad language competence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07935v1)
