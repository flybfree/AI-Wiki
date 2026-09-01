---
title: When LLM Meets Tree Search: A Systematic View of Inference as Search in Large Language Models
published: 2026-08-31T07:49:56Z
authors: Jiaqi Wei, Xiang Zhang, Yuejin Yang, Wenxuan Huang, Juntai Cao, Sheng Xu, Xiang Zhuang, Zhangyang Gao, Muhammad Abdul-Mageed, Laks VS Lakshmanan, Chenyu You, Wanli Ouyang, Siqi Sun
url: http://arxiv.org/abs/2608.30395v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When LLM Meets Tree Search: A Systematic View of Inference as Search in Large Language Models

## Abstract
As pretraining scaling laws approach saturation, Test-Time Scaling (TTS) has emerged as an important direction for improving reasoning by allocating inference-time compute to a fixed model prior. Viewed at a high level, TTS reframes inference as search over a space of partial reasoning states. While Chain-of-Thought (CoT) exposes intermediate steps, common instantiations rely on single-trajectory decoding, limiting recovery from early errors and exploration. This survey systematizes recent progress in tree-search-based reasoning, viewing inference as instance-specific optimization rather than decoding. We trace the evolution from uninformed search to Monte Carlo Tree Search (MCTS), highlighting how sampling-based control supports principled exploration-exploitation trade-offs. To unify a fragmented literature, we introduce a Unified Design Space spanning search topology, evaluation signals, and control dynamics, and advocate a standardized compute-reporting abstraction to make compute-accuracy trade-offs explicit and comparable.

## Metadata
- **Published**: 2026-08-31T07:49:56Z
- **Authors**: Jiaqi Wei, Xiang Zhang, Yuejin Yang, Wenxuan Huang, Juntai Cao, Sheng Xu, Xiang Zhuang, Zhangyang Gao, Muhammad Abdul-Mageed, Laks VS Lakshmanan, Chenyu You, Wanli Ouyang, Siqi Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30395v1)