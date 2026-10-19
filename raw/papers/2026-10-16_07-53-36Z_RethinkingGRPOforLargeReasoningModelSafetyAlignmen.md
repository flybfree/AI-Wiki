---
title: Rethinking GRPO for Large Reasoning Model Safety Alignment
published: 2026-10-16T07:53:36Z
authors: Jiawei Chen, Yi Zhang, Jiawei Du, Zhonghou Lv, Tairan Chen, Junyuan Shang, Jinchang Hou, Xiao Yang, Yu Tian, Chenfu Bao, Chao Yu, Zhaoxia Yin
url: http://arxiv.org/abs/2610.23085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking GRPO for Large Reasoning Model Safety Alignment

## Abstract
Large reasoning models (LRMs) exhibit strong reasoning capabilities but remain vulnerable to unsafe outputs. While Group Relative Policy Optimization (GRPO) is widely used for safety alignment, its group-relative optimization may provide insufficient safety-directed learning signals. In this paper, we identify two failure modes: advantage collapse, where homogeneous rollout groups yield vanishing advantages, and unsafe diversification, where unsafe behaviors persist and become increasingly diverse. Our theoretical analysis reveals that behavioral consistency weakens within-group safety contrasts, while entropy regularization can diversify unsafe responses when relative signals vanish. To address these challenges, we propose Beacon, comprising Safety Signal Recovery (SSR) and Safety-Utility Decoupled Alignment (SUDA). SSR combines advantage-guided trajectory filtering and safe reference supervision to recover effective safety learning signals, while SUDA employs category-aware rewards and benign-only KL anchoring to mitigate over-refusal without compromising safety. Experiments across four Qwen3 and DeepSeek-R1-Distill variants and eight benchmarks show that our framework achieves the best average safety and reasoning performance, reducing average safety error by up to 32.83 percentage points while maintaining low over-refusal.

## Metadata
- **Published**: 2026-10-16T07:53:36Z
- **Authors**: Jiawei Chen, Yi Zhang, Jiawei Du, Zhonghou Lv, Tairan Chen, Junyuan Shang, Jinchang Hou, Xiao Yang, Yu Tian, Chenfu Bao, Chao Yu, Zhaoxia Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23085v1)