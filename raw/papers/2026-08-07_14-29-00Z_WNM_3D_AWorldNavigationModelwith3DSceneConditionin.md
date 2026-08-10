---
title: WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN
published: 2026-08-07T14:29:00Z
authors: Yuehao Huang, Yunzi Wu, Xiaotao Zhang, Xinhai Li, Jiankun Dong, Jiajun Lv, Chi Zhang, Chenjia Bai, Yong Liu, Xuelong Li
url: http://arxiv.org/abs/2608.07267v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN

## Abstract
Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric training does not explicitly model how the agent's visual observations should evolve under its predicted motion. Generative world-action models (WAMs) jointly predict future observations and actions, yet existing WAMs for continuous VLN do not condition joint future-view and action generation on geometry-aware representations inferred from the observed history. We present WNM-3D, a generative World Navigation Model with 3D scene conditioning for continuous VLN. To consolidate past observations into persistent scene context, a frozen feed-forward geometry encoder extracts geometry-aware representations from the monocular egocentric RGB history, and a trainable 3D Scene-to-Token Adapter converts them into a fixed-length prefix in the token space of the world-action Diffusion Transformer. Through block-causal attention, this prefix conditions every future video-action block, providing a shared geometric context for both future-view and action generation. We train WNM-3D through supervised world-action fine-tuning on A*-generated demonstrations, DAgger-style adaptation on policy-visited states, and DanceGRPO-based closed-loop policy optimization. Experiments on GN-Bench show that WNM-3D outperforms strong VLM-based navigation policies and its 2D-conditioned counterpart in closed-loop navigation. On a fixed near-goal evaluation set, WNM-3D also achieves higher flow-action consistency and lower visual-motion error.

## Metadata
- **Published**: 2026-08-07T14:29:00Z
- **Authors**: Yuehao Huang, Yunzi Wu, Xiaotao Zhang, Xinhai Li, Jiankun Dong, Jiajun Lv, Chi Zhang, Chenjia Bai, Yong Liu, Xuelong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07267v1)