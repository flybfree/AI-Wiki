---
title: SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks
published: 2026-10-23T10:06:55Z
authors: Tianyun Zhong, Wei Wang, Jialin Li, Jianhong Tu, Liyao Li, Chuqiao Kuang, Tianshi Zheng, Songchi Zhou, Weiqi Zhai, Qile Jin, Jiajia Li, Jiasheng Zheng, Boxi Cao, Yaojie Lu, Hongyu Lin, Shiwei Ye, Bing Zhao, Hu Wei, Lin Qu, Xianpei Han
url: http://arxiv.org/abs/2610.32441v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks

## Abstract
Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, limiting a comprehensive characterization of scientific agents' strengths and weaknesses in realistic research workflows. We introduce SCI-AGENT-EXAM, a workflow-oriented benchmark comprising 120 expert-curated tasks across 11 scientific fields and 7 research task types defined by the Scientific Workflow Task Taxonomy (SWTT). Each task requires both executable artifacts (e.g., code and scripts) and textual artifacts (e.g., reports and explanations). To evaluate the heterogeneous task outputs, we develop a hybrid evaluation protocol combining deterministic programmatic verification for executable artifacts with a calibrated, expert-validated LLM-based judge for textual artifacts. Beyond outcome assessment, we analyze progress and solution stability along execution trajectories to characterize how agents reach their final results. Experiments with 10 frontier LLM agents reveal substantial performance gaps: GPT-6 Astra achieves the highest overall score of 80.9, yet only 26.0% of its runs exceed the 0.95 success threshold. Further analyses uncover distinct capability profiles across scientific task types and substantial variation in execution efficiency and stability. Our code and data are available at https://github.com/SKYLENAGE-AI/Sci-Agent-Exam.

## Metadata
- **Published**: 2026-10-23T10:06:55Z
- **Authors**: Tianyun Zhong, Wei Wang, Jialin Li, Jianhong Tu, Liyao Li, Chuqiao Kuang, Tianshi Zheng, Songchi Zhou, Weiqi Zhai, Qile Jin, Jiajia Li, Jiasheng Zheng, Boxi Cao, Yaojie Lu, Hongyu Lin, Shiwei Ye, Bing Zhao, Hu Wei, Lin Qu, Xianpei Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32441v1)