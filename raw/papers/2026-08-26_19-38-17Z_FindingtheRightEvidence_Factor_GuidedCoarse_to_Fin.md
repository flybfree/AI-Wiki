---
title: Finding the Right Evidence: Factor-Guided Coarse-to-Fine Reasoning for Long Videos
published: 2026-08-26T19:38:17Z
authors: Baixuan Xu, Yinyui Xu, Tianshi Zheng, Zhaowei Wang, Weiqi Wang, Haochen Shi, Jiayu Liu, Qing Zong, Xiyu Ren, Xinyu Geng, Zhitao He, Yangqiu Song
url: http://arxiv.org/abs/2608.26355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finding the Right Evidence: Factor-Guided Coarse-to-Fine Reasoning for Long Videos

## Abstract
While LVLMs rapidly improve, long-video question answering still remains challenging: relevant evidence is sparse, and question-relevant context often fails to provide cues that discriminate the correct answer from plausible alternatives. Diagnostic analysis on a manually annotated subset of MMR-V shows that prior agentic systems substantially improve cue retrieval over direct VLM inference yet fail to achieve a corresponding gain in answer accuracy, indicating that the bottleneck lies in option-discriminative evidence rather than topical relevance alone. We propose PACE (Progressive Acquisition of Critical Evidence), a factor-guided framework for long-video evidence acquisition. PACE proceeds in two stages: it first indexes clip-level descriptions guided by question-derived factors without observing the candidate answers; it then uses the candidate answers to derive contrastive cues and queries the index for verification. On MMR-V with the open-source Qwen3-VL backbone, PACE achieves 42.6% accuracy, outperforming direct inference and prior agentic baselines including Deep Video Discovery (DVD). On the same diagnostic subset, PACE recovers 66.9% of the annotated cues, providing empirical evidence that its gains are associated with improved evidence recovery rather than stronger answer-side priors alone. Consistent gains over DVD on LVBench, Video-MME, EgoSchema, and LongVideoBench suggest that option-aware evidence acquisition transfers beyond MMR-V. Code is available at https://github.com/HKUST-KnowComp/PACE.

## Metadata
- **Published**: 2026-08-26T19:38:17Z
- **Authors**: Baixuan Xu, Yinyui Xu, Tianshi Zheng, Zhaowei Wang, Weiqi Wang, Haochen Shi, Jiayu Liu, Qing Zong, Xiyu Ren, Xinyu Geng, Zhitao He, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26355v1)