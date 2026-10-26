---
title: Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation
published: 2026-10-23T10:17:43Z
authors: Zifan Peng, Peng Huang, Jingyi Zheng, Yingjie Xue, Xuechao Wang, Xinlei He, Xia Hu, Dongrui Liu
url: http://arxiv.org/abs/2610.32453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation

## Abstract
AI agents can inspect code and run tests to support smart contract security. SlowMist reports about $38.6 billion in losses across the broader blockchain ecosystem. Existing evaluations can reward memorized or copied answers, including attack code recovered from public blockchain transactions. Reconstructing contracts and validating tasks also require costly manual effort. To address these issues, we propose CONSTRAINTDIAL, a framework for lifelong construction of smart contract security tasks via protocol mutation. It automates local contract reconstruction and uses attack execution to select changes to the required calls or inputs. Execution checks guide revisions that make the original attack fail while preserving exploitability, the security objective, and normal functionality. New incidents and audit findings enter the same procedure. With CONSTRAINTDIAL, we construct 3,045 task inputs from 203 public cases, covering detect, exploit, and patch. Compared with reconstruction alone, protocol mutation reduces success with supplied public answers by 10.9 percentage points on average across detect, exploit, and patch. The fraction of tasks solved by copying online answers falls by 9.3 points.

## Metadata
- **Published**: 2026-10-23T10:17:43Z
- **Authors**: Zifan Peng, Peng Huang, Jingyi Zheng, Yingjie Xue, Xuechao Wang, Xinlei He, Xia Hu, Dongrui Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32453v1)