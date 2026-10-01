---
title: ArchitectureIQ: On the Measure of Training Intuition
published: 2026-09-30T13:28:28Z
authors: Zirui Ren, Shaoyang Guo, Chencheng Tang, Jinxin Wang, Chengyu Xiong, Shanbin Yu, Peihang Li, Yidi Wu, Bangzhe Huang, Qingyu Qu, Leqian Yang, Ziming Liu
url: http://arxiv.org/abs/2609.39714v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ArchitectureIQ: On the Measure of Training Intuition

## Abstract
Top researchers have good intuition, but do language models have as good intuition about model training as top AI researchers? To measure model intuition of LLMs and humans, we introduce the ArchitectureIQ benchmark. Each question presents a synthetic dataset and several training recipes, and the test-taker is asked to predict the recipe yielding the best test metric. Overall, we find that LLMs' model intuition is good but has four limitations: (1) The intuition is imperfect, or even sub-human in some cases. Frontier models achieve around 76% accuracy (random choice 33%) vs best human researcher (66.0%), yet remain far from perfect. For architecture-only questions, best human achieves 65% while GPT-6 Astra only has 38%. (2) The intuition is empirical, not structured, supported by the fact that more CoT compute does not lead to substantial improvement. Unlike math, we still lack a "Science of AI" language that enables structured reasoning on AI. (3) The intuition is not maximally condensed, and can be further compressed into a knoledge base. Our constructed knowledge base with only 20 items yields large gains for weak models: GPT-4o equipped with the accumulated knowledge almost matches the performance of Claude Opus 5. (4) The intuition is insensitive to dataset properties, but the best model should in general depend on data properties. This suggests that data is the real "dark matter" in AI -- LLMs (so do human researchers) understand too little about data, even less than model architectures.

## Metadata
- **Published**: 2026-09-30T13:28:28Z
- **Authors**: Zirui Ren, Shaoyang Guo, Chencheng Tang, Jinxin Wang, Chengyu Xiong, Shanbin Yu, Peihang Li, Yidi Wu, Bangzhe Huang, Qingyu Qu, Leqian Yang, Ziming Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39714v1)