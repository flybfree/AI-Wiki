---
title: Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems
published: 2026-10-12T09:43:48Z
authors: Xin Xu, Ke Cheng, Hao Wang, Yangru Huang, Yanghao Xiao, Zhichao Chen, Zhisheng Zhong, Xun Liu, Yi Li, Qian Li, Haibin Lv, Jun Zhang, Jie Jiang, Zhouchen Lin
url: http://arxiv.org/abs/2610.16491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems

## Abstract
Improving an agent through successive revisions requires balancing exploration and evaluation under a limited budget. A narrow search can miss useful sequences of edits, while fully evaluating every intermediate version can exhaust the budget before those sequences yield a verified improvement. We introduce Speculative Recursive Self-Improvement (SpecRSI), which drafts executable successor agents before their predecessors are fully evaluated, while requiring complete verification before adoption. Verification-Aware Tree Search (VATS) allocates the budget between further edits and outstanding checks using the predicted verified return of a continuation. Group Verification Optimization (GVO) learns the improver from completed searches while keeping the real evaluator fixed. In the main scientific comparison, terminal gains exceed Janus by 33.3%--40.0%. Additional evaluations show that SpecRSI outperforms Janus in all 50 scientific backbone--task pairs and exceeds MetaRSI-v1 by 1.85%--2.38% in macro-average system score across twenty backbones. Coding-validation success reaches 69.4% versus HGM's 64.3% at a 20.8% lower target-cost index.

## Metadata
- **Published**: 2026-10-12T09:43:48Z
- **Authors**: Xin Xu, Ke Cheng, Hao Wang, Yangru Huang, Yanghao Xiao, Zhichao Chen, Zhisheng Zhong, Xun Liu, Yi Li, Qian Li, Haibin Lv, Jun Zhang, Jie Jiang, Zhouchen Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16491v1)