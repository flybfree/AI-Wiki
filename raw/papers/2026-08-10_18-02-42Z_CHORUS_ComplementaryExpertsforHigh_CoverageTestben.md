---
title: CHORUS: Complementary Experts for High-Coverage Testbench Stimulus Generation
published: 2026-08-10T18:02:42Z
authors: Hejia Zhang, Sheng Lu, Zhongming Yu, Chia-Tung Ho, Brucek Khailany, Jishen Zhao
url: http://arxiv.org/abs/2608.10090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CHORUS: Complementary Experts for High-Coverage Testbench Stimulus Generation

## Abstract
Large language models (LLMs) have advanced code generation, where executable feedback provides a more reliable learning signal than textual imitation alone. Hardware verification is an important application of code generation and accounts for a substantial fraction of modern chip design effort, with high-coverage testbench stimulus generation as a key task. We present CHORUS, a post-training framework that pushes performance beyond what a conventional supervised fine-tuning (SFT)-to-reinforcement learning (RL) pipeline achieves. CHORUS builds on two observations. First, staged SFT produces behaviorally diverse checkpoints, and dense-reward RL turns them into strong experts with comparable aggregate performance but distinct task-level strengths. Second, these complementary strengths can be exploited through either training-free model merging or further post-training to outperform the best individual expert. By consolidating the resulting specialists into a single 4B model, CHORUS achieves 88.0% Pass@1 on CVDP-ECov, outperforming DeepSeek-R1 (671B) by 13.5 percentage points.

## Metadata
- **Published**: 2026-08-10T18:02:42Z
- **Authors**: Hejia Zhang, Sheng Lu, Zhongming Yu, Chia-Tung Ho, Brucek Khailany, Jishen Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10090v1)