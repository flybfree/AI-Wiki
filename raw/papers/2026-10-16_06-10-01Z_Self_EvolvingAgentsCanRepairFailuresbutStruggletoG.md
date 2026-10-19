---
title: Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them
published: 2026-10-16T06:10:01Z
authors: Weixiang Zhao, Yichen Zhang, Yanyan Zhao, Jinming Bai, Bin Liang, Ruifeng Xu, Bing Qin, Ting Liu
url: http://arxiv.org/abs/2610.22984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them

## Abstract
Experience-driven self-evolution offers a promising path for large language model (LLM) agents to continually improve through interaction. Yet existing approaches often rely on successful trajectories or external evaluation signals, leaving unclear whether agents can evolve when such positive anchors are unavailable. We study this question through Cold-Start Failure-Only Evolution (CFOE), where agents start without accumulated experience and learn only from failed interactions without privileged guidance. Across three self-evolving paradigms, multiple LLM backbones, and four interactive environments, we uncover a consistent repair-generalization gap: failure-derived experience can help repair previously failed tasks, but rarely yields sustained improvements on unseen tasks. Further analysis shows that agents often misinterpret failures, while even verified-correct experience remains difficult to transfer. Relaxing CFOE reveals that verifier feedback and additional interaction provide limited gains, whereas successful trajectories substantially improve transfer. These findings suggest that current self-evolving agents are better at repairing observed failures than building generalizable capabilities from failure.

## Metadata
- **Published**: 2026-10-16T06:10:01Z
- **Authors**: Weixiang Zhao, Yichen Zhang, Yanyan Zhao, Jinming Bai, Bin Liang, Ruifeng Xu, Bing Qin, Ting Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22984v1)