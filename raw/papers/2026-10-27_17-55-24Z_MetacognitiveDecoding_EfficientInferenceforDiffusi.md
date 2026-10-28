---
title: Metacognitive Decoding: Efficient Inference for Diffusion Language Agents
published: 2026-10-27T17:55:24Z
authors: Mingyu Zhao, Shuhang Lin, Ligong Han, Xiaojing Yu, Zhenting Wang, Yifei Pang, Yang Zhou, Dimitris N. Metaxas
url: http://arxiv.org/abs/2610.37642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Metacognitive Decoding: Efficient Inference for Diffusion Language Agents

## Abstract
Diffusion language models offer a promising path to efficient agents through parallel token generation. However, efficient interaction requires adapting both where computation is spent and how much text is generated. We introduce a metacognitive controller that guides diffusion generation according to the needs of the current response and the agent's interaction with the environment. It learns when to finalize tokens and how far generation should extend, reducing overall computation within responses. Our controller, a lightweight plug-in for the diffusion backbone, is trained on agent trajectories to balance correctness and generation cost. This approach connects the agent's generation process to the interaction the agent serves. Experiments across five benchmarks demonstrate that our approach reduces inference FLOPs by 20.6% on average compared with the most efficient baseline, while maintaining competitive task accuracy. Ablation studies further validate the effectiveness of our approach.

## Metadata
- **Published**: 2026-10-27T17:55:24Z
- **Authors**: Mingyu Zhao, Shuhang Lin, Ligong Han, Xiaojing Yu, Zhenting Wang, Yifei Pang, Yang Zhou, Dimitris N. Metaxas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.37642v1)