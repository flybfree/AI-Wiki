---
title: Motion-as-Prompt: Enhancing Motion Reasoning in Multimodal Large Language Models via Motion-Guided Cross-Frame Visual Prompting
published: 2026-08-12T04:54:32Z
authors: Xikai Sun, Kebin Liu, Haotian Wang, Li Liu, Xu Wang, Yunhao Liu
url: http://arxiv.org/abs/2608.11655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Motion-as-Prompt: Enhancing Motion Reasoning in Multimodal Large Language Models via Motion-Guided Cross-Frame Visual Prompting

## Abstract
Motion-centric video reasoning is fundamental to interactive applications such as robotic manipulation and autonomous navigation. However, multimodal large language models (MLLMs) typically process videos through sparse uniform sampling to control visual-token and attention costs. This strategy may discard critical transitions between sampled frames, limiting reasoning about object movement, collisions, and causal interactions. To mitigate this issue, we propose Motion-as-Prompt (MaP), a track-guided cross-frame visual prompting framework. MaP recovers dense point trajectories, selects motion-informative frames, and marks the trajectories accumulated between consecutive sampled frames directly onto the visual inputs, making otherwise hidden displacement, direction changes, and interactions observable to frozen MLLMs. Experiments on CLEVRER and Something-Something-v2 show that MaP consistently improves average motion-reasoning accuracy, yielding gains of 4.2% and 8.9% for GPT-5.5, respectively. Notably, these improvements are obtained without degrading non-motion understanding, highlighting the robustness of MaP. These results demonstrate that MaP provides a simple and effective solution for enhancing motion-centric video reasoning without model training or architectural modification. Project page:https://github.com/SunVictor23/MaP.

## Metadata
- **Published**: 2026-08-12T04:54:32Z
- **Authors**: Xikai Sun, Kebin Liu, Haotian Wang, Li Liu, Xu Wang, Yunhao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11655v1)