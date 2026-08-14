---
title: UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models
published: 2026-08-13T16:38:57Z
authors: Yukun Dai, Mingzhe Dai, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu
url: http://arxiv.org/abs/2608.13453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models

## Abstract
Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $π_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.

## Metadata
- **Published**: 2026-08-13T16:38:57Z
- **Authors**: Yukun Dai, Mingzhe Dai, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13453v1)