---
title: Controllable Image Captioning with Prompt-Conditioned Scene Rewards
published: 2026-09-01T04:36:23Z
authors: Jongyeop Hyun, Taeyoung Kim, Hyounghun Kim
url: http://arxiv.org/abs/2609.00709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Controllable Image Captioning with Prompt-Conditioned Scene Rewards

## Abstract
Large Vision-Language Models produce fluent image descriptions but offer limited semantic control: users cannot reliably specify whether captions should emphasize attributes, relations, or particular image regions. We present Fine-grained Captioning Control Using Scene Rewards (FoCUS), a controllable image captioning method that lets users steer captions toward specific semantic emphases through natural-language control prompts. The core idea is a prompt-conditioned control objective based on scene-graph-aligned component scores. Generated captions are parsed and aligned to scene-graph components such as objects, attributes, and relations. These components are differentially weighted, including negative weights, according to the requested emphasis. We optimize this objective with GRPO and further improve its reliability through a stricter object validity threshold and reasoning-based verification for attribute and relation scoring. To evaluate controllability, we introduce Semantic Control and Precision Evaluation (SCoPE), a benchmark with contrastive Include/Avoid constraints for measuring both target content coverage and out-of-scope suppression. Experiments on two VLM backbones show that FoCUS consistently improves controllability and fine-grained caption quality without degrading general caption performance.

## Metadata
- **Published**: 2026-09-01T04:36:23Z
- **Authors**: Jongyeop Hyun, Taeyoung Kim, Hyounghun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00709v1)