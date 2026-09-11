---
title: Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents
published: 2026-09-10T09:47:44Z
authors: Minghao Guo, Meng Cao, Sui Zhao, Siyu Ning, Xin Wang, Haoze Zhao, Jiaxuan Yang, Haihong Hao, Mingfei Han, Shunlin Rong, Haijun Wu, Xiaodan Liang, Xiaojun Chang
url: http://arxiv.org/abs/2609.11318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents

## Abstract
Deep research agents are increasingly capable of web search, tool use, multimodal evidence analysis, and information synthesis. However, existing benchmarks mainly evaluate medium-horizon exploration and rarely test whether agents can sustain long, dependency-heavy research processes. We introduce Mr.LHDR (Multimodal real-world Long-Horizon Deep Research), a benchmark for evaluating real-world deep research over long, irreducible chains of interdependent evidence across eight categories. Each question is constructed from a hidden Node-Relation graph and requires an average of 12.1 necessary intermediate conclusions with a mean dependency depth of 10.4 before reaching a short, unique, and verifiable answer. Questions incorporate multimodal evidence, including images, maps, PDFs, logos, charts, tables, and video frames, with at least one non-text element that changes the reasoning state. Mr.LHDR evaluates both final answers and the correctness of intermediate conclusions under annotated dependencies. We evaluate general models, deep research systems, and agent frameworks using Overall Accuracy (OA), Strict Accuracy (SA), Checklist Score (CS), and Dependency-Aware Checklist Score (DACS). Results show that even the strongest system achieves only 43.1% OA and 34.3% SA, indicating that final-answer accuracy substantially overestimates complete research success. Removing images reduces DACS by 12.6 points, demonstrating the importance of multimodal evidence, while SA consistently declines as reasoning chains become longer. These findings reveal sustained, dependency-consistent evidence integration, rather than isolated fact retrieval, as a key bottleneck for current deep research agents.

## Metadata
- **Published**: 2026-09-10T09:47:44Z
- **Authors**: Minghao Guo, Meng Cao, Sui Zhao, Siyu Ning, Xin Wang, Haoze Zhao, Jiaxuan Yang, Haihong Hao, Mingfei Han, Shunlin Rong, Haijun Wu, Xiaodan Liang, Xiaojun Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11318v1)