---
title: SWE-Game: Can Coding Agents Build the Games We Want?
published: 2026-09-27T15:38:20Z
authors: Xiaoyu Chen, Lai Wei, Jin Wang, Xiangyu Zou, Ruochen Fan, Enze Luo, Mingzhe Yao, Jiahui Zhu, Yuhua Wen, Linghe Kong, Weiran Huang
url: http://arxiv.org/abs/2609.33678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-Game: Can Coding Agents Build the Games We Want?

## Abstract
We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D. Five task types cover development from a brief, implementation from a game design document, skeleton completion, repair of 83 injected-fault cases, and Godot-to-Unity porting. Reference materials specify the intended gameplay, while a shared instrumentation interface lets evaluator-owned drivers and probes execute actions and observe independently implemented games. Evaluation combines engine-state checks, certified reference-input replay, and agent-authored feature demonstrations to assess mechanic correctness, demonstrated playability, and behavioral restoration and preservation after repairs. Game-specific vision-language rubrics separately assess presentation. Across six models, Opus5 achieves the highest overall score in all five task types. Best overall scores remain below 60 out of 100 across the three construction tasks, with Brief-to-Game reaching 50.38. Analysis of reviewed submissions identifies requirement omissions and gameplay logic errors as predominant implementation problems. On human-labeled behaviors from 100 agent-built games, executable checks achieve 92.59% balanced accuracy, compared with 78.41% for a video-based VLM judge. Rubric-based visual scores reach a Spearman correlation of 0.829 with human ratings of 200 gameplay clips. Together, these results characterize current agent capabilities across game-development activities and support combining runtime evidence with visual assessment.

## Metadata
- **Published**: 2026-09-27T15:38:20Z
- **Authors**: Xiaoyu Chen, Lai Wei, Jin Wang, Xiangyu Zou, Ruochen Fan, Enze Luo, Mingzhe Yao, Jiahui Zhu, Yuhua Wen, Linghe Kong, Weiran Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33678v1)