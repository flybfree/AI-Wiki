---
title: Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement
published: 2026-09-29T04:14:48Z
authors: Ziqi Zhao, Fanqing Meng, Haocheng Lu, Lingxiao Du, Qiguang Chen, Mengkang Hu, Xiao-Ming Wu
url: http://arxiv.org/abs/2609.36675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement

## Abstract
Recursive self-improvement (RSI) aims to achieve compounding gains by having models improve themselves. While most existing RSI systems optimize external agent harnesses or prompts around a frozen base model, data-centric RSI directly updates the model's own parameters by training on agent-generated data. However, because validating data strategies requires expensive model training, existing methods face a fundamental dilemma: a single agent gets trapped in narrow directions and lacks exploration breadth, while naive parallel search or heavy trace sharing sacrifices long-horizon search depth. To address this challenge, we introduce G"odel Forest, a multi-agent framework that organizes recursive self-improvement as an ensemble of co-evolving search trees. In G"odel Forest, each agent autonomously grows a persistent tree, deepening, branching, or pruning data strategies based on model feedback to secure depth, while parallel trees explore distinct regions of the data space to expand breadth. Crucially, rather than leaving trees isolated or flooding them with heavy execution logs, a dynamically co-evolving memory connects the forest: agents continuously distill their successes and failures into compact procedural lessons anchored to a global leaderboard. Through this forest ecosystem, a dead-end in one tree instantly warns the whole forest against unpromising paths, while an empirical breakthrough quickly seeds new exploration branches in neighboring trees. Evaluated on RSIBench-Data across six diverse domains, G"odel Forest outperforms the single-agent baseline by an average of 10.70% while reducing wall-clock time on five tasks. Ablations confirm that co-evolving shared memory yields a +7.00% gain over independent parallel search, demonstrating that collective distillation is key to scalable self-improvement. The code is available at https://github.com/evolvent-ai/Godel-Forest.

## Metadata
- **Published**: 2026-09-29T04:14:48Z
- **Authors**: Ziqi Zhao, Fanqing Meng, Haocheng Lu, Lingxiao Du, Qiguang Chen, Mengkang Hu, Xiao-Ming Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36675v1)