---
title: Game-Creation-Agents: Autonomous Game Production
published: 2026-10-12T13:34:08Z
authors:  Tencent Multimodal RL Team, Xiangxin Zhou, Jiaqi Tang, Ke Ma, Wenhao Yang, Jiarui Yao, Boye Niu, Haiyang Guo, Yifei Zhao, Huanjin Yao, Pu Jian, Ruihuang Li, Haitao Wu, Yushi Huang, Xiangyan Liu, Yan Sun, Kaixin Li, Tianyu Pang
url: http://arxiv.org/abs/2610.16776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Game-Creation-Agents: Autonomous Game Production

## Abstract
Game-Creation-Agents (GCA) turns a natural-language request into a runnable Phaser 4 browser game. The pipeline first builds a multimodal game design document that couples mechanics and scene contracts to grounded visual references. It then projects that document into a runtime scaffold, machine-readable contracts, and deterministic tests. Eight specialized agents next carry out production: scenes are implemented serially, assets are produced in parallel, and one reduced manifest joins the two branches into a single build. Build-linked real-UI checks and a code-blind critic then verify that build and decide whether the game may ship. Each blocker returns to the agent that owns the affected artifact for a bounded repair, and the game is released once all the gates pass. We evaluate finished games separately, through their rendered interfaces alone, over prompt-matched tasks run under a common protocol. GCA achieves stronger requirement satisfaction, core mechanics, content depth, and functional visuals than a comparable open pipeline. In a side-by-side human study, raters also score GCA's games higher on every dimension and prefer them overall.

## Metadata
- **Published**: 2026-10-12T13:34:08Z
- **Authors**:  Tencent Multimodal RL Team, Xiangxin Zhou, Jiaqi Tang, Ke Ma, Wenhao Yang, Jiarui Yao, Boye Niu, Haiyang Guo, Yifei Zhao, Huanjin Yao, Pu Jian, Ruihuang Li, Haitao Wu, Yushi Huang, Xiangyan Liu, Yan Sun, Kaixin Li, Tianyu Pang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16776v1)