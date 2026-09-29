---
title: BIABench: Evaluating AI agents on real-world bioimage analysis tasks
published: 2026-09-28T04:22:51Z
authors: Zixuan Pan, Davide Panzeri, Lukas Johanns, Marilin Moor, Yu Zhou, Hedi Peterson, Yiyu Shi, Jianxu Chen
url: http://arxiv.org/abs/2609.34274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BIABench: Evaluating AI agents on real-world bioimage analysis tasks

## Abstract
Artificial-intelligence (AI) agents hold promise for automating bioimage analysis, yet no benchmark evaluates whether they can carry out real-world analyses end to end. Such analyses are hard for agents because 2D images, 3D volumes and time-lapse sequences are often too large to read as context, so an agent must choose and run an analysis through code, specialized software and rendered views. Published studies make this capability testable, because each pairs raw images with a peer-reviewed result. We introduce BIABench, a benchmark of 16 tasks reconstructed from published biological studies that retain their scientific questions, imaging data and ground truth. The tasks span eleven analysis subtasks and modalities from H&E histology to single-molecule localization microscopy. Each submission receives an outcome score, which compares the output files with the ground truth using field-standard metrics, and a process score, in which a vision-language model judges method choice and quality control against an expert-written rubric. We evaluated general-purpose and biology-specific agents across several language models, with repeated runs of every task. Routine two-dimensional tasks were solved well, but on some tasks that added a third dimension or a time axis no agent scored above 0.19. Neither biological specialization, stronger models nor detailed expert instructions closed this gap. The agents were also unreliable, with scores varying more between repeated runs of one agent than between different agents, and without ground truth a correct run could not be told from a wrong one by its process score or by the time spent. Released openly with its data and code, BIABench provides a verifiable framework for evaluating, and eventually training, agents for reliable long-horizon bioimage analysis.

## Metadata
- **Published**: 2026-09-28T04:22:51Z
- **Authors**: Zixuan Pan, Davide Panzeri, Lukas Johanns, Marilin Moor, Yu Zhou, Hedi Peterson, Yiyu Shi, Jianxu Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34274v1)