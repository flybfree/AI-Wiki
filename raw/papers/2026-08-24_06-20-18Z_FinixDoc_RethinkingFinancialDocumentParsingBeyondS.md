---
title: FinixDoc: Rethinking Financial Document Parsing Beyond Saturated Benchmarks
published: 2026-08-24T06:20:18Z
authors: Hang Wang, Jin Zhang, Guoliang Xu, Pengyue Lu, Yao Li, Zijiao Zhang, Tianyu Huang, Weiqi Xiong, Yulong Wang, Chuqiao Lu, Wenkang Huang, Kai Yang, Yadong Li, Hui Li, Xingzhong Xu, Xiao Xu
url: http://arxiv.org/abs/2608.22842v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinixDoc: Rethinking Financial Document Parsing Beyond Saturated Benchmarks

## Abstract
Financial document parsing requires accuracy, structural consistency, and verifiability that current benchmarks often fail to reflect. We present FinixDoc, an end-to-end agentic parsing system for real-world financial documents, with FinixDoc-VL, a 4B-scale vision-language model built on Qwen3-VL-4B, as its core parser. To characterize the gap between benchmark and deployment performance, we introduce a Document Parsing Capability Matrix organized along two practical axes: visual quality and document scale. Guided by this matrix, FinixDoc-VL is trained with a domain-adapted recipe combining homoglyph-aware contrastive learning and multi-stage reinforcement learning with composite domain-specific rewards. To better leverage our accumulated advantage in low-quality financial-document data and support large-scale, high-quality data production, we further build a human-in-the-loop Data Factory pipeline with confidence-aware expert review. For evaluation, we construct FinixDocBench, a financial-domain evaluation suite covering digital-native, camera-captured, ultra-large-page, and internal-workflow scenarios, with a compliance-reviewed subset released alongside this technical report. On its main subsets, FinixDoc-VL achieves the highest overall score (81.43) among evaluated baselines, outperforming the next-best open-source model by 5.13 points, with the largest gains on internal financial workflows (FinixInner: 84.08 vs. 78.73).

## Metadata
- **Published**: 2026-08-24T06:20:18Z
- **Authors**: Hang Wang, Jin Zhang, Guoliang Xu, Pengyue Lu, Yao Li, Zijiao Zhang, Tianyu Huang, Weiqi Xiong, Yulong Wang, Chuqiao Lu, Wenkang Huang, Kai Yang, Yadong Li, Hui Li, Xingzhong Xu, Xiao Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22842v1)