---
title: MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories
published: 2026-10-20T02:39:26Z
authors: Guorui Chen, Tao Liu, Zhenzhen Huang, Yidan Zhang, Liyu Jiang, Shuoyuan Wang, Hanchen Sun, Xu He, Dong Li, Yihan Hu, Jianye Hao, Lei Feng
url: http://arxiv.org/abs/2610.27524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories

## Abstract
Code agents increasingly work on evolving real repositories, and memory systems aim to help them reuse earlier experience. However, such experience is diverse and evolving, so it remains unclear how memory systems organize it and thereby affect code agents. Existing benchmarks cannot answer this reliably because they lack either temporally valid histories or control over prior-task relevance. In this paper, we present MemDev-Bench to evaluate how memory systems affect code agents over diverse repository histories. It pairs each task with relevance-annotated earlier tasks from the same repository to build histories with controlled relevance. We also build an automated pipeline that reliably makes these earlier tasks executable and verifiable, producing 4,869 historical tasks for 555 base tasks. Based on MemDev-Bench, our systematic evaluation of memory systems across diverse development scenarios yields three main findings. (1) Memory mainly improves fine-grained localization and editing, increasing functional correctness. (2) Memory also causes failures on otherwise solvable tasks even with related history, and unrelated history tends to increase such failures. These failures mainly stem from agents reusing memory without reassessing its applicability. (3) Compared with using memory systems, directly providing agents with raw historical trajectories substantially reduces their steps. Further analysis suggests that agents save these steps by reusing process information that compressed memories tend to omit. These results suggest that future memory systems should preserve process information and reassess memory applicability against current task context.

## Metadata
- **Published**: 2026-10-20T02:39:26Z
- **Authors**: Guorui Chen, Tao Liu, Zhenzhen Huang, Yidan Zhang, Liyu Jiang, Shuoyuan Wang, Hanchen Sun, Xu He, Dong Li, Yihan Hu, Jianye Hao, Lei Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27524v1)