---
title: Reactivating Test-Time Scaling for Plane Geometry Problem Solving
published: 2026-08-31T02:15:04Z
authors: Xiaoqiang Kang, Shengen Wu, Maizhen Ning, Xiaobo Jin, Kaizhu Huang, Yutao Yue, Xiaowei Huang, Qiufeng Wang
url: http://arxiv.org/abs/2608.30156v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reactivating Test-Time Scaling for Plane Geometry Problem Solving

## Abstract
Plane geometry problem (PGP) solving has become a critical benchmark for multimodal reasoning because it requires accurate visual perception and precise multi-step symbolic deduction. Although test-time scaling (TTS) has demonstrated remarkable success in general mathematical reasoning, it fails to scale effectively under the symbolic-program paradigm for plane geometry. We identify two key obstacles: limited reasoning diversity induced by rigid symbolic programs and insufficient explicit visual grounding before symbolic deduction. To address these issues, we propose Multi-Trace Synthesis (MTS), which converts each symbolic program into heterogeneous reasoning traces, including executable Python scripts and CoT-augmented variants. We further propose Perception-Augmented (PA) training, which parses diagrams into structured semantic clauses before deduction, and Consensus-Guided Multi-Trace Ensemble (CG-MTE) for efficient self-adaptive inference. Experiments on three geometry benchmarks show that our method consistently improves PGP-solving across model scales and achieves strong performance against both general-purpose MLLMs and specialized geometry solvers. Under test-time scaling, CG-MTE achieves comparable accuracy to high-budget self-consistency while reducing sampling cost by up to 8x. Code and data are publicly available at https://github.com/Jason8Kang/ReTTS-PGPS.

## Metadata
- **Published**: 2026-08-31T02:15:04Z
- **Authors**: Xiaoqiang Kang, Shengen Wu, Maizhen Ning, Xiaobo Jin, Kaizhu Huang, Yutao Yue, Xiaowei Huang, Qiufeng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30156v1)