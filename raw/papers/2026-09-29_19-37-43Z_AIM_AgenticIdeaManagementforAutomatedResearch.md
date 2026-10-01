---
title: AIM: Agentic Idea Management for Automated Research
published: 2026-09-29T19:37:43Z
authors: Hyeong Kyu Choi, Bhavana Dalvi Mishra, Jiefeng Chen, Mihir Parmar, Rui Meng, Chun-Liang Li, Xiangru Tang, Sharon Li, Jinsung Yoon, Tomas Pfister
url: http://arxiv.org/abs/2609.38445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AIM: Agentic Idea Management for Automated Research

## Abstract
Frontier LLMs are increasingly used to automate scientific research through iterative search. We distinguish idea-driven search from solution-driven search and identify three core challenges: organizing evolving research ideas, selecting promising directions, and maintaining alignment between ideas and their implementations. To address these challenges, we introduce the Agentic Idea Manager (AIM), a fully autonomous framework for managing and exploring research directions in idea-driven automated research. Inspired by Bayesian optimization, AIM uses an Agentic Surrogate and an Agentic Acquisition mechanism to organize discovered ideas and guide their selection. A Solution Auditor maintains idea-solution integrity, while a Resource Planner adaptively allocates the remaining experimental budget across parallel search branches. Experiments on 10 AutoLab benchmark tasks show that AIM surpasses the strongest baseline by 1.6 percentage points on System Optimization tasks and 4.9 percentage points on long-horizon Model Development & CUDA tasks. Notably, AIM reaches the best baseline performance up to 3.1x faster in wall-clock time. We further provide a theoretical analysis of when searching over ideas becomes beneficial. Our analysis shows that explicit idea-level allocation makes semantic coverage directly controllable, and that broader coverage becomes increasingly valuable when competitive research directions are sparse among many plausible alternatives. Project Page: https://imhgchoi.github.io/agentic-idea-manager/

## Metadata
- **Published**: 2026-09-29T19:37:43Z
- **Authors**: Hyeong Kyu Choi, Bhavana Dalvi Mishra, Jiefeng Chen, Mihir Parmar, Rui Meng, Chun-Liang Li, Xiangru Tang, Sharon Li, Jinsung Yoon, Tomas Pfister
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38445v1)