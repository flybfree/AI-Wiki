---
title: IterCAD: Iterative Program Repair for CAD Code Generation from Orthographic Views
published: 2026-08-25T03:22:10Z
authors: Yuchuan Wu, Ke Niu, Haiyang Yu, Zhuofan Chen, Xiangyang Xue, Bin Li
url: http://arxiv.org/abs/2608.24020v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IterCAD: Iterative Program Repair for CAD Code Generation from Orthographic Views

## Abstract
Generating executable parametric CAD code from dimension-annotated orthographic drawings is a challenging task requiring geometric understanding, procedural reasoning, and precise numerical prediction. Existing vision-language approaches typically formulate this problem as one-shot generation, preventing the model from inspecting intermediate CAD results and correcting early mistakes, often leading to non-executable code or geometrically inconsistent outputs. In this paper, we propose IterCAD, an iterative framework that reformulates orthographic-view-to-CAD generation as a progressive program repair process. Instead of predicting the final CAD code in a single pass, IterCAD repeatedly analyzes the current CAD result, reasons about its discrepancy with the target views, and explicitly decides whether to REVISE the code or STOP the refinement process. To make iterative repair learnable, we further construct IterCAD-RS, a structured revise-or-stop supervision set containing both repairable intermediate CAD states and already-correct states, and develop a three-stage training strategy for initial generation, revision learning, and multi-turn RL optimization. By closing the loop between visual understanding, geometric verification, and code refinement, IterCAD progressively corrects structural and parametric errors. Experiments on CADExpert show that IterCAD consistently improves code executability and geometric fidelity over strong one-shot baselines.

## Metadata
- **Published**: 2026-08-25T03:22:10Z
- **Authors**: Yuchuan Wu, Ke Niu, Haiyang Yu, Zhuofan Chen, Xiangyang Xue, Bin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24020v1)